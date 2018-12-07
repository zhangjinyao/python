# import  requests
# import  re
# import pymysql
# url='https://www.zhipin.com/c101010100/?query=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95'
# head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
# res=requests.get(url=url,headers=head)
# html=res.content.decode('utf-8')
# patt=re.compile(r'ka="related-search-(.*?)">(.*?)</a>')
# items=patt.findall(html)
# print(items)
# abc=pymysql.connect(host='192.168.0.108',port=3306,user='root',password='123456',charset='utf8')
# a=abc.cursor()
# a.execute('use test1;')
# a.execute('create table biao10(软件测试 char(222));')
# for i,j in enumerate(items):
#     a.execute('insert into biao10 values("{}");'.format(items[i][1]))
#     abc.commit()



# from selenium import webdriver
# from time import sleep
# dr=webdriver.Firefox()
# dr.get('http://www.jd.com')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="key"]').send_keys('电脑')
# sleep(2)
# dr.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div[2]/button').click()
# sleep(2)
# dr.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/div[1]/div/div[2]/ul/li[1]/div/div[7]/a[3]').click()
# sleep(2)



