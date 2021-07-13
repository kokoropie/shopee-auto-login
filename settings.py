# settings
import logging
import json
import requests
import os

from requests.exceptions import HTTPError

__all__ = ['log', 'CONFIG', 'req']

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%Y-%m-%dT%H:%M:%S')


log = logger = logging


class _Config:
    CHECK_IN_URL = 'https://shopee.vn/mkt/coins/api/v2/checkin_new'
    COIN_URL = 'https://shopee.vn/mkt/coins/api/v1/cs/coins'
    SETTING_URL = 'https://shopee.vn/mkt/coins/api/v2/settings'
    REFERER_URL = 'https://shopee.vn/shopee-coins'
    USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.67'


class ProductionConfig(_Config):
    LOG_LEVEL = logging.INFO


class DevelopmentConfig(_Config):
    LOG_LEVEL = logging.DEBUG


class HttpRequest(object):
    @staticmethod
    def to_python(json_str: str):
        return json.loads(json_str)

    @staticmethod
    def to_json(obj):
        return json.dumps(obj, indent=4, ensure_ascii=False)

    def request(self, method, url, max_retry: int = 2,
            params=None, data=None, json=None, headers=None, **kwargs):
        for i in range(max_retry + 1):
            try:
                s = requests.Session()
                response = s.request(method, url, params=params,
                    data=data, json=json, headers=headers, **kwargs)
            except HTTPError as e:
                log.error(f'HTTP error:\n{e}')
                log.error(f'The NO.{i + 1} request failed, retrying...')
            except KeyError as e:
                log.error(f'Wrong response:\n{e}')
                log.error(f'The NO.{i + 1} request failed, retrying...')
            except Exception as e:
                log.error(f'Unknown error:\n{e}')
                log.error(f'The NO.{i + 1} request failed, retrying...')
            else:
                return response
        raise Exception(f'All {max_retry + 1} HTTP requests failed, die.')


req = HttpRequest()

RUN_ENV = os.environ.get('RUN_ENV', 'dev')
if RUN_ENV == 'dev':
    CONFIG = DevelopmentConfig()
else:
    CONFIG = ProductionConfig()

log.basicConfig(level=CONFIG.LOG_LEVEL)

MESSAGE_TEMPLATE = '''{today:#^28}
    ID: {userid}
    Tài khoản: {username}
    Xu tăng: {increase_coins}
    Kết quả điểm danh: {status}
    Xu hiện tại: {coins}
    {end:#^28}'''

CONFIG.MESSAGE_TEMPLATE = MESSAGE_TEMPLATE