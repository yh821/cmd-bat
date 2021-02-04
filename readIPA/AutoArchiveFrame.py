#!/usr/bin/env python
# coding=utf-8

# import os
import subprocess
import time
from AutoArchiveBaseFrame import *

project_name = '99YOU'  # 项目名称输出的路径
exporrt_folder = 'Archive'  # 输出的文件夹


class AutoArchiveFrame(AutoArchiveBaseFrame):
	def __init__(self, parent):
		AutoArchiveBaseFrame.__init__(self, parent)

	def clean(self):
		print("\n\n===========开始clean操作===========")
		start = time.time()
		clean_opt = 'xcodebuild clean -workspace %s/%s.xcworkspace -scheme Unity-iPhone -configuration Release' % (
			self.project_path, project_name)
		clean_opt_run = subprocess.Popen(clean_opt, shell=True)
		clean_opt_run.wait()
		end = time.time()

		# clean 结果
		clean_result_code = clean_opt_run.returncode
		if clean_result_code != 0:
			print("===========clean失败,用时:%.2f秒===========" % (end - start))
		else:
			print("===========clean成功,用时:%.2f秒===========" % (end - start))
			self.archive()

	def archive(self):
		print("\n\n===========开始archive操作===========")
		subprocess.call(['rm', '-rf', '%s/%s' % (self.project_path, exporrt_folder)])
		time.sleep(1)
		subprocess.call(['mkdir', '-p', '%s/%s' % (self.project_path, exporrt_folder)])
		time.sleep(1)
		start = time.time()
		archive_opt = 'xcodebuild archive -workspace %s/%s.xcworkspace -scheme Unity-iPhone -configuration Release -archivePath %s/%s' % (
			self.project_path, project_name, self.project_path, exporrt_folder)
		archive_opt_run = subprocess.Popen(archive_opt, shell=True)
		archive_opt_run.wait()
		end = time.time()

		# archive 结果
		archive_result_code = archive_opt_run.returncode
		if archive_result_code != 0:
			print("===========archive失败,用时:%.2f秒===========" % (end - start))
		else:
			print("===========archive成功,用时:%.2f秒===========" % (end - start))

		# 导出IPA
		self.export()

	def export(self):
		print("\n\n===========开始export操作===========")
		start = time.time()
		export_opt = 'xcodebuild -exportArchive -archivePath %s/%s.xcarchive -exportPath %s/%s -exportOptionsPlist %s/ExportOptions.plist' % (
			self.project_path, exporrt_folder, self.project_path, exporrt_folder, self.project_path)
		export_opt_run = subprocess.Popen(export_opt, shell=True)
		export_opt_run.wait()
		end = time.time()

		# ipa导出结果
		export_result_code = export_opt_run.returncode
		if export_result_code != 0:
			print("===========导出IPA失败,用时:%.2f秒===========" % (end - start))
		else:
			print("===========导出IPA成功,用时:%.2f秒===========" % (end - start))

	# 删除archive.xcarchive文件
	# subprocess.call(['rm', '-rf', '%s/%s.xcarchive' % (self.project_path, exporrt_folder)])

	def OnClickStart(self, event):
		# description = input("请输入更新的日志描述:")
		# pwd = input("请输入蒲公英安装密码:")
		self.project_path = self.m_dirPicker1.GetPath()
		if self.project_path == None:
			print('请选择工程目录')
			return
		self.clean()
		self.export()
