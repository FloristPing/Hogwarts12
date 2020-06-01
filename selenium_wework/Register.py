# -*- coding: utf-8 -*-
'''
Created on 2020/6/1

@author: Amy.Guo
'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Resgiter:

    def __init__(self, driver: WebDriver):
        """
        :param driver: WebDriver
        driver 传进来进行复用
        加个WebDriver标签，进行解释
        私有变量，外部不能访问，前面加_
        """
        self._driver = driver

    def resgiter(self):
        """
        1.输入用户名，密码
        2.点击注册按钮
        :return:
        """
        time.sleep(5)
        self._driver.find_element(By.ID, "corp_name").send_keys("user111222333")
        self._driver.find_element(By.ID, "manager_name").send_keys("admin123456")
        # 点击注册按钮
        time.sleep(5)
        self._driver.quit()
        # 测试后记得清理环境，退出driver
        return True