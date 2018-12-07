from appium import webdriver
import unittest
import time
desired_caps={ 'platformName':'Android',   #版本
                #'platformVersion':'6.0.1',  #banben
              'deviceName':'127.0.0.1:62025',  #设备名
              'appPackage':'com.netease.newsreader.activity',   #安装名
              'appActivity':'com.netease.nr.biz.ad.AdActivity'}   #activity的值
driver =webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
time.sleep(10)
driver.find_element_by_id('com.netease.newsreader.activity:id/eu').click()
time.sleep(3)
driver.find_element_by_id('com.netease.newsreader.activity:id/bye').send_keys('宋小宝')
time.sleep(3)
driver.find_element_by_id('com.netease.newsreader.activity:id/fl').click()

# class aa(unittest.TestCase):
#     def 网易(self):
#             self.desired_caps={'platformName':'Android',
#                           #'platformVersion':'6.2',
#                           'deviceName':'127.0.0.1:62001',
#                           'appPackage':'com.netease.cloudmusic',
#                           'appActivity':'activity.LoadingActivity'}
#
#             self.driver=webdriver.Remote('http://localhost:4723/wd/hub',self.desired_caps)
#             print('立即体验')
#             self.driver.find_element_by_id('com.netease.cloudmusic:id/mw').click()
#             time.sleep(3)
#             self.driver.find_element_by_id('com.netease.cloudmusic:id/pt').click()
#             time.sleep(5)
#             self.driver.find_element_by_id('com.netease.cloudmusic:id/i4').send_keys(15837806865)
#             time.sleep(5)
#             self.driver.find_element_by_id('com.netease.cloudmusic:id/i2').send_keys(15837806865)
#             time.sleep(5)
#             self.driver.find_element_by_id('com.netease.cloudmusic:id/pt').click()
#             time.sleep(5)
#             self.driver.find_element_by_id('com.netease.cloudmusic:id/py').click()
#             time.sleep(5)
#             self.driver.find_element_by_id('com.netease.cloudmusic:id/b3t').click()
#             time.sleep(5)
#             self.driver.find_element_by_id('com.netease.cloudmusic:id/yr').click()
#             time.sleep(5)
#             self.driver.find_element_by_id('com.netease.cloudmusic:id/b64').click()
#             time.sleep(5)
#             self.driver.find_element_by_id('com.netease.cloudmusic:id/aku').click()
#             time.sleep(5)
#             self.driver.find_element_by_id('com.netease.cloudmusic:id/i4').send_keys('15660600605')
#             time.sleep(3)
#             self.driver.find_element_by_id('com.netease.cloudmusic:id/i2').send_keys('15660600605')
#             time.sleep(3)
#             self.driver.find_element_by_id('com.netease.cloudmusic:id/pt').click()
#             print('132')
# aa().网易()