# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 23:24:28 2019

@author: Talib
"""

def BubbleSort(a):
    n = len(a)
    x = 0
    for i in range(0,n-x):
        for i in range(1,n):
            if(a[i-1]>a[i]):
                print(swap(a,i-1,i))
        x+=1
    return a
            
            
def swap(a,x,y):
    a[x],a[y] = a[y],a[x]
    return a            