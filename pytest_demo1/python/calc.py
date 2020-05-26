# -*- coding: utf-8 -*-
'''
Created on 2020/5/20

@author: Amy.Guo
'''


class Calc:

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        try:
            a / b
        except ZeroDivisionError:
            print("除数不能为0")
            return "异常"
        else:
            return a / b

