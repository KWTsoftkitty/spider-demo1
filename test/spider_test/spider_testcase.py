"""spider testcase"""

from unittest import TestCase
from unittest import mock

from spider.spider import Spider


class SpiderTestCase(TestCase):
    """spider testcase object"""

    def setUp(self):
        self.url = 'url'
        self.params = {'params': 'params'}
        self.headers = {'headers': 'headers'}
        self.spider = Spider(self.url, self.params, self.headers)
        self.spider.datas = [{'address': '86/2 falcon way', 'suburb': 'Tweed Heads South',
                              'permalink': 'https://test/86-2-falcon-way-tweed-heads-south-nsw-2486-39207/'},
                             {'address': '11 Etheridge Street', 'suburb': 'Mount Louisa',
                              'permalink': 'https://test/11-etheridge-street-mount-louisa-qld-4814-38283/'},
                             {'address': '1 Coghlan Road', 'suburb': 'Cowes',
                              'permalink': 'https://test/1-coghlan-road-cowes-vic-3922-39171/'},
                             {'address': '3 Boss Drive', 'suburb': 'Caboolture South',
                              'permalink': 'https://test/3-boss-drive-caboolture-south-qld-4510-39211/'},
                             {'address': '3/5 Tannock Street', 'suburb': 'Ashmore',
                              'permalink': 'https://test/3-5-tannock-street-ashmore-qld-4214-39227/'}]

    def test_get_address_info(self):
        """test get address info"""
        self.spider._get_datas = mock.Mock(return_value=self.spider.datas)
        self.spider._get_datas('.data')
        json_data = '''86/2 FALCON WAY, TWEED HEADS SOUTH, NSW, 2486\n11 ETHERIDGE STREET, MOUNT LOUISA, QLD, 4814\n1 COGHLAN ROAD, COWES, VIC, 3922\n3 BOSS DRIVE, CABOOLTURE SOUTH, QLD, 4510\n3/5 TANNOCK STREET, ASHMORE, QLD, 4214'''
        address_info = self.spider.get_address_info('.address', '.suburb', '.permalink')
        self.assertEqual(json_data, '\n'.join(address_info))
