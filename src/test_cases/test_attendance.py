#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   : test_attendance.py    
@Author : Susie
@Create : 2019-09-30 14:45
@Desc   : 打卡潘多拉口语课/幸福课
"""

from src.pages.main_page import MainPage
from src.pages.cource_detail_page import CourseDetailPage


class TestAttendance(object):
    def test_Attendance(self):
        course_no = input("\n请输入你想打卡的课程号 1口语课 2哈佛幸福课：")
        print("Received input is : " + course_no)
        if course_no == "1":
            page = MainPage().goto_course_detail_page("口语课") # 进入口语课详情页
        else:
            page = MainPage().goto_course_detail_page("哈佛幸福课")  # 进入口语课详情页

        for k in range(70):
            print("\n-------- 页面："+str(k+1)+" ---------")
            type = page.getTQuestionype()   # type数值 1跟读题,2填词,3对话,4其他页面
            if type == 1:
                page.passReadQuestion()  # type=1,跟读
            elif type == 2:
                page.passInputQuestion()  # type=2,填词
            elif type == 3:
                page.passTalkingQuestion()  # type=3,对话
            elif type == 4:
                page.passListenQuestion()  # type=4,只听
            elif type == 5:
                page.passChooseQuestion()  # type=5,单选题
            else:
                page.passResult()   # type=0,单选题
                break




