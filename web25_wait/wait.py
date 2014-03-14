#coding=utf-8
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import os
import selenium.webdriver.support.ui as ui
if 'HTTP_PROXY'in os.environ:del os.environ['HTTP_PROXY']

file_path = 'file:///'+os.path.abspath('wait.html')
dr = webdriver.Chrome()
dr.get(file_path)

#点击click
dr.find_element_by_id('btn').click()

wait = ui.WebDriverWait(dr,10)
wait.until(lambda dr:dr.find_element_by_class_name('label').is_displayed())

sleep(5)
dr.quit()