# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 12:25:59 2024

@author: tran9
"""

#bai43
n=int(input("nhap vao he so N:"))
s=0
while n<=0:
    n=int(input("nhap lai he so N: "))
for i in range(1,n+1):
    s+=i/(i+1)
print("kqua",s)