#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   : main_page.py
@Author : Susie
@Create : 2019-09-30 11:43
@Desc   : 打开app并前往指定页面
"""

from src.driver.android_mumu import AndroidClient
from src.pages.cource_detail_page import CourseDetailPage
from src.tools.find_element import FindElement
import time


class MainPage(object):
    def __init__(self):
        AndroidClient.restart_app("com.qingclass.pandora", "ui.SplashActivity")  # 打开app首页

    def goto_course_detail_page(self, courseName):  # 进入课程详情页,需传入课程中文名
        time.sleep(2)
        AndroidClient.driver.swipe(200, 50, 200, 400)
        time.sleep(1)
        AndroidClient.driver.swipe(200, 50, 200, 400)  # 默认会进入课程列表，这里要下拉到已购课程列表
        courseXpath = '//*[@resource-id="com.qingclass.pandora:id/tv_course" and @text="' + courseName + '"]'
        AndroidClient.driver.find_element_by_xpath(courseXpath).click()  # 进入口语课详情
        if FindElement().ifExistById('com.qingclass.pandora:id/tv_sure'): # 有可能出现学习新旧课程弹窗
            AndroidClient.driver.find_element_by_id('com.qingclass.pandora:id/tv_sure').click()
        else:
            AndroidClient.driver.find_element_by_id('com.qingclass.pandora:id/tv_enter').click()  # 进入今天课程
        return CourseDetailPage()

