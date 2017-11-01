#!/usr/bin/python
# -*- coding:utf-8 -*-

shoplist = ['apple', 'orange', 'banana']
print(shoplist)
print(shoplist[0])
print(shoplist[1:3])
print(shoplist[1:-1])

shoplist.append('aaa')
print(shoplist)
print(shoplist[-1])

tuple = ('a', 'b', ['A', 'B'])
tuple[2][0] = 'X'
tuple[2][1] = 'Y'
#tuple[0] = 'Z' //元组的值是const的，所以不能修改，这和list有区别，list中的值是可以修改的
