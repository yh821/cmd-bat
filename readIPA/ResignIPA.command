#!/usr/bin/env python
# coding: utf-8
import os
import sys

path = os.path.dirname(sys.argv[0])
os.chdir(path)
#导入wx模块
try:
    import wx
except:
    print ('\033[31m' + '缺少wx模块，正在安装wx模块，请等待...' + '\033[0m')
    success = os.system('sudo pip install wxpython')
    if success == 0:
        print('\033[7;32m' + 'wx模块安装成功.' + '\033[0m')
        import wx
    else:
      print ('\033[31m' + 'wx安装失败，自己搞吧!' + '\033[0m')
      quit()

reload(sys)
sys.setdefaultencoding('utf-8')

from ResignIPAFrame import *
# 入口
if __name__ == "__main__":
    app = wx.App()
    frame = ResignIPAFrame(None)
    frame.Show()
    app.MainLoop()