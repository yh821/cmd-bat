# -*- coding: utf-8 -*-

import os
import random

from GenTemplate import *

allClassNameList = None
allMethodNameList = None
allPropertyNameList = None


class BaseInfo:
	access = None  # public or private
	typo = None  # void
	name = ""

	def __init__(self, name):
		self.name = name


class ClassInfo(BaseInfo):
	imports = None
	namespace = None
	implement = None  # MonoBehaviour
	methods = None
	attributes = None
	properties = None

	def __init__(self, name):
		BaseInfo.__init__(self, name)
		self.access = 'public'


class MethodInfo(BaseInfo):
	params = None  # BaseInfoList

	def __init__(self, name, typo):
		BaseInfo.__init__(self, name)
		self.typo = typo


class AttributeInfo(BaseInfo):
	canset = False

	def __init__(self, name, typo, canset=False):
		BaseInfo.__init__(self, name)
		self.access = 'public'
		self.typo = typo
		self.getset = canset


class PropertiesInfo(BaseInfo):
	value = None

	def __init__(self, name, typo):
		BaseInfo.__init__(self, name)
		self.typo = typo


# mc: 函数数量
# pc: 变量数量
# ac: 属性数量
def ClassGenerater(mc, pc, ac):
	_class = ClassInfo(GetClassName())
	# _class.implement = 'MonoBehaviour'
	_class.methods = []
	for i in range(0, mc):
		_class.methods.append(MethodInfo(GetMethodName(), GetRandomType()))
	_class.properties = []
	for i in range(0, pc):
		_class.properties.append(PropertiesInfo(GetVariableName(), GetRandomType()))
	_class.attributes = []
	for j in range(0, ac):
		_class.attributes.append(AttributeInfo(GetVariableName(), GetRandomType()))

	return _class


# 获取类名
def GetClassName(hasExt=True):
	global allClassNameList
	if allClassNameList is None:
		allClassNameList = []
		path = os.path.join(os.getcwd(), 'config/allClass.txt')
		with open(path, 'rU') as f:
			for line in f.readlines():
				allClassNameList.append(line.strip())
	index = random.randint(0, len(allClassNameList) - 1)
	className = allClassNameList[index]
	allClassNameList.remove(className)
	return className.capitalize() + (hasExt and GetRendomExt() or '')


# 获取函数名
def GetMethodName(isCap=True):
	global allMethodNameList
	if allMethodNameList is None:
		allMethodNameList = []
		allMethodFilePath = os.path.join(os.getcwd(), 'config/allMethod.txt')
		with open(allMethodFilePath, 'rU') as f:
			for line in f.readlines():
				allMethodNameList.append(line.strip())
	index = random.randint(0, len(allMethodNameList) - 1)
	methodName = allMethodNameList[index]
	allMethodNameList.remove(methodName)
	if isCap:
		return methodName.capitalize()
	else:
		return methodName


# 获取变量名
def GetVariableName():
	global allPropertyNameList
	if allPropertyNameList is None:
		allPropertyNameList = []
		path = os.path.join(os.getcwd(), 'config/allProperty.txt')
		with open(path, 'rU') as f:
			for line in f.readlines():
				allPropertyNameList.append(line.strip())
	index = random.randint(0, len(allPropertyNameList) - 1)
	propertyName = allPropertyNameList[index]
	allPropertyNameList.remove(propertyName)
	return propertyName


# 获取类型
def GetRandomType():
	index = random.randint(0, len(TypeList) - 1)
	return TypeList[index]


def GetRendomExt():
	index = random.randint(0, len(CtrlList) - 1)
	return CtrlList[index]


def WriteLine(content, append, tab=0):
	for i in range(0, tab):
		content += '\t'
	return content + append + '\r\n'


def PrintClass(info):
	tab = 0
	content = WriteLine('', info.access + ' class ' + info.name + (
			info.implement != None and (' : ' + info.implement) or ''), tab)
	content = WriteLine(content, '{', tab)
	tab += 1

	if info.properties != None:
		for m in info.properties:
			content = WriteLine(content, PrintProperty(m, tab))

	if info.attributes != None:
		for m in info.attributes:
			content = WriteLine(content, PrintAttribute(m, tab))

	if info.methods != None:
		for m in info.methods:
			content = WriteLine(content, PrintMethod(m, tab))

	tab -= 1
	content = WriteLine(content, '}', tab)

	return content


def PrintMethod(info, tab):
	param_str = ''
	if info.params != None:
		i = 0
		for arg in info.params:
			if i == 0:
				param_str += '{0} {1}'.format(arg.typo, arg.name)
			else:
				param_str += ', {0} {1}'.format(arg.typo, arg.name)

	content = '{0} {1} {2} ({3}) {{'.format(info.access or 'private', info.typo or 'void', info.name, param_str)
	content = WriteLine('', content, tab)
	tab += 1
	if info.typo in MethodList:
		methods = MethodList[info.typo]
		method_str = methods[random.randint(0, len(methods) - 1)]
		content = WriteLine(content, method_str.format(1, 2, 3), tab)
	tab -= 1
	content = WriteLine(content, '}', tab)
	return content


def PrintAttribute(info, tab):
	content = '{0} {1} {2} {{'.format(info.access, info.typo, info.name)
	content = WriteLine('', content, tab)
	tab += 1
	content = WriteLine(content, 'get {{ return {0}; }}'.format(TypeDefaultValue[info.typo]), tab)
	if info.canset:
		content = WriteLine(content, 'set {{ value = {0}; }}'.format(TypeDefaultValue[info.typo]), tab)
	tab -= 1
	content = WriteLine(content, '}', tab)

	return content


def PrintProperty(info, tab):
	content = WriteLine('', '{0} {1} {2};'.format(info.access or 'private', info.typo, info.name), tab)
	return content
