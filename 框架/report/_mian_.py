from 框架.test.test_学校 import *
import time
from 外部测试.report import HTMLTestRunnertest


class Test_run():
    def run_多个(self,a):
        suit=unittest.TestSuite()
        for i in a:
            disvover=unittest.defaultTestLoader.discover(r'..\test',pattern='{}.py'.format(i.strip()))
            suit.addTest(disvover)
        now =time.strftime('%Y %m %d %H-%M-%S',time.localtime(time.time()))
        f=open('awb.html','wb')
        runner= HTMLTestRunnertest.HTMLTestRunner(tester='张金铫',
                                                  description='测试结果如下:',
                                                  title='学校测试报告',
                                                  stream=f)
        runner.run(suit)
        f.close()


    def run_all(self):
        suit=unittest.TestSuite()
        disvover=unittest.defaultTestLoader.discover(r'..\test',pattern='test*.py')
        suit.addTest(disvover)
        now = time.strftime('%Y %m %d %H-%M-%S', time.localtime(time.time()))
        f = open('awb.html', 'wb')
        runner = HTMLTestRunnertest.HTMLTestRunner(tester='张金铫',
                                                   description='测试结果如下:',

                                                   title='学校测试报告',
                                                   stream=f)
        runner.run(suit)
        f.close()
