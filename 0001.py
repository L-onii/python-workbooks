'''
Created on 2020年6月1日

python练习册0001题：
使用 Python 如何生成 200 个激活码。
'''

# random方法
import random
import string

def create_str(num,long):
    #使用str中的字符生成随机激活码
    str = string.ascii_letters + string.digits
    #print (str)
    #随机字符生成
    b = []
    for i in range(num):#激活码数目
        a= ''
        for j in range(long):#随机激活码
            a +=random.choice(str)#从一个非空序列中随机选择
        #a = random.choices(str,k=long)  choices用来生成一个k个字符的随机列表。
        b.append(a)
    return b

if __name__ == '__main__':
    str = create_str(200, 10)
    print (str)

'''
uuid1()——基于时间戳
由MAC地址、当前时间戳、随机数生成。可以保证全球范围内的唯一性，但MAC的使用同时带来安全性问题，局域网中可以使用IP来代替MAC。
uuid2()——基于分布式计算环境DCE（Python中没有这个函数）
算法与uuid1相同，不同的是把时间戳的前4位置换为POSIX的UID，实际中很少用到该方法。
uuid3()——基于名字的MD5散列值
通过计算名字和命名空间的MD5散列值得到，保证了同一命名空间中不同名字的唯一性，和不同命名空间的唯一性，但同一命名空间的同一名字生成相同的uuid。
uuid4()——基于随机数
由伪随机数得到，有一定的重复概率，该概率可以计算出来。
uuid5()——基于名字的SHA-1散列值
算法与uuid3相同，不同的是使用 Secure Hash Algorithm 1 算法


#uuid
import uuid
for i in range(2):
    print (uuid.uuid1())
'''
       
    
    
    

