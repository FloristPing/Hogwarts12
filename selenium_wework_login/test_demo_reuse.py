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
        # self.driver = webdriver.Chrome()
        has_options = Options()
        has_options.debugger_address = "127.0.0.1:9222"
        print(has_options)
        # 复用浏览器前需要关闭后台所有的chrome
        # chrome --remote-debugging-port=9222
        # 这两个端口要一致，才能联通复用
        self.driver = webdriver.Chrome(options=has_options)
        #   复用浏览器时该步骤报错


    def teardown(self):
        self.driver.quit()

    def test_demo(self):
        # self.driver.get("https://home.testing-studio.com/")
        sleep(3)
        self.driver.find_element(By.LINK_TEXT, "分类").click()
        # 对文本进行定位
        sleep(5)