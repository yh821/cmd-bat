# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class BaseFrame
###########################################################################

class BaseFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"输出位置", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.m_outputDirPicker = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"选择输出文件的路径", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE|wx.DIRP_SMALL )
		bSizer2.Add( self.m_outputDirPicker, 1, wx.ALL, 5 )


		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"文件个数", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer4.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.m_classCountTextCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_classCountTextCtrl, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"开始", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button1, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( bSizer3, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_outputDirPicker.Bind( wx.EVT_DIRPICKER_CHANGED, self.OnOutputDirChanged )
		self.m_classCountTextCtrl.Bind( wx.EVT_TEXT, self.OnClassCountChanged )
		self.m_button1.Bind( wx.EVT_BUTTON, self.OnClickStart )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnOutputDirChanged( self, event ):
		event.Skip()

	def OnClassCountChanged( self, event ):
		event.Skip()

	def OnClickStart( self, event ):
		event.Skip()


