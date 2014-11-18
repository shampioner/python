#-*- coding:utf-8 -*-
#author:shampioner,XDU

def myAlign(string,length=0):
    if length == 0:
        return string
    slen = len(string)
    re = string
    if isinstance(string,str):
        placeholder = ''
    else:
        placeholder = u''
    while slen < length:
        re += placeholder
        slen += 1
    return re

str1 = u'我是个短句子'
str2 = u'我是个很长很长很长很长很长很长的句子'
print (myAlign(str1,30) + myAlign(str2,20))
print (myAlign(str2,30) + myAlign(str1,20))
