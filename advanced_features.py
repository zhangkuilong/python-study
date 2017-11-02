#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 14:35:30 2017

@author: ekuilzh
"""

#高级特性
#1.切片
l = list(range(101))
print(l)
print()
print(l[0:12])
print(l[:10])#前10个数
print(l[-10:])#后10个数
print(l[:10:2])#对于前10个数，每2个取一次
print(l[1:12:2])
print(l[::5])#所有数，每5个取一次

#迭代
d = {'a':'1', 'b':'2', 'c':'3'}
for key in d:
    print(key)
for value in d.values():
    print(value)
for k, v in d.items():
    print(k, '=', v)
    
dic = [k + '=' + v for k,v in d.items()]
print(dic)

#列表生成式
L = []
for x in range(10):
    L.append(x * x)
print(L)

print([x * x for x in range(10) if x % 2 == 0] )
print([m + n for m in 'ABC' for n in 'XYZ'])

import os
vars = [d for d in os.listdir('.')]
for var in vars:
    print('./' + var)
    
L = ['Hello', 'World', 'IBM', 'Apple']
v = [s.upper() for s in L]
print(v)

#practice
L = ['Apple', 'oraNGE', 18, 'Hello', None]
print([s.lower() for s in L if isinstance(s, str)])


#生成器
g = (x * x for x in range(10))
for n in g:
    print('n = %d' % n)
    
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib(8)
for n in f:
    print(n)

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5
    
o = odd()
print(o)
for n in o:
    print(n)
    
#迭代器
from collections import Iterable
b = isinstance([], Iterable)
print(b)
g = isinstance((x for x in range(10)), Iterable)#生成器也是可以迭代的
print(g)
    
