#!/usr/bin/python
# coding: UTF-8

import os
import sys
import time
import threading

proj_path = ""
svn_handle_time = 0
svn_handle_timeout = 30
cur_state = 1

def main():
	global proj_path
	proj_path = sys.argv[1]
	global wait_time
	wait_time = int(sys.argv[2]) or 60
	global waitStrLen
	waitStrLen = len(str(wait_time)) + 1

	global delta_time
	delta_time = wait_time
	global wait_count
	wait_count = 0

	update()
	check_svn_conflict()

def update():
	global cur_state
	global delta_time
	global wait_count

	if cur_state==0:
		delta_time = delta_time - 1
		if delta_time < 0:
			delta_time = wait_time
			cur_state = 1
		else:
			strTime = " {0}".format(delta_time)
			strTime = strTime + " " * (waitStrLen - len(strTime))
			print(strTime, end="")
			print("\b" * waitStrLen, end="", flush=True)
	elif cur_state==1:
		global svn_handle_time
		svn_handle_time = time.time()
		ecode,logs = svn_update()
		if ecode>0:
			print("更新异常!!!")
			svn_handle_time = 0
			svn_conflict()
		elif ecode==0:
			print("开始更新...")
			if logs!=None:
				for log in logs:
					print(log)
			print("更新完成.")
			svn_handle_time = 0
			cur_state = 0
		elif ecode==-1:
			if wait_count>0:
				back_space(30)
			wait_count = wait_count + 1
			print("没有更新,第{0}次等待...".format(wait_count), end="")
			svn_handle_time = 0
			cur_state = 0

	global update_timer
	update_timer = threading.Timer(1,update)
	update_timer.start()

def back_space(count):
	print("\b" * count, end="", flush=True)
	print(" " * count, end="")
	print("\b" * count, end="", flush=True)
	pass

def svn_update():
	f = os.popen("svn up %s" % proj_path)
	lines = f.readlines()
	f.close()
	if len(lines)==0:
		return 1, None
	logs = []
	for line in lines:
		line = line.strip()
		logs.append(line)
	for log in logs:
		if log.startswith("U ") or log.startswith("A ") or log.startswith("D "):
			return 0, logs
	return -1, None

def svn_cleanup():
	os.system("svn cleanup %s\\Assets" % proj_path)
	pass

def svn_revert():
	os.system("svn revert -R %s\\Assets" % proj_path)
	pass

def svn_conflict():
	if cur_state==1:
		print("SVN可能已冲突, 进行SVN冲突解决")
		svn_cleanup()
		svn_revert()

def check_svn_conflict():
	if svn_handle_time>0 and time.time()>svn_handle_time+svn_handle_timeout:
		svn_conflict()

	global check_svn_conflict_timer
	check_svn_conflict_timer = threading.Timer(1, check_svn_conflict)
	check_svn_conflict_timer.start()

main()