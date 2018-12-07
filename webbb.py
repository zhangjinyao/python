# from selenium import webdriver
# from time import sleep
# dr=webdriver.Firefox()
# dr.get('http://www.moore.ren')
# dr.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div[1]/li[1]/a').click()
# #print(dr.current_window_handle)   #获取当前的句柄
# sleep(2)
# a=dr.window_handles   #获取所有窗口的句柄
# print(a)
# sleep(2)
# dr.switch_to.window(a[1])   #根据句柄，切换窗口
# dr.switch_to.frame('login_frame')   #切换到内嵌框架,只能切换ID属性和name属性的，定位到框架
# print(dr.title)