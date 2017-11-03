# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 16:03:05 2017

@author: ekuilzh
"""

def add(x, y, f):
    result = f(x) + f(y)
    print("result = %d" % result)
    return result
    
add(2,3,abs)

def f(x):
    return x + x
    
#map, reduce的使用
r = map(f, ['abc', 'cdf', 'wewe'])
s = list(r)
print(s)

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def fn(x, y):
    return x * 10 + y

from functools import reduce
a = reduce(fn, map(char2num, '13579'))
print(a)

def normalize(name):
    return str.title(name)
L1=['adm','LISA','barT']
L2=list(map(normalize,L1))
print(L2)

def fun(s):
    r1 = s[1:2].upper()
    r2 = s[2:].lower()
    return r1 + r2

L = ['AbbbCdE', 'bbbbCCCDDDD', 'bDSfFSsdffFSD']
s = list(map(fun, L))
print(s)

def cheng(x, y):
    return x * y

L = [1,2,3,4]
S = reduce(cheng, L)
print(S)

def str2float(s):
    r = s.index('.')
    r1 = s[0:r]
    r2 = s[r + 1:]
    r1, r2
    
    print(r1, r2)
    z3 = list(map(char2num, r1))
    z4 = list(map(char2num, r2))

    def fn(x, y):
        return x * 10 + y

    w1 = reduce(fn, map(char2num, r1))
    w2 = reduce(fn, map(char2num, r2))
    w3 = w1 + w2 / (10 ** len(r2))
    print(w3)
    
str2float('123123.23422')
str2float('1111111111.232323211')

#filter函数的使用
def is_odd(n):
    return n % 2 == 1

s = list(filter(is_odd, [1,2,3,4,5,6]))
print(s)
t = list(map(is_odd, [1,2,3,4,5,6]))
print(t)

#sorted函数的用法
s = sorted([12, 23, -91, 3434], key = abs)
print(s)
z = sorted(['AAZsdf', 'Zada', 'Zbcc', 'abc'], key = str.lower, reverse=True)#按照ASCII的大小比较
print(z)

#使用sorted排序， 例子为按照L中的名字逆序排列
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(L[0][0])
def by_name(t):
    return t[0]
    
print(sorted(L, key = by_name, reverse = True))

if __name__ == '__main__':
    str2float('123123.234')
    print('zhangkuilong')

