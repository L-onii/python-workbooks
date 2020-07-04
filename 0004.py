'''
Created on 2020年6月9日

python练习册0003题：
任一个英文的纯文本文件，统计其中的单词出现的个数
'''
# _*_ coding:utf-8 _*_

import os
import re
from collections import Counter

print ('当前工作目录:')
print (os.getcwd())
os.chdir(r'D:\python-test\0004')
print ('查询文件所在目录:')
print (os.getcwd())
print ('**************************************')


def Get_Word(File):
    with open(File) as fp:
        Data = fp.read()        
        #替换掉文件中非字母和数字的字符，并去掉开始和结尾的多余空格
        #Data = Data.replace('{^a-zA-Z0-9}',' ')  replace方法似乎不能使用正则表达式进行替换
        Data = re.sub('[^a-zA-Z0-9]+',' ',Data).strip()
        #print (Data)
        New_Data = re.split(' ',Data)
        
    #print (New_Data)
    #遍历字符串中的单词，将其出现次数加入字典
    Word_Counter = {}   
    for i in New_Data:
        if i not in Word_Counter:
            Word_Counter[i]=1
        else:
            Word_Counter[i]+=1
    
    #print (Word_Counter)
    print ('文档中单词出现次数为:')       
    for key,value in Word_Counter.items():
        print ((key+':').rjust(15),value)


if __name__ == '__main__':
    Get_Word('test.txt')