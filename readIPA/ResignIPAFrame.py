# -*- coding: utf-8 -*-

import os
import re
import time
import zipfile
import datetime
from biplist import *
from ResignIPABaseFrame import *


def unzip(inputPath, outputPath):
	zip_file = zipfile.ZipFile(inputPath)
	zip_list = zip_file.namelist()
	for f in zip_list:
		zip_file.extract(f, outputPath)
	zip_file.close()


def zipDir(inputPath, outputPath):
	print ('压缩资源:%s' % inputPath)
	print ('压缩目标:%s' % outputPath)
	zip_file = zipfile.ZipFile(outputPath, "w", zipfile.ZIP_DEFLATED)
	for path, dirnames, filenames in os.walk(inputPath):
		fpath = path.replace(inputPath, '')
		for filename in filenames:
			zip_file.write(os.path.join(path, filename), os.path.join(fpath, filename))
	zip_file.close()


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
		inputFile = self.m_filePicker1.GetPath()
		if inputFile == None:
			print('请选择IPA文件')
			return
		bundleId = self.m_textCtrl1.GetValue()
		if bundleId == None:
			print('请输入bundleId')
			return
		displayName = self.m_textCtrl2.GetValue()
		version = self.m_textCtrl3.GetValue()
		build = self.m_textCtrl4.GetValue()
		print("===========开始导出===========")
		start = time.time()
		pathFile = os.path.split(inputFile)
		fileExt = os.path.splitext(inputFile)
		unzipPath = os.path.join(pathFile[0], 'temp')
		zipFile = fileExt[0] + '.zip'
		plist_dict, plist_path = getIpaPlist(inputFile, unzipPath)
		bundleVersion = plist_dict['CFBundleShortVersionString']
		buildVersion = plist_dict['CFBundleVersion']
		dateString = datetime.datetime.now().strftime('%Y%m%d%H%M')
		outputFile = u'{0}_{1}b{2}_{3}.ipa'.format(fileExt[0], bundleVersion, buildVersion, dateString)
		resign_info_plist(plist_dict, plist_path, bundleId, displayName, version, build)
		zipDir(unzipPath, zipFile)
		os.rename(zipFile, outputFile)
		end = time.time()
		print("===========导出成功,用时:%.2f秒===========" % (end - start))
