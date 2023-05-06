"""这是一份实例配置文件

将其修改为你需要的配置，并将文件夹config_example重命名为config
"""

# hoshino监听的端口与ip
PORT = 8080
HOST = '127.0.0.1'          # 本地部署使用此条配置（QQ客户端和bot端运行在同一台计算机）
# HOST = '0.0.0.0'          # 开放公网访问使用此条配置（不安全）

DEBUG = False               # 调试模式

BLACK_LIST = [1974906693]   # 黑名单，权限为 BLACK = -999
WHITE_LIST = []             # 白名单，权限为 WHITE = 51
SUPERUSERS = [10000]        # 填写超级用户的QQ号，可填多个用半角逗号","隔开，权限为 SUPERUSER = 999
NICKNAME = ''               # 机器人的昵称。呼叫昵称等同于@bot，可用元组配置多个昵称

COMMAND_START = {''}        # 命令前缀（空字符串匹配任何消息）
COMMAND_SEP = set()         # 命令分隔符（hoshino不需要该特性，保持为set()即可）

# 发送图片的协议
# 可选 http, file, base64
# 当QQ客户端与bot端不在同一台计算机时，可用http协议
RES_PROTOCOL = 'file'
# 资源库文件夹，需可读可写，windows下注意反斜杠转义
RES_DIR = r'./res/'
# 使用http协议时需填写，原则上该url应指向RES_DIR目录
RES_URL = 'http://127.0.0.1:5000/static/'

# B站视频解析配置
analysis_blacklist = [] # 不解析里面填写的QQ号发的链接 List[int]
analysis_display_image = True # 是否显示封面 True/False


# 启用的模块
# 初次尝试部署时请先保持默认
# 如欲启用新模块，请认真阅读部署说明，逐个启用逐个配置
# 切忌一次性开启多个
MODULES_ON = {
    'botmanage',
    'dice',
    'groupmaster',
    # 'hourcall',
    # 'kancolle',
    # 'mikan',
    'pcrclanbattle',    # 禁用
    'priconne',
    # 'setu',   # 未禁用
    # 'translate',
    # 'twitter',
    'picfinder',    # 官方整合的picfinder_take
    # 以下为自添加插件
    # 'picfinder_take',   # https://github.com/pcrbot/picfinder_take 官方已整合，弃用
    'groupguess',   # https://github.com/BeiYazi0/groupguess
    'huannai_plugin_fortune',   # https://github.com/SonderXiaoming/huannai_plugin_fortune
    'yaowoyizhi',   # https://github.com/watermellye/yaowoyizhi/
    'whattoeat',    # https://github.com/A-kirami/whattoeat
    'generator',
    'dailywife',    # https://github.com/SonderXiaoming/dailywife
    'headimg_generator',    # https://github.com/pcrbot/cappuccilo_plugins/tree/master/generator
    'pcrjjc_huannai',   # https://github.com/SonderXiaoming/pcrjjc_huannai
    'good_morning',     # https://github.com/azmiao/good_morning
    'ai',   # https://github.com/joeyHXD/ai
    'lifeRestart_bot',      # https://github.com/DaiShengSheng/lifeRestart_bot
    'image_generator',      # https://github.com/BlueDeer233/image_generator
    'Wordle4Hoshino',   # https://github.com/kokoro-ele/Wordle4Hoshino
    'groupchat',    # https://github.com/zangxx66/HoshinoBot-xcwRecord/tree/master/groupchat
    'draw-card',    # https://github.com/BeiYazi0/draw-card
    'tarot',    # https://github.com/haha114514/tarot_hoshino
    'login_bonus',  # https://github.com/SonderXiaoming/login_bonus
    'homo',     # https://github.com/SonderXiaoming/homo
    'determine',    # https://github.com/pcrbot/determine
    'RSS',  # https://github.com/pcrbot/RSS
    'youzi_voice',  # https://github.com/SonderXiaoming/youzi_voice
    'aichat-chatGPT',   # https://github.com/Cosmos01/aichat-chatGPT
    'traceanime',   # https://github.com/pcrbot/determine
    'custom',   # https://github.com/mengshouer/HoshinoBot-Plugins/tree/master/custom
    'resou',    # https://github.com/BeiYazi0/resou
    'GenshinUID',   # https://github.com/KimigaiiWuyi/GenshinUID
    'genshin-gacha',    # https://github.com/H-K-Y/Genshin_Impact_bot/tree/main/gacha
    'Blue_Archive_HoshinoBot',      # https://github.com/Cosmos01/Blue_Archive_HoshinoBot
    'akgacha',      # https://github.com/xulai1001/akgacha
    'akinator',     # https://github.com/Rinco304/akinator
    'hoshinobot-plugin-ddcheck',    # https://github.com/Rinco304/hoshinobot-plugin-ddcheck
    'answersbook',      # https://github.com/A-kirami/answersbook
    'image_lssv'    # https://github.com/RSRH-Rs/image_lssv
}
