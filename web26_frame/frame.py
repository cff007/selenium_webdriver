#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import selenium.webdriver.support.ui as ui
if 'HTTP_PROXY'in os.environ: del os.environ['HTTP_PROXY']

dr = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('frame.html')

dr.get(file_path)
dr.implicitly_wait(30)

#先到f1再到f2
f1 = dr.find_element_by_id('f1')
dr.switch_to_frame('f1')
time.sleep(5)
f2 = dr.find_element_by_id('f2')
dr.switch_to_frame('f2')
time.sleep(5)

#往f2的百度输入框中输入内容
dr.find_element_by_id('kw').send_keys('watir-webdriver')
dr.find_element_by_id('su').click()
time.sleep(3)

#直接跳出所有frame
dr.switch_to_default_content()
time.sleep(3)

#再到f1
dr.switch_to_frame('f1')
time.sleep(2)
dr.find_element_by_link_text('click').click()
time.sleep(3)

try:
	alert=dr.switch_to_alert()
	alert.accept()
	print alert.text
except:
	print 'lllllllll'

time.sleep(2)
dr.quit()