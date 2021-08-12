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
## Class BaseForm
###########################################################################

class BaseForm ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"B站视频封面提取工具", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( -1,-1 ), wx.Size( -1,-1 ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, u"输入av/bv/视频链接（支持批量导入）", wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.m_textCtrl1.SetMinSize( wx.Size( -1,100 ) )

		bSizer2.Add( self.m_textCtrl1, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"开始提取", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_button2.SetMinSize( wx.Size( 100,100 ) )

		bSizer2.Add( self.m_button2, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer1.Add( self.m_staticText2, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer3.Add( self.m_staticText4, 1, wx.ALL, 5 )

		self.m_gauge1 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge1.SetValue( 0 )
		bSizer3.Add( self.m_gauge1, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer3, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button2.Bind( wx.EVT_BUTTON, self.OnStart )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnStart( self, event ):
		event.Skip()


