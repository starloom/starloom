import time
from concurrent.futures import ThreadPoolExecutor
import asyncio
import openai
import json
from sanic import Request, Websocket, Sanic, response
from sanic.log import logger
from fortunetelling.config import OPENAI_API_KEY
from fortunetelling.prompt import system_prompt_mapping
from fortunetelling.prompt_3_5 import system_prompt_mapping_3_5

executor = ThreadPoolExecutor(max_workers=10)


async def http(request: Request):
    data = request.json
    device_id = data.get("device_id", "")
    character = data.get("character", "")
    product = data.get("product", "astroai")
    messages = data.get("messages", "")
    logger.info('http gpt 收到请求 %s', data)
    resp_msg = {
        'character': character,
        'message': "",
    }
    if character not in system_prompt_mapping.keys():
        return response.json(
            {"code": 10003, "msg": "参数错误", "data": f"character: {character} not in {system_prompt_mapping.keys()}"})

    if product not in {"astroai"}:
        return response.json({"code": 10003, "msg": "参数错误", "data": f"product: {product}"})

    if not device_id:
        return response.json({"code": 10003, "msg": "参数错误", "data": f"device_id: {device_id}"})

    # 请求 gpt3
    # logger.info("######################## 准备请求 gpt3 " + request.ip)
    r = await call_gpt4(character, messages)

    # 回复消息
    resp_msg['message'] = r

    return response.json({"code": 0, "msg": "success", "data": resp_msg})


async def _call_gpt3_5_turbo_16k(character: str, _input: list):
    sys_prompt = system_prompt_mapping_3_5[character]
    if len(_input) == 1:
        _prompt = f"{sys_prompt}\n{_input[0]}"
    else:
        n = len(_input)
        _sub_input = _input[:n - 1]
        context = "\n".join(_sub_input)
        _prompt = f"{context}\n{sys_prompt}\n{_input[-1]}"
    response = openai.Completion.create(
        engine="text-davinci-003",  # 使用GPT-3.5-Turbo（16K模型）
        prompt=_prompt,
        max_tokens=400  # 生成的最大长度
    )
    return response.choices[0].text.strip()


async def _call_gpt4(character: str, input: list):
    messages = _build_conversation(input)
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(executor, gpt, messages, "gpt-4", OPENAI_API_KEY, character)
    return result


async def _call_gpt3_5(character: str, input: list):
    messages = _build_conversation(input)
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(executor, gpt, messages, "gpt-3.5-turbo", OPENAI_API_KEY, character)
    return result


async def call_gpt4(character, messages):
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(executor, gpt, messages, "gpt-4", OPENAI_API_KEY, character)
    return result


def _build_conversation(input):
    _messages = []
    for item in input:
        _question = {"role": "user", "content": item}
        _messages.append(_question)
    return _messages


def gpt(messages: list, model: str, open_api_key: str, character: str = None):
    character = "default" if character is None else character
    openai.api_key = open_api_key
    sys_prompt = system_prompt_mapping[character]
    messages.insert(0, sys_prompt)

    try:
        # logger.debug(
        #     '######################## 开始请求 gpt, model: ' + model + " msg: " + json.dumps(messages, ensure_ascii=False))
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=0.5,  # 值在[0,1]之间，越大表示回复越具有不确定性
            max_tokens=3000,
            top_p=1,
            frequency_penalty=0.0,  # [-2,2]之间，该值越大则更倾向于产生不同的内容
            presence_penalty=0.0,  # [-2,2]之间，该值越大则更倾向于产生不同的内容
        )
        # logger.info("######################## 收到响应 gpt: %s", json.dumps(response, ensure_ascii=False))

        result = ''
        for choice in response.choices:
            result += choice.message.content

        return result

    except openai.error.RateLimitError as e:
        logger.error("openai.error.RateLimitError: %s", e)
        return "提问太快啦，请休息一下再问我吧"
    except openai.error.APIConnectionError as e:
        logger.error("openai.error.APIConnectionError: %s", e)
        return "我连接不到网络，请稍后重试"
    except openai.error.Timeout as e:
        logger.error("openai.error.Timeout: %s", e)
        return "我没有收到消息，请稍后重试"
    except Exception as e:
        logger.error("Exception: %s", e)
        return "系统繁忙"

    return ""
