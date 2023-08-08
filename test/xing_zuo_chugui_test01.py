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
# https://www.smxs.com/xingzuochugui/read/id/11954.html 白羊男
# https://www.smxs.com/xingzuochugui/read/id/11942.html 白羊女
def _get_smxs_xingzuo_chugui () :
    url = f"https://www.smxs.com//xingzuochugui/index.html"
    _xuexing = ['1', '2']
    for sign, (start_month, start_day), (end_month, end_day) in date_ranges:
        for _xue in _xuexing:
            urlData = requests.post(url, data={'submit': 1, 'xingming': '', 'yearType': 1, 'sdYear': '2012', 'sdMonth': start_month,
                                               'sdDay': start_day, 'sex': _xue}).content
            soup = BeautifulSoup(urlData, 'html.parser')
            _div = soup.find_all('div', class_='box2 mt10 p10')[1]
            _h1 = _div.find('h1')
            if _h1:
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
                        else:
                            current_dict['content'] += str(content)
                # 最后一个字典可能还没有添加进结果列表
                _key = 'XING_ZUO_CHU_GUI_' + str(sign).upper() + '_' + _xue
                redis_client.set(_key, json.dumps(current_dict, ensure_ascii=False))
                print(json.dumps(current_dict, ensure_ascii=False))
            else:
                print(_xue, start_month, start_day, '没有匹配')
        print('----------------------')
def _get_error_data () :
    url = f"https://www.smxs.com/xingzuochugui/read/id/11954.html"
    urlData = requests.get(url).content
    soup = BeautifulSoup(urlData, 'html.parser')
    _div = soup.find_all('div', class_='box2 mt10 p10')[0]
    _h1 = _div.find('h1')
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
            else:
                current_dict['content'] += str(content)
    # 最后一个字典可能还没有添加进结果列表

    _key = 'XING_ZUO_CHU_GUI_' + 'baiyang'.upper() + '_1'
    # redis_client.set(_key, json.dumps(current_dict, ensure_ascii=False))
    print(_key)
    print(json.dumps(current_dict, ensure_ascii=False))

def _get_smxs_xingzuo_xuexing_redis ():
    _xuexing = ['1', '2']
    for sign, (start_month, start_day), (end_month, end_day) in date_ranges:
        for _xue in _xuexing:
            _key = 'XING_ZUO_CHU_GUI_' + str(sign).upper() + '_' + _xue
            _redis_data = redis_client.get(_key)
            if _redis_data:
                print(_redis_data.decode('UTF-8'))
# _get_smxs_xingzuo_xuexing_redis()


# is_within_sex_ranges([('男', 1), ('女', 2)], [('nan', 1), ('nv', 2)])