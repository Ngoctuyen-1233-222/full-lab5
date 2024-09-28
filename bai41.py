# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 12:15:37 2024

@author: tran9
"""

#bai41
n=int(input("nhap vao so nguyen N:"))
s=0
while n<=0:
    n=int(input("nhap lai so nguyen N:"))
for i in range(0,n+1):
    s+=1/(2*i+1)
print("kqua",s)