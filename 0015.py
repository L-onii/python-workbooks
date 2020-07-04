'''
Created on 2020年6月28日

python练习册0015题：
纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：
{
    "1" : "上海",
    "2" : "北京",
    "3" : "成都"
}
请将上述内容写到 city.xls 文件中，
'''
import json
import os
import xlwt

os.chdir(r'D:\python-test\0015')
with open('city.txt','r',encoding='utf-8') as fp:
    data = fp.read()
#    print (data)
    
data_json = json.loads(data)

#print (data_json)
#print (type(data_json))

workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('sheet', cell_overwrite_ok='true')

row=0
for key in data_json.keys():
    worksheet.write(row,0,key)
    worksheet.write(row,1,data_json[key])
    row+=1

workbook.save('city.xls')