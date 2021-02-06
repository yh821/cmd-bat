#!/usr/bin/python
# -*- coding: UTF-8 -*-
#---------------------------------------------------------#

# import shutil,os
# #复制单个文件, 目标不能存在, 否则报错
# shutil.copy("C:\\a\\1.txt","C:\\b")
# #复制并重命名新文件
# shutil.copy("C:\\a\\2.txt","C:\\b\\121.txt")
# #复制整个目录(备份)
# shutil.copytree("C:\\a","C:\\b\\new_a")

# #删除文件
# os.unlink("C:\\b\\1.txt")
# os.unlink("C:\\b\\121.txt")
# #删除空文件夹
# try:
#     os.rmdir("C:\\b\\new_a")
# except Exception as ex:
#     print("错误信息："+str(ex))#提示：错误信息，目录不是空的
# #删除文件夹及内容
# shutil.rmtree("C:\\b\\new_a")

# #移动文件, 目标不能存在, 否则报错
# shutil.move("C:\\a\\1.txt","C:\\b")
# #移动文件夹, 目标不能存在, 否则报错
# shutil.move("C:\\a\\c","C:\\b")

# #重命名文件, 目标不能存在, 否则报错
# shutil.move("C:\\a\\2.txt","C:\\a\\new2.txt")
# #重命名文件夹, 目标不能存在, 否则报错
# shutil.move("C:\\a\\d","C:\\a\\new_d")

#---------------------------------------------------------#

# if ('/Bugly/' in '/iOS/Bugly/Bugly.framework/Bugly'):
# 	print('true')
# else:
# 	print('false')

#---------------------------------------------------------#

# line = 'http://n1041yjzxgb.xw66.top/foaalpios/login/serverlist '
# index = line.index(':')
# key = line[:index].strip()
# value = line[index+1:].strip()
# if key=='http':
# 	print(value)
# 	array = value.split('/')
# 	print(array)
# 	print(array[2])
# else:
# 	print(value)

#---------------------------------------------------------#

# import xlrd
# from datetime import date,datetime

# wb = xlrd.open_workbook('/Users/leo/Desktop/IOS内购产品ID.xlsx')#打开文件
# print(wb.sheet_names())#获取所有表格名字
# sheet1 = wb.sheet_by_index(0)#通过索引获取表格
# #sheet2 = wb.sheet_by_name('Sheet1')#通过名字获取表格
# #print(sheet1,sheet2)
# #print(sheet1.name,sheet1.nrows,sheet1.ncols)
# #rows = sheet1.row_values(2)#获取行内容
# #cols = sheet1.col_values(3)#获取列内容
# #print(rows)
# #print(cols)
# rmblist = sheet1.col_values(1)#获取rmb内容
# itemIds = sheet1.col_values(3)#获取产品ID内容
# itemIDs = {}
# for i in range(2, len(itemIds)):
# 	key = rmblist[i].encode('utf-8').replace('元','').strip()
# 	itemIDs[key]=itemIds[i]
# for key,value in itemIDs:
# 	print(key,value)
# #print(sheet1.cell(1,0).value)#获取表格里的内容，三种方式
# print(sheet1.cell_value(1,0))
# #print(sheet1.row(1)[0].value)

#---------------------------------------------------------#

# import pandas
# import numpy

# path = '/Users/leo/Desktop/IOS内购产品ID.numbers'
# data_file = pd.read_csv(path)
# print (data_file[0:3])

#---------------------------------------------------------#

# L1 = ['AdmIn','anny','LUCY','sandY','wILl']
# def normallize(name):
# 	#return name.upper()#全大写
# 	#return name.capitalize()#首字母大写其余小写
# 	return name.lower()#全小写
# L2 = list(map(normallize,L1))
# print(L2)

#---------------------------------------------------------#

# import os
# import sys

# print('sys.path:'+sys.path[0])
# print('sys.argv:'+sys.argv[0])
# print('__file__:'+__file__)
# print('os.getcwd():'+os.getcwd())
# print('os.path.realpath():'+os.path.realpath(__file__))
# print('(os.path.abspath(__file__)):'+os.path.abspath(__file__))
# print('os.path.dirname(os.path.realpath()):'+os.path.dirname(os.path.realpath(__file__)))
# print('os.path.dirname(os.path.abspath(__file__)):'+os.path.dirname(os.path.abspath(__file__)))

#---------------------------------------------------------#

# import os
# import sys
# print(sys.path)

#---------------------------------------------------------#

# list1 = [9,8,7,6,5]
# list1.sort()
# print list1

#---------------------------------------------------------#

# import os

# path = '/Users/m5pro/Documents/M5-C/release-2.0/Assets/Scripts'
# for root, directory, files in os.walk(path):  # 当前根,根下目录,目录下的文件
# 	for filename in files:
# 		name, suf = os.path.splitext(filename)  # 文件名,文件后缀
# 		if suf == '.cs':
# 			print os.path.join(root, filename)  # 把一串字符串组合成路径

#---------------------------------------------------------#

# import re
# # str = "if (info && 0 < [info[@\"sfsess\"] length])"\
# #       "if (info && 0 == [info[@\"sfsess\"] length])"\
# #       "if (info && 0 <= [info[@\"sfuid\"] length])"
# # key = re.findall("if.*?\(.+?\)",str)
# str="NSString *nstr=@\"Counrt\";"\
#     "if (c == d)"\now = int(time.time())
#     "NSData *data = [wd daf];"\
#     "bool b = c == d;"
# key = re.findall("[^=]+?[=]{1}[^=]+?;",str)
# print(key)

#---------------------------------------------------------#

# import time
# print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# print str(int(time.time()))

#---------------------------------------------------------#

# str1 = '/Users/m5pro/Documents/M5-C/ios-release-2.0/VerifyAssets/Mods'
# li = str1.rindex('/');
# print str1[0:li]

#---------------------------------------------------------#

# str1 = '666'
# iii = 666
# print type(str1)==str
# print type(iii)
# print type(iii)==int

#---------------------------------------------------------#

# import os
# import zipfile

# skin_path = "/Users/m5pro/Documents/M5-C/release-2.0/VerifyAssets/Mods/Mods_OnlyTest/iOS/skin"
# skin_zip = "{0}.zip".format(skin_path)
# with zipfile.ZipFile(skin_zip, 'w') as target:
# 	for i in os.walk(skin_path):
# 		for n in i[2]:
# 			path = ''.join((i[0], '/', n))
# 			zip_path = path.replace(skin_path, 'skin')
# 			target.write(path, zip_path)

#---------------------------------------------------------#

# class MyTest():
# 	def sayhi(self):
# 		print('hello world.')

# 	def func1(self):
# 		self.items={}

# 	def func2(self):
# 		if hasattr(self, 'items'):
# 			print('yes')
# pass

# obj = MyTest()
# obj.sayhi()
# obj.func1()
# obj.func2()

#---------------------------------------------------------#

# import Tkinter
# top = Tkinter.Tk()
# top.mainloop()

#---------------------------------------------------------#

# import wx  # 导入wx包
# app = wx.App()  # 创建一个应用程序对象
# frm = wx.Frame(None, title="Hello World")  # 创建一个界面
# frm.Show()  # 显示它
# app.MainLoop()   # 启动一个时间循环

#---------------------------------------------------------#

# str1='Hello'
# print 'h' in str1 
# print 'H' in str1
# num1=[1,2]
# print 1 in num1
# table = {'int':'1','float':'2','long':'3'}
# print None in table
# print '%s,%d,%2.2f' % ('test',2,134.1534)

#---------------------------------------------------------#

import re
# func_regex = re.compile(r'\w+\s+\w+\s*\(\w*\)\s*\{')   # 查找数字
# name_regex = re.compile(r'\b\w+\s*\(')
appId = re.compile(r'initWithAppid:@\"[\w\.]+?\"')
appName = re.compile(r'URLSchemes:@\"[\w\.]+?\"')

#with open('/Users/m5pro/Documents/M5-C/release-2.0/Assets/Editor/MixResource/FileNameTranslatorEditor.cs') as file:
with open('/Users/m5pro/Documents/M5-C/release/22KO_JuanSongLueLan_b131/iOS/Script/JuanSongLueLanAppController.mm') as file:
	content = file.read()
	result1 = appId.findall(content)
	result2 = appName.findall(content)
print result1
print result2
# with open('/Users/m5pro/Documents/func_name.txt', 'w+') as f:
# 	for v in result:
# 		array = name_regex.findall(v)
# 		if len(array)==1:
# 			f.write(array[0][:-1].strip()+'\n')

#---------------------------------------------------------#



#---------------------------------------------------------#



#---------------------------------------------------------#



#---------------------------------------------------------#



#---------------------------------------------------------#



#---------------------------------------------------------#



#---------------------------------------------------------#



#---------------------------------------------------------#



#---------------------------------------------------------#


