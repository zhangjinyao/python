import unittest#python自带的做单元测试自动化的框架
from 框架.data.读取_shuju  import shuju
from 框架.config.xuexiao_chaxun import 学校1
class 学校33(unittest.TestCase):
    tes_2=学校1().aa
    shuju=shuju()
    def test_1(self):  # 测试用例必须以test开头后面的以ascll排序
        b=self.tes_2(self.shuju[0][0])
        self.assertEqual(b['code'],int(self.shuju[0][1]))
       # self.assertEqual(type(b["data"]),shuju[0][2])
    def test_2(self):
        b=self.tes_2(self.shuju[1][0])
        self.assertEqual(b['code'],int(self.shuju[1][1]))
       # self.assertEqual(len(b['data'],range(int(shuju[0][2]))))
    def test_3(self):
        b=self.tes_2(self.shuju[2][0])
        self.assertEqual(b['code'],int(self.shuju[2][1]))
