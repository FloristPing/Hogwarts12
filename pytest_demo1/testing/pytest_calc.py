# -*- coding: utf-8 -*-
'''
Created on 2020/5/21

@author: Amy.Guo
'''
# from pytest_demo1.python import Calc
from pytest_demo1.python.calc import Calc


class TestCalc:

    def setup(self):
        self.calc = Calc()

    def test_add(self):
        result = self.calc.add(1, 2)
        assert 3 == result

    def test_sub(self):
        result = self.calc.sub(4,2)
        assert 2 == result

    def test_div(self):
        result = self.calc.div(4,2)
        assert 2 == result

    def test_mul(self):
        result = self.calc.mul(4, 2)
        assert 8 == result
