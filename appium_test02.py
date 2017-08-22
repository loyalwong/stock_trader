import os
from time import sleep
from appium import webdriver

import unittest

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'QMS4C15C28005345'
desired_caps['app'] = PATH('ApiDemos-debug.apk'
                           )
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

el = driver.find_element_by_accessibility_id('Graphics')
el.click()
el = driver.find_element_by_accessibility_id('Arcs')
driver.back()
el = driver.find_element_by_accessibility_id("App")
els = driver.find_elements_by_android_uiautomator("new UiSelector().clickable(true)")
driver.find_element_by_android_uiautomator('text("API Demos")')

el = driver.find_element_by_accessibility_id('Graphics')
el.click()
el = driver.find_element_by_accessibility_id('Arcs')
el.click()
driver.find_element_by_android_uiautomator('new UiSelector().text("Graphics/Arcs")')

driver.quit()
