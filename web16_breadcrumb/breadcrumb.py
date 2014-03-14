#coding=utf-8
from selenium import webdriver
from time import sleep
import os

dr = webdriver.Chrome()
file_path = 'file:///'+os.path.abspath('breadcrumb.html')
dr.get(file_path)

#获得其父层级
aa = dr.find_element_by_class_name('breadcrumb').find_elements_by_tag_name('a')
for link in aa:
	print link.text
sleep(5)

#获取当前层级
#由于页面上可能有很多class为active的元素
#所以使用层级定位最为保险

print dr.find_element_by_class_name('breadcrumb').find_element_by_class_name('active').text
sleep(5)
dr.quit()