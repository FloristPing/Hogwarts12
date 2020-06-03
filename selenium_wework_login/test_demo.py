# -*- coding: utf-8 -*-
'''
Created on 2020/6/3

@author: Amy.Guo
'''

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestDemo:

    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    def test_demo(self):
        self.driver.get("https://home.testing-studio.com/")
        sleep(3)
        self.driver.find_element(By.LINK_TEXT, "分类").click()
        # 对文本进行定位
        sleep(5)

