from datetime import datetime
import re
from dateutil.parser import parse
import json
from utils.redis_utils import redis_client
import requests
from bs4 import BeautifulSoup
from fortunetelling.yunshiConfig import xingzuo_data_map,ai_qing_guan_map,xing_zuo_date_map,date_ranges
def test_redis () :
    user_data = {
        'name': '张三',
        'age': 25,
        'email': 'alice@example.com'
    }
    for field, value in user_data.items():
        redis_client.hset('user:1', field, value)
    user_info = redis_client.hgetall('user:1')
    decoded_data = {key.decode('utf-8'): value.decode('utf-8') for key, value in user_info.items()}
    print(decoded_data)
def fibonacci(p_labels, index):
    if index == len(p_labels):
        return {'p': '', 'index': index}
    p = p_labels[index]
    index = index + 1
    if len(p.find_all('p')) > 0:
        return {'p': p, 'index': index}
    else:
        return fibonacci(p_labels, index)

def fibonacci_shengrimima(p_labels, index, content):
    if index == len(p_labels):
        return {'p': '', 'index': index}
    p = p_labels[index]
    index = index + 1
    if len(content['content']) > 0 and content['content'].find(str(p)) != -1:
        return fibonacci_shengrimima(p_labels, index, content)
    else:
        return {'p': p, 'index': index}
def get_smxs_shengrishu () :
    for i in range(1, 13):
        for j in range(1, 32):
            _key = 'SHENG_RI_SHU_' + str(i) + '-' + str(j)
            url = f"https://www.smxs.com/shengrishu/read/date/{i}_{j}.html"
            urlData = requests.get(url).content
            soup = BeautifulSoup(urlData, 'html.parser')
            div_1 = soup.find_all('div', class_='box2 mt10 p10')[0]
            h1_text = div_1.find('h1').text
            h2_labels = div_1.find_all('h2')
            p_labels = div_1.find_all('p')
            h2_content_index = 0
            out_d = {'title':h1_text, 'contents': []}
            for h2_label in h2_labels:
                res_obj = fibonacci(p_labels, h2_content_index)
                out_s = {'title': h2_label.text, 'content': str(res_obj['p'])}
                out_d['contents'].append(out_s)
                h2_content_index = res_obj['index']
            redis_client.set(_key, json.dumps(out_d, ensure_ascii=False))
            print(json.dumps(out_d, ensure_ascii=False))
def get_smxs_shengrishu_redis ():
    for i in range(1, 13):
        for j in range(1, 32):
            _key = 'SHENG_RI_SHU_' + str(i) + '-' + str(j)
            _redis_data = redis_client.get(_key)
            print(_redis_data.decode('UTF-8'))

def get_smxs_shengrimima ():
    for i in range(1, 13):
        for j in range(1, 32):
            _key = 'SHENG_RI_MI_MA_' + str(i) + '-' + str(j)
            url = f"https://www.smxs.com/shengrimima/read/date/{i}_{j}.html"
            urlData = requests.get(url).content
            soup = BeautifulSoup(urlData, 'html.parser')
            div_1 = soup.find_all('div', class_='box2 mt10 p10')[0]
            # print(div_1)
            h1_text = div_1.find('h1').text
            # print(h1_text)
            h2_labels = div_1.find_all('h2')
            p_labels = div_1.find_all('p')
            if len(p_labels) == 0:
                continue
            title_1 = div_1.find_all('p')[0]
            title_2 = div_1.find_all('p')[1]
            title_3 = div_1.find_all('p')[2]
            title_4 = div_1.find_all('p')[3]
            content_ = str(title_1) + str(title_2) + str(title_3) + str(title_4)
            h2_content_index = 4
            out_d = {'title': h1_text, 'content': content_, 'contents': []}
            for h2_label in h2_labels:
                _index = len(out_d['contents']) - 1
                res_obj = fibonacci_shengrimima(p_labels, h2_content_index, {'title': '', 'content': ''} if _index < 0 else out_d['contents'][_index])
                out_s = {'title': h2_label.text, 'content': str(res_obj['p'])}
                out_d['contents'].append(out_s)
                h2_content_index = res_obj['index']
            redis_client.set(_key, json.dumps(out_d, ensure_ascii=False))
            print(json.dumps(out_d, ensure_ascii=False))
def get_smxs_shengrimima_redis ():
    for i in range(1, 13):
        for j in range(1, 32):
            _key = 'SHENG_RI_MI_MA_' + str(i) + '-' + str(j)
            _redis_data = redis_client.get(_key)
            print(_redis_data.decode('UTF-8'))

def get_smxs_shengrihua ():
    for i in range(1, 13):
        for j in range(1, 32):
            _key = 'SHENG_RI_HUA_' + str(i) + '-' + str(j)
            url = f"https://www.smxs.com/shengrihua/read/date/{i}_{j}.html"
            urlData = requests.get(url).content
            soup = BeautifulSoup(urlData, 'html.parser')
            div_1 = soup.find_all('div', class_='box2 mt10 p10')[0]
            # print(div_1)
            h1_text = div_1.find('h1').text
            # print(h1_text)
            h2_labels = div_1.find_all('h2')
            p_labels = div_1.find_all('p')
            h2_content_index = 0
            out_d = {'title': h1_text, 'contents': []}
            for h2_label in h2_labels:
                _index = len(out_d['contents']) - 1
                res_obj = fibonacci_shengrimima(p_labels, h2_content_index, {'title': '', 'content': ''} if _index < 0 else out_d['contents'][_index])
                out_s = {'title': h2_label.text, 'content': str(res_obj['p'])}
                out_d['contents'].append(out_s)
                h2_content_index = res_obj['index']
            redis_client.set(_key, json.dumps(out_d, ensure_ascii=False))
            print(json.dumps(out_d, ensure_ascii=False))
def get_smxs_shengrihua_redis ():
    for i in range(1, 13):
        for j in range(1, 32):
            _key = 'SHENG_RI_HUA_' + str(i) + '-' + str(j)
            _redis_data = redis_client.get(_key)
            print(_redis_data.decode('UTF-8'))

def get_smxs_xingzuo_query ():
    for key in xingzuo_data_map.keys():
        _key = 'XING_ZUO_CHA_XUN_' + key
        url = f"https://www.smxs.com/xingzuo/{key}.html"
        out_ds = []
        urlData = requests.get(url).content
        soup = BeautifulSoup(urlData, 'html.parser')
        _div = soup.find_all('div', class_='box2 mt10 p10')[0]
        _a_array_1 = _div.find_all('a')[1]
        _url_1 = _a_array_1['href']
        _a_array_2 = _div.find_all('a')[2]
        _url_2 = _a_array_2['href']
        _a_array_3 = _div.find_all('a')[3]
        _url_3 = _a_array_3['href']
        _a_array_4 = _div.find_all('a')[4]
        _url_4 = _a_array_4['href']
        _a_array_5 = _div.find_all('a')[5]
        _url_5 = _a_array_5['href']
        _a_array_6 = _div.find_all('a')[6]
        _url_6 = _a_array_6['href']
        _xing_zuo_jian_jie = _div.find('h1').text
        _xing_zuo_jian_jie_1 = _div.find('span', class_='gray').text
        _xing_zuo_content = _div.find('p')
        _xing_zuo_te_zhi = _div.find('h2').text
        _div_xzintro = _div.find_all('div', class_='xzintro')[0]
        _xing_zuo_te_zhi_xzintro = str(_div_xzintro).replace('<div class="xzintro">', '').replace('</div>', '')
        _title = _xing_zuo_jian_jie + '(' + xing_zuo_date_map[_xing_zuo_jian_jie] + ')'
        out_d = {'title': _title, 'content': str(_xing_zuo_content), 'contents': [{'title': _xing_zuo_te_zhi, 'content': _xing_zuo_te_zhi_xzintro}]}
        result = out_d['contents']
        contents = _div.find_all(['p', 'h2'])
        current_dict = {}
        for content in contents:
            if content.name == 'h2':
                if content.text.find('座特质') !=-1:
                    continue
                if current_dict:
                    result.append(current_dict)
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
        if current_dict:
            result.append(current_dict)
        out_ds.append(out_d)
        out_ds.append(get_shenhua(_url_1))
        out_ds.append(get_kaiyun_shuijing(_url_2))
        out_ds.append(get_xingge(_url_3))
        out_ds.append(get_xingge(_url_4))
        out_ds.append(get_aiqing_nan(_url_5))
        out_ds.append(get_aiqing_nv(_url_6))
        redis_client.set(_key, json.dumps(out_ds, ensure_ascii=False))
        print(json.dumps(out_ds, ensure_ascii=False))
def get_shenhua (url):
    url = f"https://www.smxs.com/{url}"
    urlData = requests.get(url).content
    soup = BeautifulSoup(urlData, 'html.parser')
    _div = soup.find_all('div', class_='box2 mt10 p10')[0]
    _title = _div.find('h1').text
    result = []
    contents = _div.find_all(['p', 'strong'])
    current_dict = {}
    for content in contents:
        if content.name == 'strong' and content.text != '':
            if current_dict:
                result.append(current_dict)
                current_dict = {}
            current_dict['title'] = content.text
        elif content.name == 'p' and content.text != '' and str(content).find('strong') == -1:
            if 'content' not in current_dict:
                current_dict['content'] = str(content)
            if 'title' not in current_dict:
                current_dict = {}
            if 'content' in current_dict and current_dict['content'].find(str(content)) == -1:
                current_dict['content'] += str(content)

    # 最后一个字典可能还没有添加进结果列表
    if current_dict:
        result.append(current_dict)
    out_d = {'title': _title, 'contents': result}
    return out_d
def get_kaiyun_shuijing(url):
    url = f"https://www.smxs.com/{url}"
    urlData = requests.get(url).content
    soup = BeautifulSoup(urlData, 'html.parser')
    _div = soup.find_all('div', class_='box2 mt10 p10')[0]
    _title = _div.find('h1').text
    result = []
    contents = _div.find_all(['p', 'strong'])
    current_dict = {}
    for content in contents:
        if content.name == 'strong' and content.text != '':
            if current_dict:
                result.append(current_dict)
                current_dict = {}
            current_dict['title'] = content.text
        elif content.name == 'p' and content.text != '' and str(content).find('strong') == -1:
            if 'content' not in current_dict:
                current_dict['content'] = str(content)
            if 'title' not in current_dict:
                current_dict = {}
            if 'content' in current_dict and current_dict['content'].find(str(content)) == -1:
                current_dict['content'] += str(content)

    # 最后一个字典可能还没有添加进结果列表
    if current_dict:
        result.append(current_dict)
    out_d = {'title': _title, 'contents': result}
    return out_d
def get_xingge(url):
    url = f"https://www.smxs.com/{url}"
    urlData = requests.get(url).content
    soup = BeautifulSoup(urlData, 'html.parser')
    _div = soup.find_all('div', class_='box2 mt10 p10')[0]
    _title = _div.find('h1').text
    result = []
    contents = _div.find_all(['p', 'strong'])
    current_dict = {}
    current_dict_2 = {}
    for content in contents:
        if content.name == 'strong' and content.text != '':
            if current_dict and 'content' in current_dict:
                result.append(current_dict)
                current_dict = {}
            current_dict['title'] = content.text
        elif content.name == 'p' and content.text != '' and str(content).find('strong') == -1:
            if 'content' not in current_dict:
                current_dict['content'] = str(content)
            if 'title' not in current_dict:
                current_dict = {}
            if 'content' in current_dict and current_dict['content'].find(str(content)) == -1:
                current_dict['content'] += str(content)
        elif content.name == 'p' and content.text != '' and str(content).find('strong') != -1 and str(content).find('span') == -1:
                if 'content' not in current_dict_2:
                    current_dict_2['content'] = str(content)
                if 'content' in current_dict_2 and current_dict_2['content'].find(str(content)) == -1:
                    current_dict_2['content'] += str(content)
                if 'title' not in current_dict_2:
                    current_dict_2['title'] = '与十二星座的关系'

    # 最后一个字典可能还没有添加进结果列表
    if current_dict and 'content' in current_dict:
        result.append(current_dict)
    if current_dict_2:
        result.append(current_dict_2)
    out_d = {'title': _title, 'contents': result}
    return out_d
def get_aiqing_nan(url):
    url = f"https://www.smxs.com/{url}"
    urlData = requests.get(url).content
    soup = BeautifulSoup(urlData, 'html.parser')
    _div = soup.find_all('div', class_='box2 mt10 p10')[0]
    _title = _div.find('h1').text
    result = []
    contents = _div.find_all(['p', 'strong'])
    current_dict = {}
    for content in contents:
        if content.name == 'strong' and content.text != '':
            if current_dict and 'content' in current_dict:
                result.append(current_dict)
                current_dict = {}
            current_dict['title'] = content.text
        elif content.name == 'p' and content.text != '' and str(content).find('strong') == -1:
            if 'content' not in current_dict:
                current_dict['content'] = str(content)
            if 'title' not in current_dict:
                current_dict = {}
            if 'content' in current_dict and current_dict['content'].find(str(content)) == -1:
                current_dict['content'] += str(content)

    # 最后一个字典可能还没有添加进结果列表
    if current_dict and 'content' in current_dict and 'title' in current_dict:
        result.append(current_dict)
    for _v in ai_qing_guan_map:
        if len(result) == _v and result[len(result) - 1]['title'].find(ai_qing_guan_map[_v]) == -1:
            result[len(result) - 1]['title'] = ai_qing_guan_map[_v] + result[len(result) - 1]['title']
    out_d = {'title': _title, 'contents': result}
    return out_d
def get_aiqing_nv(url):
    url = f"https://www.smxs.com/{url}"
    urlData = requests.get(url).content
    soup = BeautifulSoup(urlData, 'html.parser')
    _div = soup.find_all('div', class_='box2 mt10 p10')[0]
    _title = _div.find('h1').text
    _p_content = _div.find('p')
    out_d = {'title': _title, 'content': str(_p_content), 'contents': []}
    contents = _div.find_all(['strong', 'p'])
    result = []
    current_dict = {}
    current_dict_2 = {}
    for content in contents:
        if content.name == 'strong' and content.text != '':
            if current_dict and 'content' in current_dict:
                result.append(current_dict)
                current_dict = {}
            current_dict['title'] = content.text
        elif content.name == 'p' and content.text != '' and str(content).find('strong') == -1:
            if 'content' not in current_dict:
                current_dict['content'] = str(content)
            if 'title' not in current_dict:
                current_dict = {}
            if 'content' in current_dict and current_dict['content'].find(str(content)) == -1:
                current_dict['content'] += str(content)
        elif content.name == 'p' and content.text != '' and str(content).find('strong') != -1 and str(content).find('span') == -1:
                if 'content' not in current_dict_2:
                    current_dict_2['content'] = str(content)
                if 'content' in current_dict_2 and current_dict_2['content'].find(str(content)) == -1:
                    current_dict_2['content'] += str(content)
                if 'title' not in current_dict_2:
                    current_dict_2['title'] = '与十二星座的关系'
    # 最后一个字典可能还没有添加进结果列表
    if current_dict and 'content' in current_dict and 'title' in current_dict:
        result.append(current_dict)
    if current_dict_2:
        result[len(result) - 2]['content'] += current_dict_2['content']
        result[len(result) - 2]['content'] += result[len(result) - 1]['content']
        del result[len(result) - 1]

    out_d['contents'] = result
    return out_d

def get_smxs_xingzuo_query_redis():
    for key in xingzuo_data_map.keys():
        _key = 'XING_ZUO_CHA_XUN_' + key
        _redis_data = redis_client.get(_key)
        if _redis_data:
            _utf_8_data = json.loads(_redis_data.decode('UTF-8'))
            print(_utf_8_data)
def remove_duplicate(content):
    pattern = r"<p>(.*?)</p>"
    unique_content = set(re.findall(pattern, content))
    return "<p>" + "</p><p>".join(unique_content) + "</p>"

get_smxs_xingzuo_query()