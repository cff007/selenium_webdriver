#coding=utf-8
#ex_login_form.py

from selenium import webdriver
import os
from time import sleep
if 'HTTP_PROXY'in os.environ:del os.environ['HTTP_PROXY']

filepath = 'file:///'+os.path.abspath('form.html')

dr = webdriver.Chrome()
print filepath
dr.get(filepath)
'''
#--------------- by id------------------------------
em_id = dr.find_element_by_id('inputEmail')
em_id.send_keys('cffppa@qq.com')

pw_id = dr.find_element_by_id('inputPassword')
pw_id.send_keys('123456')

rm = dr.find_element_by_class_name('checkbox')
rm.click()
sleep(3)

sign = dr.find_element_by_class_name('btn')
sign.click()
sleep(3)

#--------------- by name ------------------------------
em_id = dr.find_element_by_name('email')
em_id.send_keys('cffppa@qq.com')

pw_id = dr.find_element_by_name('password')
pw_id.send_keys('123456')

rm = dr.find_element_by_class_name('checkbox')
rm.click()
sleep(3)

sign = dr.find_element_by_class_name('btn')
sign.click()
sleep(3)
'''

#by id    点击email输入框
dr.find_element_by_id('inputEmail').click()
sleep(2)
#by name    点击passport输入框
dr.find_element_by_name('password').click
sleep(3)
#by tagname
print dr.find_element_by_tag_name('form').get_attribute('class')

#by class_name
e = dr.find_element_by_class_name('controls')
dr.execute_script('$(arguments[0]).fadeOut().fadeIn()',e)
sleep(5)

#---------------------by link text  找register---------------------------
link = dr.find_element_by_link_text('register')
dr.execute_script('$(arguments[0]).fadeOut().fadeIn()',link)
sleep(5)

#by partial link text   找register
link = dr.find_element_by_partial_link_text('reg')
dr.execute_script('$(arguments[0]).fadeOut().fadeIn()',link)
sleep(5)

#by class selector
div = dr.find_element_by_css_selector('.controls')
dr.execute_script('$(arguments[0]).fadeOut().fadeIn()',div)
sleep(5)

#by xpath   勾选remember me
dr.find_element_by_xpath('/html/body/form/div[3]/div/label/input').click()

sleep(5)
dr.quit()

