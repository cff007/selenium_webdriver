from selenium import webdriver
import time

dr = webdriver.Chrome()

url = 'http://zhan.renren.com'

dr.get(url)

time.sleep(5)

print "maximize window"

dr.maximize_window()

time.sleep(5)

print 'Close window'

dr.quit()