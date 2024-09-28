# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 12:13:21 2024

@author: tran9
"""
#bai40
n=int(input("nhap vao he so N:"))
s=0
while n<=0:
    n=int(input("nhap lai he so N:"))
for i in range(1,n+1):
    s+=1/(2*n)
print("kqua",s)
