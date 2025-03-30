from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # 新增导入

# 指定驱动路径（注意路径中的反斜杠要转义或使用原始字符串）
driver_path = r"E:\yao Python\venv\Scripts\chromedriver.exe"

# 通过Service对象加载驱动
driver = webdriver.Chrome(service=Service(driver_path))