'''
Created on 2020年6月1日

python练习册0000题：
将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。

'''


from PIL import Image,ImageFont,ImageColor,ImageDraw

def add_num(img,num):
    #将img生成draw对象
    draw=ImageDraw.Draw(img)
    #定义使用的字体和大小
    draw_font=ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', size=60)
    #定义使用的颜色
    draw_color=ImageColor.colormap.get('red')
    #获取图片的长度和宽度
    wide,height=img.size
    #将数字写入对象中
    draw.text((wide-40,0), num, fill=draw_color, font=draw_font)
    #保存图片
    img.save(r'D:\python-test\0000\0001.jpg')
    
if __name__=='__main__':
    #打开图片
    image=Image.open(r'D:\python-test\0000\0000.jpg')
    #定义数字
    num='2'
    #执行添加数字操作
    add_num(image, num)
    
