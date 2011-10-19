#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mytdd.test import succ
import unittest

class MyFirstTest(unittest.TestCase):

    def testAssertIt(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()
