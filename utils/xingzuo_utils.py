from datetime import datetime
import re
output_format = '%m-%d'
output_format_1 = '%Y-%m-%d'
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
