#coding=utf-8
#checkbox 定位一组元素

from selenium import webdriver
import os
from time import sleep

#输出html文件路径
filepath = 'file:///'+os.path.abspath('checkbox.html')
print filepath

dr = webdriver.Chrome()
dr.get(filepath)

#选择所有的checkbox并全部勾选
checkboxes = dr.find_elements_by_css_selector('input[type=checkbox]')
for checkbox in checkboxes:
	checkbox.click()
sleep(5)
dr.refresh()
sleep(5)

#打印当前页面上有多少个checkbox
print len(dr.find_elements_by_css_selector('input[type=checkbox]'))

#选择页面上所有的input,然后从中过滤出所有的checkbox并勾选之 
inputs = dr.find_elements_by_tag_name('input')
for input in inputs:
	if input.get_attribute('type') == 'checkbox':
		input.click()
sleep(5)

#把页面上最后一个checkbox的勾给去掉
dr.find_elements_by_css_selector('input[type=checkbox]').pop().click()
sleep(5)

#去掉倒数第二个勾
dr.find_element_by_tag_name('form').find_element_by_id('c2').click()
sleep(5)
#点击radio
dr.find_element_by_css_selector('input[type=radio]').click()
sleep(5)

dr.quit()
