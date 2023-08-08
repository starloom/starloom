from utils.mysql_utils import connection_pool

def _insert_xingzuo_votes (xing_zuo_id, votes_num, question_id) :
    _sql = 'insert into xing_zuo_votes_ranking (xing_zuo_id, votes_num, question_id) values(%s, %s, %s)'
    conn = connection_pool.get_connection()
    cursor = conn.cursor()
    _params = (xing_zuo_id, votes_num, question_id)
    cursor.execute(_sql, _params)
    conn.commit()
    cursor.close()
    conn.close()

def _select_xingzuo_question_by_type(_type, _page, _page_size):
    _sql = ''
    _params = ()
    _page = (_page - 1) * _page_size
    if _type:
        _sql = 'select id, title, content, img_url, type from xing_zuo_question where `type` = %s limit %s,%s'
        _params = (int(_type), _page, _page_size)
    else:
        _sql = 'select id, title, content, img_url, type from xing_zuo_question limit %s,%s'
        _params = (_page, _page_size)
    conn = connection_pool.get_connection()
    cursor = conn.cursor()
    cursor.execute(_sql, _params)
    _result = cursor.fetchall()
    cursor.close()
    conn.close()
    return _result
def _select_xingzuo_question_by_type_count(_type):
    _sql = ''
    _params = ()
    if _type:
        _sql = 'select count(*) from xing_zuo_question where `type` = %s'
        _params = (int(_type), )
    else:
        _sql = 'select count(*) from xing_zuo_question'
    conn = connection_pool.get_connection()
    cursor = conn.cursor()
    cursor.execute(_sql, _params)
    _result = cursor.fetchall()
    cursor.close()
    conn.close()
    return _result

def _select_xingzuo_question_by_id(_id):
    _sql = 'select id,title, content, img_url, type from xing_zuo_question where id = %s'
    conn = connection_pool.get_connection()
    cursor = conn.cursor()
    _params = (int(_id), )
    cursor.execute(_sql, _params)
    _result = cursor.fetchall()
    cursor.close()
    conn.close()
    return _result

def _select_xingzuo_ranking_by_question_id(_id):
    _sql = 'select x1.name, x1.img_url as imgUrl, x2.votes_num as votesNum from xing_zuo x1 left join xing_zuo_votes_ranking x2 on x2.xing_zuo_id = x1.id where x2.question_id = %s'
    conn = connection_pool.get_connection()
    cursor = conn.cursor()
    _params = (int(_id),)
    cursor.execute(_sql, _params)
    _result = cursor.fetchall()
    cursor.close()
    conn.close()
    return _result

def _select_xingzuo_question_by_title(_title):
    _sql = 'select id,title, content, img_url, type from xing_zuo_question where `title` like  %s'
    conn = connection_pool.get_connection()
    cursor = conn.cursor()
    _search_title = '%' + _title + '%'
    _params = (_search_title,)
    cursor.execute(_sql, _params)
    _result = cursor.fetchall()
    cursor.close()
    conn.close()
    return _result