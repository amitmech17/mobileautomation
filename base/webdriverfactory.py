"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import traceback
import os
from appium import webdriver


class Driver():

    def getWebDriverInstance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['automationName'] = 'UIAutomator2'
        desired_caps['app'] = ('d://app-debug.apk')
        # desired_caps['appPackage'] = 'com.code2.kwad'
        # desired_caps['appActivity'] = 'com.code2.kwadio.MainActivity'
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        return driver
