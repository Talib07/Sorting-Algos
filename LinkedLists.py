# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 13:14:20 2019

@author: Talib
"""

class node:
    def __init__(self,names):
        self.names = names
        self.next = None
        
class initiallinker:
    def __init__(self):
        self.head = None
        
    def Printlist(self):
        nameval = self.head
        while nameval is not None:
            print(nameval.names)
            nameval = nameval.next
            
    # Insertion at  beginning
    def insertbeg(self,newdata):
        NewNode = node(newdata)
        #Update
        NewNode.next = self.head
        self.head = NewNode
    
    #Insertion at end
    def insertend(self,newdata):
        NewNode = node(newdata)
        #update
        if self.head is None:
            self.head = NewNode
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = NewNode
    
    #insert anywhere    
    def insertany(self,newdata,place):
        if place is None:
            print("No such place to insert")
        else:
            NewNode = node(newdata)
        #update
            NewNode.next = place.next
            place.next = NewNode
            
    def delete(self,key):
        Headval = self.head
        if Headval is not None:
            if(Headval.names == key):
                self.head = Headval.next
                Headval = None
                return 
        while(Headval is not None):
            if Headval.names == key:
                    break
            prev = Headval
            Headval = Headval.next
                
        if (Headval == None):
            return 
        prev.next = Headval.next
        Headval = None
        
    
                
            
        
ob1 = initiallinker()
ob1.head = node("Mon")
ob2 = node("Tue")
ob3 = node("Wed")
'''ob4 = node("Thur")
ob5 = node("Fri")'''

ob1.head.next = ob2
ob2.next = ob3

ob1.insertbeg("Sun")
ob1.insertend("Sat")