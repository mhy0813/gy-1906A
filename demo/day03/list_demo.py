#! /usr/bin/env python
# -*- coding: utf-8 -*-

#增
#创建
a = []
#列表最后新增单个值
a.append(6)
a.append(9)
a.append('dbfjsdbfvjs')
print(a)
#合并
b = [5,8,7,'4554hjkhjk']
#使用两表合并生成一个新的列表
print(a+b)
print(a)
#使用extend合并两个表格生成新的列表
a.append(b)
print(a)
# #删
# #根据列表下标删除某个元素
a.pop(1)
print(a)
# #默认删除列表中的最后一个元素
a.pop()
print(a)
# #清空一个列表1
# a = []
# print(a)
# #清空一个列表2
# a.clear()
# print(a)
#改
#根据下标修改某个元素的值
a[1]=999
print(a)
#等价
a[0],a[1]='ghgasgdasbglj',787947564
print(a)
#查
#根据下标查询某个元素
print(a[1])
print(a[0])
#根据遍历（借助循环）
for i in a:
    print(i)
#截取
#截取部分数据
print(a[0:1])
#倒序
print(a[::-1])
#步长 元素隔一个显示出来
print(a[2::])
#长度
print(len(a))
#成员判断
if(4 in a):
    print('存在列表中')
else:
    print('不存在列表中')

