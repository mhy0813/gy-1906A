#! /usr/bin/env python
# -*- coding: utf-8 -*-
#增
#创建
#字典的特点：字典中key是唯一的。
          #1.不允许同一个键出现两次，创建时如果同一个键被赋值两次，后一个值会被记住
          #2.key是不可以被改变的  数字，字符串，元组。
          #元组(1,2,3,5)可以 做 key，(1,2,3,5,[3])不可以 不包括list 列表

a={}
#字典新增一对数据
a['姓名'] = "马洪颍\(^o^)/~"
print(a)
#删
#删除某一对值，pop参数只能是key
#a.pop("姓名")
#del a["姓名"]
print(a)
# #清空字典
a.clear()
print(a)
#改
a['姓名'] = "比较快乐"
print(a)
#根据key 查找value
print(a['姓名'])
#遍历字典【借助循环】
for key in a:
    print(a[key])
#字典 合并
d={'性别':"女"}
f={"7990":'mhy'}
#把一个字典合并到另一个字典中
f.update(d)
print(f)
#两个字典合并，生成一个新字典
print(dict(d,**f))
print(f)
print(d)
#成员判断只能用（key）
if(4 in a):
    print('存在字典中')
else:
    print('不存在字典中')

#获取字典 长度
a=(len(a))
print(a)