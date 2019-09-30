#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   : android_mumu.py
@Author : Susie
@Create : 2019-09-30 11:24
@Desc   : 启动安卓模拟器上的应用
"""

from appium.webdriver.webdriver import WebDriver
from appium import webdriver


class AndroidClient(object):

    driver : WebDriver
    @classmethod
    def install_app(cls, appPackage, appActivity) -> WebDriver:  # 安装应用
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "mumu"
        caps["appPackage"] = appPackage
        caps["appActivity"] = appActivity
        caps["autoGrantPermissions"] = "true"  # 不显示第一次启动时各种权限
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(20)
        return cls.driver

    @classmethod
    def restart_app(cls, appPackage, appActivity) -> WebDriver:  # 重启应用无需安装
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "mumu"
        caps["appPackage"] = appPackage
        caps["appActivity"] = appActivity
        caps["autoGrantPermissions"] = True
        caps['noReset'] = True  # 重启，并保留之前的数据
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(20)
        return cls.driver

