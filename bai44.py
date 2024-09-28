# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 12:30:56 2024

@author: tran9
"""

#bai44
n=int(input("nhap vao he so N:"))
s=0
while n<=0:
    n=int(input("nhap lai he so N:"))
for i in range(0,n+1):
    s+=(2*i+1)/(2*i+2)
print("kqua",s)