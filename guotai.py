# coding: utf-8
from time import sleep
from appium import webdriver
from . import helpers


class guotai ( object ):
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
        #        desired_caps['unicodeKeyboard'] = True
        self.driver = webdriver.Remote ( 'http://localhost:4723/wd/hub', desired_caps )

    def alert_popup_kickout(self):
        try:
            elem1 = self.driver.find_element_by_xpath ( '//android.widget.TextView[contains(@text,"新股申购提醒")]' )
        except Exception:
            print ( "no alert need press" )
            return True
        else:
            self.driver.find_element_by_xpath ( '//android.widget.TextView[contains(@text,"取消")]' ).click ( )
            print ( "any popup window is cancelled" )
            return True

    def mainscreen_in(self):
        sleep ( 10 )
        self.alert_popup_kickout ( )
        sleep ( 10 )
        try:
            elem1 = self.driver.find_element_by_xpath ( '//android.widget.TextView[contains(@text,"我的")]' )
        except Exception:
            print ( "not in mainscreen" )
            return False
        else:
            elem1.click ( )
            print ( "go into mainscreen my" )
            return True

    def sms_verify_code_get(self):
        return '123456'

    def appacount_login(self):
        if self.mainscreen_in ( ) == True:
            try:  # check already login
                elem1 = self.driver.find_element_by_id ( 'com.guotai.dazhihui:id/tv_usercenter_nickname' )
            except Exception:
                try:
                    account = helpers.file2dict ( "./config/account.json" )
                    user = account['appaccount']['user']
                    elem2 = self.self.driver.find_element_by_xpath (
                        '//android.widget.Button[contains(@text,"立即登录/注册")]' )
                    elem2.click ( )
                    elem3 = self.self.driver.find_element_by_xpath (
                        '//android.widget.TextView[contains(@text,"短信登录")]' )
                    elem3.click ( )
                    elem4 = self.driver.find_element_by_id ( 'com.guotai.dazhihui:id/et_register_phonenum_smsmode' )
                    elem4.clear ( )
                    elem4.send_keys ( user )
                    elem5 = self.driver.find_element_by_id ( 'com.guotai.dazhihui:id/btn_register_get_verifycode' )
                    elem5.click ( )
                    elem6 = self.driver.find_element_by_id ( 'com.guotai.dazhihui:id/et_register_verify_code' )
                    verify_code = self.sms_verify_code_get ( )
                    elem6.clear ( )
                    elem6.send_keys ( verify_code )
                    elem7 = self.driver.find_element_by_id ( 'com.guotai.dazhihui:id/btn_register_confirm' )
                    elem7.click ( )
                except Exception:
                    print ( "something wrong while login app account" )
                    return False
                else:
                    print ( "login app account this time" )
                    return True
            else:
                print ( "already login app account" )
                return True

    def stockaccount_login(self):
        if self.appacount_login == True:
            try:  # check already login
                elem1 = self.driver.find_element_by_id ( 'com.guotai.dazhihui:id/tv_usercenter_zjaccount' )
            except Exception:
                try:
                    elem2 = self.driver.find_element_by_id ( 'com.guotai.dazhihui:id/btn_usercenter_login' )
                    elem2.click()
                    elem3 = self.driver.find_element_by_id ( 'com.guotai.dazhihui:id/et_password' )
                    elem3.clear ( )
                    elem3.send_keys ( '17765178235' )
                except Exception:
                    print ( "something wrong while login stock account" )
                    return False
                else:
                    print ( "login stock account this time" )
                    return True
            else:
                print ( "already login stock account" )
                return True

    def stock_buy(self, code, price, qty):
        return True

    def stock_sell(self, code, price, qty):
        return True

    def tearDown(self):
        self.driver.quit ( )
