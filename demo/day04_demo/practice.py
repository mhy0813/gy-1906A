#! /usr/bin/env python
# -*- coding: utf-8 -*-


# '''
# 按照扑克牌的规则，现在有6张牌，只要5张
# 黑桃（S）红桃（H）方块（D）梅花（C）
# 牌：2.3.4.5.6.7.8.9.10.J.Q.K.A
# 数据库存的是下面格式的数据，写脚本验证满足3带2的牌型
# [''D1'' , ''H1'' , ''H10'' , ''H7'' , ''S1'' , ''S7'']
# ["C9" , "D6" , "D9" , "H13" , "H9" , "S7"]
# ["C2" , "D13" , "D2" , "H2" , "H9" , "S13"]
# '''
# a = '''[''D1'' , ''H1'' , ''H10'' , ''H7'' , ''S1'' , ''S7'']'''
# #字符串的替换
# a = a.replace("''",'"')
# #字符串截取
# a = a[2:-2]
#
# print(a)
#
# #字符串的切片方法
#
# b = a.split('" , "')
#
# print(b)
#
# #key 唯一；并且存一对数据
# #key存牌的大小，value存key出现的次数
# #{'1':3,"10":1,"7":2}
# s={}
# for i in b:
#     c=i[1:]
#     if(c in s):
#         s[c] +=1
#     else:
#         s[c]=1
#print(s)
def juge_3_2(s):
    # 第一步：统一符号  对字符串的处理，用replace（）[''D1'' , ''H1'' , ''H10'' , ''H7'' , ''S1'' , ''S7'']

    s=s.replace("''",'"')
    # print(s)
    # 第二步：去掉中括号 字符串截取  [::]
    s=s[2:-2]
    # print(s)
    # 第三步：变成list  字符串切片  .split（） 新建一个list变量
    x=s.split('''" , "''')
    # print(x)
    # 第四步：取出后面的数字  循环遍历取出list里面的每个值，对这个值进行截取
    r={}
    for o in x:
        y=o[1:]
    # 第五步：统计相同的数字个数  用字典去统计
        if(y in r):
            r[y] +=1
        else:
            r[y]=1
    # print(r)
    # 第六步：判断数据中有没有同时存在三个相同数字和两个相同数字  if判断
    v1=0 # 如果key对应的数值有3的 v1 = 1，如果没有则为0
    v2=0 # 如果key对应的数值有2的 v2 = 1，如果没有则为0
    for key in r:
        if(r[key]==3):
            v1=1
        if(r[key]==2):
            v2=1
    if(v1==1 and v2==1):
        print('3带2')
    else:
        print('就不是3带2')
with open('D:\\softwareData\\python\\mhy7\\17\\demo\\day04_demo\\caids.txt',"r") as f:
    a= f.readlines()
    for li in a:
        li=li.replace('\n',"")
        print(li)
        juge_3_2(li)





