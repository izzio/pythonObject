## 原理

每一张图片都是由一个一个的像素点所组成的，而每个像素点都有自己的颜色，其颜色可以用一个数组表示：`(a, b, c)`，其中每位数的取值范围都是0-255

比如`(0, 0, 0)`代表白色，`(255，255，255)`代表黑色

当像素点足够多的时候，就形成了一张图片

只要每个元素取出一个像素值，并使用这个像素做为该字的颜色即可，在像素量够多的情况下，从远处看，是能看到原来图像的轮廓的

## 开始实现

首先使用 `pillow.Image` 读取图像，并使用`load`函数获取到每一个像素值

```python
img_raw = Image.open(img_path)
img_array = img_raw.load()
```

然后新建一张画布，并选好使用的字体和字体大小

```python
img_new = Image.new("RGB", img_raw.size, (0, 0, 0))
draw = ImageDraw.Draw(img_new)
font = ImageFont.truetype(text_type, font_size)
```

由于需要不断的循环文字，所以这里使用while循环yield来实现一个生成器

```python
def character_generator(text):
    while True:
        for i in range(len(text)):
            yield text[i]
```

最后给这些字加上相应的颜色，写入新创建的画布中

```python
for y in range(0, img_raw.size[1], font_size):
    for x in range(0, img_raw.size[0], font_size):
        draw.text((x, y), next(ch_gen), font=font, fill=img_array[x, y], direction=None)
```

最后将成品保存

```python
img_new.convert("RGB").save(img_save)
```



原图：

![photo](https://cdn.jsdelivr.net/gh/izzio/picbed@master/uPic/photo.jpg)

效果图

![save](https://cdn.jsdelivr.net/gh/izzio/picbed@master/uPic/save.jpeg)