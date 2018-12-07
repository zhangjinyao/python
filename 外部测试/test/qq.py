from  外部测试.config.qq import qq
import unittest
from 外部测试.data.qqshuju import bb
class 测试(unittest.TestCase):
    a=qq().aa
    shuju=bb()
    def test_1(self):
        b=self.a(self.shuju[0][0],self.shuju[1][0])
        self.assertIn('成功',b)
if __name__=='__main__':
    unittest.main()