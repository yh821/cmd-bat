#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import shutil
import re
from frame import *

###########################################################################
## global function
###########################################################################

def Init():
	frame = MainFrameEx()
	frame.Show()

def ShowTipsDialog(title,message):
	dlg = wx.MessageDialog(None, message, title, wx.OK)
	dlg.ShowModal()
	dlg.Destroy()

def ShowAskDialog(title,message):
	dlg = wx.MessageDialog(None, message, title, wx.YES_NO)
	ret = False
	if dlg.ShowModal()==wx.ID_YES:
		ret = True
	dlg.Destroy()
	return ret

def copy_dir(src_path, target_path):
	if os.path.isdir(src_path) and os.path.isdir(target_path):
		filelist_src = os.listdir(src_path)
		for file in filelist_src:
			path = os.path.join(os.path.abspath(src_path), file)
			if os.path.isdir(path):
				path1 = os.path.join(os.path.abspath(target_path), file)
				if not os.path.exists(path1):
					os.mkdir(path1)
				copy_dir(path,path1)
			else:
				shutil.copy(path,target_path)
		return True
	else:
		return False

###########################################################################
## frame
###########################################################################

class MainFrameEx(MainFrame):
	def __init__(self):
		MainFrame.__init__(self,None)
		self.exe_name_input.SetValue("main.command")
		self.output_dir_picker.SetPath(os.path.join(os.path.expanduser('~'),"Desktop"))

	def OnToolPathSelect( self, event ):
		path = self.tool_dir_picker.GetPath()
		list = re.findall("\w+",path)
		if len(list)>0:
			self.app_name_input.SetValue(list[-1])

	def OnArchiveClick( self, event ):
		appName = "{p}/{n}.app".format(p=self.output_dir_picker.GetPath(),n=self.app_name_input.GetValue())
		if os.path.exists(appName):
			shutil.rmtree(appName)
		os.makedirs("{app}/Contents/MacOS".format(app=appName))
		os.makedirs("{app}/Contents/Resources".format(app=appName))
		fname = "{app}/Contents/Info.plist".format(app=appName)
		cmd = self.exe_name_input.GetValue()
		fstr = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n" \
		       "<!DOCTYPE plist PUBLIC \"-//Apple//DTD PLIST 1.0//EN\" \"http://www.apple.com/DTDs/PropertyList-1.0.dtd\">\n" \
		       "<plist version=\"1.0\">\n" \
		       "<dict>\n" \
		       "\t<key>CFBundleIconFile</key>\n" \
		       "\t<string>????</string>\n" \
		       "\t<key>CFBundleSignature</key>\n" \
		       "\t<string>????</string>\n" \
		       "\t<key>CFBundleInfoDictionaryVersion</key>\n" \
		       "\t<string>1.0</string>\n" \
		       "\t<key>CFBundleExecutable</key>\n" \
		       "\t<string>run.sh</string>\n" \
		       "\t<key>CFBundlePackageType</key>\n" \
		       "\t<string>APPL</string>\n" \
		       "\t<key>CFBundleVersion</key>\n" \
		       "\t<string>1.0</string>\n" \
		       "</dict>\n" \
		       "</plist>"
		with open(fname,"w") as file:
			file.write(fstr)

		epath = "{app}/Contents/MacOS".format(app=appName)
		# copy_dir(self.tool_dir_picker.GetPath(),epath)
		# os.system("cd {ep} && ln -s {src}/{cmd} {cmd}".format(ep=epath,src=self.tool_dir_picker.GetPath(),cmd=cmd))
		fstr = "#!/bin/bash\n\ncd {p}\n./{c}".format(p=self.tool_dir_picker.GetPath(),c=cmd)
		fname = "{p}/run.sh".format(p=epath)
		with open(fname,"w") as file:
			file.write(fstr)

		os.system("chmod a+x {fn}".format(fn=fname))

		ShowTipsDialog("提示","制作完成")