# -*- coding: utf-8 -*-
'''
Created on 2020/6/1

@author: Amy.Guo
'''
# https://ceshiren.com/t/topic/2207
# 使用 cookies 登录企业微信，并点击通讯录
# 使用shelve对数据临时存储

import time
import shelve
from selenium import webdriver

class TestCookies():

    def setup(self):
        self._driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.url = ("https://work.weixin.qq.com/wework_admin/frame")


    def teardown(self):
        self._driver.quit()

    def test_cookies(self):
        self._driver.get(self.url)
        # get_cookies()获取cookies
        # self.db["cookies"] = self.driver.get_cookies()
        # 获取cookies使用shelve存到本地db[cookies]中
        # db['cookies'] = self.driver.get_cookies()
        # 使用cookies看是否生效
        db = shelve.open("cookies")
        cookies = db['cookie']
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self._driver.add_cookie(cookie)
        self._driver.get(self.url)
        time.sleep(3)
        # 同步关闭db
        db.close()
        # 不加等待会报错，所以加了1秒
        time.sleep(1)

