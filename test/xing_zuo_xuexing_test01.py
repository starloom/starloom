import json
import requests
from utils.redis_utils import redis_client
from bs4 import BeautifulSoup
date_ranges = [
        ("shuiping", (1, 20), (2, 18)),
        ("shuangyu", (2, 19), (3, 20)),
        ("baiyang", (3, 21), (4, 19)),
        ("jinniu", (4, 20), (5, 20)),
        ("shuangzi", (5, 21), (6, 21)),
        ("juxie", (6, 22), (7, 22)),
        ("shizi", (7, 23), (8, 22)),
        ("chunv", (8, 23), (9, 22)),
        ("tiancheng", (9, 23), (10, 23)),
        ("tianxie", (10, 24), (11, 22)),
        ("sheshou", (11, 23), (12, 21)),
        ("mojie", (12, 22), (1, 19)),
    ]
# https://www.smxs.com/xingzuoxuexing/read/id/6920.html 双鱼 B
def _get_smxs_xingzuo_xuexing () :
    url = f"https://www.smxs.com/xingzuoxuexing/index.html"
    _xuexing = ['A', 'B', 'O', 'AB']
    for sign, (start_month, start_day), (end_month, end_day) in date_ranges:
        for _xue in _xuexing:
            urlData = requests.post(url, data={'submit': 1, 'xingming': '', 'yearType': 1, 'sdYear': '2012', 'sdMonth': start_month,
                                               'sdDay': start_day, 'xuexing': _xue}).content
            soup = BeautifulSoup(urlData, 'html.parser')
            _div = soup.find_all('div', class_='box2 mt10 p10')[1]
            _h1 = _div.find('h1')
            if _h1:
                out_d = {'title': _h1.text, 'contents': []}
                contents = _div.find_all(['h2', 'p'])
                result = []
                current_dict = {}
                for content in contents:
                    if content.name == 'h2' and content.text != '':
                        if current_dict and 'content' in current_dict:
                            result.append(current_dict)
                            current_dict = {}
                        current_dict['title'] = content.text
                    elif content.name == 'p':
                        if 'content' not in current_dict:
                            current_dict['content'] = str(content)
                        if 'title' not in current_dict:
                            current_dict = {}
                        else:
                            current_dict['content'] += str(content)
                # 最后一个字典可能还没有添加进结果列表
                if current_dict and 'content' in current_dict and 'title' in current_dict:
                    result.append(current_dict)
                out_d['contents'] = result
                _key = 'XING_ZUO_XUE_XING_' + str(sign).upper() + '_' + _xue
                redis_client.set(_key, json.dumps(out_d, ensure_ascii=False))
                print(json.dumps(out_d, ensure_ascii=False))
            else:
                print(_xue, start_month, start_day, '没有匹配')
        print('----------------------')

def _get_error_data () :
    url = f"https://www.smxs.com/xingzuoxuexing/read/id/6920.html"
    urlData = requests.get(url).content
    soup = BeautifulSoup(urlData, 'html.parser')
    _div = soup.find_all('div', class_='box2 mt10 p10')[0]
    _h1 = _div.find('h1')
    out_d = {'title': _h1.text, 'contents': []}
    contents = _div.find_all(['h2', 'p'])
    result = []
    current_dict = {}
    for content in contents:
        if content.name == 'h2' and content.text != '':
            if current_dict and 'content' in current_dict:
                result.append(current_dict)
                current_dict = {}
            current_dict['title'] = content.text
        elif content.name == 'p':
            if 'content' not in current_dict:
                current_dict['content'] = str(content)
            if 'title' not in current_dict:
                current_dict = {}
            else:
                current_dict['content'] += str(content)
    # 最后一个字典可能还没有添加进结果列表
    if current_dict and 'content' in current_dict and 'title' in current_dict:
        result.append(current_dict)
    out_d['contents'] = result
    _key = 'XING_ZUO_XUE_XING_' + 'shuangyu'.upper() + '_B'
    # redis_client.set(_key, json.dumps(out_d, ensure_ascii=False))
    print(json.dumps(out_d, ensure_ascii=False))

def _get_smxs_xingzuo_xuexing_redis ():
    _xuexing = ['A', 'B', 'O', 'AB']
    for sign, (start_month, start_day), (end_month, end_day) in date_ranges:
        for _xue in _xuexing:
            _key = 'XING_ZUO_XUE_XING_' + str(sign).upper() + '_' + _xue
            _redis_data = redis_client.get(_key)
            if _redis_data:
                print(_redis_data.decode('UTF-8'))
_get_error_data()