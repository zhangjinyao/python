#! /usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
import HTMLTestRunner
import time
import requests
import json
class Test_case(unittest.TestCase):
    def setUp(self):
        print('进入')
    def test1(self):
        url='http://47.93.217.79:8085/aixue/user/insertTeacher'
        parms={'lon':'113.123',
                'password':'123456',
                'username':'zhang576',
                'lat':'45.2'
               }
        response=requests.post(url=url,params=parms)
        items=response.text
        self.assertEqual('SUCCESS',items)
    def test2(self):
        url='http://47.93.217.79:8085/aixue/user/getTeachers'
        querystring = {"name": "zhang576", "begin": "0", "size": "5"}
        response = requests.get(url,params=querystring)
        response=response.json()
        self.assertEqual('zhang576',response['data'][0]['userName'])
if __name__=='__main__':
    unittest.main()