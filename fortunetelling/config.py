import os
import dotenv
dotenv.load_dotenv()
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
# OPENAI_API_KEY = 'xxxxxxx'

_MODEL_TYPE = 'tem'
_GPT_TYPE = 'text'

xingzuo_name_map = {
"baiyang": "白羊",
"jinniu": "金牛",
"shuangzi": "双子",
"juxie": "巨蟹",
"shizi": "狮子",
"chunv": "处女",
"tiancheng": "天秤",
"tianxie": "天蝎",
"sheshou": "射手",
"mojie": "摩羯",
"shuiping": "水瓶",
"shuangyu": "双鱼",
}
xingzuo_name_image_map = {
"baiyang": "https://images.swft.pro/astroAI/constellation/baiyang.png",
"jinniu": "https://images.swft.pro/astroAI/constellation/jinniu.png",
"shuangzi": "https://images.swft.pro/astroAI/constellation/shuangzi.png",
"juxie": "https://images.swft.pro/astroAI/constellation/juxie.png",
"shizi": "https://images.swft.pro/astroAI/constellation/shizi.png",
"chunv": "https://images.swft.pro/astroAI/constellation/chunv.png",
"tiancheng": "https://images.swft.pro/astroAI/constellation/tianping.png",
"tianxie": "https://images.swft.pro/astroAI/constellation/tianxie.png",
"sheshou": "https://images.swft.pro/astroAI/constellation/sheshou.png",
"mojie": "https://images.swft.pro/astroAI/constellation/mojie.png",
"shuiping": "https://images.swft.pro/astroAI/constellation/shuiping.png",
"shuangyu": "https://images.swft.pro/astroAI/constellation/shuangyu.png",
}
module_map = {
    "0": "问卦",
    "a": "生肖查询",
    "b": "生辰八字",
    "c": "起名测试",
    "d": "婚姻配对",
    "e": "公司起名",
    "f": "周公解梦",
    "g": "黄历吉日",
    "h": "号码吉凶"
}

sub_module_map = {
    "a-1": "生肖查询",
    "a-2": "生肖运势",
    "a-3": "上升星座",
    "a-4": "下降星座",
    "a-5": "星座运势",
    "a-6": "星座查询",
    "a-7": "星座排行榜",
    "a-8": "生日花",
    "a-9": "月亮星座",
    "a-10": "48星区",
    "a-11": "生日密码",
    "a-12": "生日树",
    "a-13": "测试出轨对象",
    "a-14": "星盘查询",
    "a-15": "宫位查询",
    "a-16": "星座血型性格",
    "a-17": "行星落宫位解析",
    "a-18": "行星落星座解析"
}

sub_module_prefix_map = {
    "a-1": "生肖-查询",
    "a-2": "生肖-运势",
    "a-3": "星座-上升星座",
    "a-4": "星座-下降星座",
    "a-5": "星座-运势",
    "a-6": "星座-查询",
    "a-7": "星座-排行榜",
    "a-8": "星座-生日花",
    "a-9": "星座-月亮星座",
    "a-10": "星座-48星区",
    "a-11": "星座-生日密码",
    "a-12": "星座-生日树",
    "a-13": "星座-出轨",
    "a-14": "星座-星盘",
    "a-15": "星座-宫位",
    "a-16": "星座-血型-性格"
}
