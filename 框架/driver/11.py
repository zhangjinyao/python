from 框架.data.读取_shuju import aa
from 框架.report._mian_ import Test_run
import unittest


class  bb(unittest.TestCase):
    b = Test_run()
    def cc(self):
        self.b.run_多个(aa)
    def aaa(self):
        self.b.run_all()
if __name__=='__main__':
    bbb=aa()
    for i in bbb:
        if 'all' in i:
            Test_run().run_all()
        else:
            Test_run().run_多个(bbb)
