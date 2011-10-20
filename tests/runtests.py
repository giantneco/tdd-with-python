#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mytdd.test import succ
from mytdd.test import AirConditionar
import unittest
from unittest import TestCase


class MyFirstTest(TestCase):

    def testAssertIt(self):
        self.assertEqual(1, 1)

class AirConditionarTest(TestCase):

    def testSetThermo(self):
        ac = AirConditionar(15)
        ac.set_thermo(28)
        self.assertEqual(28, ac.thermo)

    def testIsCooler(self):
        ac = AirConditionar(15)
        self.assert_(ac.is_cooler())
        
    def testCoolerWith28(self):
        ac = AirConditionar(28)
        self.assert_(ac.is_light_lamp())

    def testCoolerWith27(self):
        ac = AirConditionar(27)
        self.assert_(not ac.is_light_lamp())

    def testCoolerWith35(self):
        ac = AirConditionar(35)
        self.assert_(ac.is_light_lamp())

    def testSetCooler(self):
        ac = AirConditionar(35)
        ac.set_cooler()
        self.assert_(ac.is_cooler())

    def testSetHeater(self):
        ac = AirConditionar(35)
        ac.set_heater()
        self.assert_(not ac.is_cooler())

    def testToggleCoolerHeater(self):
        ac = AirConditionar(35)
        ac.set_heater()
        self.assert_(not ac.is_cooler())
        ac.set_cooler()
        self.assert_(ac.is_cooler())

    def testHeaterWith20(self):
        ac = AirConditionar(20)
        ac.set_heater()
        self.assert_(ac.is_light_lamp())

if __name__ == '__main__':
    unittest.main()
