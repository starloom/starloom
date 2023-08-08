from datetime import datetime
import re
from dateutil.parser import parse


date_str1 = '公历生日1997年10月20日'
date_str2 = '公历生日1997-10-20'
date_str3 = '公历生日1997/10/20'
date_str4 = '公历生日1997.10.20'
output_format = '%m-%d'
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
    return date_object.strftime(output_format)

s1 = extract_birthday(date_str1)
s2 = extract_birthday(date_str2)
s3 = extract_birthday(date_str3)
s4 = extract_birthday(date_str4)
print(s1, convert_to_output_format(s1, output_format))
print(s2, convert_to_output_format(s2, output_format))
print(s3, convert_to_output_format(s3, output_format))
print(s4, convert_to_output_format(s4, output_format))
