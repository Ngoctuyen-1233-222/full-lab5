# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 12:09:22 2024

@author: tran9
"""
#bai39
n=int(input("nhap vao he so N:"))
s=0
while n<=0:
    n=int(input("nhap lai he so N:"))
for i in range(1,n+1):
    s+=1/i
print("kqua",s)
    



