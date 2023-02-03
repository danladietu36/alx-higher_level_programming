#!/usr/bin/python3
"""This is thd unittest module
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_return_ideal(self):
        lst = [2, 4, 6, 8]
        res = max_integer(lst)
        self.assertEqual(res, 8)
    def test_empty_list(self):
        lst = []
        res = max_integer(lst)
        self.assertEqual(res, None)
    def checklist_notint(self):
        with self.assertRaises(TypeError):
            max_integer([1, "a"])
