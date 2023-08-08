from datetime import datetime
import re
from dateutil.parser import parse
import json
from utils.redis_utils import redis_client
import requests
from bs4 import BeautifulSoup
def fibonacci_shengrimima(p_labels, index, content):
    if index == len(p_labels):
        return {'p': '', 'index': index}
    p = p_labels[index]
    index = index + 1
    if str(p).find('<p class="kg"></p>') != -1:
        return fibonacci_shengrimima(p_labels, index, content)
    if len(content['content']) > 0 and content['content'].find(str(p)) != -1:
        return fibonacci_shengrimima(p_labels, index, content)
    else:
        return {'p': p, 'index': index}
# https://www.name321.com/shengxiao/
def get_smxs_shengxiao_query () :
    for i in range(1942, 2026):
        _key = 'SHENG_XIAO_CHA_XUN_' + str(i)
        url = "https://www.name321.com/shengxiao/"
        urlData = requests.post(url, data={'y': {i}, 'gemei': 'yes', 'submit': '开始查询'}).content
        soup = BeautifulSoup(urlData, 'html.parser')
        _div_content = soup.find_all('div', class_='content')[0]
        _h2_title_text = _div_content.find('h2').text
        _div_read_content = soup.find_all('div', class_='read-content')[0]
        _p0 = _div_content.find_all('p')[0]
        _p1 = _div_content.find_all('p')[1]
        _p2 = _div_content.find_all('p')[2]
        _p3 = _div_content.find_all('p')[3]
        _p4 = _div_content.find_all('p')[4]
        _p5 = _div_content.find_all('p')[5]

        _content = str(_p0).replace('<h6>', '').replace('</h6>', '').replace('class="kg"', '') + str(_p1).replace('<h6>', '').replace('</h6>', '').replace('class="kg"', '') + str(_p2).replace('<h6>', '').replace('</h6>', '').replace('class="kg"', '') + str(_p3).replace('<h6>', '').replace('</h6>', '').replace('class="kg"', '') + str(_p4).replace('<h6>', '').replace('</h6>', '').replace('class="kg"', '') + str(_p5).replace('<h6>', '').replace('</h6>', '').replace('class="kg"', '')
        out_d = {'title': _h2_title_text, 'content':  _content, 'contents': []}
        _arrays = []
        out_s = {}
        for element in _div_read_content:
            if element.name:
                if element.name == 'h4':
                    out_s = {'title': element.text, 'content': ''}
                if element.name == 'h3':
                    out_s = {'title': element.text, 'content': ''}
                if element.name == 'p' and str(element) != '<p class="kg"></p>':
                    out_s['content'] = str(element)
                    out_r = {'title':  out_s['title'], 'content': ''}
                    out_r['content'] = str(element)
                    _arrays.append(out_r)
        grouped_data = {}
        for item in _arrays:
            title = item['title']
            content = item['content']
            if title in grouped_data:
                # 如果title已存在字典中，将content追加到对应的值后面
                grouped_data[title] += content.replace('class="kg"', '')
            else:
                # 如果title不存在字典中，将title作为键，content作为值加入字典
                grouped_data[title] = content.replace('class="kg"', '')
        out_d['contents'] = [{'title': title, 'content': content} for title, content in grouped_data.items()]
        redis_client.set(_key, json.dumps(out_d, ensure_ascii=False))
        print(json.dumps(out_d, ensure_ascii=False))
def get_smxs_shengxiao_query_redis ():
    for i in range(1942, 2026):
        _key = 'SHENG_XIAO_CHA_XUN_' + str(i)
        _redis_data = redis_client.get(_key)
        print(_redis_data.decode('UTF-8'))
# https://www.name321.com/shengxiao/yunshi/
def get_smxs_shengxiao_yunshi_query () :
    for i in range(1, 13):
        for j in range(2023, 2025):
            _key = 'SHENG_XIAO_CHA_XUN_' + str(i) + '-' + str(j)
            url = "https://www.name321.com/shengxiao/yunshi/"
            urlData = requests.post(url, data={'sx': {i}, 'y': {j}, 'gemei': 'yes', 'submit': '开始查询'}).content
            soup = BeautifulSoup(urlData, 'html.parser')
            _div_content = soup.find_all('div', class_='content')[0]
            # 找到所有的子标签，包括直接子标签和后代子标签
            contents = _div_content.find_all(['p', 'h3'])
            # 构造结果列表
            result = []
            current_dict = {}
            for content in contents:
                if content.name == 'h3':
                    if current_dict:
                        result.append(current_dict)
                        current_dict = {}
                    current_dict['title'] = content.text
                elif content.name == 'p':
                    if 'content' not in current_dict:
                        current_dict['content'] = str(content).replace('class="kg"', '')
                    else:
                        current_dict['content'] += str(content).replace('class="kg"', '')

            # 最后一个字典可能还没有添加进结果列表
            if current_dict:
                result.append(current_dict)
            _obj = result[0]
            _parent_obj = BeautifulSoup(_obj['content'], 'html.parser')
            _p_labels = _parent_obj.find_all('p')
            _title = _p_labels[0].text
            _content_1 = _p_labels[1].text
            _content_2 = _p_labels[2].text
            del result[0]
            out_d = {'title': _title, 'content': _content_1 + _content_2, 'contents': result}
            redis_client.set(_key, json.dumps(out_d, ensure_ascii=False))
            print(_key, json.dumps(out_d, ensure_ascii=False))

def get_smxs_shengxiao_yunshi_query_redis ():
    for i in range(1, 13):
        for j in range(2023, 2025):
            _key = 'SHENG_XIAO_CHA_XUN_' + str(i) + '-' + str(j)
            _redis_data = redis_client.get(_key)
            print(_redis_data.decode('UTF-8'))

get_smxs_shengxiao_query()
