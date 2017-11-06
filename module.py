# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 13:48:08 2017

@author: ekuilzh
"""

#!/usr/bin/env python3
# -*- coding:utf-8 -*-

' a test module '

__author__= 'kuilong zhang'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('hello, world!')
    elif len(args) == 2:
        print('hello, %s!' % args[1])
    else:
        print('too many arguments!')
        
if __name__ == '__main__':
    test()
    print(sys.argv)