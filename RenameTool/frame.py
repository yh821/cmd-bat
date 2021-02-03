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
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,350 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"build目录", wx.DefaultPosition, wx.Size( 65,-1 ), 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer3.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.build_dir_path = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE|wx.DIRP_SMALL )
		bSizer3.Add( self.build_dir_path, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer1.Add( bSizer3, 0, wx.EXPAND, 5 )

		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Mods目录", wx.DefaultPosition, wx.Size( 65,-1 ), 0 )
		self.m_staticText7.Wrap( -1 )

		bSizer8.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.mod_dir_path = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE|wx.DIRP_SMALL )
		bSizer8.Add( self.mod_dir_path, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer1.Add( bSizer8, 0, wx.EXPAND, 5 )

		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText81 = wx.StaticText( self, wx.ID_ANY, u"命名数量", wx.DefaultPosition, wx.Size( 65,-1 ), 0 )
		self.m_staticText81.Wrap( -1 )

		bSizer9.Add( self.m_staticText81, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		rn_num_choiceChoices = []
		self.rn_num_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), rn_num_choiceChoices, 0 )
		self.rn_num_choice.SetSelection( 0 )
		bSizer9.Add( self.rn_num_choice, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer1.Add( bSizer9, 0, wx.EXPAND, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"重命名IPA文件", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_button2, 0, wx.ALL|wx.EXPAND, 5 )

		self.log_output = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer1.Add( self.log_output, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.build_dir_path.Bind( wx.EVT_DIRPICKER_CHANGED, self.OnBuildDirSelect )
		self.mod_dir_path.Bind( wx.EVT_DIRPICKER_CHANGED, self.OnModDirSelect )
		self.m_button2.Bind( wx.EVT_BUTTON, self.OnRenameClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnBuildDirSelect( self, event ):
		event.Skip()

	def OnModDirSelect( self, event ):
		event.Skip()

	def OnRenameClick( self, event ):
		event.Skip()


