#！ /usr/bin/env python
# -*- coding:utf-8 -*-
# import requests
# import re
# a=1
# url='https://www.qiushibaike.com/8hr/page/{}/'.format(a)
# header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
# res=requests.get(url=url,headers=header)
# html=res.content.decode('utf-8')
# # print(res.text)
# pattern=re.compile(r'<div class="content">(.*?)</div>',re.S)
# items=pattern.findall(html)
# print(items)
# for i in items:
#     i=i.replace('<span>','').replace('<br/>','').replace('/span','').replace('<>','')
#     i=i.strip()
#     # with open(r'C:\Users\zjy\Desktop\12.txt','a') as f:
#     #     f.write(i+'\n\n')

