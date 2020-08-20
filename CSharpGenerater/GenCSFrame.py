# -*- coding: utf-8 -*-

###########################################################################
## Class GenCSFrame
###########################################################################

import sys
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


class GenCSFrame(BaseFrame):

	def __init__(self, parent):
		BaseFrame.__init__(self, parent)
		Redirect(self.m_logTextCtrl)

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
		self.RefreshGenCount()
		path = self.m_outputDirPicker.GetPath()
		if path == '':
			self.ShowMessageDialog('错误', '请选择输出路径')
			return
		space = GetNameSpace()
		outdir = os.path.join(path, space)
		if not os.path.exists(outdir):
			os.makedirs(outdir)
		for i in range(0, self.classCount):
			info = ClassGenerater(space, self.methodCount, self.attrCount, self.varCount)
			path = os.path.join(outdir, '%s.cs' % info.name)
			with open(path, 'w+') as f:
				f.write(PrintClass(info))
				print '生成文件: %s' % path
		print '========生成完成,类:{0},函数:{1},属性:{2},变量:{3}========'.format(
			self.classCount, self.methodCount, self.attrCount, self.varCount)

	def ShowMessageDialog(self, title, message):
		dlg = wx.MessageDialog(None, message, title, wx.OK)
		ret = dlg.ShowModal()
		if ret == wx.ID_OK:
			dlg.Destroy()
			pass
