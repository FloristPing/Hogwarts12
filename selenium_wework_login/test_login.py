# -*- coding: utf-8 -*-
'''
Created on 2020/6/3

@author: Amy.Guo
'''

import shelve
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestLogin:

    def setup(self):
        has_options = Options()
        has_options.debugger_address = "127.0.0.1:9223"
        print(has_options)
        # 复用浏览器前需要关闭后台所有的chrome
        # chrome --remote-debugging-port=9222
        # 这两个端口要一致，才能联通复用
        self.driver = webdriver.Chrome(options=has_options)
        #   复用浏览器时该步骤报错

    def teardown(self):
        self.driver.quit()

    def test_login(self):
        cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688854133768335'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'MCG2jjOCv4mpK0cIvFnZfZRRhX3isH47Bozt6iVocKjV9yqnZHrnd9rOZhYLETu3b8109lL8jiT0aSupya8SI4TS3cC-Oo-FiKrem_UUSNC31u6AOdoLZl5q17-5RLuY_JTgPzTWdBdHNr52_THqFWLvgRqG0occuwL8fgIPwvzWGbnuqKs7AEzTZk3NlELirz3k05ER41lxuBPmPHRnlXGvb0Xq2dZV-k6kxQHkpJcNkEzYddP_D40Zhk3qLw4FB9-ePQJ38xyE3FWEEDcOCQ'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688854133768335'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324956140936'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a6267671'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.logined', 'path': '/', 'secure': False, 'value': 'true'}, {'domain': '.qq.com', 'expiry': 1591261533, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.606640221.1591175129'}, {'domain': 'work.weixin.qq.com', 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '701032191'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '4072431461419381'}, {'domain': '.qq.com', 'expiry': 1591175189, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 1654247133, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1807111289.1591175129'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'Yvgw6a6c_y6xiJQKULfxt9n-3rfe9RqZndYtSXk_H2LmQpaIVbTf5Hz3XiCXX5On'}, {'domain': '.work.weixin.qq.com', 'expiry': 1593767136.275842, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}]
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # sleep(8)
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            #     expiry过期时间为小数时会报错
            self.driver.add_cookie(cookie)
        sleep(5)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(5)

    def test_login_shelve(self):
        # shelve.open打开或创建一个shelve对象,文件不存在则创建，存在则打开
        # 保存一份cookies到db，一个小型数据库
        db = shelve.open("cookies")
        db["cookies"] = self.driver.get_cookies()
        # 将cookies保存到db中
        # 第二次就可以不执行 db["cookies"] = self.driver.get_cookies()，直接获取cookies
        cookies = db["cookies"]
        print(cookies)
        # # 获取cookies
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            #     expiry过期时间为小数时会报错
            self.driver.add_cookie(cookie)
            sleep(5)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(5)
        db.close()
        sleep(1)





