#coding=utf-8

from selenium import webdriver
from time import sleep
import os
#if ['HTTP_PROXY']in os.environ:del os.environ['HTTP_PROXY']

file_path = 'file:///'+os.path.abspath('pagination.html')
dr = webdriver.Chrome()
dr.get(file_path)

#获得所有分页的数量
#-2是因为要去掉上一个和下一个

total_pages = len(dr.find_element_by_class_name('span6').find_elements_by_tag_name('li'))-2
print 'total page is :%s' %total_pages

total_pages_2 = len(dr.find_elements_by_tag_name('a'))-2
print 'method 2:total_pages is %d' %total_pages_2

#获取当前页面的url以及当前页面是第几页
current_page = dr.find_element_by_class_name('span6').find_element_by_class_name('active').text
print 'current page is %s' %current_page

dr.quit()