from datetime import datetime, date
import re
from bs4 import BeautifulSoup
import requests
from lunardate import LunarDate
import json

from fortunetelling.yunshiConfig import xia_jiang_date_map, xia_jiang_minute_map
from fortunetelling.city_config import city_list
from fortunetelling.xingpanConfig import _xing_image_map, _xing_image_yellow_map
output_format_1 = '%Y-%m-%d'
nong_li_month = {
    '1': '一月',
    '2': '二月',
    '3': '三月',
    '4': '四月',
    '5': '五月',
    '6': '六月',
    '7': '七月',
    '8': '八月',
    '9': '九月',
    '10': '十月',
    '11': '十一月',
    '12': '十二月',
}
nong_li_day = {
    '1': '初一',
    '2': '初二',
    '3': '初三',
    '4': '初四',
    '5': '初五',
    '6': '初六',
    '7': '初七',
    '8': '初八',
    '9': '初九',
    '10': '初十',
    '11': '十一',
    '12': '十二',
    '13': '十三',
    '14': '十四',
    '15': '十五',
    '16': '十六',
    '17': '十七',
    '18': '十八',
    '19': '十九',
    '20': '二十',
    '21': '廿一',
    '22': '廿二',
    '23': '廿三',
    '24': '廿四',
    '25': '廿五',
    '26': '廿六',
    '27': '廿七',
    '28': '廿八',
    '29': '廿九',
    '30': '三十',
}
xia_jiang_date_map = {
    '0:': '00',
    '1:': '01',
    '2:': '02',
    '3:': '03',
    '4:': '04',
    '5:': '05',
    '6:': '06',
    '7:': '07',
    '8:': '08',
    '9:': '09',
    '10:': '10',
    '11:': '11',
    '12:': '12',
    '13:': '13',
    '14:': '14',
    '15:': '15',
    '16:': '16',
    '17:': '17',
    '18:': '18',
    '19:': '19',
    '20:': '20',
    '21:': '21',
    '22:': '22',
    '23:': '23',
}
xia_jiang_minute_map = {
    '0': '00',
    '1': '01',
    '2': '02',
    '3': '03',
    '4': '04',
    '5': '05',
    '6': '06',
    '7': '07',
    '8': '08',
    '9': '09',
    '10': '10',
    '11': '11',
    '12': '12',
    '13': '13',
    '14': '14',
    '15': '15',
    '16': '16',
    '17': '17',
    '18': '18',
    '19': '19',
    '20': '20',
    '21': '21',
    '22': '22',
    '23': '23',
    '24': '24',
    '25': '25',
    '26': '26',
    '27': '27',
    '28': '28',
    '29': '29',
    '30': '30',
    '31': '31',
    '32': '32',
    '33': '33',
    '34': '34',
    '35': '35',
    '36': '36',
    '37': '37',
    '38': '38',
    '39': '39',
    '40': '40',
    '41': '41',
    '42': '42',
    '43': '43',
    '44': '44',
    '45': '45',
    '46': '46',
    '47': '47',
    '48': '48',
    '49': '49',
    '50': '50',
    '51': '51',
    '52': '52',
    '53': '53',
    '54': '54',
    '55': '55',
    '56': '56',
    '57': '57',
    '58': '58',
    '59': '59',
}
_url_pre = 'https://www.smxs.com'
def _get_gongwei(_query):
    _date = extract_birthday(_query)
    _format_time = convert_to_output_format(_date, output_format_1).split('-')
    _minute = ''
    _shi_chen = ''
    # 解析 时辰
    for _key, _value in xia_jiang_date_map.items():
        if _query.find(_key) != -1:
            _shi_chen = _value
            break
    _new_query = str(_query).replace(_date, '')
    _query_split = str(_new_query).split(':')
    if len(_query_split) == 1:
        _query_split = str(_new_query).split('：')
    if len(_query_split) == 1:
        _minute = ''
    for _key, _value in xia_jiang_minute_map.items():
        if _query_split[1].find(_key) != -1:
            _minute = _value
            break
    _year = _format_time[0]
    _month = _format_time[1]
    _day = _format_time[2]
    _lunar_year, _lunar_month, _lunar_day = get_lunar_date(int(_year), int(_month), int(_day))
    nong_li_m = ''
    for _key, _value in nong_li_month.items():
        if _key == str(int(_lunar_month)):
            nong_li_m = _value
            break
    nong_li_d = ''
    for _key, _value in nong_li_day.items():
        if _key == str(int(_lunar_day)):
            nong_li_d = _value
            break
    if int(_shi_chen) < 10:
        _shi_chen = '0' + str(int(_shi_chen))
    if int(_minute) < 10:
        _minute = '0' + str(int(_minute))

    birthday = str(int(_year)) + '-' + str(int(_month)) + '-' + str(int(_day)) + '+' + _shi_chen + ':' + _minute
    birthday_lunar = str(_lunar_year) + '年' + str(nong_li_m) + str(nong_li_d)
    _xing_bie_1 = [('男', 1), ('女', 2)]
    _xing_bie_2 = [('nan', 1), ('nv', 2)]
    _xing_bie_3 = {1: '男', 2: '女'}
    _xing_bie = ''
    _xing_bie = is_within_sex_ranges(_query, _xing_bie_1)
    if _xing_bie == '':
        _xing_bie = is_within_sex_ranges(_query, _xing_bie_2)
    _longitude = 0
    _latitude = 0
    _area = ''
    for _city in city_list:
        province = _city['province']
        city = _city['city']
        district = _city['district']
        longitude = _city['longitude']
        latitude = _city['latitude']
        if _query.find(province) != -1 or _query.find(city) != -1 or _query.find(district) != -1 or _query.find(str(province).replace('省', '')) != -1 or _query.find(str(province).replace('市', '') or _query.find(str(city).replace('市', '')) != -1 or _query.find(district)) != -1:
            _longitude = float(longitude)
            _latitude = float(latitude)
            if str(province) == str(city):
                _area = str(city).replace('市', '') + '-' + str(district)
            else:
                _area = str(province).replace('省', '').replace('市', '') + '-' + str(city).replace('市', '')
            break
    _url = 'https://www.smxs.com/xingzuo/gongwei.html'
    _params = {'sex': _xing_bie, 'birthday': birthday, 'birthday_lunar': birthday_lunar, 'longitude': _longitude, 'latitude': _latitude, 'area': _area}
    print(_params)
    _res_data = requests.post(_url, data=_params).content
    soup = BeautifulSoup(_res_data, 'html.parser')
    _div_xptu = soup.find('div', class_='xptu')
    _div_xptu_img = _div_xptu.find('img')
    # 星图 图片
    xpt_img_url = _div_xptu_img.attrs['src']
    out_d = {'astrolabeImgUrl': _url_pre + xpt_img_url, 'housePlanet': [], 'planetPosition': []}
    _div_0 = soup.find_all('div', class_='xpbox')[0]
    _div_xpwztit = _div_0.find('div', class_='xpwztit').text
    # 宫位数据
    _div_hxitem_left = _div_0.find_all('div', class_='hxitem_left')
    # 宫位对应行星数据
    _div_hxitem_right = _div_0.find_all('div', class_='hxitem_right')
    house_planet = []
    for _index, fruit in enumerate(_div_hxitem_left):
        _right_data = _div_hxitem_right[_index]
        _div_xxinfo = _right_data.find_all('div', class_='xxinfo')
        _house_planet_obj = {'house': str(fruit.text).strip(), 'planets': []}
        for _data in _div_xxinfo:
            _planet_obj = {'name': str(_data.text).strip(), 'imgUrl': ''}
            _house_planet_obj['planets'].append(_planet_obj)
        house_planet.append(_house_planet_obj)

    # 行星位置
    _div_1 = soup.find_all('div', class_='xpbox')[1]
    _div_1_xpwztit = _div_1.find('div', 'xpwztit').text
    _div_1_xxwzkuang = _div_1.find('div', 'xxwzkuang')
    _div_1xxwxitem = _div_1_xxwzkuang.find_all('div', class_='xxwxitem')
    planet_position = []
    for _data in _div_1xxwxitem:
        _data_xing = _data.find('div', class_='itemxx')
        _data_xing_zuo = _data.find('div', class_='itemds')
        _data_gong_wei = _data.find('div', class_='itemgw')
        _planet_obj = {'name': str(_data_xing.text).strip(), 'imgUrl': ''}
        _constellation_degrees_obj = {'name': str(_data_xing_zuo.text).strip(), 'imgUrl': ''}
        _palnet_dict = {'planet': _planet_obj, 'constellationDegrees': _constellation_degrees_obj, 'house': str(_data_gong_wei.text).strip()}
        planet_position.append(_palnet_dict)
    out_d['housePlanet'] = house_planet
    out_d['planetPosition'] = planet_position
    print(json.dumps(out_d, ensure_ascii=False))
def get_lunar_date(year, month, day):
    lunar_date = LunarDate.fromSolarDate(year, month, day)
    _lunar_year = lunar_date.year
    _lunar_month = lunar_date.month
    _lunar_day = lunar_date.day
    return _lunar_year, _lunar_month, _lunar_day
def extract_birthday(text):
    # 定义匹配日期的正则表达式模式
    pattern1 = r'\d{4}年\d{1,2}月\d{1,2}日'
    pattern2 = r'\d{4}-\d{1,2}-\d{1,2}'
    pattern3 = r'\d{4}/\d{1,2}/\d{1,2}'
    pattern4 = r'\d{4}.\d{1,2}.\d{1,2}'

    # 在文本中查找匹配的日期
    matches1 = re.findall(pattern1, text)
    matches2 = re.findall(pattern2, text)
    matches3 = re.findall(pattern3, text)
    matches4 = re.findall(pattern4, text)

    if matches1:
        return matches1[0]  # 返回第一个匹配的日期
    if matches2:
        return matches2[0]  # 返回第一个匹配的日期
    if matches3:
        return matches3[0]
    if matches4:
        return matches4[0]
    else:
        return None

def convert_to_output_format(date_str, out_format):
    input_format1 = '%Y年%m月%d日'
    input_format2 = '%Y-%m-%d'
    input_format3 = '%Y/%m/%d'
    input_format4 = '%Y.%m.%d'
    date_object = ''
    try:
        date_object = datetime.strptime(date_str, input_format1)
    except ValueError:
        try:
            date_object = datetime.strptime(date_str, input_format2)
        except ValueError:
            try:
                date_object = datetime.strptime(date_str, input_format3)
            except ValueError:
                try:
                    date_object = datetime.strptime(date_str, input_format4)
                except ValueError:
                    return None
    return date_object.strftime(out_format)
def is_within_sex_ranges (_query, sex_ranges):
    for key, value in sex_ranges:
        if _query.find(key) != -1:
            return value

    return ''
_get_gongwei('1998-9-1 河北石家庄 00:00 子时 女')
