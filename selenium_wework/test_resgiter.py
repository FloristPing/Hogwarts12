# -*- coding: utf-8 -*-
'''
Created on 2020/5/19

@author: Amy.Guo
'''
import os
from selenium import webdriver
from selenium_wework.index import Index

class TestRegister:

    def setup(self):
        self.index = Index()

    def test_register(self):
        self.index.goto_login().goto_register().register()
        self.index.goto_resister().register()