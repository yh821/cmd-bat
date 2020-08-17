# -*- coding: utf-8 -*-

class ClassInfo:
	p = ""
	name = "default"
	implement = None
	attributes = None
	typemap = None

	def __init__(self, name):
		self.name = name


def ClassGenerater():
	_class = ClassInfo(GetNextClassName())
	username = {}
	username[_class.name] = True
	pass


def GetNextClassName():
	return "666"
