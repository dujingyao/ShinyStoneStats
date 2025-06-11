# -*- coding: utf-8 -*-
"""
    总体过程总结：
    1.# -*- coding: utf-8 -*-:告诉 Python 解释器该源代码文件使用 UTF-8 编码
                              使 Python 能够正确处理文件中的中文等非 ASCII 字符
                              防止出现编码相关的错误，如 SyntaxError: Non-UTF-8 code
    2.导入所需模块
    3.service = Service():
        创建 ChromeDriver 服务实例
        管理浏览器驱动程序的启动和关闭
        处理浏览器和 WebDriver 之间的通信
      options = webdriver.ChromeOptions():
        创建浏览器配置对象
        允许你设置浏览器的各种选项（如无头模式、窗口大小、代理等）
        即使不添加任何选项，也需要创建这个实例
      driver = webdriver.Chrome(service=service, options=options):
        使用上面的 service 和 options 初始化 Chrome 浏览器
        创建与浏览器的连接
        返回可以控制浏览器的 WebDriver 实例pip install selenium-wirepip install selenium-wire
    4.使用 driver.get() 方法打开指定的 URL
    5.使用 driver.find_element() 方法查找页面元素
    6.使用 driver.execute_script() 方法执行 JavaScript 代码：
        scrollIntoView() 是一个 JavaScript 方法，使页面滚动到指定元素可见的位置
        arguments[0] 引用传入的第一个参数，即 element
        整体效果是将页面滚动到"切换城市"按钮可见的位置
    7.使用element.click()模拟鼠标点击element对应的位置
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
import time

# 正确初始化Chrome驱动
# 创建服务实例，自动下载和管理 ChromeDriver
service = Service()
# 创建浏览器选项实例
options = webdriver.ChromeOptions()
# 初始化浏览器
driver = webdriver.Chrome(service=service, options=options)

try:
    # 打开百度新闻
    driver.get('https://news.baidu.com/')
    time.sleep(5)
    # 滚动到特定元素
    element = driver.find_element(By.ID, "change-city")
    # 点击切换城市
    driver.execute_script("arguments[0].scrollIntoView();", element)
    element.click()
    time.sleep(3)
    # 点击河南
    #<a href="javascript:void(0);" mon="col=10&amp;locname=河南&amp;locid=0" prop="河南||0">河南</a>
    local=driver.find_element(By.XPATH, '//a[@prop="河南||0"]')
    local.click()
    time.sleep(3)
    # 点击新乡
    #<a href="javascript:void(0);" mon="col=10&amp;locname=新乡&amp;locid=4468" prop="新乡|4468|0">新乡</a>
    city=driver.find_element(By.XPATH, '//a[@prop="新乡|4468|0"]')
    city.click()
    time.sleep(3)
    # 爬取新闻列表
    # <ul class="ulist focuslistnews" id="localnews-focus"><li class="bold-item"><span class="dot"></span><a href="http://baijiahao.baidu.com/s?id=1827794191652980896" mon="c=civilnews&amp;ct=0&amp;a=27&amp;col=8&amp;locname=%E6%96%B0%E4%B9%A1&amp;locid=4468" target="_blank">有求必应 无事不扰！原阳县召开民营企业座谈会</a></li><li><a href="http://baijiahao.baidu.com/s?id=1827737791228054356" mon="c=civilnews&amp;ct=0&amp;a=27&amp;col=8&amp;locname=%E6%96%B0%E4%B9%A1&amp;locid=4468" target="_blank">新疆生产建设兵团第六师芳草湖农场综治中心：只进...</a></li><li><a href="http://baijiahao.baidu.com/s?id=1827830557554993421" mon="c=civilnews&amp;ct=0&amp;a=27&amp;col=8&amp;locname=%E6%96%B0%E4%B9%A1&amp;locid=4468" target="_blank">暖心接力！河南延津多方协作助走失妇女平安回家</a></li><li><a href="http://baijiahao.baidu.com/s?id=1827882732474592376" mon="c=civilnews&amp;ct=0&amp;a=27&amp;col=8&amp;locname=%E6%96%B0%E4%B9%A1&amp;locid=4468" target="_blank">“开门红”点燃建设热浪，“进度条”加速通车目标</a></li><li><a href="http://baijiahao.baidu.com/s?id=1827793443790652227" mon="c=civilnews&amp;ct=0&amp;a=27&amp;col=8&amp;locname=%E6%96%B0%E4%B9%A1&amp;locid=4468" target="_blank">北大荒集团共青农场有限公司：关注安全教育 共建...</a></li><li><a href="http://baijiahao.baidu.com/s?id=1827698242768815576" mon="c=civilnews&amp;ct=0&amp;a=27&amp;col=8&amp;locname=%E6%96%B0%E4%B9%A1&amp;locid=4468" target="_blank">河南工学院驻村工作队助农增收暖民心</a></li><li><a href="http://baijiahao.baidu.com/s?id=1827656187573214277" mon="c=civilnews&amp;ct=0&amp;a=27&amp;col=8&amp;locname=%E6%96%B0%E4%B9%A1&amp;locid=4468" target="_blank">对校园欺凌说“不”，吴家洼监狱为师生带来“法治...</a></li><li><a href="http://baijiahao.baidu.com/s?id=1827849937437549784" mon="c=civilnews&amp;ct=0&amp;a=27&amp;col=8&amp;locname=%E6%96%B0%E4%B9%A1&amp;locid=4468" target="_blank">新乡高新区：“行走的思政课”——让榜样力量浸润...</a></li></ul>
    # 使用XPath直接获取所有新闻标题
    news_titles = driver.find_elements(By.XPATH, '//ul[@id="localnews-focus"]//a')
    for title in news_titles:
        print(title.text)

finally:
    driver.quit()