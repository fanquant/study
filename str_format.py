# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 14:22:24 2017

@author: fanl
"""
age=20
name='Swaroop'
print('{0} was {1} years old when he wrote this book'.format(name,age))
print('Why is {0} playing with that python?'.format(name))
print(name+' was '+str(age)+' years old when he wrote this book')
print('{} was {} years old when he wrote this book?'.format(name,age))
print('Why is {} playing with that python?'.format(name))
print('{0:.4f}'.format(2/3))
print ('{0:_^11}'.format('hello'))
print('{name} wrote {book}'.format(name='Bob',book='A Byte of Python'))
print('a',end='')
print('b')
print(" what's your name?")
print('what\'s your name?')
print('This is the first line\nThis is the second line')
print("This is the first sentence.\
      This is the second sentence.")
print(r"Newlines are indicated by \n")#加r后，就不对后面的字符串进行转义
