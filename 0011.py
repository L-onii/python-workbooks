'''
Created on 2020年6月16日

python练习册0011题：
敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

北京
程序员
公务员
领导
牛比
牛逼
你娘
你妈
love
sex
jiangge


'''
'''
import os
import sys

class Str_Parse():
    def __init__(self,input_str):
        self.input_str = input_str
        
    def Str_Check(self):
        os.chdir(r'D:\python-test\0011')
        with open('filtered_words.txt',encoding='utf-8') as fp: #打开文件方式设置为utf-8
            words = fp.read().split('\n')
            for i in words:
                if i in self.input_str:
                    print ('Freedom')
                    break
            else:
                print ('Human Rights')
                
    def Str_replace(self):
        os.chdir(r'D:\python-test\0011')
        flag = '*'
        new_str = self.input_str
        with open('filtered_words.txt',encoding='utf-8') as fp: 
            words = fp.read().split('\n')
            for i in words:
                if i in self.input_str:
                    new_str = self.input_str.replace(i,flag*len(i))
            print (new_str)


if __name__ == '__main__':
    while (1):        
        str = input('please input the words:')
        Str_parse = Str_Parse(str)
        if str == '0':
            sys.exit(0)
        else:
            Str_parse.Str_replace()
'''

import os

word_filter=set()
os.chdir(r'D:\python-test\0011')
with open('filtered_words.txt',encoding='utf-8') as f:
    for w in f.readlines():
        word_filter.add(w.strip())

while True:
    s=input()
    if s == 'exit':
        break
    for w in word_filter:
        if w in s:
            s= s.replace(w,'*'*len(w))
    print(s)        
