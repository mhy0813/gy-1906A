#! /usr/bin/env python
# -*- coding: utf-8 -*-

print("hello world!!")

#代表变量名  =赋值符 表示把右边的值存在左边的变量中
#字符串有四种表示方法，"第一种方法"，  '第二种方法，'"第三种方法"'，""第四种方法""
a = """这是一个字符"""
#print() 在控制台打印，type()显示变量存的数据的类型
a =4555744
print(type(a))
b="佩奇"
print(type(b))
#[]表示list代表一个列表，可以存多个数据，多个数据中间","隔开
c = [1,2,5,4,7]
print(type(c))
#()表示tuple代表一个元组，可以存多个数据，多个数据中间","隔开
d = (74,79,877,995)
print(type(d))
#键值对数据类型，姓名：马洪颍，手机号：18516038970，爱好：折腾
#{}dict表示一个字典，可以储存多个键值对数据，多个键值对数据中间用","隔开，key和value中间用","隔开
e = {"姓名":"马洪颍","手机号":"18516038970","爱好":"折腾"}
print(type(e))
type(e)

#练习
#第一组数据：张三，李四，王五，赵六，钱七
#第二组数据：姓名：张三 年龄：18 性别：女 科目：语文 成绩：80
#第三组数据：A，2，3，4，5，6，7，8，9，J,Q,K
#第四组数据：10000
#第五组数据：学生

f = ["张三","李四","王五","赵六","钱七"]
print(f)
g = {"姓名":"张三","年龄":18,"性别":"女 ","科目":"语文 ","成绩":80}
print(g)
h = ("A",2,3,4,5,6,7,8,9,"J","Q","K")
print(h)
i = (10000)
print(i)
j = ("学生")
print(j)
#小明有20块钱，红双喜10块钱，玉溪25块钱，大前门5块钱   求出小明可以买那种烟  【练习逻辑运算符】
k = 20
if(k>=10):
    print(k,"元可以买红双喜")
if(k>=25):
    print(k,"元可以买玉溪")
if(k>=5):
    print(k,"元可以买大前门")







