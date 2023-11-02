
import pytest
import requests


class TestApi:

    def test_get_token(self):
        url = "https://api.weixin.qq.com/cgi-bin/token"
        params = {
            "grant_type": "client_credential",
            "appid": "wx51f605c204d32479",
            "secret": "4d90172f3c8d290c44409d1999893ccf"
        }

        res = requests.get(url=url, params=params)
        print(res.text)


if __name__ == '__main__':
    pytest.main()
