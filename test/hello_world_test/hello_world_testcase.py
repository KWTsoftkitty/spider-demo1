"""
Test Case
"""


from unittest import TestCase
from unittest.mock import patch
from entity.hello_world import HelloWorld


class HelloWorldTestCase(TestCase):
    """
    helloWorld类的测试用例
    """
    def setUp(self):
        """
        用例初始化
        :return:
        """
        self.helloWorld = HelloWorld('Wentao')

    def test_name(self):
        """
        测试对象的name属性值
        :return: true or false
        """
        self.assertEqual('Wentao', self.helloWorld.name)

    def test_say_hello(self):
        """
        测试对象的say_hello方法
        :return: true or false
        """
        with patch('builtins.print') as mocked_print:
            self.helloWorld.say_hello()
            mocked_print.assert_called_with('Hello, Wentao')
