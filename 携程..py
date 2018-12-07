from selenium import webdriver
from time import sleep
dr=webdriver.Firefox()
dr.get('http://www.ctrip.com/')
dr.maximize_window()
dr.find_element_by_xpath('//*[@id="searchHotelLevelSelect"]').click()
sleep(2)
for i in range(1,6):
    j=[1,'大','哥','你','最','帅']
    dr.find_element_by_xpath('//*[@id="HD_TxtKeyword"]').send_keys('{}'.format(j[i]))
    dr.find_element_by_xpath('/html/body/div[11]/div/div[1]/form[1]/div[4]/div[1]/select/option[{}]'.format(i)).click()
    sleep(2)
dr.quit()