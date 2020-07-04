'''
Created on 2020年7月4日

pythonl练习册0017题：
 将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中，如：
 <?xml version="1.0" encoding="UTF-8"?>
<root>
<students>
<!-- 
    学生信息表
    "id" : [名字, 数学, 语文, 英文]
-->
{
    "1" : ["张三", 150, 120, 100],
    "2" : ["李四", 90, 99, 95],
    "3" : ["王五", 60, 66, 68]
}
</students>
</root>
'''

#xls文件内容读取
import xlrd
import os
import json

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

os.chdir(r'D:\python-test')

def read_xls(path):
    #打开工作簿
    workbook = xlrd.open_workbook(path,encoding_override='utf-8')
    #获取其中的表项，可以通过表名（sheet_by_name）,索引（sheet_by_index）来获取
    worksheet = workbook.sheet_by_index(0)
    #获取sheet中的行数和列数
    rows = worksheet.nrows
    cols = worksheet.ncols
    #循环读取表项内容
    
    dict={}
    for i in range(rows):
        flag = worksheet.row_values(i)
        values = list()
        for j in range(1,cols):
            #单元格类型判断，数字改为整型***python读取Excel类型，0：empty，1：string，2：number，3：data，4：bool，5：error
            ctype = worksheet.cell(i,j).ctype
            if ctype == 2 and worksheet.cell_value(i,j) is not None:
                values.append(int(worksheet.cell_value(i,j)))
        dict[flag[0]] = values
    
    return dict
    

def write_xml(data):
    #创建一个元素    
    root = ET.Element('root')
    #root.tail = '\n'
    #创建root元素的子元素
    sub = ET.SubElement(root, 'students')
    #sub.tail = '\n'
    #将root元素指定为student_xml的根节点
    student_xml = ET.ElementTree(root)
    #注释
    comment = ET.Comment('学生信息表\n"id":[名字, 数学, 语文, 英文]')
    sub.append(comment)
    #sub元素的内容
    xml_data = json.dumps(data,ensure_ascii=False)
    print (xml_data)
    sub.text = xml_data
    
    student_xml.write('0017\\student.xml',encoding = 'utf-8')


if __name__ == '__main__':
    data = read_xls('0014\\student.xls')
    write_xml(data)