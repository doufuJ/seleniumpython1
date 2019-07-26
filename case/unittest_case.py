
# coding = utf-8
import unittest

class FirstCase01(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        print("所有case之前执行")

    @classmethod
    def tearDownClass(cls):
        print("所有case执行之后执行")

    def setUp(self):
        print("这个是case的前置条件")

    def tearDown(self):
        print("这个是case的后置条件")
    @unittest.skip('不执行第一条')
    def testfirst01(self):
        print("这是第一个case")

    def testfirst02(self):
        print("这是第二条case")


if __name__ == '__main__':
    unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(FirstCase01('testfirst02'))
    # unittest.TextTestRunner().run(suite)
