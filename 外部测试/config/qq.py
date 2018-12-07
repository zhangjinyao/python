#！/usr/bin/env python
#  -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
class qq():
    def aa(self,a,b):
        dr=webdriver.Firefox()
        dr.get('https://user.qzone.qq.com/')
        dr.maximize_window()
        web = dr.find_element_by_id('login_frame')
        dr.find_element_by_id('u').send_keys('{}'.format(a))
        sleep(2)
        dr.find_element_by_id('p').send_keys('{}'.format(b))
        sleep(2)
        dr.find_element_by_css_selector('#login_button').click()
        sleep(2)
        web = dr.find_element_by_xpath('/html/body/div[1]/div[11]/div[2]/iframe')
        dr.switch_to.frame(web)
        web = dr.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]')
        ac = ActionChains(dr)  # dr当做参数传输给了ActionChains赋值给ac
        ac.move_to_element(web)
        ac.drag_and_drop_by_offset(web,184,0)
        ac.perform()
        sleep(2)




