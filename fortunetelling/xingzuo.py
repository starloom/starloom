import os
import json
import requests
from pathlib import Path
import pandas as pd
import io
from bs4 import BeautifulSoup
import random
from lunardate import LunarDate
import requests
import aiohttp
import asyncio
from fortunetelling.config import _MODEL_TYPE, _GPT_TYPE
import fortunetelling
from fortunetelling.config import xingzuo_name_map, xingzuo_name_image_map
from fortunetelling.yunshiConfig import xingzuo_en_map, xingzuo_zh_map, date_ranges,xingzuo_data_map, xia_jiang_date_map, xia_jiang_minute_map
from utils.xingzuo_utils import extract_birthday, convert_to_output_format, output_format, output_format_1
from utils.redis_utils import redis_client
from fortunetelling.shengxiaoConfig import shengxiao_num_map,shengxiao_py_map,shengxiao_url_map
from sql.execute_sql import _select_xingzuo_question_by_type,_select_xingzuo_question_by_id,_select_xingzuo_ranking_by_question_id,_select_xingzuo_question_by_title,_select_xingzuo_question_by_type_count
from datetime import datetime, date
from utils.response_data import _return_data
from fortunetelling.xingpanConfig import xing_zuo, xing_xing_map, shi_er_gong, xing_xing_py_map
async def _get_xingzuo_yunshi(xingzuo_py):
    if xingzuo_py not in xingzuo_name_map:
        return {}
    url = f"https://www.zuixingzuo.net/yunshi/{xingzuo_py}/"
    async with aiohttp.ClientSession() as session:
        # async with session.get(url, proxy='http://127.0.0.1:7890') as resp:
        async with session.get(url) as resp:
            urlData = await resp.content.read()
    # urlData = requests.get(url).content
    soup = BeautifulSoup(urlData, 'html.parser')
    out1 = soup.find_all('div', class_='yunshi_summary')
    l1 = []
    for _1 in soup.find_all('div', class_='yunshi_summary'):
        for _2 in _1.find_all('ul'):
            for _3 in _2.find_all('li'):
                _d = {}
                _s = _3.text
                _d['k'] = _s.split('：')[0]
                _4 = _3.find('em')
                if _4:
                    _d['v'] = _4.get('class')[1]
                else:
                    _d['v'] = _s.split('：')[1]
                l1.append(_d)     
    l2 = []
    for _1 in soup.find_all('div', class_='yunshi_content'):
        for _2 in _1.find_all('p'):
            _s = _2.text
            _k = _2.find('span').text
            _d = {'k': _k, 'v': _s.strip(f"{_k}|\n|\r| ")}
            l2.append(_d)     
    out_d = {}
    _d = {}
    for kv in l1:
        _d[kv['k']] = kv['v']
    out_d["运势摘要"] = _d
    _d = {}
    for kv in l2:
        _d[kv['k']] = kv['v']
    out_d["运势内容"] = _d
    return out_d
async def _get_xingzuo_yunshi_2(xingzuo_py, _index):
    if _index == '':
        _index = 0
    else:
        _index = int(_index)
    _jk_name = ''
    _image_name = ''
    xingzuo_py = xingzuo_py.lower()
    if xingzuo_py in xingzuo_en_map.keys():
        _jk_name = xingzuo_py
    if _jk_name == '':
        for _zh_name in xingzuo_zh_map.keys():
            if xingzuo_py.find(_zh_name) != -1:
                _jk_name = xingzuo_zh_map[_zh_name]
                break
    if _jk_name == '':
        for _py_name in xingzuo_name_map.keys():
            if xingzuo_py.find(_py_name) != -1:
                _jk_name = xingzuo_zh_map[xingzuo_name_map[_py_name]]
                break
        if _jk_name == '':
            return _return_data(_GPT_TYPE, 'a-5', '查询gpt')
    for _en_name in xingzuo_en_map.keys():
        if _jk_name == _en_name:
            for _key in xingzuo_name_map.keys():
                if xingzuo_name_map[_key] == xingzuo_en_map[_en_name]:
                    _image_name = _key
                    break
        break

    url = f"https://www.xzw.com/fortune/{_jk_name}/"
    url_1 = f"https://www.xzw.com/fortune/{_jk_name}/1.html"
    url_2 = f"https://www.xzw.com/fortune/{_jk_name}/2.html"
    url_3 = f"https://www.xzw.com/fortune/{_jk_name}/3.html"
    url_4 = f"https://www.xzw.com/fortune/{_jk_name}/4.html"
    _yunshi_res = ''
    if _index == 0:
        _yunshi_res = _get_xingzuo_yunshi_util(url, _image_name)
    if _index == 1:
        _yunshi_res = _get_xingzuo_yunshi_util(url_1, _image_name)
    if _index == 2:
        _yunshi_res = _get_xingzuo_yunshi_util(url_2, _image_name)
    if _index == 3:
        _yunshi_res = _get_xingzuo_yunshi_util(url_3, _image_name)
    if _index == 4:
        _yunshi_res = _get_xingzuo_yunshi_util(url_4, _image_name)
    if _yunshi_res == '':
        return _return_data(_GPT_TYPE, 'a-5', '查询gpt')
    _yunshi_res['question'] = xingzuo_py
    return _return_data(_MODEL_TYPE, 'a-5', _yunshi_res)
async def _get_xingzuo_yunshi_params(xingzuo_py, _index, _input):
    xingzuo_en = ''
    if _index == '':
        _index = 0
    else:
        _index = int(_index)
    for _key, _value in xingzuo_zh_map.items():
        if xingzuo_py in xingzuo_data_map.keys():
            if xingzuo_data_map[xingzuo_py] == _key:
                xingzuo_en = _value
        break
    if xingzuo_en == '':
        return _return_data(_GPT_TYPE, 'a-5', '查询gpt')
    url = f"https://www.xzw.com/fortune/{xingzuo_en}/"
    url_1 = f"https://www.xzw.com/fortune/{xingzuo_en}/1.html"
    url_2 = f"https://www.xzw.com/fortune/{xingzuo_en}/2.html"
    url_3 = f"https://www.xzw.com/fortune/{xingzuo_en}/3.html"
    url_4 = f"https://www.xzw.com/fortune/{xingzuo_en}/4.html"
    _yunshi_res = ''
    if _index == 0:
        _yunshi_res = _get_xingzuo_yunshi_util(url, xingzuo_py)
    if _index == 1:
        _yunshi_res = _get_xingzuo_yunshi_util(url_1, xingzuo_py)
    if _index == 2:
        _yunshi_res = _get_xingzuo_yunshi_util(url_2, xingzuo_py)
    if _index == 3:
        _yunshi_res = _get_xingzuo_yunshi_util(url_3, xingzuo_py)
    if _index == 4:
        _yunshi_res = _get_xingzuo_yunshi_util(url_4, xingzuo_py)
    if _yunshi_res == '':
        return _return_data(_GPT_TYPE, 'a-5', '查询gpt')
    _yunshi_res['question'] = _input
    return _return_data(_MODEL_TYPE, 'a-5', _yunshi_res)

def _get_xingzuo_yunshi_util(url, _xingzuo) :
    urlData = requests.get(url).content
    soup = BeautifulSoup(urlData, 'html.parser')
    _dl_1 = soup.find_all('dl')[1]
    _title = _dl_1.find_all('h4')[0]
    _date = _title.find_all('small')[0]
    _title_str = _title.text.replace(_date.text, '').strip()
    _lis = _dl_1.find_all('li')
    out_d = {}
    # print(_title_str, '(', _date.text, ')')
    out_d['title'] = _title_str + '(' + _date.text + ')'
    out_d['imageUrl'] = xingzuo_name_image_map[_xingzuo]
    out_d['yunshi'] = []
    for _li in _lis:
        if _li.find('em'):
            _son_title = _li.find('label').text.replace('：', '').strip()
            _lv = _li.find('em').attrs['style']
            _scope = int(_lv.replace('width:', '').replace('px', '').replace(';', ''))
            out_d['yunshi'].append({'title': _son_title, 'content': _scope / 16})
            # print(_son_title, )
        else:
            # print(_li.text)
            out_d['yunshi'].append({'title': _li.text.split('：')[0].strip(), 'content': _li.text.split('：')[1].strip()})
    _div_cont = soup.find_all('div', class_='c_cont')[0]
    out_d['describe'] = []
    _p_label = _div_cont.find_all('p')
    index = 0
    _span_index = 0
    for _p in _p_label:
        index = index + 1
        _label_index = 'p' + str(index)
        if _p.find('strong', class_=_label_index):
            _strong_text = _p.find('strong', class_=_label_index).text.strip()
            _span_text = _p.find_all('span')[_span_index].text.replace('星(座(屋', '').replace('星C座C屋', '').strip()
            _span_index + 1
            # print(_strong_text, '：' + _span_text)
            out_d['describe'].append({'title': _strong_text, 'content': _span_text})
        else:
            index = index + 1
            _label_index = 'p' + str(index)
            if _p.find('strong', class_=_label_index):
                _strong_text = _p.find('strong', class_=_label_index).text.strip()
                _span_text = _p.find_all('span')[_span_index].text.replace('星(座(屋', '').replace('星C座C屋', '').strip()
                _span_index + 1
                # print(_strong_text, '：' + _span_text)
                out_d['describe'].append({'title': _strong_text, 'content': _span_text})
    return out_d
async def _get_xingzuo_shengrihua(xingzuo_py):
    _date = extract_birthday(xingzuo_py)
    if not _date:
        return _return_data(_GPT_TYPE, 'a-8', '查询gpt')
    _format_time = convert_to_output_format(_date, output_format_1).split('-')
    _date = convert_to_output_format(_date, output_format)
    if not _date:
        return _return_data(_GPT_TYPE, 'a-8', '查询gpt')
    _date_1 = _date.split('-')[0]
    _date_2 = _date.split('-')[1]
    _key = 'SHENG_RI_HUA_' + str(int(_date_1)) + '-' + str(int(_date_2))
    _redis_data = redis_client.get(_key)
    if _redis_data:
        return _return_data(_MODEL_TYPE, 'a-8', [_get_user_base_info(_format_time[0], _format_time[1], _format_time[2], None, None), json.loads(_redis_data.decode('UTF-8'))])
    return _return_data(_GPT_TYPE, 'a-8', '查询gpt')
async def _get_xingzuo_shengrihua_params(year, month, day):
    _key = 'SHENG_RI_HUA_' + str(int(month)) + '-' + str(int(day))
    _redis_data = redis_client.get(_key)
    if _redis_data:
        return _return_data(_MODEL_TYPE, 'a-8', [_get_user_base_info(year, month, day, None, None), json.loads(_redis_data.decode('UTF-8'))])
    return _return_data(_GPT_TYPE, 'a-8', '查询gpt')
async def _get_xingzuo_shengrishu(xingzuo_py):
    _date = extract_birthday(xingzuo_py)
    if not _date:
        return _return_data(_GPT_TYPE, 'a-12', '查询gpt')
    _format_time = convert_to_output_format(_date, output_format_1).split('-')
    _date = convert_to_output_format(_date, output_format)
    if not _date:
        return _return_data(_GPT_TYPE, 'a-12', '查询gpt')
    _date_1 = _date.split('-')[0]
    _date_2 = _date.split('-')[1]
    _key = 'SHENG_RI_SHU_' + str(int(_date_1)) + '-' + str(int(_date_2))
    _redis_data = redis_client.get(_key)
    if _redis_data:
        return _return_data(_MODEL_TYPE, 'a-12', [_get_user_base_info(_format_time[0], _format_time[1], _format_time[2], None, None), json.loads(_redis_data.decode('UTF-8'))])
    return _return_data(_GPT_TYPE, 'a-12', '查询gpt')
async def _get_xingzuo_shengrishu_params(year, month, day):
    _key = 'SHENG_RI_SHU_' + str(int(month)) + '-' + str(int(day))
    _redis_data = redis_client.get(_key)
    if _redis_data:
        return _return_data(_MODEL_TYPE, 'a-12', [_get_user_base_info(year, month, day, None, None), json.loads(_redis_data.decode('UTF-8'))])
    return _return_data(_GPT_TYPE, 'a-12', '查询gpt')
async def _get_xingzuo_shengrimima(xingzuo_py):
    _date = extract_birthday(xingzuo_py)
    if not _date:
        return _return_data(_GPT_TYPE, 'a-11', '查询gpt')
    _format_time = convert_to_output_format(_date, output_format_1).split('-')
    _date = convert_to_output_format(_date, output_format)
    if not _date:
        return _return_data(_GPT_TYPE, 'a-11', '查询gpt')
    _date_1 = _date.split('-')[0]
    _date_2 = _date.split('-')[1]
    _key = 'SHENG_RI_MI_MA_' + str(int(_date_1)) + '-' + str(int(_date_2))
    _redis_data = redis_client.get(_key)
    if _redis_data:
        return _return_data(_MODEL_TYPE, 'a-11', [_get_user_base_info(_format_time[0], _format_time[1], _format_time[2], None, None), json.loads(_redis_data.decode('UTF-8'))])
    return _return_data(_GPT_TYPE, 'a-11', '查询gpt')
async def _get_xingzuo_shengrimima_params(year, month, day):
    _key = 'SHENG_RI_MI_MA_' + str(int(month)) + '-' + str(int(day))
    _redis_data = redis_client.get(_key)
    if _redis_data:
        return _return_data(_MODEL_TYPE, 'a-11', [_get_user_base_info(year, month, day, None, None), json.loads(_redis_data.decode('UTF-8'))])
    return _return_data(_GPT_TYPE, 'a-11', '查询gpt')
async def _get_xingzuo_ranking (_type, _page, _page_size):
    _questions = _select_xingzuo_question_by_type(_type, _page, _page_size)
    _total_count = _select_xingzuo_question_by_type_count(_type)
    if _questions:
        _objects = []
        for objs in _questions:
            _objects.append({'id': objs[0], 'title': objs[1], 'content': objs[2], 'imgUrl': objs[3]})
        result = {'totalCount': _total_count[0][0], 'list': _objects}
        return _return_data(_MODEL_TYPE, 'a-7', result)
    return _return_data(_GPT_TYPE, 'a-7', '查询gpt')
async def _get_xingzuo_ranking_get (_id):
    _questions = _select_xingzuo_question_by_id(_id)
    if _questions:
        _objects = []
        _rankings = _select_xingzuo_ranking_by_question_id(_id)
        for _item in _rankings:
            _objects.append({'name': _item[0], 'imgUrl': _item[1], 'votesNum': _item[2]})
        return _return_data(_MODEL_TYPE, 'a-7', _objects)
    return _return_data(_MODEL_TYPE, 'a-7', 'error params')
async def _get_xingzuo_ranking_question (_question):
    _questions = _select_xingzuo_question_by_title(_question)
    if _questions:
        _objects = []
        if len(_questions) == 1:
            _rankings = _select_xingzuo_ranking_by_question_id(_questions[0][0])
            for _item in _rankings:
                _objects.append({'name': _item[0], 'imgUrl': _item[1], 'votesNum': _item[2]})
            return _return_data(_MODEL_TYPE, 'a-7', _objects)
        if len(_questions) > 3:
            _questions = random.sample(_questions, 3)
        for objs in _questions:
            _objects.append({'id': objs[0], 'title': objs[1], 'content': objs[2], 'imgUrl': objs[3]})
        result = {'totalCount': len(_objects), 'list': _objects}
        return _return_data(_MODEL_TYPE, 'a-7', result)
    return _return_data(_GPT_TYPE, 'a-7', '查询gpt')

async def _get_xingzuo_xuexing (_query):
    # 解析 日期
    _date = extract_birthday(_query)
    if not _date:
        return _return_data(_GPT_TYPE, 'a-16', '查询gpt')
    _format_time = convert_to_output_format(_date, output_format_1).split('-')
    _date = convert_to_output_format(_date, output_format)
    if not _date:
        return _return_data(_GPT_TYPE, 'a-16', '查询gpt')
    _date_1 = _date.split('-')[0]
    _date_2 = _date.split('-')[1]
    _xingzuo = is_within_date_ranges(int(_date_1), int(_date_2))
    if _xingzuo == '':
        return _return_data(_GPT_TYPE, 'a-16', '查询gpt')
    # 解析 血型
    _xuexing = ['AB', 'B', 'O', 'A']
    _xue_xing = ''
    for _xue in _xuexing:
        if _query.find(_xue) != -1:
            _xue_xing = _xue
            break
    _key = 'XING_ZUO_XUE_XING_' + _xingzuo.upper() + '_' + _xue_xing
    _redis_data = redis_client.get(_key)
    if _redis_data:
        return _return_data(_MODEL_TYPE, 'a-16', [_get_user_base_info(_format_time[0], _format_time[1], _format_time[2], None, _xue_xing), json.loads(_redis_data.decode('UTF-8'))])
    return _return_data(_GPT_TYPE, 'a-16', '查询gpt')
# xuexing A B O AB
async def _get_xingzuo_xuexing_params (xuexing, year, month, day):
    xingzuo_py = is_within_date_ranges(int(month), int(day))
    _key = 'XING_ZUO_XUE_XING_' + xingzuo_py.upper() + '_' + xuexing
    _redis_data = redis_client.get(_key)
    if _redis_data:
        return _return_data(_MODEL_TYPE, 'a-16', [_get_user_base_info(year, month, day, None, xuexing), json.loads(_redis_data.decode('UTF-8'))])
    return _return_data(_GPT_TYPE, 'a-16', '查询gpt')

async def _get_xingzuo_chugui (_query):
    # 解析 日期
    _date = extract_birthday(_query)
    if not _date:
        return _return_data(_GPT_TYPE, 'a-13', '查询gpt')
    _format_time = convert_to_output_format(_date, output_format_1).split('-')
    _date = convert_to_output_format(_date, output_format)
    if not _date:
        return _return_data(_GPT_TYPE, 'a-13', '查询gpt')
    _date_1 = _date.split('-')[0]
    _date_2 = _date.split('-')[1]
    _xingzuo = is_within_date_ranges(int(_date_1), int(_date_2))
    if _xingzuo == '':
        return _return_data(_GPT_TYPE, 'a-13', '查询gpt')
    # 解析 性别
    _xing_bie_1 = [('男', 1), ('女', 2)]
    _xing_bie_2 = [('nan', 1), ('nv', 2)]
    _xing_bie_3 = {1: '男', 2: '女'}
    _xing_bie = ''
    _xing_bie = is_within_sex_ranges(_query, _xing_bie_1)
    if _xing_bie == '':
        _xing_bie = is_within_sex_ranges(_query, _xing_bie_2)
    if _xing_bie == '':
        return _return_data(_GPT_TYPE, 'a-13', '查询gpt')

    _key = 'XING_ZUO_CHU_GUI_' + _xingzuo.upper() + '_' + str(_xing_bie)
    _redis_data = redis_client.get(_key)
    if _redis_data:
        return _return_data(_MODEL_TYPE, 'a-13', [_get_user_base_info(_format_time[0], _format_time[1], _format_time[2], _xing_bie_3[_xing_bie], None), json.loads(_redis_data.decode('UTF-8'))])
    return _return_data(_GPT_TYPE, 'a-13', '查询gpt')
# xing_bie 男 1 女 2
async def _get_xingzuo_chugui_params (xingzuo_py, xing_bie, year, month, day):
    _key = 'XING_ZUO_CHU_GUI_' + xingzuo_py.upper() + '_' + str(xing_bie)
    _redis_data = redis_client.get(_key)
    _xing_bie_3 = {1: '男', 2: '女'}
    if _redis_data:
        return _return_data(_MODEL_TYPE, 'a-13', [_get_user_base_info(year, month, day, _xing_bie_3[xing_bie], None), json.loads(_redis_data.decode('UTF-8'))])
    return _return_data(_GPT_TYPE, 'a-13', '查询gpt')
async def _get_xingzuo_48 (_query):
    # 解析 日期
    _date = extract_birthday(_query)
    if not _date:
        return _return_data(_GPT_TYPE, 'a-10', '查询gpt')
    _format_time = convert_to_output_format(_date, output_format_1).split('-')
    # 解析 性别
    _key = 'XING_ZUO_48_' + _format_time[0] + '_' + str(int(_format_time[1])) + '_' + str(int(_format_time[2]))
    _redis_data = redis_client.get(_key)
    if _redis_data:
        _json_list = json.loads(_redis_data.decode('UTF-8'))
        move_last_to_first(_json_list)
        return _return_data(_MODEL_TYPE, 'a-10', [_get_user_base_info(_format_time[0], _format_time[1], _format_time[2], None, None), _json_list])
    return _return_data(_GPT_TYPE, 'a-10', '查询gpt')
async def _get_xingzuo_48_params (year, month, day):
    # 解析 性别
    _key = 'XING_ZUO_48_' + str(year) + '_' + str(int(month)) + '_' + str(int(day))
    _redis_data = redis_client.get(_key)
    if _redis_data:
        return _return_data(_MODEL_TYPE, 'a-10', [_get_user_base_info(year, month, day, None, None), json.loads(_redis_data.decode('UTF-8'))])
    return _return_data(_GPT_TYPE, 'a-10', '查询gpt')
def move_last_to_first(arr):
    if len(arr) > 0:
        last_element = arr.pop()
        arr.insert(0, last_element)

async def _get_xingzuo_xiajiang (_query):
    # 解析 日期
    _date = extract_birthday(_query)
    if not _date:
        return _return_data(_GPT_TYPE, 'a-4', '查询gpt')
    _format_time = convert_to_output_format(_date, output_format_1).split('-')
    _shi_chen = ''
    # 解析 时辰
    for _key, _value in xia_jiang_date_map.items():
        if _query.find(_key) != -1:
            _shi_chen = _value
            break
    if _shi_chen == '':
        return _return_data(_GPT_TYPE, 'a-4', '查询gpt')
    # 解析 性别
    _xing_bie_1 = [('男', 1), ('女', 2)]
    _xing_bie_2 = [('nan', 1), ('nv', 2)]
    _xing_bie_3 = {1: '男', 2: '女'}
    _xing_bie = ''
    _xing_bie = is_within_sex_ranges(_query, _xing_bie_1)
    if _xing_bie == '':
        _xing_bie = is_within_sex_ranges(_query, _xing_bie_2)
    if _xing_bie == '':
        return _return_data(_GPT_TYPE, 'a-4', '查询gpt')
    _key = 'XING_ZUO_XIA_JIANG_' + str(int(_format_time[1])) + '_' + str(int(_format_time[2])) + '_' + _shi_chen + '_' + str(_xing_bie)
    _redis_data = redis_client.get(_key)
    if _redis_data:
        return _return_data(_MODEL_TYPE, 'a-4', [_get_user_base_info(_format_time[0], _format_time[1], _format_time[2], _xing_bie_3[_xing_bie], None), json.loads(_redis_data.decode('UTF-8'))])
    return _return_data(_GPT_TYPE, 'a-4', '查询gpt')
async def _get_xingzuo_xiajiang_params (_shichen, _xing_bie, year, month, day):
    _xing_bie_3 = {1: '男', 2: '女'}
    _key = 'XING_ZUO_XIA_JIANG_' + str(int(month)) + '_' + str(int(day)) + '_' + str(_shichen) + '_' + str(_xing_bie)
    _redis_data = redis_client.get(_key)
    if _redis_data:
        return _return_data(_MODEL_TYPE, 'a-4', [_get_user_base_info(year, month, day, _xing_bie_3[_xing_bie], None), json.loads(_redis_data.decode('UTF-8'))])
    return _return_data(_GPT_TYPE, 'a-4', '查询gpt')

async def _get_xingzuo_yueliang (_query):
    # 解析 日期
    _date = extract_birthday(_query)
    if not _date:
        return _return_data(_GPT_TYPE, 'a-9', '查询gpt')
    _format_time = convert_to_output_format(_date, output_format_1).split('-')
    _shi_chen = ''
    # 解析 时辰
    for _key, _value in xia_jiang_date_map.items():
        if _query.find(_key) != -1:
            _shi_chen = _value
            break
    if _shi_chen == '':
        return _return_data(_GPT_TYPE, 'a-9', '查询gpt')
    # 解析 性别
    _xing_bie_1 = [('男', 1), ('女', 2)]
    _xing_bie_2 = [('nan', 1), ('nv', 2)]
    _xing_bie_3 = {1: '男', 2: '女'}
    _xing_bie = ''
    _xing_bie = is_within_sex_ranges(_query, _xing_bie_1)
    if _xing_bie == '':
        _xing_bie = is_within_sex_ranges(_query, _xing_bie_2)
    if _xing_bie == '':
        return _return_data(_GPT_TYPE, 'a-9', '查询gpt')
    sign = is_within_date_ranges(int(_format_time[1]), int(_format_time[2]))
    _key = 'XING_ZUO_YUE_LIANG_' + str(sign).upper() + '_' + str(_xing_bie)
    _redis_data = redis_client.get(_key)
    if _redis_data:
        return _return_data(_MODEL_TYPE, 'a-9', [_get_user_base_info(_format_time[0], _format_time[1], _format_time[2], _xing_bie_3[_xing_bie], None), json.loads(_redis_data.decode('UTF-8'))])
    return _return_data(_GPT_TYPE, 'a-9', '查询gpt')

async def _get_xingzuo_yueliang_params (_shichen, _xing_bie, year, month, day):
    _xing_bie_3 = {1: '男', 2: '女'}
    sign = is_within_date_ranges(int(month), int(day))
    _key = 'XING_ZUO_YUE_LIANG_' + str(sign).upper() + '_' + str(_xing_bie)
    _redis_data = redis_client.get(_key)
    if _redis_data:
        return _return_data(_MODEL_TYPE, 'a-9', [_get_user_base_info(year, month, day, _xing_bie_3[_xing_bie], None), json.loads(_redis_data.decode('UTF-8'))])
    return _return_data(_GPT_TYPE, 'a-9', '查询gpt')

async def _get_xingzuo_shangsheng (_query):
    # 解析 日期
    _date = extract_birthday(_query)
    if not _date:
        return _return_data(_GPT_TYPE, 'a-3', '查询gpt')
    _format_time = convert_to_output_format(_date, output_format_1).split('-')
    _shi_chen = ''
    # 解析 时辰
    for _key, _value in xia_jiang_date_map.items():
        if _query.find(_key) != -1:
            _shi_chen = _value
            break
    if _shi_chen == '':
        return _return_data(_GPT_TYPE, 'a-3', '查询gpt')
    _minute = ''
    _new_query = str(_query).replace(_date, '')
    _query_split = str(_new_query).split(':')
    if len(_query_split) == 1:
        _query_split = str(_new_query).split('：')
    if len(_query_split) == 1:
        return _return_data(_GPT_TYPE, 'a-3', '查询gpt')
    for _key, _value in xia_jiang_minute_map.items():
        if _query_split[1].find(_key) != -1:
            _minute = _value
            break
    if _minute == '':
        return _return_data(_GPT_TYPE, 'a-3', '查询gpt')
    # 解析 性别
    _xing_bie_1 = [('男', 1), ('女', 2)]
    _xing_bie_2 = [('nan', 1), ('nv', 2)]
    _xing_bie_3 = {1: '男', 2: '女'}
    _xing_bie = ''
    _xing_bie = is_within_sex_ranges(_query, _xing_bie_1)
    if _xing_bie == '':
        _xing_bie = is_within_sex_ranges(_query, _xing_bie_2)
    if _xing_bie == '':
        return _return_data(_GPT_TYPE, 'a-3', '查询gpt')
    _key = 'XING_ZUO_SHANG_SHENG_' + str(int(_format_time[1])) + '_' + str(int(_format_time[2])) + '_' + _shi_chen + '_' + _minute
    _redis_data = redis_client.get(_key)
    if _redis_data:
        return _return_data(_MODEL_TYPE, 'a-3', [_get_user_base_info(_format_time[0], _format_time[1], _format_time[2], _xing_bie_3[_xing_bie], None), json.loads(_redis_data.decode('UTF-8'))])
    return _return_data(_GPT_TYPE, 'a-3', '查询gpt')

async def _get_xingzuo_shangsheng_params (_shichen, _xing_bie, year, month, day):
    _xing_bie_3 = {1: '男', 2: '女'}
    _key = 'XING_ZUO_SHANG_SHENG_' + str(int(month)) + '_' + str(int(day)) + '_' + str(int(str(_shichen).split(':')[0])) + '_' + str(int(str(_shichen).split(':')[1]))
    _redis_data = redis_client.get(_key)
    if _redis_data:
        return _return_data(_MODEL_TYPE, 'a-3', [_get_user_base_info(year, month, day, _xing_bie_3[_xing_bie], None), json.loads(_redis_data.decode('UTF-8'))])
    return _return_data(_GPT_TYPE, 'a-3', '查询gpt')
async def _get_shengxiao_query(query):
    _year = ''
    for i in range(1942, 2025) :
        if query.find(str(i)) != -1:
            _year = str(i)
            break
    if _year == '':
        return _return_data(_GPT_TYPE, 'a-1', '查询gpt')
    _key = 'SHENG_XIAO_CHA_XUN_' + str(_year)
    result = redis_client.get(_key)
    if result:
        _shengxiao_url = _get_shengxiao_url(_year)
        _res_json = json.loads(result.decode('UTF-8'))
        _res_json['imgUrl'] = _shengxiao_url
        return _return_data(_MODEL_TYPE, 'a-1', _res_json)
    return _return_data(_GPT_TYPE, 'a-1', '查询gpt')
async def _get_shengxiao_query_params(year):
    _key = 'SHENG_XIAO_CHA_XUN_' + str(year)
    result = redis_client.get(_key)
    if result:
        _shengxiao_url = _get_shengxiao_url(year)
        _res_json = json.loads(result.decode('UTF-8'))
        _res_json['imgUrl'] = _shengxiao_url
        return _return_data(_MODEL_TYPE, 'a-1', _res_json)
    return _return_data(_GPT_TYPE, 'a-1', '查询gpt')

async def _get_shengxiao_yunshi(query):
    _shengxiao = ''
    _years = ''
    for num in shengxiao_num_map.keys():
        if query.find(shengxiao_num_map[num]) != -1:
            _shengxiao = num
            break
    for num in shengxiao_py_map.keys():
        if query.find(shengxiao_py_map[num]) != -1:
            _shengxiao = num
            break
    if _shengxiao == '':
        return _return_data(_GPT_TYPE, 'a-2', '查询gpt')
    current_year = datetime.now().year
    next_year = current_year + 1
    if query.find(str(current_year)) != -1:
        _years = str(current_year)
    if _years == '' and query.find(str(next_year)) != -1:
        _years = str(next_year)
    if _years == '':
        return _return_data(_GPT_TYPE, 'a-2', '查询gpt')
    _key = 'SHENG_XIAO_CHA_XUN_' + _shengxiao + '-' + _years
    result = redis_client.get(_key)
    if result:
        _shengxiao_url = shengxiao_url_map[shengxiao_num_map[_shengxiao]]
        _res_json = json.loads(result.decode('UTF-8'))
        _res_json['imgUrl'] = _shengxiao_url
        return _return_data(_MODEL_TYPE, 'a-2', _res_json)
    return _return_data(_GPT_TYPE, 'a-2', '查询gpt')
#sheng_xiao 参考 shengxiao_num_map
async def _get_shengxiao_yunshi_params(sheng_xiao, _year):
    _key = 'SHENG_XIAO_CHA_XUN_' + sheng_xiao + '-' + str(_year)
    result = redis_client.get(_key)
    if result:
        _shengxiao_url = shengxiao_url_map[shengxiao_num_map[sheng_xiao]]
        _res_json = json.loads(result.decode('UTF-8'))
        _res_json['imgUrl'] = _shengxiao_url
        return _return_data(_MODEL_TYPE, 'a-2', _res_json)
    return _return_data(_GPT_TYPE, 'a-2', '查询gpt')
async def _get_xingzuo_chaxun(xingzuo_py):
    _date = extract_birthday(xingzuo_py)
    if not _date:
        return _return_data(_GPT_TYPE, 'a-6', '查询gpt')
    _format_time = convert_to_output_format(_date, output_format_1).split('-')
    _date = convert_to_output_format(_date, output_format)
    if not _date:
        return _return_data(_GPT_TYPE, 'a-6', '查询gpt')
    _date_1 = _date.split('-')[0]
    _date_2 = _date.split('-')[1]
    _xingzuo = is_within_date_ranges(int(_date_1), int(_date_2))
    if _xingzuo == '':
        return _return_data(_GPT_TYPE, 'a-6', '查询gpt')
    _key = 'XING_ZUO_CHA_XUN_' + _xingzuo
    result = redis_client.get(_key)
    if result:
        return _return_data(_MODEL_TYPE, 'a-6', [_get_user_base_info(_format_time[0], _format_time[1], _format_time[2], None, None), json.loads(result.decode('UTF-8'))])
    return _return_data(_GPT_TYPE, 'a-6', '查询gpt')
async def _get_xingzuo_chaxun_params(year, month, day):
    _xingzuo_py = is_within_date_ranges(month, day)
    _key = 'XING_ZUO_CHA_XUN_' + _xingzuo_py
    result = redis_client.get(_key)
    if result:
        return _return_data(_MODEL_TYPE, 'a-6', [_get_user_base_info(year, month, day, None, None), json.loads(result.decode('UTF-8'))])
    return _return_data(_GPT_TYPE, 'a-6', '查询gpt')
async def _get_xingzuo_match(xingzuo_py):
    j_p = Path(*Path(fortunetelling.__path__[0]).parts[:-1], "examples/match_json", f"{xingzuo_py}.json")
    if not Path(j_p).exists():
        return {}
    import json
    with open(j_p, 'r') as f:
        _jdata = json.load(f)
    return _jdata

async def _get_xing_luo_gongwei(_query):
    _xing_xing = ''
    for _key, _value in xing_xing_map.items():
        if _query.find(_value) !=-1:
            _xing_xing = _key
            break
    _gong_wei = ''
    for _key, _value in shi_er_gong.items():
        if _query.find(_value) !=-1:
            _gong_wei = _key
            break
        if _value.find(_query) != -1:
            _gong_wei = _key
    _key_redis = 'XING_ZUO_LUO_GONG_WEI_' + str(_xing_xing) + '_' + str(_gong_wei)
    result = redis_client.get(_key_redis)
    if result:
        return _return_data(_MODEL_TYPE, 'a-?', json.loads(result.decode('UTF-8')))
    return _return_data(_GPT_TYPE, 'a-?', '查询gpt')
# _planet 行星: 太阳，金星，木星等等
# _house 宫位: 第一宫，第二宫....等等
async def _get_xing_luo_gongwei_params(_planet, _house):
    _xing_xing = ''
    for _key, _value in xing_xing_py_map.items():
        if _planet.find(_value) !=-1:
            _xing_xing = _key
            break
    _gong_wei = ''
    for _key, _value in shi_er_gong.items():
        if _house.find(_value) !=-1:
            _gong_wei = _key
            break
        if _value.find(_house) != -1:
            _gong_wei = _key
            break
    _key_redis = 'XING_ZUO_LUO_GONG_WEI_' + str(_xing_xing) + '_' + str(_gong_wei)
    result = redis_client.get(_key_redis)
    if result:
        return _return_data(_MODEL_TYPE, 'a-17', json.loads(result.decode('UTF-8')))
    return _return_data(_GPT_TYPE, 'a-17', '查询gpt')

# _planet 行星: 太阳，金星，木星等等
# _xingzuo_py 星座: baiyang，....等等
async def _get_xing_luo_xingzuo_params(_planet, _xingzuo_py):
    _xing_xing = ''
    for _key, _value in xing_xing_py_map.items():
        if _planet.find(_value) !=-1:
            _xing_xing = _key
            break
    _xing_zuo = ''
    for _key, _value in xing_zuo.items():
        if _xingzuo_py.find(_value) !=-1:
            _xing_zuo = _key
            break
        if _value.find(_xingzuo_py) != -1:
            _xing_zuo = _key
            break
    _key_redis = 'XING_ZUO_XING_LUO_XING_ZUO_' + str(_xing_xing) + '_' + str(_xing_zuo)
    result = redis_client.get(_key_redis)
    if result:
        return _return_data(_MODEL_TYPE, 'a-18', json.loads(result.decode('UTF-8')))
    return _return_data(_GPT_TYPE, 'a-18', '查询gpt')

def is_within_date_ranges(month, day):
    for sign, (start_month, start_day), (end_month, end_day) in date_ranges:
        if (month == start_month and day >= start_day) or (month == end_month and day <= end_day):
            return sign

    return ''
def is_within_sex_ranges (_query, sex_ranges):
    for key, value in sex_ranges:
        if _query.find(key) != -1:
            return value

    return ''
def get_lunar_date(year, month, day):
    lunar_date = LunarDate.fromSolarDate(year, month, day)
    return lunar_date.year, lunar_date.month, lunar_date.day

def calculate_age(birth_year, birth_month, birth_day):
    # 获取当前日期
    today = date.today()

    # 计算年龄差值
    age = today.year - birth_year - ((today.month, today.day) < (birth_month, birth_day))

    return age
def _get_user_base_info(year, month, day, _sex, _xuexing):
    # 农历年月日
    lunar_date_year, lunar_date_month, lunar_date_day = get_lunar_date(int(year), int(month), int(day))
    # 年纪
    _age = calculate_age(int(year), int(month), int(day))
    _xing_zuo = xingzuo_data_map[is_within_date_ranges(int(month), int(day))]
    _shengxiao = shengxiao_num_map[str((int(year) - 4) % 12 + 1)]
    _gong_li = str(year) + '年' + str(int(month)) + '月' + str(int(day)) + '日'
    _nong_li = str(lunar_date_year) + '年' + str(lunar_date_month) + '月' + str(lunar_date_day) + '日'
    if _sex:
        return {'gongli': _gong_li, 'nongli': _nong_li, 'age': _age, 'zodiac': _shengxiao, 'xingzuo': _xing_zuo, 'sex': _sex}
    if _xuexing:
        return {'gongli': _gong_li, 'nongli': _nong_li, 'age': _age, 'zodiac': _shengxiao, 'xingzuo': _xing_zuo, 'xuexing': _xuexing}
    return {'gongli': _gong_li, 'nongli': _nong_li, 'age': _age, 'zodiac': _shengxiao, 'xingzuo': _xing_zuo}

def _get_shengxiao_url(_years):
    _shengxiao = shengxiao_num_map[str((int(_years) - 4) % 12 + 1)]
    _shengxiao_url = shengxiao_url_map[_shengxiao]
    return _shengxiao_url
