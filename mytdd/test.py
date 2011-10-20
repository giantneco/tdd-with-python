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
        return self.is_cooler

    def is_light_lamp(self):
        return self.thermo < 29
