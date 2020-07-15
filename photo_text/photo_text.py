# -*- coding: utf-8 -*-
# @Time    : 22020/6/25 18:22
# @Author  : Seventy
# @Site    : 将图片用文字渲染出来
# @File    : photo_text.py
# @Software: PyCharm

from PIL import Image, ImageDraw, ImageFont

# 文字大小
font_size = 12
# 文字内容
text_msg = "我喜欢你"
# 图片路径
img_path = "./photo.jpg"
# 字体文件
text_type = "./站酷快乐体2016修订版.ttf"
# 图片保存路径
img_save = "./save.jpeg"

# 使用 pillow.Image 读取图像
img_raw = Image.open(img_path)
# 使用 load 函数获取到每一个像素值
img_array = img_raw.load()

# 新建画布，并选好要使用的字体和字体大小
img_new = Image.new("RGB", img_raw.size, (0, 0, 0))
draw = ImageDraw.Draw(img_new)
font = ImageFont.truetype(text_type, font_size)


# 循环文字内容
def character_generator(text):
    while True:
        for i in range(len(text)):
            yield text[i]


ch_gen = character_generator(text_msg)

# 给字加上相应的颜色，写入新创建的画布中
for y in range(0, img_raw.size[1], font_size):
    for x in range(0, img_raw.size[0], font_size):
        draw.text((x, y), next(ch_gen), font=font, fill=img_array[x, y], direction=None)

# 保存成品
img_new.convert("RGB").save(img_save)
