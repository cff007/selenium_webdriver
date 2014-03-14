from selenium import webdriver
from time import sleep

dr = webdriver.Chrome()

print 'Maximize window.'

dr.maximize_window()

sleep(5)

print 'set window size'

dr.set_window_size(600,1000)

sleep(5)

dr.quit()