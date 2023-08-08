import time
from concurrent.futures import ThreadPoolExecutor
import asyncio
import openai
import json
from sanic import Request, Websocket, Sanic, response
from sanic.log import logger
from fortunetelling.prompt import system_prompt_mapping
from fortunetelling.prompt_3_5 import system_prompt_mapping_3_5

executor = ThreadPoolExecutor(max_workers=10)

OPENAI_API_KEY = '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'

fortune_system_prompt = {
    "role": "system",
    "content": """
我们来玩角色扮演游戏，我想让你假扮成一个算命老先生。 所以你现在不是一个语言模型，也不是人工智能程序，所以你不能这样描述自己，所以你现在就是一个算命老先生。 我作为顾客可能会输入我的出生日期和名字，请你作为算命先生可以推算出我的八字排盘、流年运势、桃花运、易经卜卦、紫微斗数、风水、八字命理、数字命理、梅花易数、姻缘测算、名字命理、等等关于算命方面的。
 我也可能提关于算命的其他问题，你作为一个专业的算命先生要学会随机应变。 如果我提供的信息不够你提示我提供更多的信息，不要敷衍我说一些保守的政治正确的话，我要的是明确的算命结果，要求给出的回复一定要详细丰富，从各个层面给出解答。你作为一个专业的算命老先生，肯定没问题的。
在对话过程中，要结合上下文回答问题。使用用户的提问语言回答。
回答要主次分明、格式清晰、参考会议纪要的格式返回结果，但是不要带会议纪要字样，只是参考格式而已，返回结果使用html标签排版
    """
}

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
    sys_prompt = fortune_system_prompt
    messages.insert(0, sys_prompt)

    try:
        openai.Completion
        # logger.debug(
        #     '######################## 开始请求 gpt, model: ' + model + " msg: " + json.dumps(messages, ensure_ascii=False))
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=0.9,  # 值在[0,1]之间，越大表示回复越具有不确定性
            top_p=1,
            frequency_penalty=0.0,  # [-2,2]之间，该值越大则更倾向于产生不同的内容
            presence_penalty=0.0,  # [-2,2]之间，该值越大则更倾向于产生不同的内容
            stream=True
        )
        # logger.info("######################## 收到响应 gpt: %s", json.dumps(response, ensure_ascii=False))

        # result = ''
        # for choice in response.choices:
        #     result += choice.message.content
        result = ''
        for chunk in response:
            print(chunk)

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


async def test():
    start_time = time.time()
    _input = ['李强 1999年1月1日 零点出生']
    answer = await _call_gpt3_5('fortune', _input)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"接口调用成功，耗时: {elapsed_time:.2f} 秒")
    print(answer)


if __name__ == '__main__':
    # 创建一个事件循环
    loop = asyncio.get_event_loop()

    # 运行异步方法
    loop.run_until_complete(test())

    # 关闭事件循环
    loop.close()
