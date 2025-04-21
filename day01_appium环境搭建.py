# -*- coding: utf-8 -*-
# @Author : 大仙
# @File : day01_appium环境搭建
# @Software: PyCharm
"""
课题：appium环境搭建

知识点：
    1.appium介绍
    2.环境搭建
模块安装pip install Appium-python-client
"""

import time, random
from appium import webdriver


class DYAction(object):

    def __init__(self, num: int = None):
        """初始化配置, 设置Desired Capabilities参数"""
        self.desired_caps = {
            'platformName': 'Android',
            'deviceName': 'SM-G955F',
            'appPackage': 'com.ss.android.ugc.aweme',
            'appActivity': '.splash.SplashActivity'
        }
        """指定Appium Server"""
        self.server = 'http://localhost:4723/wd/hub'
        """创建driver对象"""
        self.driver = webdriver.Remote(self.server, self.desired_caps)
        """获取模拟器/手机的分辨率(px)"""
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        """设置滑动初始坐标和滑动距离"""
        self.start_x = width // 2  # 屏幕宽度中心点
        self.start_y = height // 3 * 2  # 屏幕高度从上开始到下三分之二处
        self.distance = height // 2  # 滑动距离：屏幕高度一半的距离
        """初始化滑动次数"""
        self.num = num

    def comments(self):
        """
        app开启之后点击一次屏幕，确保页面的展示
        :return:
        """
        time.sleep(random.randint(5, 10))
        self.driver.tap([(500, 1200)], 500)

    def scroll(self):
        """
        滑动函数
        :return:
        """
        start_num = 0
        if self.num is None:
            self.num = 20
        """循环滑动"""
        while True:
            print('滑动ing----logging----logging!!!')
            self.driver.swipe(self.start_x, self.start_y,
                              self.start_x, self.start_y-self.distance)
            """等待视频加载"""
            time.sleep(random.randint(1, 3))
            """调用解析视频数据，提取"""
            self.get_mp4_info_data()
            """判断是否退出"""
            if self.num == start_num:
                break
            start_num += 1

    def get_mp4_info_data(self):
        """
        获取视频的详细信息
        :return:
        """
        print(self.driver.page_source)

    def run_main(self):
        self.comments()
        time.sleep(random.randint(5, 10))
        self.scroll()


if __name__ == '__main__':
    d = DYAction()
    d.run_main()


















































































