# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 00:19:24 2019

@author: Talib
"""

def InsertionSort(a):
    for i in range(1,len(a)):
        key = a[i]
        j = i-1
        print(key,a[j])
        while(j>=0 and key<a[j]):
            print(j)
            a[j+1] = a[j]
            j-=1
        a[j+1] = key
        print(a)
    return a