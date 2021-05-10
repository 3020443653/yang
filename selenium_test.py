#coding = utf-8
from selenium import webdriver
from time import sleep,ctime
import os

options = webdriver.ChromeOption()
#这里是chrome浏览器可执行文件的地址
options.binary_location = "C:/Users/30204/AppData/Local/Google/Chrome/Application/chrome.exe"
#这里是浏览器驱动：chromedriver的下载地址
chrome_driver_binary = "C:/Users/30204/AppData/Local/Google/Chrome/Applicatio/chromedriver.exe"
#这里是要测试的网页，打开网页
driver.get("http://www.baidu.com")
sleep(3)
#这里是找到id为"kw"的控件，输入测试文本：
driver.find_element_by_id("kw").send_keys("Test search")
dirver.find_element_by_id("su").click()
sleep(3)
driver.quit()