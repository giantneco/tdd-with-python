#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" functions """

def succ(arg):
    """succeeded of interger"""
    return arg + 1

class AirConditionar():
    """AirConditonar Class"""

    def __init__(self, thermo):
        self.thermo = thermo
        self.is_cooler_ = True
        pass

    def set_thermo(self, thermo):
        """ set thermo to AirConditonar """
        self.thermo = thermo

    def is_cooler(self):
        return self.is_cooler_

    def is_light_lamp(self):
        if self.is_cooler_:
            return self.thermo >= 28
        else:
            return self.thermo <= 20

    def set_cooler(self):
        self.is_cooler_ = True

    def set_heater(self):
        self.is_cooler_ = False
