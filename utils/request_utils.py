import requests

from utils.config import host
from utils.decorators import request_check


class RequestsUtil:

    def __init__(self):
        self.sess = requests.session()
        self.sess.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cookie': "buvid3=EE608266-D29E-3D39-02E6-DA137654450128347infoc; b_nut=1671604728; _uuid=8105D6454-33DE-D8"
                      "98-2D4F-AA51CC7F9C8429050infoc; CURRENT_FNVAL=4048; rpdid=|(u)~J~R~RlJ0J'uY~k~JuRR~; i-wanna-go-"
                      "back=-1; buvid4=92A2A25E-2E49-2404-9163-631F457C2E7D29593-022122114-AOc2%2FD4Q7%2B%2Bb6wPB7dInRA"
                      "%3D%3D; SESSDATA=9818423f%2C1692011031%2C670f4%2A22; bili_jct=9cc0b5211dd3c9e6e491a3b9eedfc214; "
                      "DedeUserID=443106609; DedeUserID__ckMd5=f083fe41094c7ad2; sid=7yunjkqc; b_ut=5; header_theme_ver"
                      "sion=CLOSE; nostalgia_conf=-1; home_feed_column=5; CURRENT_PID=1675d090-cab3-11ed-9e53-e7331738a"
                      "adb; buvid_fp_plain=undefined; LIVE_BUVID=AUTO7016804854491132; CURRENT_QUALITY=80; hit-new-styl"
                      "e-dyn=0; hit-dyn-v2=1; PVID=1; FEED_LIVE_VERSION=V8; fingerprint=6a9d3d875674fffb7ccd38b64c64607"
                      "0; buvid_fp=4f35bb21a1ed92129737cd425d2c1eeb; bp_video_offset_443106609=806265327090401300; b_ls"
                      "id=65E8610E6_188AF598BCF; innersign=0; bsource=search_baidu; browser_resolution=2560-1329",
            'Origin': 'https://space.bilibili.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.'
                          '0.0.0 Safari/537.36'
        }

    @request_check
    def call(self, url, method, **kwargs):
        params = kwargs['params'] if 'params' in kwargs else None
        data = kwargs['data'] if 'data' in kwargs else None
        json = kwargs['json'] if 'json' in kwargs else None
        files = kwargs['files'] if 'files' in kwargs else None
        headers = kwargs['headers'] if 'headers' in kwargs else None
        return self.sess.request(method=method, url=host + url, params=params, data=data, json=json, files=files,
                                 headers=headers)


req = RequestsUtil()
