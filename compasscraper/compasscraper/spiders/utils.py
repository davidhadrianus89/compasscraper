import itertools

import requests
from lxml.html import fromstring


class ExpectedConditionModifier:
    """ Use with WebDriverWait to combine expected_conditions
        in an OR.
    """
    def __init__(self, *args):
        self.ecs = args

    def __call__(self, driver):
        for fn in self.ecs:
            try:
                if fn(driver):
                    return True
            except:
                pass


def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies


def list_to_dict(_list):
    ringkasan_spesifikasi = []
    for line in _list:
        if not line.strip() == "":
            ringkasan_spesifikasi.append(line)

    return dict(itertools.zip_longest(*[iter(ringkasan_spesifikasi)] * 2, fillvalue=""))