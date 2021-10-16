
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import os,sys

#os.chmod('/usr/bin/chromedriver', 755)

caps = DesiredCapabilities.CHROME
caps['goog:loggingPrefs'] = {'performance':'ALL'}

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")

#driver = webdriver.Chrome( executable_path="/bin/chromedriver",desired_capabilities=caps, options=options)
driver = webdriver.Chrome( desired_capabilities=caps, options=options)
driver.get('https://www.dazn.com/ja-JP/fixture/ContentId:dx0qyslu3jspwnd1kk8etbbx0/dx0qyslu3jspwnd1kk8etbbx0')


driver.quit()