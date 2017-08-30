#import os
#from time import sleep
from appium import webdriver


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'QMS4C15C28005345'
desired_caps['udid'] = 'QMS4C15C28005345'
desired_caps['appPackage'] = 'com.guotai.dazhihui'
desired_caps['appActivity'] = 'com.android.dazhihui.view.screen.NewMainScreen'
desired_caps['noReset'] = True
desired_caps['fullReset'] = False
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

#driver.tap([(860,1676)],500)

#我的
el = driver.find_element_by_id('com.guotai.dazhihui:id/bottom_menu_button5')
el.click()
#立即登录/注册
el = driver.find_element_by_id('com.guotai.dazhihui:id/btn_usercenter_register')
el.click()

driver.back()

driver.quit()
