'''
Created on 2020年6月24日

python练习册0013题：
用 Python 写一个爬图片的程序，爬 这个链接里的日本妹子图片 :-)[http://tieba.baidu.com/p/2166231880]
'''
import requests
from bs4 import BeautifulSoup
import os 

os.chdir(r'D:\python-test\0013')

#获取网页内容
data = requests.get('http://tieba.baidu.com/p/2166231880').text
#将网页内容转换为Beautifulsoup对象,使用lxml解析器,速度快，容错能力强，python标准库的解析器为html解析器，html.parse
data_soup = BeautifulSoup(data,features='lxml')


for count,i in enumerate(data_soup.select('img.BDE_Image')):#选择属性为BDE_Image的img标签
    img = requests.get(i['src'])#对图片的源地址进行请求
    with open('%04d.jpg' %  count,'wb') as f:
        f.write(img.content)







