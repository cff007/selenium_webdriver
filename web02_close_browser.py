from selenium import webdriver
from time import sleep

dr = webdriver.Firefox()

sleep(5)

dr.quit()

#dr.close()