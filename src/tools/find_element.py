#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   : find_element.py
@Author : Susie
@Create : 2019-09-30 12:03
@Desc   : 改造的元素定位方法
"""

from src.driver.android_mumu import AndroidClient


class FindElement(object):

    def ifExistById(self, ele_id):  # 传入元素resource_id，存在元素返回true，不存在返回false
        result = True
        try:
            AndroidClient.driver.find_element_by_id(ele_id)
        except Exception as e:
            result = False
        return result

    def ifExistByXpath(self, ele_xpath):  # 传入元素xpath，存在元素返回true，不存在返回false
        result = True
        try:
            AndroidClient.driver.find_element_by_xpath(ele_xpath)
        except Exception as e:
            result = False
        return result

    def ifExistByIdSwipeUp(self, ele_id):  # 传入元素resource_id，存在元素返回true，不存在则上拉页面循环找几次
        result = False
        for i in range(1, 3):
            result = FindElement().if_exist_by_id(ele_id)
            if result:
                break
            AndroidClient.driver.swipe(200, 400, 200, 20)
        return result

    def findElementById(self, ele_id):  # 传入元素resource_id，存在元素返回ele_object，不存在返回null
        try:
            ele = AndroidClient.driver.find_element_by_id(ele_id)
        except Exception as e:
            ele = None
        return ele

    def findElementsById(self, ele_id):  # 传入元素resource_id，存在元素返回ele_objects，不存在返回null
        try:
            eles = AndroidClient.driver.find_element_by_id(ele_id)
        except Exception as e:
            eles = None
        return eles

    def findElementByXpath(self, ele_xpath):  # 传入元素xpath，存在元素返回ele_object，不存在返回null
        try:
            ele = AndroidClient.driver.find_element_by_xpath(ele_xpath)
        except Exception as e:
            ele = None
        return ele

    def findElementsByXpath(self, ele_xpath):  # 传入元素xpath，存在元素返回ele_object，不存在返回null
        try:
            eles = AndroidClient.driver.find_elements_by_xpath(ele_xpath)
        except Exception as e:
            eles = None
        return eles
