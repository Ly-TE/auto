from utils import *
import time
import json
import requests

class TestBili:
    account_token = ''

    def setup_class(self):
        self.yaml_data = YamlUtil('tese_case.yml').read_yaml

    def setup_method(self, method):
        data = self.yaml_data[method.__name__]
        self.url, self.method, self.params = data['url'], data['method'], data['params']

    def test_search(self):
        print(self.yaml_data)
        data = self.yaml_data['test_search']
        url, method, params = data['url'], data['method'], data['params']

        # rep = req.call(url, method, params=params).json()
        # assert rep['data']['page']['count'] == 29
        # self.params['wts'] =  str(int(time.time()))
        # print(self.url, self.method, self.params,'ccccc')
        # headers = {
        #     'Accept': 'application/json, text/plain, */*',
        #     'Accept-Encoding': 'gzip, deflate',
        #     'Accept-Language': 'zh-CN,zh;q=0.9',
        #     'Cookie': "buvid3=EE608266-D29E-3D39-02E6-DA137654450128347infoc; b_nut=1671604728; _uuid=8105D6454-33DE-D8"
        #               "98-2D4F-AA51CC7F9C8429050infoc; CURRENT_FNVAL=4048; rpdid=|(u)~J~R~RlJ0J'uY~k~JuRR~; i-wanna-go-"
        #               "back=-1; buvid4=92A2A25E-2E49-2404-9163-631F457C2E7D29593-022122114-AOc2%2FD4Q7%2B%2Bb6wPB7dInRA"
        #               "%3D%3D; SESSDATA=9818423f%2C1692011031%2C670f4%2A22; bili_jct=9cc0b5211dd3c9e6e491a3b9eedfc214; "
        #               "DedeUserID=443106609; DedeUserID__ckMd5=f083fe41094c7ad2; sid=7yunjkqc; b_ut=5; header_theme_ver"
        #               "sion=CLOSE; nostalgia_conf=-1; home_feed_column=5; CURRENT_PID=1675d090-cab3-11ed-9e53-e7331738a"
        #               "adb; buvid_fp_plain=undefined; LIVE_BUVID=AUTO7016804854491132; CURRENT_QUALITY=80; hit-new-styl"
        #               "e-dyn=0; hit-dyn-v2=1; PVID=1; FEED_LIVE_VERSION=V8; fingerprint=6a9d3d875674fffb7ccd38b64c64607"
        #               "0; buvid_fp=4f35bb21a1ed92129737cd425d2c1eeb; bp_video_offset_443106609=806265327090401300; b_ls"
        #               "id=65E8610E6_188AF598BCF; innersign=0; bsource=search_baidu; browser_resolution=2560-1329",
        #     'Origin': 'https://space.bilibili.com',
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.'
        #                   '0.0.0 Safari/537.36'
        # }
        # rep = req.call(self.url, self.method, params=self.params).json()
        # rep = requests.get(url='https://api.bilibili.com/x/space/wbi/arc/search?mid=170901672&ps=30&tid=0&pn=1&keyword='
        #                        '&order=pubdate&platform=web&web_location=1550101&order_avoided=true&w_rid=e5b3ff6c4957d'
        #                        'c2b1e9c76516ba87589&wts=1686569270',headers=headers)
        # print('reeeeeeee',rep)
        # assert rep['data']['page']['count'] == 29
    #
    # def test_getSettings(self):
    #     # data = self.yaml_data['test_getSettings']
    #     # url, method, params = data['url'], data['method'], data['params']
    #     # rep = req.call(url, method, params=params).json()
    #     # assert rep['status'] == True
    #     rep = req.call(self.url, self.method, params=self.params).json()
    #     assert rep['status'] == True
    #
    # def test_locs(self):
    #     rep = req.call(self.url, self.method, params=self.params).json()
    #     assert rep['count'] == 1

    def test_geoip(self):
        res = req.call(self.url, self.method, params=self.params).json()
        assert res['data']['province_code'] == 'HB'
