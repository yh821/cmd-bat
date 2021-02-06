# -*- coding: utf-8 -*-

import os
import re
import time
import zipfile
import datetime
from biplist import *
from subprocess import call
from ResignIPABaseFrame import *


def unzip(inputPath, outputPath):
	zip_file = zipfile.ZipFile(inputPath)
	zip_list = zip_file.namelist()
	for f in zip_list:
		zip_file.extract(f, outputPath)
	zip_file.close()


def zip(inputPath, outputPath):
	print ('压缩资源:%s' % inputPath)
	print ('压缩目标:%s' % outputPath)
	zip_file = zipfile.ZipFile(outputPath, "w", zipfile.ZIP_DEFLATED)
	for path, dirnames, filenames in os.walk(inputPath):
		fpath = path.replace(inputPath, '')
		for filename in filenames:
			zip_file.write(os.path.join(path, filename), os.path.join(fpath, filename))
	zip_file.close()


def zipLinux(srcDir, zipDir, zipFile):
	print ('开始压缩')
	start = time.time()
	os.chdir(srcDir)
	call(['zip', '-r', zipFile, zipDir])
	end = time.time()
	print ('压缩完成, 用时:%.2f秒' % (end - start))


def unzipLinux(srcDir, zipFile):
	print ('开始解压')
	start = time.time()
	os.chdir(srcDir)
	call(['unzip', '-o', zipFile])
	end = time.time()
	print ('解压完成, 用时:%.2f秒' % (end - start))


def getIpaPlist(ipa_path, unzipPath):
	zip_file = zipfile.ZipFile(ipa_path)
	zip_list = zip_file.namelist()
	plist_file = find_plist_path(zip_list)
	for f in zip_list:
		zip_file.extract(f, unzipPath)
	zip_file.close()

	plist_path = os.path.join(unzipPath, plist_file)
	return readPlist(plist_path), plist_path  # python 2.7


def find_plist_path(name_list):
	pattern = re.compile(r'Payload/[^/]*.app/Info.plist')
	for path in name_list:
		m = pattern.match(path)
		if m is not None:
			return m.group()


def resign_info_plist(plist_dict, plist_path, bundleId, displayName, version, build):
	plist_dict['CFBundleIdentifier'] = bundleId
	try:
		plist_dict['CFBundleURLTypes'][0]['CFBundleURLSchemes'][0] = bundleId
	except:
		print ('info.plist缺少URLTypes配置!')
	if displayName != '':
		plist_dict['CFBundleDisplayName'] = displayName
	if version != '':
		plist_dict['CFBundleShortVersionString'] = version
	if build != '':
		plist_dict['CFBundleVersion'] = build
	writePlist(plist_dict, plist_path)
	print ('Display Name: %s' % plist_dict['CFBundleDisplayName'])
	print ('Bundle Identifier: %s' % plist_dict['CFBundleIdentifier'])
	print ('Version: %s' % plist_dict['CFBundleShortVersionString'])
	print ('Build: %s' % plist_dict['CFBundleVersion'])


class ResignIPAFrame(ResignIPABaseFrame):
	def __init__(self, parent):
		ResignIPABaseFrame.__init__(self, parent)

	def OnClickStart(self, event):
		ipaFile = self.m_filePicker1.GetPath()
		if ipaFile == None:
			print('请选择IPA文件')
			return
		bundleId = self.m_textCtrl1.GetValue()
		if bundleId == None:
			print('请输入bundleId')
			return
		print("===========开始导出===========")
		start = time.time()
		displayName = self.m_textCtrl2.GetValue()
		version = self.m_textCtrl3.GetValue()
		build = self.m_textCtrl4.GetValue()
		filePaths = os.path.split(ipaFile)
		fileExt = os.path.splitext(ipaFile)
		fileDir = filePaths[0]
		unzipPath = os.path.join(fileDir, 'temp')
		zipFile = fileExt[0] + '.zip'
		plist_dict, plist_path = getIpaPlist(ipaFile, unzipPath)
		bundleVersion = plist_dict['CFBundleShortVersionString']
		buildVersion = plist_dict['CFBundleVersion']
		dateString = datetime.datetime.now().strftime('%Y%m%d%H%M')
		outputFile = u'{0}_{1}b{2}_{3}.ipa'.format(fileExt[0], bundleVersion, buildVersion, dateString)
		resign_info_plist(plist_dict, plist_path, bundleId, displayName, version, build)
		zipLinux(fileDir, unzipPath, zipFile)
		os.rename(zipFile, outputFile)
		end = time.time()
		print("===========导出成功,用时:%.2f秒===========" % (end - start))
