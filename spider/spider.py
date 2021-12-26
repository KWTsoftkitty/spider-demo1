"""spider realty"""

import re

import requests

from extractor.extractor import extractor


class Spider:
    """spider realty"""

    def __init__(self, target_url, params, url_headers):
        self.headers = url_headers
        self.url = target_url
        self.payload = params
        self.datas = None

    def _get_datas(self, jq_pth):
        """get all data"""
        res = requests.get(self.url, params=self.payload, headers=self.headers)
        if res.status_code == 200:
            datas = extractor(res.json(), jq_pth)
            # permalinks is None, if not permalinks, permalinks == None区别
            if not datas:
                print('Response body is not contain data information')
            self.datas = datas
        else:
            print('request failed')

    def get_address_info(self, *jq_path):
        """get address"""
        if not self.datas:
            print('response data is None')
            return
        regex = r'-(?P<state>\w+)-(?P<post>\d+)'
        pattern = re.compile(regex)
        jq_path_address, jq_path_suburb, jq_path_permalink = jq_path
        _address_info = []
        for data in self.datas:
            address = extractor(data, jq_path_address)
            suburb = extractor(data, jq_path_suburb)
            permalink = extractor(data, jq_path_permalink)
            matched = pattern.search(permalink)
            if matched:
                _address_info.append(address.upper() + ', ' + suburb.upper() + ', ' + matched.group(
                    'state').upper() + ', ' + matched.group('post').upper())
        return _address_info


if __name__ == '__main__':
    url = 'https://www.atrealty.com.au/wp-json/hi-api/v1/properties'
    headers = {'Use-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, '
                            'like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
    payload = {'page': 1, 'per_page': 5}
    spider = Spider(url, payload, headers)
    spider._get_datas('.data')
    address_info = spider.get_address_info('.property_address', '.property_suburb', '.permalink')
    print('\n'.join(address_info))
