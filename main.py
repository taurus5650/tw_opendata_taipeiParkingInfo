"""
api : https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_alldesc.json
dataset : https://data.gov.tw/dataset/128435

1. 列出 car 和 motor 小於 5 的停車格數
2. 列出每個 area  的 car 和 motor 總停車格數
3. 列出 car 和 motor 相加總數，列出最高 5 名

"""

import json
import textwrap

import allure
import requests

from utility.time import Time

from .configurations import GeneralConfig


class BaseAPI:

    def __init__(self, waiting_time=None):
        self.waiting_time = waiting_time or GeneralConfig.DEFAULT_ACCEPTABLE_WAITING_TIME
        self._session = requests.Session()

    @allure.step("[{method}] {url}")
    def _send_request(self, method: str, url: str, **kwargs):
        acceptable_wating_time = kwargs.pop('waiting_time', None) or self.waiting_time
        try:
            response = self._session.request(method, url, **kwargs)
            duration = response.elapsed.total_seconds()
            self._debug_print(response=response)
            assert duration <= acceptable_wating_time, (f"Response Time > {acceptable_wating_time}s, Cost: {duration}s")
        except requests.exceptions.RequestException as e:
            response = None
            print(f"Request Error > url: [{method}] {url}, kwargs: {kwargs}, error: {str(e)}")
        return response

    def _debug_print(self, response: requests.Response):
        req_body = response.request.body
        if req_body:
            req_body = json.loads(req_body)

        information = {
            'datetime': f"{Time.now():%Y/%m/%d %H:%M:%S}",
            'request': f"[{response.request.method}] {response.request.url}",
            'headers': json.dumps(dict(response.request.headers), indent=4, ensure_ascii=False),
            'body': json.dumps(req_body, indent=4, ensure_ascii=False),
            'elapsed': f"{response.elapsed.total_seconds()} s",
            'status': response.status_code,
            'response': json.dumps(response.json(), indent=4, ensure_ascii=False)
        }

        print(textwrap.dedent(
            """
            --------------------------------
            🐞 debug prints
            --------------------------------
            {content}
            --------------------------------
            """
        ).format(content=''.join([f"\n * {key}: {val}" for key, val in information.items()])))
