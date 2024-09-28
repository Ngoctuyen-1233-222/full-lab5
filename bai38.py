# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 12:07:28 2024

@author: tran9
"""

#bai38
n=int(input("nhap vao he so n:"))
s=1
while n<=0:
    n=int(input("nhap lai he so n:"))
for i in range(1,n+1):
    s*=i
print("kqua",s)