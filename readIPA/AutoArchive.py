#!/usr/bin/env python
# coding=utf-8
# 环境: UAT&SIT

# import os
# import requests
# import webbrowser
import subprocess
import time
# import smtplib

# 路径信息
project_name = '99YOU'  # 项目名称
project_path = '/Users/m5pro/Documents/M5-C/release/99YOU_b131_Auto'  # 项目路径
export_directory = '/Users/m5pro/Documents/M5-C/release/99YOU_b131_Auto'  # 输出的路径
exporrt_folder = 'auto_archive'  # 输出的文件夹

# # 蒲公英app地址、USER_KEY、API_KEY,具体见蒲公英官网: 账户设置-->API信息
# ipa_download_url = 'https://www.pgyer.com/manager/dashboard/app/xxxxxxxxxxxxxxxx'
# USER_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
# API_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'


class AutoArchive(object):
	def __init__(self):
		pass

	def clean(self):
		print("\n\n===========开始clean操作===========")
		start = time.time()
		clean_opt = 'xcodebuild clean -workspace %s/%s.xcworkspace -scheme Unity-iPhone -configuration Release' % (
		project_path, project_name)
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
		subprocess.call(['rm', '-rf', '%s/%s' % (export_directory, exporrt_folder)])
		time.sleep(1)
		subprocess.call(['mkdir', '-p', '%s/%s' % (export_directory, exporrt_folder)])
		time.sleep(1)
		start = time.time()
		archive_opt = 'xcodebuild archive -workspace %s/%s.xcworkspace -scheme Unity-iPhone -configuration Release -archivePath %s/%s' % (
		project_path, project_name, export_directory, exporrt_folder)
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
		export_directory, exporrt_folder, export_directory, exporrt_folder, export_directory)
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
		# subprocess.call(['rm', '-rf', '%s/%s.xcarchive' % (export_directory, exporrt_folder)])
		# 上传
		# self.upload('%s/%s/ZBank.ipa' % (export_directory, exporrt_folder))

	# def upload(self, ipa_path):
	# 	print("\n\n===========开始上传蒲公英操作===========")
	# 	if ipa_path:
	# 		# 蒲公英操作API
	# 		# https://www.pgyer.com/doc/api
	# 		url = 'http://www.pgyer.com/apiv1/app/upload'
	# 		data = {
	# 			'uKey': USER_KEY,
	# 			'_api_key': API_KEY,
	# 			'installType': '2',
	# 			'password': pwd,
	# 			'updateDescription': description
	# 		}
	# 		files = {'file': open(ipa_path, 'rb')}
	# 		r = requests.post(url, data=data, files=files)
	# 		if r.status_code == 200:
	# 			self.open_browser(self)
	# 	else:
	# 		print("\n\n===========没有找到对应的ipa===========")
	# 		return
	#
	# @staticmethod
	# # 上传成功,通过浏览器打开蒲公英网站
	# def open_browser(self):
	# 	webbrowser.open(ipa_download_url, new=1, autoraise=True)

#
# if __name__ == '__main__':
# 	# description = input("请输入更新的日志描述:")
# 	# pwd = input("请输入蒲公英安装密码:")
# 	archive = AutoArchive()
# 	#archive.clean()
# 	archive.export()
