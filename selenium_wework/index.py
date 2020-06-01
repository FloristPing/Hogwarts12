# -*- coding: utf-8 -*-
'''
Created on 2020/6/1

@author: Amy.Guo
'''


"""
1. 快捷导入 ALT+ENTER
2. PO原则：一个页面跳转到另一个页面，使用return返回页面PO
登陆：
    - 点击登录，进入登录页面
    - 执行goto login，进入页面后，返回页面po, 即Login PO
注册
    - 从登陆页面进入注册页面，进行注册
    - 直接进入注册页面，进行注册
    - 执行goto resgiter，进入页面后，返回页面po, 即Resgiter PO
    
3. test中最好不要出现self._driver, element locator等

"""
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium_wework.Register import Resgiter
from selenium_wework.login import Login


class Index:

    def __init__(self):
        self._driver = webdriver.Chrome()
        self._driver.get('https://work.weixin.qq.com/')

    def goto_login(self):
        """
        1.find  element
        2.click login
        :return:
        """
        self._driver.find_element(By.CSS_SELECTOR, 'a.index_top_operation_loginBtn').click()
        return Login()

    def goto_resgiter(self):
        """
        1.find  element
        2.click resgiter
        :return:
        """
        self._driver.find_element(By.CSS_SELECTOR, 'a.index_head_info_pCDownloadBtn').click()
        return Resgiter()


