'''
Created on 2020年6月28日

python练习册0015题：
纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：
[
    [1, 82, 65535], 
    [20, 90, 13],
    [26, 809, 1024]
]
请将上述内容写到 numbers.xls 文件中
'''

import json
import xlwt
import os


os.chdir(r'D:\python-test\0016')

with open('numbers.txt','r') as fp:
    data = fp.read()
#    print (data)
data_json_list = json.loads(data)

workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('sheet',cell_overwrite_ok = 'true')

 
#range函数注意（0,2）的范围是0和1，不包括2
for row in range(3):
    for col in range(3):
        worksheet.write(row,col,data_json_list[row][col])

#save报错permissdenied，可能是excel文件打开没有关闭       
workbook.save('numbers.xls')
    