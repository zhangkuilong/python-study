#!/usr/bin/python
# -*- coding:utf-8 -*-

shoplist = ['apple', 'orange', 'banana']
print(shoplist)
print(shoplist[0])
print(shoplist[1:3])
print(shoplist[1:-1])

tuple = ('a', 'b', ['A', 'B'])
tuple[2][0] = 'X'
tuple[2][1] = 'Y'

print(tuple)

#input返回的类型为str
age = int(input("pls input the person's age: ")) 
if age >= 18:
    print("this person is adult")
elif age >= 6:
    print("this person is a teenager")
else:
    print("this person is a children")
    
#practice if...elif..else
height = 1.75
weight = 80.5
bmi = weight / height

if bmi < 18.5:
    print("too light")
elif bmi >= 18.5 and bmi < 25:
    print("normal")  
elif bmi >= 25 and bmi < 28:
    print("too fat")
elif bmi >= 28 and bmi < 32:
    print("fat")
else:
    print("severely obese")
    
names = ['Mr.zhang', 'Mrs.li', 'Teacher.zhang']
for name in names:
    print(name)
    
sum = 0
for x in range(101):
    sum += x
print(sum)

#字典
persons = ['k', 'l', 'm']
animals = ['n', 'o', 'p']
dic = {'z':persons, 'x':animals}
print(dic['z'][0])
d = 'z' in dic
print(d)
dic.pop('z')
print(dic)
g = dic.get('z', -1)
print(g)
person = ('a', 'b', 'z')
animal = ('x', 'y', 'z')
dic1 = {person:'kuilong', animal:'fei'}
dic1[person]

s = set([1,2,3,3])
print(len(s))
s.add(23)
print(len(s))

def sum(n):
    result = 0
    for x in range(n + 1):
        result += x*x
    return result

n = int(input("pls input the ingeger what you want: "))
mysum = sum(n)
print(mysum)

n1 = 100
n2 = str(hex(n1))
print(len(n2))
n3 = n2.index('x')
print(n3)

import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx,ny

r = move(100, 100, 60, math.pi / 6)
print(r)

def quadratic(a, b, c):
    x1 = (-b + math.sqrt(b *b - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b *b - 4 * a * c)) / (2 * a)
    return x1, x2

test = quadratic(2, 5, 1)
print(test)

#默认参数
def print_info(name, age, city = '成都', street = '人民路'):
    print('姓名', '      年龄', '  所在城市', '  具体街道')
    print(name, age, city, street)
    
print_info('zhangsan', 14)

#可变参数， 用*代表
def calc(*numbers):
    s = 0
    for n in numbers:
        print('n = %d' % n)
        s = s + n * n 
    print('s = %d' % s)
    return s

calc(1,2,3,4,5,6)

arr = [23, 2, 12]
calc(*arr)
calc()


#关键字参数，用**代表
def creatial(name, age, **kw):
    print('my name is ', name, 'and my age is ', age, 'other info are: ', kw)
    return kw
    
vva = creatial('zhangkuilong', 23, city = 'chengdu', school = 'uestc')
if 'uestc' == vva['school'] and 'chengdu' == vva['city']:
    print('this is true, that uestc in chengdu')
    
extra = {'city': 'Beijing', 'job': 'Engineer'}
creatial('feili', 27, **extra)

def person(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name', name, 'age', age, 'other', kw)
    
person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)

def per(name, age, *args, city, job):
    print(name, age, city, job)
    
per('zhag', 23, city = 'chengdu', job = 'it')


#参数组合
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
    
f1(12,23,222, 'a', 'b')
f1(2, 3, args = {'a':'b'}, kw = {13:'sdfsdf'})
f2(12, 23, d = 12, city = {'a':'sdfsdf'})