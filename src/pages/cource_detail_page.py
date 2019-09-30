#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File   : cource_detail_page.py
@Author : Susie
@Create : 2019-09-30 11:45
@Desc   : 课程详情的各种操作
'''

from src.driver.android_mumu import AndroidClient
from src.tools.find_element import FindElement
import time


class CourseDetailPage(object):

    def getTQuestionype(self):  #识别是什么题目type: 1跟读题、2填词、3对话、4、只听题、5、单选题
        time.sleep(2)
        if(FindElement().ifExistById('com.qingclass.pandora:id/ll_voice')):  # 有对话框就是对话题
            type = 3
        elif(FindElement().ifExistById('com.qingclass.pandora:id/holder')):  # 有填空是填空题
            type = 2
        elif(FindElement().ifExistById('com.qingclass.pandora:id/right_button')):
            type = 4  # 是知识点/昨天回顾，只需听，可以直接下一步
        elif (FindElement().ifExistByXpath('//*[@resource-id="com.qingclass.pandora:id/tv_left" and @text="听原音"]')):  # 有左按钮（听原音）是跟读题
            type = 1  # 跟读题
        elif (FindElement().ifExistByXpath('//*[@resource-id="com.qingclass.pandora:id/tv_right" and @text="完成学习"]')):
            type = 0  # 课程结束页
        else:
            type = 5  # 单项选择题
        return type

    def passReadQuestion(self):  # 完成跟读题,type=1
        print("---------->>页面类型1 跟读题：")
        AndroidClient.driver.find_element_by_id("com.qingclass.pandora:id/middle").click()  #点击录音
        AndroidClient.driver.find_element_by_id('com.qingclass.pandora:id/wave').click()  # 暂停录音
        time.sleep(2) #评分会很久
        AndroidClient.driver.find_element_by_id('com.qingclass.pandora:id/right').click()  # 下一步

    def passInputQuestion(self): # 完成选词填空,type=2
        print("---------->>页面类型2 填空题：")
        hold_num = len(AndroidClient.driver.find_elements_by_id('com.qingclass.pandora:id/holder'))  # 获取空格数
        print("---------->>>>空格数：" + str(hold_num))
        for j in range(2): # 一般不会对，需要2次输入,才有下一步入口
            AndroidClient.driver.swipe(200, 400, 200, 50)
            eles = AndroidClient.driver.find_elements_by_xpath('//*[@class="android.widget.LinearLayout"]/*[@resource-id="com.qingclass.pandora:id/tv_des"]')
            for i in range(len(eles)):
                print("------------>>>>准备填空：" + str(i))
                eles[i].click()
                print("------------>>>>填空j结束：" + str(i))
                time.sleep(1)
            time.sleep(1)
            if FindElement().ifExistById('com.qingclass.pandora:id/bt_next'): #如果一次就对，不需要重复
                break
        AndroidClient.driver.find_element_by_id('com.qingclass.pandora:id/bt_next').click()

    def passTalkingQuestion(self):  # 完成对话题,type=3
        print("---------->>页面类型3 对话题：")
        for i in range(10):
            AndroidClient.driver.find_element_by_id("com.qingclass.pandora:id/middle").click()  # 点击录音
            if FindElement().ifExistById('com.qingclass.pandora:id/wave'):  # 如果有暂停录音就暂停
                AndroidClient.driver.find_element_by_id('com.qingclass.pandora:id/wave').click()
            if FindElement().ifExistById('com.qingclass.pandora:id/right'):  # 出现右侧按钮时表示对话到底，可以结束循环
                AndroidClient.driver.find_element_by_id('com.qingclass.pandora:id/right').click()  # 下一步
                break
            if FindElement().ifExistById('com.qingclass.pandora:id/tv_change_again'):  #出现切换角色时表示对话到底，可以结束循环
                AndroidClient.driver.find_element_by_id('com.qingclass.pandora:id/right').click()  # 下一步
                break
        time.sleep(2)

    def passListenQuestion(self):  # 完成只听题,type=4
        print("---------->>页面类型4 只听就好：")
        AndroidClient.driver.find_element_by_id("com.qingclass.pandora:id/right_button").click() # 直接点击下一步

    def passResult(self):  # 最后完成页面，type=0
        print("---------->>页面类型0 结束页：")
        AndroidClient.driver.find_elements_by_xpath('//*[@resource-id="com.qingclass.pandora:id/tv_right" and @text="完成学习"]').click()
        print("------------撒花✿✿ヽ(°▽°)ノ✿ 打卡成功 -------------")

    def passChooseQuestion(self): # 完成单选题,type=5
        print("---------->>页面类型5 单选题：")
        for i in range(2):
            AndroidClient.driver.find_elements_by_id("com.qingclass.pandora:id/tv_question")[2].click()
            print("---------选中选项")
        AndroidClient.driver.find_element_by_id("com.qingclass.pandora:id/tv_next").click()  # 点击下一步








