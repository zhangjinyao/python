#！/usr/bin/env python
#  -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
dr=webdriver.Firefox()
dr.get('https://user.qzone.qq.com/')
dr.maximize_window()
#dr.switch_to_default_content()   #跳出窗口
web = dr.find_element_by_id('login_frame')   #输入定位信息
sleep(3)
dr.switch_to.frame(web)
dr.find_element_by_id('switcher_plogin').click()
sleep(1)
dr.find_element_by_id('u').send_keys('1')
sleep(2)
dr.find_element_by_id('p').send_keys('hhxxttxs')
sleep(2)
dr.find_element_by_css_selector('#login_button').click()
sleep(2)
web = dr.find_element_by_xpath('/html/body/div[1]/div[11]/div[2]/iframe')
dr.switch_to.frame(web)
web = dr.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]')
ac = ActionChains(dr)   #dr当做参数传输给了ActionChains赋值给ac
ac.move_to_element(web)
ac.drag_and_drop_by_offset(web,184,0)
ac.perform()
sleep(2)
