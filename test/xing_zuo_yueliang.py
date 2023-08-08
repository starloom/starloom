import json
import requests
from utils.redis_utils import redis_client
from fortunetelling.yunshiConfig import date_ranges2
from bs4 import BeautifulSoup
def _get_smxs_xingzuo_yueliang () :
    for sign, (start_month, start_day), (end_month, end_day) in date_ranges2:
        for _n in range(1, 3):
            url = f"https://www.smxs.com/yueliangxingzuo/index.html"
            params = {'submit': '1', 'xingming': '', 'yearType': '1',
                                          'sdYear': '1987',
                                          'sdMonth': start_month, 'sdDay': start_day, 'hour': '15', 'minute': '15',
                                          'sex': _n}
            # print('请求参数:', json.dumps(params, ensure_ascii=False))
            urlData = requests.post(url, data=params).content
            soup = BeautifulSoup(urlData, 'html.parser')
            _div = soup.find_all('div', class_='box2 mt10 p10')[1]
            _title = _div.find('h2').text
            # print(_title)
            current_dict = {'title': _title, 'contents': []}
            _a = _div.find('a')
            _xingge_url_data = requests.get('https://www.smxs.com/' + _a.attrs['href']).content
            # print(_a.text)
            _xingge_soup = BeautifulSoup(_xingge_url_data, 'html.parser')
            _xingge_div = _xingge_soup.find_all('div', class_='box2 mt10 p10')[0]
            # print(_xingge_div)
            contents = _xingge_div.find_all(['h1', 'p'])
            result = []
            current_dict_sub = {}
            for content in contents:
                if content.name == 'h1' and content.text != '':
                    if current_dict_sub and 'content' in current_dict_sub:
                        current_dict_sub = {}
                    current_dict_sub['title'] = content.text
                elif content.name == 'p':
                    if 'content' not in current_dict_sub:
                        _all_spans = content.find_all('span')
                        for _span in _all_spans:
                            if _span.attrs and 'style' in _span.attrs:
                                _style = _span.attrs['style']
                                if _style == 'color:#000000;':
                                    del _span.attrs['style']
                        current_dict_sub['content'] = str(content)
                    if 'title' not in current_dict_sub:
                        current_dict_sub = {}
                    if 'content' in current_dict_sub and current_dict_sub['content'].find(str(content)) == -1:
                        _all_spans = content.find_all('span')
                        for _span in _all_spans:
                            if _span.attrs and 'style' in _span.attrs:
                                _style = _span.attrs['style']
                                if _style == 'color:#000000;':
                                    del _span.attrs['style']
                        current_dict_sub['content'] += str(content)
            if current_dict_sub and 'content' in current_dict_sub and 'title' in current_dict_sub:
                result.append(current_dict_sub)
            current_dict['contents'] = result
            _key = 'XING_ZUO_YUE_LIANG_' + str(sign).upper() + '_' + str(_n)
            redis_client.set(_key, json.dumps(current_dict, ensure_ascii=False))
            print(_key, json.dumps(current_dict, ensure_ascii=False))

def _get_smxs_xingzuo_yueliang_redis ():
    _keys = redis_client.keys('XING_ZUO_YUE_LIANG_*')
    print(len(_keys))
    for _key in _keys:
        print(redis_client.get(_key.decode('UTF-8')).decode('UTF-8'))
_get_smxs_xingzuo_yueliang_redis()
