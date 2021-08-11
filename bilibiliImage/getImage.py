#!/usr/bin/python
# coding: UTF-8

import sys
import re
import requests
import bs4
import urllib
from collections import deque
from BaseForm import *

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.51"}

class GetImage(BaseForm):
	#https://www.bilibili.com/video/BV1x7411d7o4/?spm_id_from=
	#https://www.bilibili.com/video/av170001
	def __init__(self, parent):
		BaseForm.__init__(self, parent)
		self.Init()

	def Init(self):
		self.logs = deque(maxlen=10)
		pass

	def OnStart(self, event):
		vid = self.m_textCtrl1.GetValue()
		if vid=="":
			self.log("请填写av/bv号或视频链接")
			return
		match = re.compile(r'(av\d{6}|BV[a-zA-Z0-9]{10})', re.S)
		vids = re.findall(match, vid)
		print(vids)
		for vid in vids:
			self.SaveImage(vid)

	def SaveImage(self, vid):
		try:
			url = "https://www.bilibili.com/video/%s" % vid
			res = requests.get(url, headers=header)
			res.encoding = res.apparent_encoding
			soups = bs4.BeautifulSoup(res.text, "html.parser")
			target = soups.find("meta", itemprop="thumbnailUrl")
			image = "image\%s.jpg" % vid
			urllib.request.urlretrieve(target["content"], image)
			self.log(image)
		except Exception:
			self.log("av/bv号有误")

	def log(self, msg):
		self.logs.append(msg)
		content = ""
		for log in self.logs:
			content += log + '\n'
			pass
		self.m_staticText2.SetLabel(content)
		pass

if __name__ == "__main__":
    app = wx.App()
    form = GetImage(None)
    form.Show()
    app.MainLoop()