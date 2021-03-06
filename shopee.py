import hashlib
import json
import time
import os
from datetime import datetime

from settings import log, CONFIG, req

class Base(object):
    def __init__(self, cookies: str = None, token: str = None):
        if not isinstance(cookies, str):
            raise TypeError('%s want a %s but got %s' %
                            (self.__class__, type(__name__), type(cookies)))
        if not isinstance(token, str):
            raise TypeError('%s want a %s but got %s' %
                            (self.__class__, type(__name__), type(token)))
        self._cookie = cookies
        self._token = token

    def get_header(self):
        header = {
            'User-Agent': CONFIG.USER_AGENT,
            'Referer': CONFIG.REFERER_URL,
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept': 'application/json',
            'Cookie': self._cookie,
            'Content-Type': 'application/json',
            'content-length': '2',
            'x-api-source': 'pc',
            'x-csrftoken': self._token,
            'x-shopee-language': 'vi'
        }
        return header

    def get_header_2(self):
        header_2 = {
            'User-Agent': CONFIG.USER_AGENT,
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept': '*/*',
            'Cookie': self._cookie,
            'x-api-source': 'pc',
            'x-shopee-language': 'vi'
        }
        return header_2

class Sign(Base):
    def __init__(self, cookies: str = None, token: str = None):
        super(Sign, self).__init__(cookies, token)

    def get_header(self):
        header = super(Sign, self).get_header()
        return header

    def get_header_2(self):
        header_2 = super(Sign, self).get_header_2()
        return header_2

    def get_coin(self):
        coin_url = CONFIG.COIN_URL
        try:
            response = req.request(
                'get', coin_url, headers=self.get_header_2()).text
        except Exception as e:
            raise Exception(e)

        return req.to_python(response)

    def run(self):
        today = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        message_list = []
        message = {
            'today': today,
            'end': ''
        }
        try:
            response = req.to_python(req.request(
                'post', CONFIG.CHECK_IN_URL, headers=self.get_header(),
                data=json.dumps({}, ensure_ascii=False)).text)
        except Exception as e:
            raise Exception(e)

        code = response.get('code', 99999)
        # 0:      success
        if code != 0:
            message_list.append(response)
            message_list.append("\n".join(response['msg']).join("\n"))
            return ''.join(str(v) for v in message_list)

        coins = self.get_coin()
        if coins: 
            message['coins'] = coins.get('coins', 0)
        else: 
            message['coins'] = 0
        message['increase_coins'] = response['data']['increase_coins']
        message['status'] = response['msg']
        message['userid'] = response['data']['userid']
        message['username'] = response['data']['username']
        message_list.append(self.message.format(**message))

        return ''.join(str(v) for v in message_list)

    @property
    def message(self):
        return CONFIG.MESSAGE_TEMPLATE

if __name__ == '__main__':
    log.info('B???t ?????u')
    ret = success_num = fail_num = 0

    OS_COOKIE = ''

    if os.environ.get('OS_COOKIE', '') != '':
        OS_COOKIE = os.environ['OS_COOKIE']

    cookie_list = OS_COOKIE.split('#')
    for i in range(len(cookie_list)):
        log.info(f'Chu???n b??? t??i kho???n th??? {i + 1} ??i???m danh...')
        csrftoken = cookie_list[i].split('csrftoken=')[1].split(';')[0]
        try:
            log.info(cookie_list[i])
            msg = f'T??i kho???n th??? {i + 1}:\n{Sign(cookie_list[i], csrftoken).run()}'
            log.info(msg)
            success_num = success_num + 1
        except Exception as e:
            log.info(cookie_list[i])
            msg = f'T??i kho???n th??? {i + 1}:\n{e}'
            fail_num = fail_num + 1
            log.error(msg)
            ret = -1
        continue
    if ret != 0:
        log.error('Abnormal exit')
        exit(ret)
    log.info('K???t th??c')
