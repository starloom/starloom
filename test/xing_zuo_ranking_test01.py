import json
from utils.redis_utils import redis_client
import requests
from bs4 import BeautifulSoup
from sql.execute_sql import _select_xingzuo_question_by_title,_insert_xingzuo_votes,_select_xingzuo_question_by_type,_select_xingzuo_question_by_id,_select_xingzuo_ranking_by_question_id
import time
def _get_smxs_xingzuo_ranking () :
    _question_count = 0
    for i in range(6837, 7000):
        url = f"https://www.smxs.com/xingzuopaihang/read/id/{i}.html"
        urlData = requests.get(url).content
        soup = BeautifulSoup(urlData, 'html.parser')
        _div = soup.find_all('div', class_='intro p10')[0]
        _h1 = _div.find('h1').text
        if _h1:
            _question = _select_xingzuo_question_by_title(str(_h1).strip())
            if len(_question) > 0:
                _question_count = _question_count + 1
                _question_id = _question[0][0]
                _tds = _div.find_all('td', class_='txt07d')
                _xingzuo_id = 1
                for _td in _tds:
                    _span = _td.find('span').text
                    _insert_xingzuo_votes(_xingzuo_id, int(_span), _question_id)
                    _xingzuo_id = _xingzuo_id + 1
            else:
                print(_h1, ', 不存在！' + url)
        else:
            print('没有这个页面: ' + url)
        break
    print('总共插入问题: ', _question_count)

def _get_xingzuo_ranking_01 ():
    # _questions = _select_xingzuo_question_by_type('', 1, 5)
    _questions = _select_xingzuo_question_by_id(1)
    _ranking = _select_xingzuo_ranking_by_question_id(_questions[0][0])
    print(len(_questions))
    print(len(_ranking))
_get_xingzuo_ranking_01()