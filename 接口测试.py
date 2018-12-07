# #接口测试：发送请求，验证响应是否符合需求的过程
#postman\JMeter
#requests 发送http请求    assert断言处理
# import requests
# import unittest#python自带的做单元测试自动化的框架
# import xlrd
# import time
# import HTMLTestRunne
# import HTMLTestRunnertest
# # unitest.Testcase     管理测试用例
# # unittest.TestSuite    测试套件
# # unittest.TestLoader     测试载入：将测试用力加载到测试套件中
# # unittest.TextTestRunner   执行测试用例
# #unitest中封装了检验返回的结果
# def aa(a):
#     url = 'http://testsupport-be.haofenshu.com/v1/schools/infos'
#     querystring = {"filterInput": "{}".format(a)}
#     headers = {
#
#         'cache-control': "no-cache,no-cache",
#         'cookie': "yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA",
#         'referer': "https://baijiahao.baidu.com/s?id=1601142086151469933&wfr=spider&for=pc",
#         'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 BIDUBrowser/8.7 Safari/537.36",
#         'x-devtools-emulate-network-conditions-client-id': "D804B14E-D1B4-4893-8ACF-5ABCB81C8702"
#     }
#     response = requests.get(url=url, headers=headers, params=querystring)
#     b = response.json()
#     return b
# class 学校(unittest.TestCase):
#     #def setUp(self):    #初始化测试环境   每次执行测试用例前执行
#     def cc(self):
#         shuju=[]
#         f=xlrd.open_workbook('小.xls')
#         sheet=f.sheets()[0]
#         num=sheet.nrows
#         for i in range(1,num):
#             aaa=sheet.row_values(i)
#             shuju.append(aaa)
#         return shuju
#     #def tearDown(self):             # 清理环境，每一次用例执行之后去执行
#         #print(2)
#     def test_1(self):                   #测试用例必须以test开头后面的以ascll排序
#         shuju=self.cc()
#         b=aa(shuju[0][0])
#         self.assertEqual(b['code'],int(shuju[0][1]))
#        # self.assertEqual(type(b["data"]),shuju[0][2])
#     def test_2(self):
#         shuju=self.cc()
#         b=aa(shuju[1][0])
#         self.assertEqual(b['code'],int(shuju[1][1]))
#        # self.assertEqual(len(b['data'],range(int(shuju[0][2]))))
#     def test_3(self):
#         shuju=self.cc()
#         b=aa(shuju[2][0])
#         self.assertEqual(b['code'],int(shuju[2][1]))
#     # def test_4(self):
#     #     b=aa(123)
#     #     self.assertIn('学校',b['msg'])
# if __name__=='__main__'   :
#     #生成测试报告，创建一个测试套件
#     suit=unittest.TestSuite()
#     #添加测试用例,将测试用例添加到测试套件中
#     # suit.addTest(学校('test_1'))
#     # suit.addTest(学校('test_2'))
#     # suit.addTest(学校('test_3'))
#     # suit.addTest(学校('test_4'))
#     #将整个类中的所有测试用例添加到测试套件中
#     suit.addTest(unittest.makeSuite(学校))
#     now =time.strftime('%Y %m %d %H-%M-%S',time.localtime(time.time()))
#     f=open('ab.html','wb')
#     runner=HTMLTestRunnertest.HTMLTestRunner(tester='张金铫',
#                                              description='测试结果如下:',
#                                              title='学校测试报告',
#                                              stream=f)
#     runner.run(suit)
#     f.close()
#



