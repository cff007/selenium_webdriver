#coding=utf-8
from selenium import webdriver
import time
import os

dr = webdriver.Chrome()
file_path =  'file:///' + os.path.abspath('operate_element.html')
dr.get(file_path)

#click   点击link1和link2
dr.find_element_by_link_text('Link1').click()
time.sleep(1)
dr.find_element_by_link_text('Link2').click()

#send keys
element = dr.find_element_by_name('q')
element.send_keys('something')
time.sleep(1)

#clear   清空输入框的内容
element.clear()
time.sleep(1)

dr.quit()