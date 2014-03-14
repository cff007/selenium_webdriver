#coding=utf-8
from selenium import webdriver
from time import sleep
import os
if 'HTTP_PROXY'in os.environ: del os.environ['HTTP_PROXY']

dr = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('form_2.html')
dr.get(file_path)

#选中checkbox
dr.find_element_by_css_selector('input[type=checkbox]').click()
sleep(2)

#选中radio
dr.find_element_by_css_selector('input[type=radio]').click()
sleep(2)

#选择下拉菜单的最后一项
dr.find_element_by_tag_name('select').find_elements_by_tag_name('option')[-1].click()
sleep(3)

#点击submit按钮
dr.find_element_by_tag_name('fieldset').find_element_by_class_name('btn').click()
sleep(5)


alert = dr.switch_to_alert()
print alert.text
alert.accept()

dr.quit()