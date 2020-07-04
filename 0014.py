'''
Created on 2020年6月26日

python练习册0014题：
纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：
{
    "1":["张三",150,120,100],
    "2":["李四",90,99,95],
    "3":["王五",60,66,68]
}
请将上述内容写到 student.xls 文件中  
txt文件内容 ---> xls文件中
'''
#__*__ coding = utf-8 __*__
import json
import xlwt
import os

os.chdir(r'D:\python-test\0014')

with open('student.txt','r',encoding='utf-8') as fp:
    data = fp.read()

#文本内容为标准json格式，可以直接加载到内存中   
json_data=json.loads(data)

'''
print (type(json_data))
print (json_data.items())
print (type(json_data.items()))# python3中dict.items()方法返回的是一个dict.items对象，而在python2中返回的是一个list对象
print (list(json_data.items()))
'''

#excel表项创建，单元格内容填充
workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('sheet',cell_overwrite_ok='true')

#循环写入
r=0
for key in json_data.keys():
    worksheet.write(r,0,key)
    j=1
    for value in json_data[key]:#取字典values时使用[ ],而不是（）
        worksheet.write(r,j,value)
        j+=1
    r+=1 

#保存文件
workbook.save('student.xls')
    



    

