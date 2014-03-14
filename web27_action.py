#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

dr = webdriver.Chrome()
url = 'http://shop.xunlei.com/'
dr.get(url)

title1 = dr.find_element_by_id('vNavBox').find_elements_by_name('category_item')[1]
wait=WebDriverWait(dr,20)
wait.until(lambda dr:title1.is_displayed())

# move_to_element 把鼠标移动到元素的中心点
ActionChains(dr).move_to_element(title1).perform()
sleep(5)

# double_click。鼠标左键双击
title2 = dr.find_element_by_css_selector('a[title=家庭影音]')
ActionChains(dr).double_click(title2).perform()
sleep(5)

# 对定位到的元素执行右键操作
title3 = dr.find_element_by_id('brand_22')
wait.until(lambda dr:title3.is_displayed())
ActionChains(dr).context_click(title3).perform()
sleep(5)

dr.quit()