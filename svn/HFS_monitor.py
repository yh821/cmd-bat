#!/usr/bin/python
# coding: UTF-8

import os
import sys
import time
import threading
import urllib.request
import urllib.error
from enum import IntEnum

class State(IntEnum):
	Wait = 0
	Request = 1
	Restart = 2
	Stop = 3

def main():
	global check_url
	check_url = sys.argv[1]
	global wait_time
	wait_time = int(sys.argv[2]) or 60
	global waitStrLen
	waitStrLen = len(str(wait_time)) + 1

	global cur_state
	cur_state = State.Request
	global delta_time
	delta_time = wait_time
	global wait_count
	wait_count = 0
	global handle_time
	handle_time = 0

	update()
	request_timeout()

def update():
	global update_timer
	global cur_state
	global delta_time
	global wait_count
	global handle_time

	if cur_state==State.Wait:
		delta_time = delta_time - 1
		if delta_time < 0:
			delta_time = wait_time
			cur_state = State.Request
		else:
			strTime = " {0}".format(delta_time)
			strTime = strTime + " " * (waitStrLen - len(strTime))
			print(strTime, end="")
			print("\b" * waitStrLen, end="", flush=True)
	elif cur_state==State.Request:
		try:
			handle_time = time.time()
			request = urllib.request.Request(check_url)
			urllib.request.urlopen(request)
			if wait_count>0:
				back_space(30)
			wait_count = wait_count + 1
			print("访问第{0}次...".format(wait_count), end="")
			cur_state = State.Wait
		except urllib.error.URLError as e:
			wait_count = 0
			cur_state = State.Restart
		finally:
			handle_time = 0
	elif cur_state==State.Restart:
		print("\n====================开始重启====================")
		os.system("hfs -q")
		time.sleep(2)
		os.system("start hfs")
		time.sleep(3)
		print("\n====================重启完成====================")
		handle_time = 0
		cur_state = State.Request
	elif cur_state==State.Stop:
		update_timer.cancel()
		return

	global update_timer
	update_timer = threading.Timer(1,update)
	update_timer.start()

def back_space(count):
	print("\b" * count, end="", flush=True)
	print(" " * count, end="")
	print("\b" * count, end="", flush=True)
	pass

def request_timeout():
	global cur_state
	if cur_state==State.Request and handle_time>0 and time.time()>handle_time+5:
		print("访问超时")
		cur_state = State.Stop
		time.sleep(3)
		update()

	global request_timeout_timer
	request_timeout_timer = threading.Timer(1, request_timeout)
	request_timeout_timer.start()

main()