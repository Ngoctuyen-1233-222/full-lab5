# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 11:24:54 2024

@author: tran9
"""
#bai32
a=int(input("nhap km taxi di duoc:"))
if a<=2:
    print("so tien cuoc taxi di duoc:15000 dong")
elif 2<=a<=6:
    s1=13500*(a-1)+15000
    print(f"so tien cuoc taxi:{s1}")
elif 6<=a<=120:
    s2=13500*4+15000+11000*(a-5)
    print(f"so tien cuoc taxi:{s2}")
elif a>120:
    s3=13500*4+15000+11000*(a-5)*0.9
    print(f"so tien cuoc taxi:{s3}")
else:
    print("can tinh lai:")
        

