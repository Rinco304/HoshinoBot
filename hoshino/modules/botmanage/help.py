from hoshino import Service, priv
from hoshino.typing import CQEvent
from . import utils

sv = Service('_help_', manage_priv=priv.SUPERUSER, visible=False)

TOP_MANUAL = '''
====================
= HoshinoBot使用说明 =
====================
发送[]内的关键词触发

==== 查看详细说明 ====
[帮助pcr会战][帮助pcr查询]
[帮助pcr娱乐][帮助pcr订阅]
[帮助artist][帮助kancolle]
[帮助umamusume]
[帮助通用]

====== 常用指令 ======
[启用会战] 选择会战版本
[怎么拆日和] 竞技场查询
[pcr速查] 常用网址
[星乃来发十连] 转蛋模拟
[官漫286] 官方四格(日文)
[猜头像][猜角色] 小游戏
[.rd] roll点

[切噜一下+待加密文本]
▲切噜语转换
[来杯咖啡+反馈内容]
▲联系维护组

====== 被动技能 ======
pcr推特转发(日)
pcr台B服官网公告推送
pcr四格漫画(日)更新推送
pcr竞技场背刺时间提醒*
赛马娘推特转发*
URA9因子嗅探者*
萌系画师推特转发*
撤回终结者*
入群欢迎* & 退群通知
番剧字幕组更新推送*°
*: 默认关闭
°: 不支持自定义

====== 模块开关 ======
※限群管理/群主控制※
[lssv] 查看各模块开关状态
[启用+空格+service]
[禁用+空格+service]
 
=====================
※Hoshino开源Project：
github.com/Ice9Coffee/HoshinoBot
您对项目作者的支持与Star是本bot更新维护的动力
💰+⭐=❤
'''.strip()
# 魔改请保留 github.com/Ice9Coffee/HoshinoBot 项目地址

'''
TOP_MANUAL = '''
====================  Cola功能说明  ====================
======================  通用功能  ======================
发送[]内的关键词触发
[帮助通用] [娱乐帮助]       通用/娱乐功能说明

[竞技场帮助]       公主连结jjc排名检测

[gs帮助] [原神抽卡帮助]       通过原神UID查询账号信息和娱乐功能
▲部分功能(如抽卡记录,自动签到等)需先使用 扫码登陆 获取账号信息

[ba日历帮助] [ba抽卡帮助]       碧蓝档案活动日历查询与娱乐功能

[明日方舟帮助]       明日方舟 模拟抽卡和蹲饼插件

[cola搜图+图片] [搜番+图片]       以图搜图/搜番
▲局部图,清晰度太低的图,查询结果可能会不太准确

[ChatGPT帮助]       ChatGPT(默认关闭,请手动启用)

[角色语音模仿帮助]       角色配音插件,可生成语音

[抽卡] [sp抽卡帮助]       一种抽卡小程序,图片源自于用户上传

[猜群友] [猜单词] [帮助猜群友] [帮助猜单词]
▲群小游戏，可多名群友参与

[查成分 + B站用户名/UID]       查询这个人到底D了多少VTuber
▲只能查询开放了关注列表的用户,隐藏显示的无法查询

[网络天才帮助]       通过玩家的提示来猜测玩家所想的角色
▲此功能不能多人一起使用,请等待他人结束游戏后再开始游戏

[头像表情包] [头像表情包帮助]
▲整合的群友头像相关的表情包,可自己发送图片代替头像

[来点taffy帮助]       关注永雏塔菲谢谢喵

[@bot+骂我]       来自xcw的热烈关怀(

[sx(缩写)+内容]       能不能好好说话(查询拼音缩写意思)

[文章生成器帮助] [表情包生成器帮助]
▲整合的一些文章生成器/表情包生成器

[娶群友]       随机抓一群友当老婆

[运势] [今日运势帮助]
▲每天都来抽一签来看看自己今天运势怎么样吧！

[问题+翻看答案]       答案之书
▲愿一切无解都有解！解除你的迷惑，终结你的纠结！

[cola签到] [收集册] [签到帮助]      可爱的印章签到收集

[早安晚安帮助] [早上好] [晚安]
▲哦哈哟！哦呀斯密！(记录群友作息)

[微博/百度/知乎/贴吧热搜+数字] [热搜帮助]
▲获取网站热搜榜(不加数字默认前10位)

[塔罗牌]       塔罗牌抽签

[鉴定] [鉴定你+@xx]       鉴定群友是0是1

[来份色图]       此为AI绘图停用前生成图的本地缓存

[/remake]       人生重开模拟器

[今天吃什么]       推荐一些好吃的,选择困难症狂喜

[@bot][夸我|来点鸡汤|今日一言]
[@bot][跟我学]+内容 复读内容
▲制作的一些未归类小功能

[恶臭化+数字]       将任意数字以114514的格式呈现

[.rd] [掷骰子帮助]       简易骰娘，可用于roll点

[来点猫猫][来点狗狗][来点狐狸]
▲来点可爱猫/狗/狐图片

[猜头像] [猜角色]       pcr小游戏

[切噜一下+待加密文本] [已加密文本+切噜]
▲切噜语转换

[来杯咖啡+反馈内容]
▲联系维护组▲
================  当bot为管理员时可用  =================
[设置群名+新群名]       修改群名

[设置群公告+内容]       添加群公告

[设置名片+内容]       修改个人群名

[设置名片+@某人+内容]       修改某个人群名

[禁言+@某人+禁言时间(单位为分钟)]       例：禁言@xxx 10

[解禁+@某人]       解除禁言

[精致睡眠]       8小时精致睡眠

[来份昏睡红茶套餐]       叫一杯先辈特调红茶
======================  模块开关  ======================
※限群管理/群主控制※
[lssv] [功能列表] [服务列表]       查看各模块开关状态
[启用+空格+service] [禁用+空格+service]
▲手动启用/禁用lssv中的某个模块

[启用 ai] [调整AI概率] [0-50](未叫名称时回复概率)
▲此为AI对话插件,默认关闭需管理员手动启用 例:调整ai概率 0
▲默认的回复概率为0,听到自己名字bot必定回复

[RSS订阅帮助]       订阅B站up主动态，开播通知等功能

[启用 ChatGPT]       启用ChatGPT

[启用/禁用 bilibili视频解析]       使用较多单独列出
'''.strip()
# 魔改请保留 github.com/Ice-Cirno/HoshinoBot 项目地址
'''

def gen_service_manual(service: Service, gid: int):
    spit_line = '=' * max(0, 18 - len(service.name))
    manual = [f"|{'○' if service.check_enabled(gid) else '×'}| {service.name} {spit_line}"]
    if service.help:
        manual.append(service.help)
    return '\n'.join(manual)


def gen_bundle_manual(bundle_name, service_list, gid):
    manual = [bundle_name]
    service_list = sorted(service_list, key=lambda s: s.name)
    for s in service_list:
        if s.visible:
            manual.append(gen_service_manual(s, gid))
    return '\n'.join(manual)


@sv.on_prefix('help', '帮助')
@sv.on_suffix('help', '帮助')
async def send_help(bot, ev: CQEvent):
    gid = ev.group_id
    arg = ev.message.extract_plain_text().strip()
    bundles = Service.get_bundles()
    services = Service.get_loaded_services()
    if not arg:
        await bot.send(ev, utils.text_to_image(TOP_MANUAL))
    elif arg in bundles:
        msg = gen_bundle_manual(arg, bundles[arg], gid)
        await bot.send(ev, utils.text_to_image(msg))
    elif arg in services:
        s = services[arg]
        msg = gen_service_manual(s, gid)
        await bot.send(ev, utils.text_to_image(msg))
    # else: ignore
