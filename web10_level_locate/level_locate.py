from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import os

dr = webdriver.Chrome()
file_path = 'file:///'+os.path.abspath('level_locate.html')
dr.get(file_path)

dr.find_element_by_link_text('Link1').click()

WebDriverWait(dr, 20).until(lambda the_driver: the_driver.find_element_by_id('dropdown1').is_displayed())
menu = dr.find_element_by_id('dropdown1').find_element_by_link_text('Another action')
time.sleep(5)

webdriver.ActionChains(dr).move_to_element(menu).perform()
time.sleep(5)

dr.quit()