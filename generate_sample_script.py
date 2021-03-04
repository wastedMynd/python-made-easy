'''
This module, generates; a sample python script file

LICENSE:
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  generate_sample_script.py
#  
#  Copyright 2021 Sizwe Mkhonza <Sizwe Mkhonza@DESKTOP-1DIKRLT>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

'''

'''
Built-in Dependencies, Imports 
'''
import os
import re
from datetime import datetime


'''
User defined,imports
'''


'''
Feature Overview
'''

_created_sample_folder = os.path.abspath('.') # places, created sample; on local project folder... 


_created_sample_file_name = 'sample_script.py' # or can be; user defined; if present; increment file counter.


_substitute_place_holders = [] # used for performance substitution; of placeholders

"""
Helper Features
"""


def get_test_class_name(sample_script_file_name)->str:
	"""
	
	"""
	# Given ...
	re_filter = '^(\d+)?\.py'
	replace_chr = '.py'
	with_chr = ''
	test_class_name = ''

	# When ...
	filter_out = lambda word: re.match(re_filter, word)
	replace = lambda word: word.replace(replace_chr, with_chr).title()
	update_test_class_name_with = lambda word: match.group(1) if (match:=filter_out(word)) else replace(word)

	# Then ...
	for word in sample_script_file_name.split('_'):
		test_class_name += update_test_class_name_with(word)

	# And ...
	return test_class_name


def get_replacements(sample_script_file_name):
	"""
	
	"""
	return [
			{
				'regex':'^#\s+\$file.py',
				'target':'$file.py',
				'replacement':sample_script_file_name,
				'occurs': 1,
			},
			{
				'regex':'^#\s+\$python$',
				'target':'$python',
				'replacement':'/usr/bin/python',
				'occurs': 1,
			},
			{
				'regex':'^#\s+Created\s+on\s+\$datetime',
				'target':'$datetime',
				'replacement':str(datetime.now()),
				'occurs': 1,
			},
			{
				'regex':'^#\s+Copyright\s+\$year*',
				'target':'$year',
				'replacement':str(datetime.now().year),
				'occurs': 1,
			},
			{
				'regex':'^#\s+Copyright\s+\d+\s+by\s+\$user',
				'target':'$user',
				'replacement':'Sizwe Mkhonza',
				'occurs': 1,
			},
			{
				'regex':'^class\s+\$testClass(TestCase)*',
				'target':'$testClass',
				'replacement':get_test_class_name(sample_script_file_name),
				'occurs': 1,
			},
	]


class SampleScriptGeneratorHelper(object):
	"""
	
	"""

	def get_sample_script_path(self)->str:
		"""
		
		"""
		return os.path.join(
			_created_sample_folder,
			_created_sample_file_name
		)

	def is_sample_script_present(self)->bool:
		"""
		
		"""
		return os.path.exists(self.get_sample_script_path())


class UserDefinedSampleScriptHelper(SampleScriptGeneratorHelper):
	"""
	
	"""

	def __init__(self,user_defined_folder=_created_sample_folder, user_defined_sample_script_file_name=_created_sample_file_name):
		super()
		
		self.user_defined_folder = user_defined_folder
		self.user_defined_sample_script_file_name = user_defined_sample_script_file_name
		pass

	def get_sample_script_path(self)->str:
		"""
		
		"""
		return os.path.join(
			self.user_defined_folder,
			self.user_defined_sample_script_file_name
		)

	def is_sample_script_present(self)->bool:
		"""
		
		"""
		return os.path.exists(self.get_sample_script_path())

	pass


def get_sample_script_text_line_by_line(sample_script_file_name=_created_sample_file_name):
	"""
	This feature, gets the sample_script.txt text, line by line
	:returns: a generator instance 
	"""
	
	# Given that, the 'sample_script.txt' file is located on this
	base_folder = os.path.abspath('.')

	# And, the sample_script.txt, file name varible must be declared as
	matches_test_sample_script = re.match('^test_*', sample_script_file_name)
	sample_script_text_file = 'sample_script.txt' if not matches_test_sample_script else 'test_sample_script.txt'

	# And, also the complete path declare, for sample_script_text_file
	# as
	sample_script_text_file_path = os.path.join(base_folder, sample_script_text_file)

	# When, I open the sample_script_text_file_path; in read mode 'r',
	# I would, get a file object as file;
	# that has the features; to get, the text content. 

	with open(sample_script_text_file_path, 'r') as file:

		# And, I can get the file's lines 
		for line_content in file.readlines():

			# Then, the line content, is yield
			yield line_content


def substitute_place_holders(line_content)->str: #[tobe tested]
	"""
	
	"""
	occuried = [] 

	for replacement in _substitute_place_holders:
		if re.match(replacement['regex'], line_content):
			line_content = line_content.replace(replacement['target'], replacement['replacement'])
			if replacement['occurs'] >= 1:
				replacement['occurs'] -= 1
				occuried.append(replacement)
	for occur in occuried:
		if occur['occurs'] == 0:
			_substitute_place_holders.remove(occur)
	
	return line_content


def _get_next_sample_script_file_number()->int:
	file_number = 2
	while True:
		yield file_number
		file_number += 1


def _get_next_sample_script_file_name(user_defined_folder=_created_sample_folder, next_sample_script_file_name=_created_sample_file_name)->str: #[Tested]
	"""
	
	"""
	
	next_replacement_sample_script_file_name = None
	
	for file_number in _get_next_sample_script_file_number():
		
		replacement = '_' + str(file_number)
		
		next_file_matched = re.match('([a-z|A-Z]+_?)+((_\d+)+)?(.py)', next_sample_script_file_name)
		
		if next_file_matched and (next_file_group_number := next_file_matched.group(2)):
			# lets replace x, where x==int; on 'sample_script_x.py'
			next_replacement_sample_script_file_name = next_sample_script_file_name.replace(
				next_file_group_number,
				replacement
			)
		else:
			# lets insert x, where x==int; on 'sample_script.py', to yield 'sample_script_x.py'
			next_replacement_sample_script_file_name = next_sample_script_file_name.replace(
				extention := next_file_matched.group(4),
				replacement + extention
			)
		
		# lets create a UserDefinedSampleScriptHelper instance, and evaluate...
		if not UserDefinedSampleScriptHelper(user_defined_folder, next_replacement_sample_script_file_name).is_sample_script_present():
			break
	
	return next_replacement_sample_script_file_name


"""
Core Features
"""

def _process_substitute_place_holders(sample_script_file_name=_created_sample_file_name):
	"""
	
	"""
	for line_content in get_sample_script_text_line_by_line(sample_script_file_name):
		yield substitute_place_holders(line_content)


def _get_sample_script_file_content(sample_script_file_name=_created_sample_file_name)->str:
	"""
	
	"""
	file_content = ''
	
	for line in _process_substitute_place_holders(sample_script_file_name):
		file_content += line
	
	return file_content


def _get_sample_script_file_name_to_create(user_defined_folder=_created_sample_folder, sample_script_file_name=_created_sample_file_name)->str:
	"""
	
	"""
	is_sample_script_present = UserDefinedSampleScriptHelper(user_defined_folder, sample_script_file_name).is_sample_script_present()
	
	if is_sample_script_present:
		file_to_create = _get_next_sample_script_file_name(user_defined_folder, sample_script_file_name)
	elif not is_sample_script_present and (sample_script_file_name == _created_sample_file_name or not sample_script_file_name):
		file_to_create = _created_sample_file_name
	else:
		file_to_create = sample_script_file_name
	
	return file_to_create


def create_sample_script(user_defined_folder=_created_sample_folder, user_defined_sample_file_name=_created_sample_file_name)->tuple:
	"""
	
	"""
	
	sample_script_file_name = _get_sample_script_file_name_to_create(user_defined_folder, user_defined_sample_file_name)
	sample_script_path = UserDefinedSampleScriptHelper(user_defined_folder, sample_script_file_name).get_sample_script_path()

	global _substitute_place_holders
	_substitute_place_holders = get_replacements(sample_script_file_name)

	with open(sample_script_path, 'w') as sample_script_file:
		sample_script_file.write(_get_sample_script_file_content(user_defined_sample_file_name))
		return sample_script_file_name, True
	
	pass


def process_sample_creation(args):
	samples = args
	
	if len(samples) == 1:
		samples.append(_created_sample_folder)
		samples.append(_created_sample_file_name)
	elif len(samples) == 2:
		samples.append(_created_sample_file_name)

	
	for sample in samples[2:]:
		
		sample_script_file_name, result = create_sample_script(samples[1], sample)
		print(
			'\n\n {\n\n\t "script":',
			f'"{sample_script_file_name}",\n\t',
			'"result":',
			'"The script; was successfully created!",' if result else '"The script; was not created!",',
			'\n\t "folder":',
			f'"{samples[1]}",\n\n',
			'}\n\n'
		)


def main(args):
	process_sample_creation(args)
	return 0


'''
Demonstrations & Testing
'''
if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
