# -*- coding: utf-8 -*-

numberValue = '0'

TypeDefaultValue = {
	'short': numberValue,
	'int': numberValue,
	'long': numberValue,
	'float': numberValue,
	'double': numberValue,
	'ushort': numberValue,
	'uint': numberValue,
	'ulong': numberValue,
	'bool': 'false',
	'string': 'string.Empty',
	'Vector2': 'Vector2.zero',
	'Vector3': 'Vector3.zero',
	'Color': 'Color.red',
}

TypeList = [
	'short',
	'ushort',
	'int',
	'uint',
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
	'short': numberMethod,
	'int': numberMethod,
	'long': numberMethod,
	'float': numberMethod,
	'double': numberMethod,
	'ushort': numberMethod,
	'uint': numberMethod,
	'ulong': numberMethod,
	'bool': [
		'return arg1 && arg2;',
		'''if (arg1) {{
				return arg1 || arg2;
			}} else {{
				return arg1 && arg2;
			}}'''
	],
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
