import re
import math
import random



from hoshino import Service, priv, util
from hoshino.typing import CQEvent

sv = Service('精致睡眠', help_='''
[精致睡眠] 8小时精致睡眠(bot需具有群管理权限)
[来份昏睡红茶套餐] 叫一杯先辈特调红茶(bot需具有群管理权限)
'''.strip())

@sv.on_fullmatch('睡眠套餐', '休眠套餐', '精致睡眠', '来一份精致睡眠套餐')
async def sleep_8h(bot, ev):
    gid = ev.group_id
    sid = ev.self_id
    owner = await bot.get_group_member_info(user_id=sid, group_id=gid)
    role = owner['role']
    if role == 'member':
        await bot.send(ev, '不许睡，起来加班')
        return
    try:
        await util.silence(ev, 8*60*60, skip_su=False)
        await bot.send(ev, '好的睡眠是一切好的开始,祝你好梦,晚安~')
    except Exception as ex:
        sv.logger.error(ex)
        # await bot.send(event, '禁言...禁言它失败了')


@sv.on_rex(r'(来|來)(.*(份|个)(.*)(睡|茶)(.*))套餐')
async def sleep(bot, ev: CQEvent):
    gid = ev.group_id
    sid = ev.self_id
    owner = await bot.get_group_member_info(user_id=sid, group_id=gid)
    role = owner['role']
    if role == 'member':
        await bot.send(ev, '咱的沏茶手艺还不是很好，等咱考上茶艺师了再来吧')
        return
    try:
        base = 0 if '午' in ev.plain_text else 5*60*60
        length = len(ev.plain_text)
        sleep_time = base + round(math.sqrt(length) * 60 * 30 + 60 * random.randint(-15, 15))
        await util.silence(ev, sleep_time, skip_su=False)
        await bot.send(ev, '香啊，很香啊（指红茶）')
    except Exception as ex:
        sv.logger.error(ex)
        # await bot.send(event, '禁言...禁言它失败了')
