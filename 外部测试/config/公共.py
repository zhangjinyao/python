from selenium import webdriver
from time import  sleep
import unittest
dr = webdriver.Firefox()
class aa():
    def 网页(self):
        dr.get('http://www.moore.ren')
        dr.maximize_window()
    def  登陆(self):
        self.网页()
        dr.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div[1]/li[1]').click()
        c=dr.title
        return c
    def 注册(self):
        self.网页()
        dr.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div[1]/li[2]/a').click()
    def 热门职位(self):
        self.网页()
        dr.find_element_by_xpath('/html/body/div[2]/div/div[4]/div[1]/div[2]/ul/li[1]').click()
        sleep(2)
        w=dr.window_handles
        dr.switch_to.window(w[-1])
        sleep(2)
        dr.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[2]/div[1]/div/a/span/div').click()
        sleep(2)
        dr.find_element_by_xpath('/html/body/div[21]/div[1]/div[2]/div[2]/div[1]/div/div/a').click()
        sleep(2)
aa().热门职位()


