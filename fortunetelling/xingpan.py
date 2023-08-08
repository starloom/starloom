from datetime import date
from lunardate import LunarDate
from fortunetelling.shengxiaoConfig import shengxiao_num_map, shengxiao_url_map
from fortunetelling.yunshiConfig import date_ranges, xingzuo_data_map
from fortunetelling.city_config import city_list
from fortunetelling.xingpanConfig import nong_li_month, nong_li_day, _xing_image_map, _xing_image_yellow_map
from bs4 import BeautifulSoup
import requests
from utils.response_data import _return_data
import json
from fortunetelling.config import _MODEL_TYPE, _GPT_TYPE
_url_pre = 'https://www.smxs.com'

async def _get_house_quwey_params(_year, _month, _day, _hour_minute, _xing_bie, _province, _citys):
    _province = str(_province)
    _citys = str(_citys)
    _hour = str(_hour_minute).split(':')[0]
    _minute = str(_hour_minute).split(':')[0]
    _shi_chen = ''
    if int(_hour) < 10:
        _shi_chen = '0' + str(int(_hour))
    else:
        _shi_chen = str(int(_hour))
    if int(_minute) < 10:
        _minute = '0' + str(int(_minute))
    else:
        _minute = str(int(_minute))

    birthday = str(int(_year)) + '-' + str(int(_month)) + '-' + str(int(_day)) + '+' + _shi_chen + ':' + _minute
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
    birthday_lunar = str(_lunar_year) + '年' + str(nong_li_m) + str(nong_li_d)
    _xing_bie_1 = [('男', 1), ('女', 2)]
    _xing_bie_2 = [('nan', 1), ('nv', 2)]
    _xing_bie_3 = {1: '男', 2: '女'}
    _longitude = 0
    _latitude = 0
    _area = ''
    for _city in city_list:
        province = _city['province']
        city = _city['city']
        district = _city['district']
        longitude = _city['longitude']
        latitude = _city['latitude']
        if _province.find(province) != -1 or _citys.find(city) != -1 or _citys.find(district) != -1 or _province.find(
                str(province).replace('省', '')) != -1 or _province.find(
                str(province).replace('市', '') or _citys.find(str(city).replace('市', '')) != -1 or _citys.find(
                        district)) != -1:
            _longitude = float(longitude)
            _latitude = float(latitude)
            if str(province) == str(city):
                _area = str(city).replace('市', '') + '-' + str(district)
            else:
                _area = str(province).replace('省', '').replace('市', '') + '-' + str(city).replace('市', '')
            break
    try:
        _url = 'https://www.smxs.com/xingzuo/gongwei.html'
        _params = {'sex': _xing_bie, 'birthday': birthday, 'birthday_lunar': birthday_lunar, 'longitude': _longitude,
                   'latitude': _latitude, 'area': _area}
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
                _planet_obj = {'name': str(_data.text).strip(), 'imgUrl': '', 'imgUrlYellow': ''}
                for _key in _xing_image_map.keys():
                    if str(_data.text).strip().find(_key) != -1:
                        _planet_obj['imgUrl'] = _xing_image_map[_key]
                        _planet_obj['imgUrlYellow'] = _xing_image_yellow_map[_key]
                        break
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
            _planet_obj = {'name': str(_data_xing.text).strip(), 'imgUrl': '', 'imgUrlYellow': ''}
            for _key in _xing_image_map.keys():
                if str(_data_xing.text).strip().find(_key) != -1:
                    _planet_obj['imgUrl'] = _xing_image_map[_key]
                    _planet_obj['imgUrlYellow'] = _xing_image_yellow_map[_key]
                    break

            _constellation_degrees_obj = {'name': str(_data_xing_zuo.text).strip(), 'imgUrl': '', 'imgUrlYellow': ''}
            _palnet_dict = {'planet': _planet_obj, 'constellationDegrees': _constellation_degrees_obj,
                            'house': str(_data_gong_wei.text).strip()}
            planet_position.append(_palnet_dict)
        out_d['housePlanet'] = house_planet
        out_d['planetPosition'] = planet_position
        _xing_bie_3 = {1: '男', 2: '女'}
        return _return_data(_MODEL_TYPE, 'a-15', [_get_user_base_info(int(_year), int(_month), int(_day), _xing_bie_3[_xing_bie], _area), out_d])
    except Exception as e:
        return _return_data(_GPT_TYPE, 'a-15', '查询gpt')

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
def _get_user_base_info(year, month, day, _sex, _place_of_birth):
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
    if _place_of_birth:
        return {'gongli': _gong_li, 'nongli': _nong_li, 'age': _age, 'zodiac': _shengxiao, 'xingzuo': _xing_zuo, 'placeOfBirth': _place_of_birth}
    return {'gongli': _gong_li, 'nongli': _nong_li, 'age': _age, 'zodiac': _shengxiao, 'xingzuo': _xing_zuo}

def _get_shengxiao_url(_years):
    _shengxiao = shengxiao_num_map[str((int(_years) - 4) % 12 + 1)]
    _shengxiao_url = shengxiao_url_map[_shengxiao]
    return _shengxiao_url
