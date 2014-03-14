# -*- coding:utf-8 -*-
#Filename:back&forward.py

from selenium import webdriver
from time import sleep

dr=webdriver.Ie()
url1='http://www.baidu.com'
print 'The first url is :%s' %(url1)
dr.get(url1)
sleep(3)

url2='http://zhan.renren.com'
print 'The second url is :%s' %(url2)
dr.get(url2)
sleep(3)

print 'Back to url:%s' %(url1)
dr.back()
sleep(3)

print 'Now forward to url:%s' %(url2)
dr.forward()
sleep(3)

dr.quit()