from socketserver import ThreadingMixIn
import HtmlTestRunner
import unittest
from BeautifulReport import BeautifulReport
from myfunc_test import TestMyfunc_test


if __name__ == '__main__':
    #使用TestSuit控制用例顺序，用例执行顺序是添加的顺序
    tests = [TestMyfunc_test('test_is_prime'), TestMyfunc_test('test_is_prime2'), TestMyfunc_test('test_is_prime3'), 
             TestMyfunc_test('test_add'), TestMyfunc_test('test_add2')]
    suite = unittest.TestSuite()
    suite.addTests(tests)
    
    file_path = './Reports' #定义报告所放置的位置
    # runner = HtmlTestRunner.HTMLTestRunner(output=file_path)
    # runner.run(suite)
    
    result = BeautifulReport(suite)
    result.report(description='测试deafult报告', filename='测试报告', report_dir=file_path, theme='theme_default')