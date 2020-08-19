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
		self.RefreshGenCount()

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
		outputPath = self.m_outputDirPicker.GetPath()
		if outputPath == '':
			self.ShowMessageDialog('错误', '请选择输出路径')
			return
		for i in range(0, self.classCount):
			info = ClassGenerater(self.methodCount, self.attrCount, self.varCount)
			path = os.path.join(outputPath, '%s.cs' % info.name)
			with open(path, 'w+') as f:
				f.write(PrintClass(info))
				print '生成C#文件: %s' % path
		print '================生成完成================'

	def OnClassCountChanged(self, event):
		self.RefreshGenCount(int(self.m_classCountTextCtrl.GetValue()))

	def ShowMessageDialog(self, title, message):
		dlg = wx.MessageDialog(None, message, title, wx.OK)
		ret = dlg.ShowModal()
		if ret == wx.ID_OK:
			dlg.Destroy()
			pass
