#coding=utf-8
'''
运行方法：进入selenium-server-standalone所在目录，执行命令：
java -jar selenium-server-standalone.jar >D:log.text
启动remote webdriver后执行该脚本就行。
'''
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

dr = webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME)
dr.get('http://www.baidu.com/')
dr.find_element_by_id('kw1').send_keys("selenium")
time.sleep(5)
dr.find_element_by_id('su1').click()
time.sleep(15)

dr.quit()
