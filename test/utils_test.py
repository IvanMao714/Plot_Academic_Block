"""
!/usr/bin/env python
 -*- coding: utf-8 -*-
 @CreateTime    : 2024-05-08 16:35
 @Author  : Ivan Mao
 @File    : utils_test.py
 @Description : 
"""
import os
import unittest
from utils import format


class TestFormat(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_file.tex"

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_generate_doc_creates_file(self):
        format.generate_doc(self.test_file)
        self.assertTrue(os.path.exists(self.test_file))

    def test_generate_doc_writes_correct_content(self):
        format.generate_doc(self.test_file)
        with open(self.test_file, "r") as f:
            content = f.read()
        self.assertEqual(content, format.init_doc())

    def test_generate_doc_with_empty_string_as_filename(self):
        with self.assertRaises(Exception):
            format.generate_doc("")

    def test_generate_doc_with_none_as_filename(self):
        with self.assertRaises(Exception):
            format.generate_doc(None)


if __name__ == '__main__':
    unittest.main()
