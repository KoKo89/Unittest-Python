from operator import truediv
import unittest#引入unittest框架
from myfunc import isprime, add, divide #引入测试模块

'''
定义测试方法类，需要继承unittest.TestCase
表示该类从哪个类继承下来的
'''
class TestMyfunc_test(unittest.TestCase): 
    
    def setUp(self) -> None: #每个用例执行前会调用setUp方法准备测试环境
        return super().setUp()
    
    def tearDown(self) -> None: #每个用例执行后会调用tearDown方法进行环境清理
        return super().tearDown()
    
    def test_is_prime(self): #测试用例以test_开头
        print('is prime')
        self.assertTrue(isprime(5))
        self.assertFalse(isprime(8))
        
    #期望该方法失败，不计入失败case数量
    @unittest.expectedFailure
    def test_is_prime2(self): 
        print('is prime2')
        self.assertTrue(isprime(8))
    
    #过滤整个测试function函数
    @unittest.skip("skip")
    def test_is_prime3(self): 
        print('is prime3')
        self.assertTrue(isprime(8))
    
    def test_add(self):
        print('add')
        self.assertEqual(3, add(1,2))
        self.assertNotEqual(4, add(1,2))
        
    #过滤该function函数的某个测试点
    def test_add2(self):
        print('add2')
        if self.assertEqual(3, add(1,2)):
            self.skipTest('skipTest')
            self.assertNotEqual(4, add(1,2))
        
        self.assertNotEqual(5, add(4,2))
        
    def test_divide(self):
        print('divide')
        self.assertEqual(1, divide(2,2))
        self.assertNotEqual(1, divide(2,3))

# if __name__ == '__main__':
#     unittest.main()
    
if __name__ == '__main__':
    
    #使用TestSuit控制用例顺序，用例执行顺序是添加的顺序
    tests = [TestMyfunc_test('test_is_prime'), TestMyfunc_test('test_is_prime2')]
    suite = unittest.TestSuite()
    suite.addTests(tests)
    
    runner = unittest.TextTestRunner()
    runner.run(suite)