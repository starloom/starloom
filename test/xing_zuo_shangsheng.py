import json
import requests
from utils.redis_utils import redis_client
from bs4 import BeautifulSoup
def _get_smxs_xingzuo_shangsheng () :
        for _j in range(4, 13):
            for _k in range(1, 32):
                for _g in range(0, 24):
                    for _h in range(0, 60):
                        url = f"https://www.smxs.com/shangshengxingzuo/index.html"
                        params = ''
                        if _g < 10:
                            _shi = '0' + str(_g)
                            if _h < 10:
                                _fen = '0' + str(_h)
                                params = {'submit': '1', 'xingming': '', 'yearType': '1', 'sdYear': '1987', 'sdMonth': _j,
                                 'sdDay': _k, 'hour': _shi, 'minute': _fen, 'sex': '1'}
                            else:
                                params = {'submit': '1', 'xingming': '', 'yearType': '1', 'sdYear': '1987', 'sdMonth': _j, 'sdDay': _k, 'hour': _shi, 'minute':  _h, 'sex': '1'}
                        else:
                            if _h < 10:
                                _fen = '0' + str(_h)
                                params = {'submit': '1', 'xingming': '', 'yearType': '1',
                                                                   'sdYear': '1987', 'sdMonth': _j, 'sdDay': _k,
                                                                   'hour': _g, 'minute': _fen, 'sex': '1'}
                            else:
                                params = {'submit': '1', 'xingming': '', 'yearType': '1',
                                                              'sdYear': '1987',
                                                              'sdMonth': _j, 'sdDay': _k, 'hour': _g, 'minute': _h,
                                                              'sex': '1'}
                        # print('请求参数:', json.dumps(params, ensure_ascii=False))
                        urlData = requests.post(url, data=params).content
                        soup = BeautifulSoup(urlData, 'html.parser')
                        _div = soup.find_all('div', class_='box2 mt10 p10')[1]
                        # print(_div)
                        contents = _div.find_all(['h1', 'p'])
                        result = []
                        current_dict = {}
                        for content in contents:
                            if content.name == 'h1' and content.text != '':
                                if current_dict and 'content' in current_dict:
                                    current_dict = {}
                                current_dict['title'] = content.text
                            elif content.name == 'p':
                                if 'content' not in current_dict:
                                    current_dict['content'] = str(content)
                                if 'title' not in current_dict:
                                    current_dict = {}
                                if 'content' in current_dict and current_dict['content'].find(str(content)) == -1:
                                    current_dict['content'] += str(content)
                        if current_dict and 'content' in current_dict and 'title' in current_dict:
                            result.append(current_dict)
                        _key = 'XING_ZUO_SHANG_SHENG_' + str(_j) + '_' + str(_k) + '_' + str(_g) + '_' + str(_h)
                        redis_client.set(_key, json.dumps(current_dict, ensure_ascii=False))
                        print(_key, json.dumps(current_dict, ensure_ascii=False))
# _get_smxs_xingzuo_shangsheng()

def _get_smxs_xingzuo_shangsheng_redis ():
    _keys = redis_client.keys('XING_ZUO_SHANG_SHENG_4_*')
    print(len(_keys))
    for _key in _keys:
        # redis_client.delete(_key.decode('UTF-8'))
        print(json.loads(redis_client.get(_key.decode('UTF-8')).decode('UTF-8')))
_get_smxs_xingzuo_shangsheng_redis()