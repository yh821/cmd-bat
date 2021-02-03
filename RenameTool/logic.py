#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import re
import sys
import zipfile
import time
from frame import *
from biplist import *

configPath = "config.plist"
configData = None

development = "dev"
appstore = "dis"
adhoc = "adhoc"
type2target = {development: "development", appstore: "app-store", adhoc: "ad-hoc"}
target2type = {"development": development, "app-store": appstore, "ad-hoc": adhoc}

rnNumDir = ["1", "2", "3", "全部"]


def Init():
	readConfigData()
	frame = MainFrameEx()
	frame.Show()


def readConfigData():
	global configData
	if os.path.exists(configPath):
		configData = readPlist(configPath)
	else:
		configData = {"Paths": {"build": "", "mod": ""}}


def writeConfigData():
	writePlist(configData, configPath, False)


def SetBuildPath(path):
	configData["Paths"]["build"] = path
	writeConfigData()


def GetBuildPath():
	return configData["Paths"]["build"]


def SetModPath(path):
	configData["Paths"]["mod"] = path
	writeConfigData()


def GetModPath():
	return configData["Paths"]["mod"]


def GetDirPathList(path):
	nlist = []
	for dirpath, dirnames, filenames in os.walk(path):
		zlDirNames = []
		for v in dirnames:
			zlDirNames.append((v, os.path.getctime(os.path.join(dirpath, v))))

		def mysort(elem):
			return elem[1]

		zlDirNames.sort(key=mysort, reverse=True)
		for v in zlDirNames:
			nlist.append(v[0])
		break
	return nlist


def GetFileNameBySuffix(path, suffix):
	dirlist = os.listdir(path)
	for v in dirlist:
		if v.rfind("." + suffix) >= 0:
			return "{0}/{1}".format(path, v)
	return ""


def ShowTipsDialog(title, message):
	dlg = wx.MessageDialog(None, message, title, wx.OK)
	dlg.ShowModal()
	dlg.Destroy()


def ShowAskDialog(title, message):
	dlg = wx.MessageDialog(None, message, title, wx.YES_NO)
	ret = False
	if dlg.ShowModal() == wx.ID_YES:
		ret = True
	dlg.Destroy()
	return ret


class redirect:
	def __init__(self,outputCtrl):
		self.stdout = sys.stdout
		self.opCtrl = outputCtrl
		sys.stdout = self

	def write(self,str):
		self.stdout.write(str)
		self.opCtrl.write(str)

	def flush(self):
		pass


class MainFrameEx(MainFrame):
	def __init__(self):
		MainFrame.__init__(self, None)
		redirect(self.log_output)
		bpath = GetBuildPath()
		self.build_dir_path.SetPath(bpath)
		mpath = GetModPath()
		self.mod_dir_path.SetPath(mpath)
		print("build目录：" + bpath)
		print("mods目录：" + mpath)
		self.rn_num_choice.Set(rnNumDir)
		self.rn_num_choice.SetSelection(1)

	def HandlePathSelect(self, path):
		if os.path.exists(path):
			SetBuildPath(path)
			nlist = GetDirPathList(path)
			self.SetIPAFileName(path, nlist[0])
			self.SetIPAFileName(path, nlist[1])

	def OnBuildDirSelect(self, event):
		path = event.Path
		print("切换Build目录路径到 " + path)
		if os.path.exists(path):
			SetBuildPath(path)

	def OnModDirSelect(self, event):
		path = event.Path
		print("切换Mods目录路径到 " + path)
		if os.path.exists(path):
			SetModPath(path)

	def GetIPAInfo(self, fname):
		ipa = zipfile.ZipFile(fname)
		znames = ipa.namelist()
		pattern = re.compile(r'Payload/[^/]*.app/Info.plist')
		for path in znames:
			mpath = pattern.match(path)
			if mpath:
				data = ipa.read(mpath.group())
				pdata = readPlistFromString(data)
				return pdata

	def GetNewIPAName(self, path, ipafname):
		mt = os.path.getmtime(ipafname)
		btime = time.strftime("%m%d%H%M", time.localtime(mt))
		info = self.GetIPAInfo(ipafname)
		gname = info["CFBundleDisplayName"]
		version = info["CFBundleShortVersionString"]
		build = info["CFBundleVersion"]
		bname = info["BuglyAppChannelString"]
		mpath = self.mod_dir_path.GetPath()
		cfgFN = "{p}/Mods_{n}/iOS/AppConfig.json".format(p=mpath, n=bname)
		with open(cfgFN, "rb") as file:
			fstr = file.read()
		dlist = re.findall("\r\nverify_timeout:.+\r\n", fstr)
		if len(dlist) > 0:
			tstr = dlist[0].replace("\r\n", "")
			otime = tstr[tstr.find(":") + 1:].replace("-", "")[4:]
		else:
			otime = ""
		edata = readPlist("{0}/{1}".format(path, "ExportOptions.plist"))
		target = target2type[edata["method"]]
		return "{n}_{v}_{vv}b{bv}_{t}_{o}".format(n=gname, v=target, vv=version, bv=build, t=btime, o=otime)

	def RenameFile(self, path):
		if os.path.exists(path):
			fname = GetFileNameBySuffix(path, "ipa")
			if fname != "":
				iname = self.GetNewIPAName(path, fname)
				rname = "{p}/{n}.ipa".format(p=path, n=iname)
				os.rename(fname, rname)
				print(rname)
			else:
				print("目录内没有ipa文件：" + path)
		else:
			print("目录不存在：" + path)

	def HandleRenameFile(self, num, path, dirs):
		if ShowAskDialog("提示", "确定要重命名build目录内的{n}个IPA文件？".format(n=num)):
			count = 0
			for v in dirs:
				cpath = "{0}/{1}".format(path, v)
				self.RenameFile(cpath)
				count = count + 1
				if count >= num:
					break
			self.ShowFinder()

	def ShowFinder(self):
		bpath = GetBuildPath()
		os.system("open {0}".format(bpath))

	def OnRenameClick(self, event):
		try:
			path = self.build_dir_path.GetPath()
			if os.path.exists(path):
				nlist = GetDirPathList(path)
				num = rnNumDir[self.rn_num_choice.GetSelection()]
				if num == "全部":
					self.HandleRenameFile(len(nlist), path, nlist)
				else:
					self.HandleRenameFile(int(num), path, nlist)
			else:
				print("build目录不存在")
		except Exception, err:
			ShowTipsDialog("出错了!", "{0}".format(err))
			print(err)
