"""extractor_test testcase"""

from unittest import TestCase
from extractor.extractor import extractor


class ExtractorTestCase(TestCase):
    """extractor_test object"""
    def setUp(self):
        """测试用例初始化"""
        self.json_data_for_extract_str = {"a": 1, "b": 2, "c": 3, "d": 4}
        self.json_data_for_extract_list = {
            'data': [{"a": 1, "b": 2, "c": 3, "d": 4}, {"a": 11, "b": 22, "c": 33, "d": 44},
                     {"a": 111, "b": 222, "c": 333, "d": 444},
                     {"a": 1111, "b": 2222, "c": 3333, "d": 4444}]}

    def test_extractor_none(self):
        """test extractor's jq_path do not get value"""
        self.assertIsNone(extractor(self.json_data_for_extract_str, ".x"))

    def test_extractor_str(self):
        """test extract str"""
        a_value = extractor(self.json_data_for_extract_str, ".a")
        self.assertEqual(1, a_value)

    def test_extractor_list(self):
        """测试dict根据key获取value"""
        a_value = extractor(self.json_data_for_extract_list, ".data")
        self.assertEqual([{"a": 1, "b": 2, "c": 3, "d": 4}, {"a": 11, "b": 22, "c": 33, "d": 44},
                     {"a": 111, "b": 222, "c": 333, "d": 444},
                     {"a": 1111, "b": 2222, "c": 3333, "d": 4444}], a_value)


