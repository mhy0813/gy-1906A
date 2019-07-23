#! /usr/bin/env python
# -*- coding: utf-8 -*-

#列表和元祖的区别
#1、元组中只有一个数据的时候，后面必须带一个逗号，列表中就不用了
a=[1,5]
b=(1,)
print(a)
print(b)
#2、元组中的数据不可以修改
# b[1]=2
# print(b)
#元组合并
r=(5,6,7,8,9)
g=(1,2,3,4,)
print(r+g)
#截取
print(g[2])
print(g[0:4])
#获取长度
print(len(r))


