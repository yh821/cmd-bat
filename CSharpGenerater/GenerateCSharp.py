# -*- coding: utf-8 -*-

import os
import random


class BaseInfo:
	access = None  # public or private
	typo = None  # void
	name = ""

	def __init__(self, name):
		self.name = name


class ClassInfo(BaseInfo):
	implement = None  # MonoBehaviour
	methods = None
	attributes = None
	properties = None
	type_map = None

	def __init__(self, name):
		BaseInfo.__init__(self, name)


class MethodInfo(BaseInfo):
	return_type = ""
	params = None


class AttributeInfo(BaseInfo):
	getset = 1  # 1:get; 2:get,set


class PropertiesInfo(BaseInfo):
	value = None


allClassNameList = None
allMethodNameList = None
allPropertyNameList = None

TypeDefaultValue = {
	'short': '0',
	'int': '0',
	'long': '0',
	'float': '0.0f',
	'double': '0.0',
	'ushort': '0',
	'uint': '0',
	'ulong': '0',
	'bool': 'false',
	'string': 'null'
	# 'Vector2': 'Vector2.zero',
	# 'Vector3': 'Vector3.zero',
	# 'Color': 'Color.red',
}

TypeList = [
	'short',
	'int',
	'long',
	'float',
	'double',
	'ushort',
	'uint',
	'ulong',
	'bool',
	'string'
]


# mc: 函数数量
# pc: 变量数量
# ac: 属性数量
def ClassGenerater(mc, pc, ac):
	_class = ClassInfo(GetClassName())
	# _class.implement = 'MonoBehaviour'
	_class.methods = []
	for i in range(0, pc):
		_class.methods.append(MethodInfo(GetMethodName()))
	_class.properties = []
	for i in range(0, pc):
		_class.properties.append(PropertiesInfo(GetVariableName()))
	_class.attributes = []
	for j in range(0, ac):
		_class.attributes.append(AttributeInfo(GetVariableName()))

	return _class


# 获取类名
def GetClassName(isCap=True):
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
	if isCap:
		return className.capitalize()
	else:
		return className


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
	global TypeList
	index = random.randint(0, len(TypeList) - 1)
	return TypeList[index]


def PrintContent(content, append, tab):
	for i in range(0, tab):
		content += '\t'
	content = content + append + '\r\n'

def PrintClass(info):
	content = info.access + ' class ' + info.name + (info.implement != None and (' : ' + info.implement) or '')

	return content


def PrintMethod(str, tab):
	content = ''
	return content


def PrintAttribute(str, tab):
	content = ''
	return content


def PrintProperty(str, tab):
	content = ''
	return content
