# -*- coding: utf-8 -*-

###########################################################################
## Class GenCSFrame
###########################################################################

from BaseFrame import *
from GenerateCSharp import *


class GenCSFrame(BaseFrame):

	def __init__(self, parent):
		BaseFrame.__init__(self, parent)
		self.RefreshGenCount()

	def RefreshGenCount(self, count=100):
		self.genCount = count

	def __del__(self):
		pass

	def OnClickStart(self, event):
		ClassGenerater(10,10,10)

	def OnOutputDirChanged(self, event):
		self.outputPath = self.m_outputDirPicker.GetPath()
		print ('输出路径:%s' % self.outputPath)

	def OnClassCountChanged( self, event ):
		self.RefreshGenCount(int(self.m_classCountTextCtrl.GetValue()))
