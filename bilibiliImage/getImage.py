#!/usr/bin/python
# coding: UTF-8

import sys
import requests
import bs4
import urllib
from BaseForm import *

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.51"}

class GetImage(BaseForm):

	def __init__(self, parent):
		BaseForm.__init__(self, parent)
		self.Init()

	def Init(self):
		pass

	def OnStart( self, event ):
		av = self.m_textCtrl1.GetValue()
		if av!=None and av!="":
			url = "https://www.bilibili.com/video/%s" % av
			res = requests.get(url, headers=header)
			res.encoding = res.apparent_encoding
			soups = bs4.BeautifulSoup(res.text, "html.parser")
			target = soups.find("meta", itemprop="thumbnailUrl")
			image = target["content"]
			urllib.request.urlretrieve(image, "image\%s.jpg" % av)
			# print(image)
		else:
			print("请填写BV号")

if __name__ == "__main__":
    app = wx.App()
    form = GetImage(None)
    form.Show()
    app.MainLoop()