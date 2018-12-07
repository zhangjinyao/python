from  外部测试.config.公共 import aa
from selenium import webdriver
import unittest
class 测试(unittest.TestCase):
    # def test_1(self):
    #     self.b = aa().登陆()
    #     self.assertIn('摩尔精英',self.b)
    def test_2(self):
        self.c=aa().热门职位()
        self.assertEqual(self.c,'摩尔精英招聘')
if __name__=='__main__':
    unittest.main()


