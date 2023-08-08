import json
import traceback
from pathlib import Path
from sanic.log import logger
from sanic import Sanic, response
import fortunetelling
from fortunetelling.xingzuo import _get_xingzuo_yunshi, _get_xingzuo_match, _get_xingzuo_yunshi_2, \
    _get_xingzuo_shengrihua, _get_xingzuo_shengrihua_params, _get_xingzuo_shengrishu, _get_xingzuo_shengrishu_params, \
    _get_xingzuo_shengrimima, _get_xingzuo_shengrimima_params, \
    _get_shengxiao_yunshi, _get_shengxiao_yunshi_params, _get_shengxiao_query, _get_shengxiao_query_params, \
    _get_xingzuo_chaxun, _get_xingzuo_chaxun_params, _get_xingzuo_ranking, _get_xingzuo_ranking_question, \
    _get_xingzuo_ranking_get, \
    _get_xingzuo_ranking_question, _get_xingzuo_xuexing, _get_xingzuo_chugui, _get_xingzuo_48, _get_xingzuo_48_params, \
    _get_xingzuo_chugui_params, _get_xingzuo_xuexing_params, _get_xingzuo_xiajiang, _get_xingzuo_yueliang, \
    _get_xingzuo_yunshi_params, \
    _get_xingzuo_xiajiang_params, _get_xingzuo_yueliang_params, _get_xingzuo_shangsheng
from fortunetelling.config import xingzuo_name_map, sub_module_prefix_map, _GPT_TYPE
from fortunetelling.yunshiConfig import xingzuo_en_map
from fortunetelling.yunshiConfig import xingzuo_zh_map
from fortunetelling.gpt import _call_gpt3_5_turbo_16k, _call_gpt4, _call_gpt3_5
from sanic import Sanic
from sanic_cors import CORS
from dispatch.query import question, isDict
from utils.response_data import _return_data
from datetime import datetime
from fortunetelling.shengxiaoConfig import shengxiao_py_num_sxkey_map
import logging

app = Sanic("ftapp")
app.config.REQUEST_TIMEOUT = 180
app.config.RESPONSE_TIMEOUT = 180
app.config.KEEP_ALIVE_TIMEOUT = 180
app.config.KEEP_ALIVE = True
ensure_ascii = False

CORS(app)  # 启用跨域资源共享

# 创建日志文件处理器
file_handler = logging.FileHandler('app.log')  # 指定日志文件名

# 配置日志格式
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# 创建日志记录器并添加处理器
logger = logging.getLogger('sanic_app_logger')
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)  # 设置日志级别为INFO或更高级别


@app.route('/xingzuo/xingge', methods=["POST", "GET"])
async def get_xingzuo_xingge(request):
    data = request.json
    xingzuo_py = data.get("query", "")
    _jk_name = ''
    xingzuo_py = xingzuo_py.lower()
    if xingzuo_py in xingzuo_en_map.keys():
        _name = xingzuo_en_map[xingzuo_py]
        for item in xingzuo_name_map.keys():
            if xingzuo_name_map[item] == _name:
                _jk_name = item
    if _jk_name == '':
        for _zh_name in xingzuo_zh_map.keys():
            if xingzuo_py.find(_zh_name) != -1:
                for item in xingzuo_name_map.keys():
                    if xingzuo_name_map[item] == _zh_name:
                        _jk_name = item
    if _jk_name == '':
        for _py_name in xingzuo_name_map.keys():
            if xingzuo_py.find(_py_name) != -1:
                _jk_name = _py_name
    if _jk_name == '':
        return response.json({"code": 10003, "msg": "参数错误", "data": ""})
    j_p = Path(*Path(fortunetelling.__path__[0]).parts[:-1], "examples/xingge_json", f"{_jk_name}.json")
    if not Path(j_p).exists():
        logger.error(f'data: {data}')
        return response.json({"code": 10003, "msg": "参数错误", "data": ""})
    import json
    with open(j_p, 'r') as f:
        _jdata = json.load(f)
    return response.json({"code": 0, "msg": "success", "data": _jdata}, ensure_ascii=ensure_ascii)


@app.route('/xingzuo/yunshi', methods=["POST", "GET"])
async def get_xingzuo_yunshi(request):
    data = request.json
    xingzuo_py = data.get("query", "")
    _index = data.get("index", 0)
    try:
        _jdata = await _get_xingzuo_yunshi_2(xingzuo_py, _index)
        if not _jdata:
            logger.error(f'data: {data}')
            return response.json({"code": 10003, "msg": "参数错误", "data": ""})
    except Exception as e:
        return response.json({"code": 10004, "msg": "执行错误", "data": ""})
    return response.json({"code": 0, "msg": "success", "data": _jdata}, ensure_ascii=ensure_ascii)


@app.route('/xingzuo/match', methods=["POST", "GET"])
async def get_xingzuo_match(request):
    data = request.json
    xingzuo_py = data.get("query", "")
    _jk_name = ''
    xingzuo_py = xingzuo_py.lower()
    if xingzuo_py in xingzuo_en_map.keys():
        _name = xingzuo_en_map[xingzuo_py]
        for item in xingzuo_name_map.keys():
            if xingzuo_name_map[item] == _name:
                _jk_name = item
    if _jk_name == '':
        for _zh_name in xingzuo_zh_map.keys():
            if xingzuo_py.find(_zh_name) != -1:
                for item in xingzuo_name_map.keys():
                    if xingzuo_name_map[item] == _zh_name:
                        _jk_name = item
    if _jk_name == '':
        for _py_name in xingzuo_name_map.keys():
            if xingzuo_py.find(_py_name) != -1:
                _jk_name = _py_name
    if _jk_name == '':
        return response.json({"code": 10003, "msg": "参数错误", "data": ""})
    try:
        _jdata = await _get_xingzuo_match(_jk_name)
        if not _jdata:
            logger.error(f'data: {data}')
            return response.json({"code": 10003, "msg": "参数错误", "data": ""})
    except Exception as e:
        return response.json({"code": 10004, "msg": "执行错误", "data": ""})
    return response.json({"code": 0, "msg": "success", "data": _jdata}, ensure_ascii=ensure_ascii)


@app.route('/xingzuo/chaxun', methods=["POST", "GET"])
async def get_xingzuo_chaxun(request):
    data = request.json
    xingzuo_py = data.get("query", "")
    try:
        _jdata = await _get_xingzuo_chaxun(xingzuo_py)
        if not _jdata:
            logger.error(f'data: {data}')
            return response.json({"code": 10003, "msg": "参数错误", "data": ""})
    except Exception as e:
        return response.json({"code": 10004, "msg": "执行错误", "data": ""})
    return response.json({"code": 0, "msg": "success", "data": _jdata}, ensure_ascii=ensure_ascii)


@app.route('/xingzuo/shengrihua', methods=["POST", "GET"])
async def get_xingzuo_shengrihua(request):
    data = request.json
    xingzuo_py = data.get("query", "")
    try:
        _jdata = await _get_xingzuo_shengrihua(xingzuo_py)
        if not _jdata:
            logger.error(f'data: {data}')
            return response.json({"code": 10003, "msg": "参数错误", "data": ""})
    except Exception as e:
        return response.json({"code": 10004, "msg": "执行错误", "data": ""})
    return response.json({"code": 0, "msg": "success", "data": _jdata}, ensure_ascii=ensure_ascii)


@app.route('/xingzuo/shengrimima', methods=["POST", "GET"])
async def get_xingzuo_shengrimima(request):
    data = request.json
    xingzuo_py = data.get("query", "")
    try:
        _jdata = await _get_xingzuo_shengrimima(xingzuo_py)
        if not _jdata:
            logger.error(f'data: {data}')
            return response.json({"code": 10003, "msg": "参数错误", "data": ""})
    except Exception as e:
        return response.json({"code": 10004, "msg": "执行错误", "data": ""})
    return response.json({"code": 0, "msg": "success", "data": _jdata}, ensure_ascii=ensure_ascii)


@app.route('/xingzuo/shengrishu', methods=["POST", "GET"])
async def get_xingzuo_shengrishu(request):
    data = request.json
    xingzuo_py = data.get("query", "")
    try:
        _jdata = await _get_xingzuo_shengrishu(xingzuo_py)
        if not _jdata:
            logger.error(f'data: {data}')
            return response.json({"code": 10003, "msg": "参数错误", "data": ""})
    except Exception as e:
        return response.json({"code": 10004, "msg": "执行错误", "data": ""})
    return response.json({"code": 0, "msg": "success", "data": _jdata}, ensure_ascii=ensure_ascii)


@app.route('/xingzuo/ranking', methods=["POST", "GET"])
async def get_xingzuo_ranking(request):
    data = request.json
    xingzuo_py = data.get("type", "")
    _page = data.get("page", 1)
    _page_size = data.get("pageSize", 10)
    try:
        _jdata = await _get_xingzuo_ranking(xingzuo_py, int(_page), int(_page_size))
        if not _jdata:
            logger.error(f'data: {data}')
            return response.json({"code": 10003, "msg": "参数错误", "data": ""})
    except Exception as e:
        return response.json({"code": 10004, "msg": "执行错误", "data": ""})
    return response.json({"code": 0, "msg": "success", "data": _jdata}, ensure_ascii=ensure_ascii)


@app.route('/xingzuo/ranking/get', methods=["POST", "GET"])
async def get_xingzuo_ranking_one(request):
    data = request.json
    xingzuo_py = data.get("id", "")
    try:
        _jdata = await _get_xingzuo_ranking_get(xingzuo_py)
        if not _jdata:
            logger.error(f'data: {data}')
            return response.json({"code": 10003, "msg": "参数错误", "data": ""})
    except Exception as e:
        return response.json({"code": 10004, "msg": "执行错误", "data": ""})
    return response.json({"code": 0, "msg": "success", "data": _jdata}, ensure_ascii=ensure_ascii)


@app.route('/xingzuo/ranking/question', methods=["POST", "GET"])
async def get_xingzuo_ranking_question(request):
    data = request.json
    xingzuo_py = data.get("query", "")
    try:
        _jdata = await _get_xingzuo_ranking_question(xingzuo_py)
        if not _jdata:
            logger.error(f'data: {data}')
            return response.json({"code": 10003, "msg": "参数错误", "data": ""})
    except Exception as e:
        return response.json({"code": 10004, "msg": "执行错误", "data": ""})
    return response.json({"code": 0, "msg": "success", "data": _jdata}, ensure_ascii=ensure_ascii)


@app.route('/xingzuo/xuexing', methods=["POST", "GET"])
async def get_xingzuo_xuexing(request):
    data = request.json
    xingzuo_py = data.get("query", "")
    try:
        _jdata = await _get_xingzuo_xuexing(xingzuo_py)
        if not _jdata:
            logger.error(f'data: {data}')
            return response.json({"code": 10003, "msg": "参数错误", "data": ""})
    except Exception as e:
        return response.json({"code": 10004, "msg": "执行错误", "data": ""})
    return response.json({"code": 0, "msg": "success", "data": _jdata}, ensure_ascii=ensure_ascii)


@app.route('/xingzuo/chugui', methods=["POST", "GET"])
async def get_xingzuo_chugui(request):
    data = request.json
    xingzuo_py = data.get("query", "")
    try:
        _jdata = await _get_xingzuo_chugui(xingzuo_py)
        if not _jdata:
            logger.error(f'data: {data}')
            return response.json({"code": 10003, "msg": "参数错误", "data": ""})
    except Exception as e:
        return response.json({"code": 10004, "msg": "执行错误", "data": ""})
    return response.json({"code": 0, "msg": "success", "data": _jdata}, ensure_ascii=ensure_ascii)


@app.route('/xingzuo/48', methods=["POST", "GET"])
async def get_xingzuo_48(request):
    data = request.json
    xingzuo_py = data.get("query", "")
    try:
        _jdata = await _get_xingzuo_48(xingzuo_py)
        if not _jdata:
            logger.error(f'data: {data}')
            return response.json({"code": 10003, "msg": "参数错误", "data": ""})
    except Exception as e:
        return response.json({"code": 10004, "msg": "执行错误", "data": ""})
    return response.json({"code": 0, "msg": "success", "data": _jdata}, ensure_ascii=ensure_ascii)


@app.route('/xingzuo/xiajiang', methods=["POST", "GET"])
async def get_xingzuo_xiajiang(request):
    data = request.json
    xingzuo_py = data.get("query", "")
    try:
        _jdata = await _get_xingzuo_xiajiang(xingzuo_py)
        if not _jdata:
            logger.error(f'data: {data}')
            return response.json({"code": 10003, "msg": "参数错误", "data": ""})
    except Exception as e:
        return response.json({"code": 10004, "msg": "执行错误", "data": ""})
    return response.json({"code": 0, "msg": "success", "data": _jdata}, ensure_ascii=ensure_ascii)


@app.route('/xingzuo/yueliang', methods=["POST", "GET"])
async def get_xingzuo_yueliang(request):
    data = request.json
    xingzuo_py = data.get("query", "")
    try:
        _jdata = await _get_xingzuo_yueliang(xingzuo_py)
        if not _jdata:
            logger.error(f'data: {data}')
            return response.json({"code": 10003, "msg": "参数错误", "data": ""})
    except Exception as e:
        return response.json({"code": 10004, "msg": "执行错误", "data": ""})
    return response.json({"code": 0, "msg": "success", "data": _jdata}, ensure_ascii=ensure_ascii)


@app.route('/xingzuo/shangsheng', methods=["POST", "GET"])
async def get_xingzuo_shangsheng(request):
    data = request.json
    xingzuo_py = data.get("query", "")
    try:
        _jdata = await _get_xingzuo_shangsheng(xingzuo_py)
        if not _jdata:
            logger.error(f'data: {data}')
            return response.json({"code": 10003, "msg": "参数错误", "data": ""})
    except Exception as e:
        return response.json({"code": 10004, "msg": "执行错误", "data": ""})
    return response.json({"code": 0, "msg": "success", "data": _jdata}, ensure_ascii=ensure_ascii)


@app.route('/shengxiao/query', methods=["POST", "GET"])
async def get_shengxiao_query(request):
    data = request.json
    xingzuo_py = data.get("query", "")
    try:
        _jdata = await _get_shengxiao_query(xingzuo_py)
        if not _jdata:
            logger.error(f'data: {data}')
            return response.json({"code": 10003, "msg": "参数错误", "data": ""})
    except Exception as e:
        return response.json({"code": 10004, "msg": "执行错误", "data": ""})
    return response.json({"code": 0, "msg": "success", "data": _jdata}, ensure_ascii=ensure_ascii)


@app.route('/shengxiao/yunshi', methods=["POST", "GET"])
async def get_shengxiao_yunshi(request):
    data = request.json
    xingzuo_py = data.get("query", "")
    try:
        _jdata = await _get_shengxiao_yunshi(xingzuo_py)
        if not _jdata:
            logger.error(f'data: {data}')
            return response.json({"code": 10003, "msg": "参数错误", "data": ""})
    except Exception as e:
        return response.json({"code": 10004, "msg": "执行错误", "data": ""})
    return response.json({"code": 0, "msg": "success", "data": _jdata}, ensure_ascii=ensure_ascii)


@app.route('/character', methods=["POST"])
async def post_character(request):
    from fortunetelling.gpt import http
    return await http(request)


async def questionWrapper(_input, sub_module):
    _answer = question(sub_module, _input, 0.8)
    logger.info('_answer=' + json.dumps(_answer, ensure_ascii=False))
    if _answer.get('is_match') == 1:
        _answer = _answer.get('answer')
        if isDict(_answer):
            tag = _answer.get('tag')
            if tag == 'get_sx_cx':
                _nian = _answer.get('nian')
                logger.info('get_sx_cx call _get_shengxiao_query_params _nian=' + _nian)
                _data = await _get_shengxiao_query_params(_nian)
            elif tag == 'get_sx_ys':
                _shengxiao = _answer.get('shengxiao')
                _nian = _answer.get('nian')
                cur_year = datetime.now().year
                if int(_nian) < cur_year:
                    return _return_data(_GPT_TYPE, 'a-2', '只能查询当前或下一年的生肖运势！')
                _shengxiao_num = shengxiao_py_num_sxkey_map.get(_shengxiao)
                if not _shengxiao_num:
                    return _return_data(_GPT_TYPE, 'a-2', '请输入正确的生肖！')
                logger.info('get_sx_ys call _get_shengxiao_yunshi_params _shengxiao_num=' + str(
                    _shengxiao_num) + ' _nian=' + str(_nian))
                _data = await _get_shengxiao_yunshi_params(_shengxiao_num, _nian)
            elif tag == 'get_xz_ssxz':
                # TODO 暂未实现
                print('暂未实现')
            elif tag == 'get_xz_xjxz':
                _shichen = _answer.get('shichen')
                _xing_bie = _answer.get('xingbie')
                _shengri = _answer.get('shengri')
                year, month, day = _shengri.split('-')
                logger.info(
                    'get_xz_xjxz call _get_xingzuo_xiajiang_params _shichen=' + str(_shichen) + ' _xing_bie=' + str(
                        _xing_bie) + ' _year=' + str(year) + ' _month=' + str(month) + ' _day=' + str(day))
                _data = await _get_xingzuo_xiajiang_params(_shichen, _xing_bie, year, month, day)
            elif tag == 'get_xz_ys':
                _xingzuo_name = _answer['xingzuo_name']
                logger.info(
                    'get_xz_ys call _get_xingzuo_yunshi_params _xingzuo_name=' + _xingzuo_name + ' _input=' + _input[
                        -1])
                _data = await _get_xingzuo_yunshi_params(_xingzuo_name, 0, _input[-1])
            elif tag == 'get_xz_cx':
                _shengri = _answer.get('shengri')
                year, month, day = _shengri.split('-')
                logger.info(
                    'get_xz_cx call _get_xingzuo_chaxun_params year=' + year + ' month=' + month + ' day=' + day)
                _data = await _get_xingzuo_chaxun_params(year, month, day)
            elif tag == 'get_xz_phb':
                logger.info(
                    'get_xz_phb call _get_xingzuo_ranking_question _input=' + _input[-1])
                _data = await _get_xingzuo_ranking_question(_input[-1])
                if _data.get('type') == _GPT_TYPE:
                    logger.info(
                        'get_xz_phb call _get_xingzuo_ranking')
                    _data = await _get_xingzuo_ranking(None, 1, 10)
            elif tag == 'get_xz_srh':
                _shengri = _answer.get('shengri')
                year, month, day = _shengri.split('-')
                logger.info(
                    'get_xz_srh call _get_xingzuo_shengrihua_params year=' + year + ' month=' + month + ' day=' + day)
                _data = await _get_xingzuo_shengrihua_params(year, month, day)
            elif tag == 'get_xz_ylxz':
                _shi = _answer.get('shi')
                _fen = _answer.get('fen')
                _shichen = _shi + ':' + _fen
                _xing_bie = _answer.get('xingbie')
                _shengri = _answer.get('shengri')
                year, month, day = _shengri.split('-')
                logger.info(
                    'get_xz_ylxz call _get_xingzuo_yueliang_params _shichen=' + _shichen + ' _xing_bie' + str(
                        _xing_bie) + ' year=' + year + ' month=' + month + ' day=' + day)
                _data = await _get_xingzuo_yueliang_params(_shichen, _xing_bie, year, month, day)
            elif tag == 'get_xz_48xq':
                _shengri = _answer.get('shengri')
                year, month, day = _shengri.split('-')
                logger.info(
                    'get_xz_48xq call _get_xingzuo_48_params year=' + year + ' month=' + month + ' day=' + day)
                _data = await _get_xingzuo_48_params(year, month, day)
            elif tag == 'get_xz_srmm':
                _shengri = _answer.get('shengri')
                year, month, day = _shengri.split('-')
                logger.info(
                    'get_xz_srmm call _get_xingzuo_shengrimima_params year=' + year + ' month=' + month + ' day=' + day)
                _data = await _get_xingzuo_shengrimima_params(year, month, day)
            elif tag == 'get_xz_srs':
                _shengri = _answer.get('shengri')
                year, month, day = _shengri.split('-')
                logger.info(
                    'get_xz_srs call _get_xingzuo_shengrishu_params year=' + year + ' month=' + month + ' day=' + day)
                _data = await _get_xingzuo_shengrishu_params(year, month, day)
            elif tag == 'get_xz_cg':
                _xingzuo_name = _answer.get('xingzuo_name')
                _xingbie = _answer.get('xingbie')
                _shengri = _answer.get('shengri')
                year, month, day = _shengri.split('-')
                logger.info(
                    'get_xz_cg call _get_xingzuo_chugui_params _xingzuo_name=' + _xingzuo_name + ' _xingbie=' + str(
                        _xingbie) + ' year=' + year + ' month=' + month + ' day=' + day)
                _data = await _get_xingzuo_chugui_params(_xingzuo_name, _xingbie, year, month, day)
            elif tag == 'get_xz_xp':
                # TODO 暂未实现
                print('暂未实现')
            elif tag == 'get_xz_gw':
                # TODO 暂未实现
                print('暂未实现')
            elif tag == 'get_xz_xx_xg':
                _xuexing = _answer.get('xuexing')
                _shengri = _answer.get('shengri')
                year, month, day = _shengri.split('-')
                logger.info(
                    'get_xz_xx_xg call _get_xingzuo_xuexing_params _xuexing=' + _xuexing + ' year=' + year + ' month=' + month + ' day=' + day)
                _data = await _get_xingzuo_xuexing_params(_xuexing, year, month, day)
            if _data['type'] == _GPT_TYPE:
                logger.info(f'query gpt,type={_GPT_TYPE},_input={_input},sub_module={sub_module}')
                # 去查询GPT
                if tag == 'get_sx_cx' or tag == 'get_sx_ys':
                    _data = await _call_gpt3_5('fortune', _input)
                else:
                    _data = await _call_gpt3_5('astro', _input)
                _data = _return_data(_GPT_TYPE, sub_module, _data)
        else:
            _data = _return_data(_GPT_TYPE, sub_module, _answer)
    else:
        _data = await _call_gpt3_5('default', _answer.get('answer'))
        _data = _return_data(_GPT_TYPE, sub_module, _answer.get('answer'))
    return _data


@app.route('/chat', methods=["POST"])
async def chat(request):
    param = request.json
    logger.info('chat request=' + json.dumps(param, ensure_ascii=False))
    if not param or not param.get('module') or not param.get('input'):
        logger.error(f'param: {param}')
        return response.json({"code": 10003, "msg": "参数错误", "data": ""})
    if param.get('module') == 'a' and not param.get('sub_module'):
        logger.error(f'param: {param}')
        return response.json({"code": 10003, "msg": "参数错误", "data": ""})
    module = param.get('module')
    sub_module = param.get('sub_module')
    _input = param.get('input')
    _data = ''
    try:
        if module == 'a':
            _data = await questionWrapper(_input, sub_module)
        elif module == 'b':
            # 生辰八字
            _data = await _call_gpt3_5('fortune', _input)
            _data = _return_data(_GPT_TYPE, 'b', _data)
        elif module == 'c':
            # 起名测试
            _data = await _call_gpt3_5('naming', _input)
            _data = _return_data(_GPT_TYPE, 'c', _data)
        elif module == 'd':
            # 婚姻配对
            _data = await _call_gpt3_5('matrimony', _input)
            _data = _return_data(_GPT_TYPE, 'd', _data)
        elif module == 'e':
            # 公司起名
            _data = await _call_gpt3_5('gongsiqiming', _input)
            _data = _return_data(_GPT_TYPE, 'e', _data)
        elif module == 'f':
            # 周公解梦
            _data = await _call_gpt3_5('zhougongjiemeng', _input)
            _data = _return_data(_GPT_TYPE, 'f', _data)
        elif module == 'g':
            # 黄历吉日
            _data = await _call_gpt3_5('huanglijiri', _input)
            _data = _return_data(_GPT_TYPE, 'g', _data)
        elif module == 'h':
            # 黄历吉日
            _data = await _call_gpt3_5('haomajixiong', _input)
            _data = _return_data(_GPT_TYPE, 'h', _data)
        elif module == '0':
            # 问卦
            _data = await questionWrapper(_input, None)
            if _data.get('type') == _GPT_TYPE:
                _data = await _call_gpt3_5('wengua', _input)
                _data = _return_data(_GPT_TYPE, '0', _data)
        else:
            _data = await questionWrapper(_input, None)
        _jdata = _data
        logger.info('response data=' + json.dumps(_jdata, ensure_ascii=False))
    except:
        traceback.print_exc()  # prints traceback information
        # logger.error('execute chat happens error', e)
        return response.json({"code": 10004, "msg": "执行错误", "data": ""})
    return response.json({"code": 0, "msg": "success", "data": _jdata}, ensure_ascii=ensure_ascii)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8001, debug=True, access_log=True)
