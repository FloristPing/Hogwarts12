# -*- coding: utf-8 -*-
'''
Created on 2020/6/1

@author: Amy.Guo
'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium_wework import Register
class Login:

    def __init__(self, driver: WebDriver):
        """
        :param driver: WebDriver
        driver 传进来进行复用
        加个WebDriver标签，进行解释
        私有变量，外部不能访问，前面加_

        """
        self._driver = driver

    def scanf(self):
        """
        扫描
        :return:
        """
        pass

    def goto_resgiter(self):
        """
        没有return时返回：AttributeError: 'NoneType' object has no attribute 'register'
        :return:
        """
        time.sleep(3)
        self._driver.find_element(By.CSS_SELECTOR, "a.login_registerBar_link").click()
        return Register(self._driver)