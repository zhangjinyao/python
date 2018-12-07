#！ /usr/bin/env python
# -*- coding:utf-8 -*-
import re
import requests
import os
class doutu(object):
    hea={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
    def kuaitu(self):
        g=[]
        h=[]
        for i in range(1,4):
            url='http://www.doutula.com/article/list/?page={}'.format(i)
            res=requests.get(url=url,headers=self.hea)
            html=res.content.decode('utf-8')
            pattern = re.compile(r'<a href="http://www.doutula.com/article/detail/(.*?)".*?<div class="random_title">(.*?)<div class="date">',re.S)
            items = pattern.findall(html)
            g.append(items[0])
            h.append(items[1])
            return g,h
    def xiaotu(self,g,h):
        for n in h:
            os.chdir('E:\zong\图')
            os.mkdir(r'E:\zong\图\{}'.format(n[1]))
            return n
        for j in g:
            new_url = 'http://www.doutula.com/article/detail/{}'.format(j[0])
            req = requests.get(url=new_url, headers=self.hea)
            htm = req.content.decode('UTF-8')
            new_pattern = re.compile(r'src="http://(.*?)".*?<td align="center" class="wr pl">(.*?)</td>', re.S)
            new_items = new_pattern.findall(htm)
            return new_items
    def baocun(self,new_items,n):
        for m in new_items:
            nnew_url = 'http://{}'.format(m[0])
            res = requests.get(url=nnew_url, headers=self.hea)
            tupian = res.content
            if nnew_url.endswith('jpg'):
                with open(r'E:\zong\图\{}\{}.jpg'.format(n[1], m[1].replace('?', ',')), 'wb') as f:
                    f.write(tupian)
            else:
                with open(r'E:\zong\图\{}\{}.gif'.format(n[1], m[1].replace('?', ',')), 'wb') as f:
                    f.write(tupian)
a=doutu()
b,h=a.kuaitu()
c,n=a.xiaotu(b,h)
d=a.baocun(c,n)
# 面向对象
import requests
import re
import os
for i in range(1,4):
    url='http://www.doutula.com/article/list/?page={}'.format(i)
    hea = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4620.400 QQBrowser/9.7.13014.400'}
    res=requests.get(url=url,headers=hea)
    html=res.content.decode('utf-8')
    pattern=re.compile(r'<a href="http://www.doutula.com/article/detail/(.*?)".*?<div class="random_title">(.*?)<div class="date">',re.S)
    items=pattern.findall(html)
    for i in items:
        new_url='http://www.doutula.com/article/detail/{}'.format(i[0])
        req = requests.get(url=new_url, headers=hea)
        htm = req.content.decode('UTF-8')
        pat = re.compile(r'src="http://(.*?)".*?<td align="center" class="wr pl">(.*?)</td>',re.S)
        ite = pat.findall(htm)
        os.mkdir(r'E:\zong\图\{}'.format(i[1]))
        for j in ite:
            ne_url='http://{}'.format(j[0])
            res=requests.get(url=ne_url,headers=hea)
            tupian=res.content
            if ne_url.endswith('jpg'):
                    with open(r'E:\zong\图\{}\{}.jpg'.format(i[1],j[1].replace('?',',')),'wb') as f:
                            f.write(tupian)
            else:
                with open(r'E:\zong\图\{}\{}.gif'.format(i[1], j[1].replace('?',',')), 'wb') as f:
                    f.write(tupian)

