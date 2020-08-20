# -*- coding: utf-8 -*-

numberValue = '0'

TypeDefaultValue = {
	'ushort': numberValue,
	'short': numberValue,
	'uint': numberValue,
	'int': numberValue,
	'ulong': numberValue,
	'long': numberValue,
	'float': numberValue,
	'double': numberValue,
	'bool': 'false',
	'string': 'string.Empty',
	'Vector2': 'Vector2.zero',
	'Vector3': 'Vector3.zero',
	'Color': 'Color.red',
}

TypeList = [
	# 'ushort',
	# 'short',
	'uint',
	'int',
	'long',
	'ulong',
	'float',
	'double',
	'bool',
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

numberMethod = [
	'return arg1 + arg2;',
	'''for (int i = 0; i < 20; i++) {{
				arg1 += arg2;
			}}
			return arg1;''',
	'''if (arg1 > 0) {{
				return arg1;
			}} else {{
				return arg2;
			}}'''
]

MethodList = {
	'ushort': numberMethod,
	'short': numberMethod,
	'uint': numberMethod,
	'int': numberMethod,
	'ulong': numberMethod,
	'long': numberMethod,
	'float': numberMethod,
	'double': numberMethod,
	'bool': [
		'return arg1 && arg2;',
		'''if (arg1) {{
				return arg1 || arg2;
			}} else {{
				return arg1 && arg2;
			}}'''
	],
	'string': [
		'return string.Concat (arg1, arg2);'
	]
}

classTemplate = '''//Auto-generated code
using System;
using System.Collections;

namespace {namespace}
{{
	public class {classname} {implement}
	{{
'''

methodTemplate = '''
		{access} {typo} {name} ({})
'''
