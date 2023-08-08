from sql.execute_sql import _select_xingzuo_question_by_id,_select_xingzuo_ranking_by_question_id

def _test01 () :
    print('---------')
    _questions = _select_xingzuo_question_by_id(1)
    _votes = _select_xingzuo_ranking_by_question_id(1)

_test01()