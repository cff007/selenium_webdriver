from selenium import webdriver
import time

dr = webdriver.Chrome()
url = 'http://zhan.renren.com/'
dr.get(url)

dr.implicitly_wait(10)

dr.find_element_by_css_selector('a[class=login]').click()
time.sleep(5)

dr.quit()