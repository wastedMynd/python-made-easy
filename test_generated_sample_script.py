# LICENSE
#
#  /usr/bin/python
#  -*- coding: utf-8 -*-
#
#  test_generated_sample_script.py
#  
#  Copyright 2021 Sizwe Mkhonza
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
Built-in Dependencies, Imports 
'''
from unittest import TestCase
import os

'''
User Defined Dependencies, Imports 
'''
from generate_sample_script import _created_sample_folder, _created_sample_file_name
from generate_sample_script import _get_sample_script_file_name_to_create
from generate_sample_script import create_sample_script, get_test_class_name
from generate_sample_script import SampleScriptGeneratorHelper
from generate_sample_script import UserDefinedSampleScriptHelper


'''
Tests
'''


class TestGetTestClassName(TestCase):
	"""
	
	"""
	
	def test_get_test_class_name_with_trilling_numeric(self):
		"""
		
		"""
		
		# Given 
		test_sample_script_file_name = 'test_sample_script_2.py'
		expected_test_sample_script_class_name = 'TestSampleScript2'
		
		# When
		actual_test_sample_script_class_name = get_test_class_name(test_sample_script_file_name)
		
		# Then
		self.assertTrue(
			actual_test_sample_script_class_name == expected_test_sample_script_class_name,
			f'{actual_test_sample_script_class_name} != {expected_test_sample_script_class_name}'
		)
		
		pass
	
	def test_get_test_class_name(self):
		"""
		
		"""
		
		# Given 
		test_sample_script_file_name = 'test_sample_script.py'
		expected_test_sample_script_class_name = 'TestSampleScript'
		
		# When
		actual_test_sample_script_class_name = get_test_class_name(test_sample_script_file_name)
		
		# Then
		self.assertTrue(
			actual_test_sample_script_class_name == expected_test_sample_script_class_name,
			f'{actual_test_sample_script_class_name} != {expected_test_sample_script_class_name}'
		)
		
		pass
	
	pass


class TestCreateSampleScriptChanged(TestCase):
	"""
	
	"""

	def setUp(self):
		"""
		create 'created_new_sample_script.py' file 
		"""
		_, actual_is_sample_script_present = create_sample_script()
		# Then
		self.assertTrue(
			actual_is_sample_script_present,
			f'actual_is_sample_script_present: {actual_is_sample_script_present} is not True'
		)
		pass
	 
	def tearDown(self):
		"""
		remove 'self.given_sample_script_file_name' file 
		"""
		os.remove(SampleScriptGeneratorHelper().get_sample_script_path())
		pass 
	
	def test__get_sample_script_file_name_to_create(self):
		"""
		"""
		# Given
		expected_changed_sample_script_file_name = "sample_script_2.py"
		
		# When
		actual_changed_sample_script_file_name = _get_sample_script_file_name_to_create(_created_sample_folder, _created_sample_file_name)

		# Then, actual_changed_sample_script_file_name == is expected_changed_sample_script_file_name
		self.assertTrue(
			 #And, if the expression is true, then the test fails
			actual_changed_sample_script_file_name == expected_changed_sample_script_file_name,
			f'actual_changed_sample_script_file_name: {actual_changed_sample_script_file_name} is not expected_changed_sample_script_file_name: {expected_changed_sample_script_file_name}'
		)
	pass


class TestCreateUserDefinedSampleScriptChanged(TestCase):
	"""
	
	"""

	def setUp(self):
		"""
		create 'created_new_sample_script.py' file 
		"""
		given_sample_script_file_name = "created_new_sample_script.py"
		
		_, self.actual_is_sample_script_present = create_sample_script(_created_sample_folder, given_sample_script_file_name)
		
		pass
	 
	def tearDown(self):
		"""
		remove 'self.given_sample_script_file_name' file 
		"""
		given_sample_script_file_name = "created_new_sample_script.py"
		os.remove(UserDefinedSampleScriptHelper(_created_sample_folder, given_sample_script_file_name).get_sample_script_path())
		pass 
	
	def test__get_sample_script_file_name_to_create(self):
		"""
		"""
		
		# Given
		given_sample_script_file_name = "created_new_sample_script.py"
		
		# Then
		self.assertTrue(
			self.actual_is_sample_script_present,
			f'self.actual_is_sample_script_present: {self.actual_is_sample_script_present} is not True'
		)

		# Given
		expected_changed_sample_script_file_name = "created_new_sample_script_2.py"
		
		# When
		actual_changed_sample_script_file_name = _get_sample_script_file_name_to_create(_created_sample_folder, given_sample_script_file_name)

		# Then, actual_changed_sample_script_file_name == is expected_changed_sample_script_file_name
		self.assertTrue(
			 #And, if the expression is true, then the test fails
			actual_changed_sample_script_file_name == expected_changed_sample_script_file_name,
			f'actual_changed_sample_script_file_name: {actual_changed_sample_script_file_name} is not expected_changed_sample_script_file_name: {expected_changed_sample_script_file_name}'
		)
	pass


class TestCreateUserDefinedSampleScriptChanged2ndOrder(TestCase):
	"""
	
	"""

	def setUp(self):
		"""
		create 'created_new_sample_script.py' file 
		"""
		
		self.samples = [
			"created_new_sample_script.py",
			"created_new_sample_script_2.py",
		]
		
		for sample in self.samples:
			self.actual_sample_script , self.actual_is_sample_script_present = create_sample_script(_created_sample_folder, sample)
		
		pass
	 
	def tearDown(self):
		"""
		remove 'self.given_sample_script_file_name' file 
		"""
		
		for sample in self.samples:
			os.remove(UserDefinedSampleScriptHelper(_created_sample_folder, sample).get_sample_script_path())
		
		pass 
	
	def test__get_sample_script_file_name_to_create(self):
		"""
		"""
		
		# Given
		given_sample_script_file_name = self.actual_sample_script
		
		# Then
		self.assertTrue(
			self.actual_is_sample_script_present,
			f'self.actual_is_sample_script_present: {self.actual_is_sample_script_present} is not True'
		)

		# Given
		expected_changed_sample_script_file_name = "created_new_sample_script_3.py"
		
		# When
		actual_changed_sample_script_file_name = _get_sample_script_file_name_to_create(_created_sample_folder, given_sample_script_file_name)

		# Then, actual_changed_sample_script_file_name == is expected_changed_sample_script_file_name
		self.assertTrue(
			 #And, if the expression is true, then the test fails
			actual_changed_sample_script_file_name == expected_changed_sample_script_file_name,
			f'actual_changed_sample_script_file_name: {actual_changed_sample_script_file_name} is not expected_changed_sample_script_file_name: {expected_changed_sample_script_file_name}'
		)
	pass



class TestCreateSampleScript(TestCase):
	"""
	
	"""

	def tearDown(self):
		"""
		remove 'sample_cript.py' file 
		"""
		os.remove(SampleScriptGeneratorHelper().get_sample_script_path())
		pass 

	def test_create_sample_script(self):
		"""
		"""
		
		# Given
		
		# When
		actual_sample_script_file_name, actual_is_sample_script_present = create_sample_script()
		
		# Then, actual_is_sample_script_present must be True
		self.assertTrue(
			actual_is_sample_script_present,
			f'actual_is_sample_script_present: {actual_is_sample_script_present}'
		)
		
		self.assertTrue(
			actual_sample_script_file_name == _created_sample_file_name,
			f'actual_sample_script_file_name: "{actual_sample_script_file_name}" is not "{_created_sample_file_name}"!'
		)
	pass


class TestCreateUserDefinedSampleScript(TestCase):
	"""
	
	"""

	def tearDown(self):
		"""
		remove 'sample_cript.py' file 
		"""
		expected_sample_script_file_name = "created_new_sample_script.py"
		os.remove(UserDefinedSampleScriptHelper(_created_sample_folder, expected_sample_script_file_name).get_sample_script_path())
		pass 

	def test_create_sample_script(self):
		"""
		"""
		
		# Given
		expected_sample_script_file_name = "created_new_sample_script.py"
				
		# When
		actual_sample_script_file_name, actual_is_sample_script_present = create_sample_script(_created_sample_folder, expected_sample_script_file_name)
		
		# Then, actual_is_sample_script_present must be True
		self.assertTrue(
			actual_is_sample_script_present,
			f'actual_is_sample_script_present: {actual_is_sample_script_present}'
		)
		
		self.assertTrue(
			actual_sample_script_file_name == expected_sample_script_file_name,
			f'actual_sample_script_file_name: "{actual_sample_script_file_name}" is not "{expected_sample_script_file_name}"!'
		)
	pass

