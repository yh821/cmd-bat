# -*- coding: utf-8 -*-

import os
import random

from GenTemplate import *

allClassNameList = None
allMethodNameList = None
allPropertyNameList = None
namespace = ''


class BaseInfo:
	access = False  # public or private
	typo = None  # void
	name = ""

	def __init__(self, name, access):
		self.name = name
		if access:
			self.access = 'public'
		else:
			self.access = 'private'


class ClassInfo(BaseInfo):
	imports = None
	namespace = None
	implement = None  # MonoBehaviour
	methods = None
	attributes = None
	properties = None

	def __init__(self, name):
		BaseInfo.__init__(self, name, True)


class MethodInfo(BaseInfo):
	havearg = False

	def __init__(self, name, access, typo, havearg):
		BaseInfo.__init__(self, name, access)
		self.typo = typo
		self.havearg = havearg


class AttributeInfo(BaseInfo):
	state = 1  # 1-3
	haveset = False

	def __init__(self, name, typo, state, haveset):
		BaseInfo.__init__(self, name, True)
		self.typo = typo
		self.state = state
		self.haveset = haveset


class PropertiesInfo(BaseInfo):
	havevalue = False

	def __init__(self, name, access, typo, havevalue):
		BaseInfo.__init__(self, name, access)
		self.typo = typo
		self.havevalue = havevalue


# mc: 函数数量
# pc: 变量数量
# ac: 属性数量
def ClassGenerater(ns, mc, pc, ac):
	_class = ClassInfo(GetClassName())
	# _class.implement = 'MonoBehaviour'
	_class.namespace = ns
	_class.methods = []
	for i in range(0, mc):
		_class.methods.append(
			MethodInfo(GetMethodName(), random.random() > 0.5, GetRandomType(), random.random() > 0.5))
	_class.properties = []
	for i in range(0, pc):
		_class.properties.append(
			PropertiesInfo(GetVariableName(), random.random() > 0.5, GetRandomType(), random.random() > 0.5))
	_class.attributes = []
	for j in range(0, ac):
		_class.attributes.append(
			AttributeInfo(GetVariableName(), GetRandomType(), random.randint(1, 3), random.random() > 0.5))

	return _class


def GetNameSpace():
	global namespace
	if namespace == '':
		namespace = GetClassName()
	return namespace


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
	content = classTemplate.format(namespace=info.namespace, classname=info.name, implement=info.implement or '')
	tab = 2
	if info.properties != None:
		for m in info.properties:
			content = WriteLine(content, PrintProperty(m, tab))

	if info.attributes != None:
		for m in info.attributes:
			content = WriteLine(content, PrintAttribute(m, tab))

	if info.methods != None:
		for m in info.methods:
			content = WriteLine(content, PrintMethod(m, tab))

	content += '\t}\r\n}'

	return content


def PrintMethod(info, tab):
	param_str = ''
	if info.havearg:
		param_str = '{0} arg1, {0} arg2'.format(info.typo)
	content = '{0} {1} {2} ({3}) {{'.format(info.access, info.typo, info.name, param_str)
	content = WriteLine('', content, tab)
	tab += 1
	if not info.havearg:
		defvalue = TypeDefaultValue[info.typo]
		content = WriteLine(content, '{0} arg1 = {1};'.format(info.typo, defvalue), tab)
		content = WriteLine(content, '{0} arg2 = {1};'.format(info.typo, defvalue), tab)
	if info.typo in MethodList:
		methods = MethodList[info.typo]
		method_str = methods[random.randint(0, len(methods) - 1)]
		content = WriteLine(content, method_str.format(1, 2, 3), tab)
	tab -= 1
	content = WriteLine(content, '}', tab)
	return content


def PrintAttribute(info, tab):
	content = ''
	value = TypeDefaultValue[info.typo]
	if info.state == 3:
		content = WriteLine(content, 'private {0} _{1} = {2};'.format(info.typo, info.name, value), tab)
	content = WriteLine(content, '{0} {1} {2} {{'.format(info.access, info.typo, info.name), tab)
	tab += 1
	if info.state == 3:
		content = WriteLine(content, 'get {{ return _{0}; }}'.format(info.name), tab)
		if info.haveset:
			content = WriteLine(content, 'set {{ _{0} = value; }}'.format(info.name), tab)
	elif info.state == 2:
		content = WriteLine(content, 'get;', tab)
		if info.haveset:
			content = WriteLine(content, 'set;', tab)
	else:
		content = WriteLine(content, 'get {{ return {0}; }}'.format(value), tab)
	tab -= 1
	content = WriteLine(content, '}', tab)

	return content


def PrintProperty(info, tab):
	content = ''
	if info.havevalue:
		content = WriteLine(content, '{0} {1} _{2} = {3};'.format(
			info.access, info.typo, info.name, TypeDefaultValue[info.typo]), tab)
	else:
		content = WriteLine(content, '{0} {1} _{2};'.format(info.access, info.typo, info.name), tab)
	return content
