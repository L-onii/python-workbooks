'''
Created on 2020年6月13日

python练习册0005题：
你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
'''
#1.遍历目录
#2.修改图片的尺寸为不大于1136*640，等比例压缩

import os
from PIL import Image

os.getcwd()
os.chdir(r'D:\python-test\0005')
print ('**********开始进行图片修改**********')

def resize(image,set_width,set_height):
    img = Image.open(image)
    width,height = img.size
    
    if width >= set_width or height >= set_height:
        #计算需要伸缩的比例
        scale_width = width / set_width
        scale_height = height / set_height
        #以宽度和高度的伸缩比例中大的为准
        Change_scale = max(scale_width,scale_height)
        #伸缩后的宽度和高度
        New_width = int(width / Change_scale)
        New_height = int(height / Change_scale)
        #修改图片
        img = img.resize((New_width,New_height),Image.ANTIALIAS) #暂时没搞清楚为什么输入size为非int类型会报类型错误
        img.save(image)
        print ('Successfully resized %s.' % image)
    else:
        print ('There is no need to resize %s.' % image)
        
def main(width,height):
    for i in os.listdir():
        try:
            resize(i,width,height)
        except IOError:
            print ('%s is not supported to make the change.' % i)
        

if __name__ == '__main__':
    main(1136,640)