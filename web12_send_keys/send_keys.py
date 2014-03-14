#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
if 'HTTP_PROXY'in os.environ:del os.environ['HTTP_PROXY']

dr = webdriver.Chrome()
file_path = 'file:///'+os.path.abspath('send_keys.html')

dr.get(file_path)

#copy content of A
dr.find_element_by_id('A').send_keys((Keys.CONTROL,'a'))     #找到A输入框，全选输入框内容
dr.find_element_by_id('A').send_keys((Keys.CONTROL,'x'))		#找到A输入框，剪切输入框内容
sleep(1)

#paste to B
dr.find_element_by_id('B').send_keys((Keys.CONTROL,'v'))     #粘贴到B
sleep(1)

##send keys to A
dr.find_element_by_id('A').send_keys('watir','-','webdriver',Keys.SPACE,'is',Keys.SPACE,'better')
sleep(2)

dr.quit()