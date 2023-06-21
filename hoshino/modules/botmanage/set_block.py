import hoshino
import re
from datetime import timedelta
from hoshino import Service, priv
from hoshino.typing import CQEvent

sv = Service('设置拉黑', visible=False)

@sv.on_prefix('拉黑')
async def set_block(bot, ev: CQEvent):
    if not priv.check_priv(ev, priv.SUPERUSER):
        return
    try:
        content = ev.message.extract_plain_text().strip()
        match = re.match(r'(\d+)\s+(.+)', content)
        if match:
            user_id = match.group(1)
            hour = match.group(2)
        else:
            # await bot.send(ev, "输入格式不正确，QQ号与封禁类型之间使用空格分隔,qq号后跟上要拉黑的时间(单位为小时)")
            return
    except Exception as e:
        # await bot.send(ev, '出现异常' + str(e))
        print(e)
    else:
        hoshino.priv.set_block_user(int(user_id), timedelta(hours=int(hour)))
        await bot.send(ev,f"拉黑 {user_id} 成功，拉黑时间为{hour}小时")
