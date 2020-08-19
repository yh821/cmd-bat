# -*- coding: utf-8 -*-

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
	'string': 'string.Empty',
	'Vector2': 'Vector2.zero',
	'Vector3': 'Vector3.zero',
	'Color': 'Color.red',
}

TypeList = [
	'bool',
	'int',
	'short',
	'long',
	'float',
	'double',
	'ushort',
	'uint',
	'ulong',
	'string',
	# 'Vector2',
	# 'Vector3',
	# 'Color',
]

CtrlList = [
	'Manager',
	'Controller',
	'Handler',
	'Data',
	'View',
	'Library',
	'SDK',
	'Plugin',
	'Assets',
	'Bundle',
	'Model'
]

MethodList = {
	'int': [
		'{0} = {1} + {2};',
		'{0} = {1} - {2};',
		'{0} = {1} * {2};',
		'{0} = {1} / {2};',
		'{0} = {1};',
		'''
		for (int i=0;i<{0};i++) {{
			{1} += 1;
			{2} += {1};
		}}
		'''
	],
	'bool': [
		'{0} = {1} && {2};',
		'''
		if ({0}) {{
			{1} = !{2};
		}}
		''',
		'''
		if ({0} && {2}) {{
			{1} = !{1};
		}}
		''',
		'''
		if ({0} || {1}) {{
			{2} = !{2};
		}}
		''',
		'{0} = {1} || {2};',
	],
}
