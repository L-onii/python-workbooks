'''
Created on 2020年6月7日

python练习册0002题：
将生成的 200 个激活码保存到 MySQL 关系型数据库中。

'''
import pymysql
CREATE_STR = __import__('0001') #对于以数字开头的文件，直接使用import会出错


def insertto_mysql(codelist):
    db = pymysql.connect('192.168.74.128','root','123456')
    cursor = db.cursor()
    cursor.execute('CREATE DATABASE IF NOT EXISTS python')
    cursor.execute('USE python')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Activation_code(
                        id INT NOT NULL AUTO_INCREMENT,
                        code varchar(32) NOT NULL,
                        PRIMARY KEY(id))''')
    cursor.execute('truncate table Activation_code')# 同delete类似，删除表中的所有行，此处让主键重新从1开始自增
    for code in codelist:
        cursor.execute('INSERT INTO Activation_code(code) VALUES(%s)',(code))
        cursor.connection.commit()
        
    db.close()
    

if __name__ == '__main__':
    codelist = CREATE_STR.create_str(200,10)
    insertto_mysql(codelist)