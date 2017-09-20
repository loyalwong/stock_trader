# coding: utf-8
from appium import webdriver

class guotai(object):
    def __init__(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'QMS4C15C28005345'
        desired_caps['udid'] = 'QMS4C15C28005345'
        desired_caps['appPackage'] = 'com.guotai.dazhihui'
        desired_caps['appActivity'] = 'com.android.dazhihui.view.screen.MainScreen'
        desired_caps['noReset'] = True
        desired_caps['fullReset'] = False
        desired_caps['session-override'] = True
        desired_caps['unicodeKeyboard'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def alert_popup(self):
        try:
            elem1 = self.driver.find_element_by_xpath('//android.widget.TextView[contains(@text,"新股申购提醒")]')
        except Exception:
            print("no alert need press")
            return True
        else:
            self.driver.find_element_by_xpath('//android.widget.TextView[contains(@text,"取消")]').click()
            return True

    def mainscreen_in(self):
        return True

    def appacount_login(self):
        return True

    def stockaccount_login(self):
        return True

    def stock_buy(self,code,price,qty):
        return True

    def stock_sell(self,code,price,qty):
        return True

    def tearDown(self):
        self.driver.quit()
