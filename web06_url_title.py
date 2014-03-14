#coding=utf-8
from selenium import webdriver
from time import sleep
import os
#if 'HTTP_PROXY'in os.environ:del os.environ['HTTP_PROXY']


dr = webdriver.Chrome()
url = 'http://zhan.renren.com'
dr.get(url)

sleep(3)

print 'Current title is:%s ' %dr.title

print 'current url is:%s ' %dr.current_url

sleep(5)

dr.quit()