import os

from selenium import webdriver

fp = webdriver.FirefoxProfile()

fp.set_preference("browser.download.folderList",2)
fp.set_preference("browser.download.manager.showWhernStarting",False)
fp.set_preference("browser.download.dir",os.getcwd())
fp.set_preference("browser.helperApps.neverAsk.saveToDisk","application/octet-stream")

browser = webdriver.Firefox(firefox_profile=fp)
url = 'http://code.google.com/p/selenium/downloads/list'
browser.get(url)
a = browser.find_elements_by_css_selector('img[alt=Download]')
a[1].click()

try:
	alert = browser.switch_to_alert()
	print alert.text
	alert.accept()
except:
	"Downloading................."

browser.quit()