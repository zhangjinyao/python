#！ /usr/bin/env python
# -*- coding:utf-8 -*-
#面向对象
# import re
# import requests
# class Yinyue(object):
#     header = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
#     }
#     def yuan_html(self):
#         url='http://www.yy8844.cn/'
#         res=requests.get(url=url,headers=self.header)
#         html=res.content.decode('gbk')
#         return html
#     def new_url(self,html):
#         g=[]
#         pattern=re.compile(r'a href="/ting(.*?).shtml"',re.S)
#         items=pattern.findall(html)
#         for i in range(5):
#             new_url="http://www.yy8844.cn/ting"+items[i]+".shtml"
#             respons=requests.get(url=new_url,headers=self.header)
#             new_html=respons.content.decode("gbk")
#             new_pattern=re.compile(r'var MusicId=(.*?);var',re.S)
#             new_items=new_pattern.findall(new_html)
#             g.append(new_items[0])
#             print(g)
#         return g
#     def xiazai(self,g):
#         for j,m in enumerate(g):
#             nnew_url='http://96.ierge.cn/{}/{}/{}.mp3'.format(int(m) // 30000,int(m) // 2000,int(m))
#             print(nnew_url)
#             new_respons=requests.get(url=nnew_url,headers=self.header)
#             nnew_html=new_respons.content
#             with open(r'E:\zong\音乐\{}.mp3'.format(j),'wb') as f:
#                 f.write(nnew_html)
# a=Yinyue()
# b=a.yuan_html()
# c=a.new_url(b)
# a.xiazai(c)
#面向过程
import re
import requests
hea = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
url='http://www.yy8844.cn/'
res=requests.get(url=url,headers=hea)
html=res.content.decode('gbk')
pa=re.compile(r'<a href="/ting(.*?).shtml"')
items=pa.findall(html)
g=[]
for m,i in enumerate(items):
    if m==5:
        break
    nurl='http://www.yy8844.cn/'+'ting'+i+'.shtml'
    nres=requests.get(url=nurl,headers=hea)
    nhtml=nres.content.decode('gbk')
    npa=re.compile(r'var MusicId=(.*?);')
    nitems=npa.findall(nhtml)
    g.append(nitems[0])
    print(g)
    for n,j in enumerate(g):
        new_url='http://96.ierge.cn/{}/{}/{}.mp3'.format(int(j)//30000,int(j)//2000,int(j))
        new_res=requests.get(url=new_url,headers=hea)
        new_html=new_res.content
        with open(r'E:\zong\音乐\{}.mp3'.format(n),'wb')as f:
            f.write(new_html)


# nurl = parseInt(MusicId / 30000) + "/" + parseInt(MusicId / 2000) + "/" + MusicId + ".mp3";