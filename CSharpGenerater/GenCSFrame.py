# -*- coding: utf-8 -*-

###########################################################################
## Class GenCSFrame
###########################################################################

from BaseFrame import *
from GenerateCSharp import *


class GenCSFrame(BaseFrame):

	def __init__(self, parent):
		BaseFrame.__init__(self, parent)

	def __del__(self):
		pass

	def OnClickStart(self, event):
		ClassGenerater()

	def OnOutputDirChanged(self, event):
		self.outputPath = self.m_outputDirPicker.GetPath()
		print ('输出路径:%s' % self.outputPath)
