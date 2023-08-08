import json
import requests
from utils.redis_utils import redis_client
from bs4 import BeautifulSoup
def _get_smxs_xingzuo_xiajiang () :
        for _j in range(1, 13):
            for _k in range(1, 32):
                for _g in range(0, 24):
                    for _n in range (1, 3):
                        url = f"https://www.smxs.com/xiajiangxingzuo/index.html"
                        urlData = ''
                        if _g < 10:
                            _shi = '0' + str(_g)
                            urlData = requests.post(url, data={'submit': '1', 'xingming': '', 'yearType': '1', 'sdYear': '1987', 'sdMonth': _j, 'sdDay': _k, 'hour': _shi, 'sex': _n}).content
                        else:
                            urlData = requests.post(url,
                                                    data={'submit': '1', 'xingming': '', 'yearType': '1', 'sdYear': '1987',
                                                          'sdMonth': _j, 'sdDay': _k, 'hour': _g, 'sex': _n}).content
                        soup = BeautifulSoup(urlData, 'html.parser')
                        _div = soup.find_all('div', class_='box2 mt10 p10')[1]

                        contents = _div.find_all(['h1', 'p'])
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
                        # 最后一个字典可能还没有添加进结果列表
                        _key = 'XING_ZUO_XIA_JIANG_' + '_' + str(_j) + '_' + str(_k) + '_' + str(_g) + '_' + str(_n)
                        if 'title' in current_dict.keys() and 'content' in current_dict.keys():
                            redis_client.delete(_key)
                            redis_client.set(_key, json.dumps(current_dict, ensure_ascii=False))
                            print(str(_j), str(_k),  str(_g), str(_n), json.dumps(current_dict, ensure_ascii=False))
                        else:
                            print(str(_j), str(_k),  str(_g), str(_n), ' 没得数据')

def _get_smxs_xingzuo_xiajiang_redis ():
    _keys = redis_client.keys('XING_ZUO_XIA_JIANG_*')
    print(len(_keys))
    for _key in _keys:
        print(_key)
_get_smxs_xingzuo_xiajiang_redis()