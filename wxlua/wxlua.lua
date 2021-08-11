----------------------------------------------------------------------------
-- Lua code generated with wxFormBuilder (version Oct 26 2018)
-- http://www.wxformbuilder.org/
----------------------------------------------------------------------------

-- Load the wxLua module, does nothing if running from wxLua, wxLuaFreeze, or wxLuaEdit
package.cpath = package.cpath..";./?.dll;./?.so;../lib/?.so;../lib/vc_dll/?.dll;../lib/bcc_dll/?.dll;../lib/mingw_dll/?.dll;"
require("wx")

UI = {}


-- create MyFrame1
UI.MyFrame1 = wx.wxFrame (wx.NULL, wx.wxID_ANY, "wxlua", wx.wxDefaultPosition, wx.wxSize( 500,300 ), wx.wxDEFAULT_FRAME_STYLE+wx.wxTAB_TRAVERSAL )
	UI.MyFrame1:SetSizeHints( wx.wxDefaultSize, wx.wxDefaultSize )

	UI.bSizer1 = wx.wxBoxSizer( wx.wxVERTICAL )

	UI.m_button1 = wx.wxButton( UI.MyFrame1, wx.wxID_ANY, "MyButton", wx.wxDefaultPosition, wx.wxDefaultSize, 0 )
	UI.bSizer1:Add( UI.m_button1, 0, wx.wxALL, 5 )


	UI.MyFrame1:SetSizer( UI.bSizer1 )
	UI.MyFrame1:Layout()

	UI.MyFrame1:Centre( wx.wxBOTH )

	UI.MyFrame1:Show(true)

wx.wxGetApp():MainLoop()
