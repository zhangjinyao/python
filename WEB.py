from selenium import webdriver
from time import  sleep
from  selenium.webdriver.common.action_chains import ActionChains
import  selenium.webdriver.support.ui as  ui
dr = webdriver.Firefox()
# dr.get('http://www.baidu.com')
# dr.set_window_position(500,200)  #设置浏览器的位置
# dr.set_window_size(1000,800)  #第一个是宽，第二个是高
# sleep(5)
# print(dr.title)     #获取网站的标题,通常用来做断言
# print(dr.current_url)  #保证所有的测试用例在同一环境下测试
# dr.quit()  #关闭浏览器

#
# dr = webdriver.Firefox()
# dr.get('http://www.moore.ren')
# dr.maximize_window()   #浏览器最大化
#dr.minimize_window()    #浏览器最小化
# wd=dr.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div[1]/li[1]/a').text
# print(wd.get_attribute('href'))    #获取某元素的值
# print(wd)


# dr.find_element_by_id('kw').send_keys('阿娇')  #通过ID属性定位,括号中写ID属性的值(1)
# dr.find_element_by_id('su').click()   #定位百度一下，click用来确认
# #dr.find_element_by_class_name('s_ipt').send_keys('肖传真')  #通过class属性定位(2)
# dr.find_element_by_name('wd').send_keys('我爱你')  #通过name的值来定位(3)
#dr.find_element_by_link_text('首页').click()   #通过文本来定位(4)
#dr.find_element_by_partial_link_text('登').click()  #模糊文本定位，只需要一部分内容就可以(5)
#dr.find_element_by_tag_name().click()  #通过标签去定位 ，通常定位多个元素(6)
#dr.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div[1]/li[1]/a').click()   (7)#通过xpath路径定位，路径标记语言 一个/是绝对路径，//从节点开始是相对路径   xml叫做可扩展标记语言作用是传输数据和存储数据  html的作用是显示数据
#dr.find_element_by_css_selector('').send_keys('')    #通过css定位(8)
# dr.find_element_by_id('su').click()e
# dr.get('http://www.jd.com')
# sleep(2)
# dr.back()  #后退
# sleep(3)
# dr.forward()  #前进
# dr.get('http://www.ifeng.com')
# wd=dr.find_elements_by_class_name('menu-box')   #wd是个列表
# for i in wd:
#     ActionChains(dr).move_to_element(i).perform()   #通过ActionCharins移动循环到i
#     sleep(2)
# wd=dr.find_element_by_xpath('//*[@id="J_cate"]').find_elements_by_tag_name('li')   #层级定位
# # print(len(wd))


#print(dr.current_window_hadle)  #获取当前窗口的句柄
#dr.window_handles   #获取所有窗口的句柄
#dr.switch_to.frame()   #切换到内嵌框架,只能切换ID属性和name属性的，定位到框架
#dr.switch_to.window(填写句柄)   #根据句柄，切换窗口
#dr.switch_to.default_content()  #推出到原始界面
#dr.switch_to.parent_frame()    # 切换到上一层框架
#alert   # 弹出框
# wd=dr.switch_to_alert()
# print(wd.text)
# wd.accept()   #确定弹出框
#wd.dismiss()  #取消弹出框

#移动滚动条  滚动条是属于浏览器的
#js='var q=document.documentElement.scrollTop=10000'   #10000表示的当前页面的高度
#dr.execute_script(js)   #执行JavaScript语句
#var q=document.documentElement.scrollTop=10000     #1.根据页面的高度来定位


#2.根据定位的元素移动滚动条
# wd=dr.find_element_by_xpath('/html/body/div/div/div/section/div[2]/div[5]/div/div/p')
# js='arguments[0].scrollIntoView();'
# sleep(2)
# dr.execute_script(js,wd)

dr.get('http://mooreelite.com/')
dr.maximize_window()
sleep(2)
#截图并保存
#dr.get_screenshot_as_file('abc.png')
#先截图然后保存
# dr.get_screenshot_as_png()
# dr.save_screenshot('aaa.png')
#智能等待
# a=ui.WebDriverWait(dr,10)
# a.until(lambda dr:dr.find_element_by_xpath('/html/body/div[2]/div[1]/header/div/div/a/img[2]').is_displayed())
# dr.quit()
# b=dr.find_element_by_xpath('/html/body/div[2]/div[1]/header/div/div/a/img[2]').is_displayed()
# if dr.find_element_by_xpath('/html/body/div[2]/div[1]/header/div/div/a/img[2]').is_enabled():
#     print(b)
#is_displayed()   #判断元素是否显示 结果为： True   Flase
#is_enabled()    #判断元素是否为灰化状态
