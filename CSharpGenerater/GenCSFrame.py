# -*- coding: utf-8 -*-

###########################################################################
## Class GenCSFrame
###########################################################################

import sys
import shutil
import re
from BaseFrame import *
from GenerateCSharp import *


class Redirect:
	def __init__(self, outputCtrl):
		self.stdout = sys.stdout
		self.opCtrl = outputCtrl
		sys.stdout = self

	def write(self, log):
		self.stdout.write(log)
		self.opCtrl.write(log)

	def flush(self):
		pass


folderFlag = 'AutoGenCS_'


class GenCSFrame(BaseFrame):

	def __init__(self, parent):
		BaseFrame.__init__(self, parent)
		self.InitPath()
		Redirect(self.m_logTextCtrl)

	def InitPath(self):
		self.project_path = '/Users/m5pro/Documents/M5-C/release-2.0'
		self.m_projectDirPicker.SetPath(self.project_path)
		self.script_path = os.path.join(self.project_path, 'Assets/Scripts')
		self.plugin_path = os.path.join(self.project_path, 'Assets/Plugins')

	def RefreshGenCount(self):
		classMin = int(self.m_classMinTextCtrl.GetValue())
		classMax = int(self.m_classMaxTextCtrl.GetValue())
		methodMin = int(self.m_methodMinTextCtrl.GetValue())
		methodMax = int(self.m_methodMaxTextCtrl.GetValue())
		attrMin = int(self.m_attrMinTextCtrl.GetValue())
		attrMax = int(self.m_attrMaxTextCtrl.GetValue())
		varMin = int(self.m_varMinTextCtrl.GetValue())
		varMax = int(self.m_varMaxTextCtrl.GetValue())

		self.classCount = random.randint(classMin, classMax)
		self.methodCount = random.randint(methodMin, methodMax)
		self.attrCount = random.randint(attrMin, attrMax)
		self.varCount = random.randint(varMin, varMax)

	def __del__(self):
		pass

	def OnClickStart(self, event):
		global folderFlag
		if not (os.path.exists(self.script_path) and os.path.exists(self.plugin_path)):
			self.ShowMessageDialog('错误', '工程目录不存在, 请重新选择')
			return
		print '\033[32m================开始生成代码================\033[0m'
		self.DoGenCSFile(self.script_path)
		self.DoGenCSFile(self.plugin_path)

	def DoGenCSFile(self, output):
		self.RefreshGenCount()
		space = GetNameSpace()
		output_dir = os.path.join(output, folderFlag + space)
		if not os.path.exists(output_dir):
			os.makedirs(output_dir)
		for i in range(0, self.classCount):
			info = ClassGenerater(space, self.methodCount, self.attrCount, self.varCount)
			path = os.path.join(output_dir, '%s.cs' % info.name)
			with open(path, 'w+') as f:
				f.write(PrintClass(info))
				print '生成文件: %s' % path
		print '\033[32m========生成完成,类:{0},函数:{1},属性:{2},变量:{3}========\033[0m'.format(
			self.classCount, self.methodCount, self.attrCount, self.varCount)

	def OnClickDelete(self, event):
		self.DeleteFolder(self.script_path)
		self.DeleteFolder(self.plugin_path)

	def DeleteFolder(self, path):
		for folder in os.listdir(path):
			if folder.startswith(folderFlag):
				dirt = os.path.join(path, folder)
				if os.path.isdir(dirt):
					shutil.rmtree(dirt)
					print '删除文件夹:%s' % dirt

	def OnProjectDirChanged(self, event):
		self.project_path = self.m_projectDirPicker.GetPath()
		self.script_path = os.path.join(self.project_path, 'Assets/Scripts')
		self.plugin_path = os.path.join(self.project_path, 'Assets/Plugins')
		print ('工程目录:%s' % self.project_path)

	def ShowMessageDialog(self, title, message):
		dlg = wx.MessageDialog(None, message, title, wx.OK)
		ret = dlg.ShowModal()
		if ret == wx.ID_OK:
			dlg.Destroy()
			pass

	def OnClickGetFuncName(self, event):
		script_files = self.GetFiles(self.script_path, '.cs')
		plugin_files = self.GetFiles(self.plugin_path, '.cs')
		script_files.extend(plugin_files)
		CSharp_files = list(set(script_files))

		output_path = self.m_outputDirPicker.GetPath()
		func_regex = re.compile(r'\w+\s+\w+\s*\(\w*\)\s*\{')
		name_regex = re.compile(r'\b\w+\s*\(')

		result = []
		for cs in CSharp_files:
			with open(cs) as file:
				content = file.read()
				result.append(func_regex.findall(content))
		with open(os.path.join(output_path, 'func_name.txt'), 'w+') as f:
			for r in result:
				for v in r:
					array = name_regex.findall(v)
					if len(array) == 1:
						f.write(array[0][:-1].strip() + '\n')
		print '导出成功'

	def GetFiles(self, dir, ext):
		allFiles = []
		for root, directory, files in os.walk(dir):  # 当前根,根下目录,目录下的文件
			for filename in files:
				name, suf = os.path.splitext(filename)  # 文件名,文件后缀
				if suf == ext:
					allFiles.append(os.path.join(root, filename))  # 把一串字符串组合成路径
		return allFiles
