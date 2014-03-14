#coding=utf-8
from selenium import webdriver
from time import sleep
import os
if 'HTTP_PROXY'in os.environ: del os.environ['HTTP_PROXY']

file_path = 'file:///'+os.path.abspath('button_group.html')

dr = webdriver.Chrome()
dr.get(file_path)
sleep(5)


#定位text是second的按钮
buttons = dr.find_element_by_class_name('btn-group').find_elements_by_class_name('btn')
for btn in buttons:
	if btn.text == 'second':
		print 'find second button'
		btn.click()
		break
sleep(10)

'''
#直接定位second这个按钮
dr.find_elements_by_class_name('btn')[1].click()
sleep(5)
'''
  
alert = dr.switch_to_alert()    #接受警告信息
print alert.text				#打印文本信息
alert.accept()
			

sleep(5)
dr.quit()