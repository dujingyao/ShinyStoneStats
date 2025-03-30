from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# 正确初始化Chrome驱动
# 创建服务实例，自动下载和管理 ChromeDriver
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

try:
    # 打开百度
    driver.get('https://www.baidu.com')
    time.sleep(3)

    # 使用新的语法查找搜索框
    search_box = driver.find_element(By.ID, "kw")
    search_box.send_keys("C语言中文网")
    search_box.submit()

    time.sleep(3)

finally:
    # 关闭浏览器
    driver.quit()