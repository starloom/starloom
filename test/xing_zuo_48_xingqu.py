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
# https://www.smxs.com/xingqu48/index.html
def _get_smxs_xingzuo_48_xingqu () :
    for _i in range(2030, 2031):
        for _j in range(1, 13):
            for _k in range(1, 32):
                url = f"https://www.smxs.com/xingqu48/index.html"
                urlData = requests.post(url, data={'submit': '1', 'xingming': '', 'yearType': '1', 'sdYear': _i, 'sdMonth': _j, 'sdDay': _k}).content
                soup = BeautifulSoup(urlData, 'html.parser')
                _div = soup.find_all('div', class_='box2 mt10 p10')[1]
                _all_a = soup.find_all('a')
                for _a in _all_a:
                    del _a['href']
                    del _a['target']
                contents = _div.find_all(['h1', 'p'])
                result = []
                current_dict = {}
                for content in contents:
                    if content.name == 'h1' and content.text != '':
                        if current_dict and 'content' in current_dict:
                            result.append(current_dict)
                            current_dict = {}
                        current_dict['title'] = content.text
                    elif content.name == 'p' and content.text.find('优点：') == -1 and content.text.find('缺点：') == -1 and content.text.find('情侣：') == -1 and content.text.find('夫妻：') == -1 and content.text.find('朋友：') == -1 and content.text.find('家人：') == -1 and content.text.find('同事：') == -1:
                        if 'content' not in current_dict:
                            current_dict['content'] = str(content).replace('<a>', '').replace('</a>', '')
                        if 'title' not in current_dict:
                            current_dict = {}
                        if 'content' in current_dict and current_dict['content'].find(str(content)) == -1:
                            current_dict['content'] += str(content).replace('<a>', '').replace('</a>', '')
                    else:
                        _strong = content.find('strong')
                        if _strong:
                            current_dict2 = {'title': _strong.text, 'content': content.text.replace(_strong.text, '')}
                            result.append(current_dict2)
                        else:
                            if content.text.find('同事：') != -1:
                                current_dict2 = {'title': '同事：',
                                                 'content': content.text.replace('同事：', '')}
                                result.append(current_dict2)
                # 最后一个字典可能还没有添加进结果列表
                if current_dict and 'content' in current_dict and 'title' in current_dict:
                    result.append(current_dict)
                _key = 'XING_ZUO_48_' + str(_i) + '_' + str(_j) + '_' + str(_k)
                if len(result) == 0:
                    redis_client.delete(_key)
                else:
                    redis_client.set(_key, json.dumps(result, ensure_ascii=False))
                    print(_i, _j, _k, json.dumps(result, ensure_ascii=False))
def _get_smxs_xingzuo_xuexing_redis ():
    print()
_get_smxs_xingzuo_48_xingqu()
