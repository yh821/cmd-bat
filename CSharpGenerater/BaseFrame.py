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


		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"文件数量范围", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer7.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.m_classMinTextCtrl = wx.TextCtrl( self, wx.ID_ANY, u"200", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		bSizer7.Add( self.m_classMinTextCtrl, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_classMaxTextCtrl = wx.TextCtrl( self, wx.ID_ANY, u"300", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		bSizer7.Add( self.m_classMaxTextCtrl, 0, wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"函数数量范围", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer7.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.m_methodMinTextCtrl = wx.TextCtrl( self, wx.ID_ANY, u"30", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		bSizer7.Add( self.m_methodMinTextCtrl, 0, wx.ALL, 5 )

		self.m_methodMaxTextCtrl = wx.TextCtrl( self, wx.ID_ANY, u"50", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		bSizer7.Add( self.m_methodMaxTextCtrl, 0, wx.ALL, 5 )


		bSizer4.Add( bSizer7, 1, wx.EXPAND, 5 )

		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"属性数量范围", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer9.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.m_attrMinTextCtrl = wx.TextCtrl( self, wx.ID_ANY, u"15", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		bSizer9.Add( self.m_attrMinTextCtrl, 0, wx.ALL, 5 )

		self.m_attrMaxTextCtrl = wx.TextCtrl( self, wx.ID_ANY, u"20", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		bSizer9.Add( self.m_attrMaxTextCtrl, 0, wx.ALL, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"变量数量范围", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer9.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.m_varMinTextCtrl = wx.TextCtrl( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		bSizer9.Add( self.m_varMinTextCtrl, 0, wx.ALL, 5 )

		self.m_varMaxTextCtrl = wx.TextCtrl( self, wx.ID_ANY, u"10", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		bSizer9.Add( self.m_varMaxTextCtrl, 0, wx.ALL, 5 )


		bSizer4.Add( bSizer9, 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer4, 0, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"开始", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button1, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( bSizer3, 0, wx.EXPAND, 5 )

		self.m_logTextCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer1.Add( self.m_logTextCtrl, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.OnClickStart )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnClickStart( self, event ):
		event.Skip()


