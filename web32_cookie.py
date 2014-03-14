#coding=utf-8
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait

dr = webdriver.Chrome()
url = 'http://www.baidu.com'
dr.get(url)

#打印登录百度前的cookies
print "Cookies before login as follows:\n%s" %(dr.get_cookies())
sleep(5)

#打印登录后的cookies

dr.find_element_by_name('tj_login').click()
sleep(5)

login = dr.find_element_by_id('TANGRAM__PSP_2__foreground')
WebDriverWait(dr,10).until(lambda dr:login.is_displayed())

dr.find_element_by_name('userName').send_keys('xxxxxxxx')
dr.find_element_by_name('password').send_keys('xxxxxxxx')
dr.find_element_by_id('TANGRAM__PSP_8__submit').click()
print "Cookies after login as follows:\n%s" %(dr.get_cookies())

#添加cookies
dr.add_cookie({'name': 'cffppa', 'value': '123456'})
dr.add_cookie({'name': 'cffppa007', 'value': '000123'})
sleep(5)

#选择前面添加的两个cookies打印
dr.get(url)

for cookie in dr.get_cookies():
	print "%s %s" %(cookie['name'],cookie['value'])

#删除所有cookies
dr.delete_all_cookies()

dr.quit()