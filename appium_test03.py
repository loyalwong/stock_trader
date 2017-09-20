#import os
#from time import sleep
from appium import webdriver


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'QMS4C15C28005345'
desired_caps['udid'] = 'QMS4C15C28005345'
desired_caps['appPackage'] = 'com.guotai.dazhihui'
desired_caps['appActivity'] = 'com.android.dazhihui.view.screen.InitScreen'
desired_caps['noReset'] = True
desired_caps['fullReset'] = False
desired_caps['session-override'] = True
desired_caps['unicodeKeyboard'] = True
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

try:
#    elem1 = driver.find_element_by_xpath('//android.widget.TextView[contains(@text,"资讯")]')
    elem2 = driver.find_element_by_class_name('//android.widget.TextView[contains(@text,"资讯")]')
except Exception:
    print("no alert need press")
else:
    driver.find_element_by_xpath('//android.widget.TextView[contains(@text,"取消")]').click()


#警告框
try:
    elem1 = driver.find_element_by_id('com.guotai.dazhihui:id/layout_mainpage_nrng_icon')
except Exception:
    driver.tap([(860, 1676)], 500)
else:
    print("no alert need press")

#我的
try:
    elem2 = driver.find_element_by_id('com.guotai.dazhihui:id/bottom_menu_button5')
except Exception:
    print("error")
else:
    elem2.click()

#立即登录/注册
try:
    elem3 = driver.find_element_by_id('com.guotai.dazhihui:id/btn_usercenter_register')
except Exception:
    print("error")
else:
    elem3.click()

#短信登录
try:
    elem3 = driver.find_element_by_id('com.guotai.dazhihui:id/tv_right')
except Exception:
    print("error")
else:
    elem3.click()

try:
    elem4 = driver.find_element_by_id('com.guotai.dazhihui:id/et_register_phonenum_smsmode')
except Exception:
    print("error")
else:
    elem4.clear()
    elem4.send_keys('17765178235')
    elem5 = driver.find_element_by_id('com.guotai.dazhihui:id/btn_register_get_verifycode')
    elem5.click()
    elem6 = driver.find_element_by_id('com.guotai.dazhihui:id/et_register_verify_code')
    elem6.clear()
    verify_code = input()
    elem6.send_keys(verify_code)
    elem6.submit()

#交易
el = driver.find_element_by_id('com.guotai.dazhihui:id/bottom_menu_button3')
el.click()


driver.back()

driver.quit()
