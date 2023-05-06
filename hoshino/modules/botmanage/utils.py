import base64
from pathlib import Path
from io import BytesIO
from PIL import Image, ImageFont, ImageDraw
from base64 import b64decode, b64encode


fontpath = Path(__file__).parent / "fonts" / "SourceHanSansCN-Medium.otf" # 字体文件的路径


def pic2b64(pic: Image) -> str:
    '''
    图片转base64
    '''
    buf = BytesIO()
    pic.save(buf, format='JPEG', quality=90)
    base64_str = base64.b64encode(buf.getvalue()).decode()
    return 'base64://' + base64_str

def pic2cq(pic: str):
    """
    图片转CQ码
    pic: base64编码的图片
    """
    return f"[CQ:image,file={pic}]"

def text_to_image(text: str) -> Image.Image:
    font = ImageFont.truetype(str(fontpath), 24) # Path是路径对象，必须转为str之后ImageFont才能读取
    padding = 10
    margin = 4
    text_list = text.split('\n')
    max_width = 0
    for text in text_list:
        w, h = font.getsize(text)
        max_width = max(max_width, w)
    wa = max_width + padding * 2
    ha = h * len(text_list) + margin * (len(text_list) - 1) + padding * 2
    i = Image.new('RGB', (wa, ha), color=(255, 255, 255))
    draw = ImageDraw.Draw(i)
    for j in range(len(text_list)):
        text = text_list[j]
        draw.text((padding, padding + j * (margin + h)), text, font=font, fill=(0, 0, 0))
    return pic2cq(pic2b64(i)) # 图片转base64并转cq码
