# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 08:02:42 2024

@author: Le Pham Nhu Y
"""
a = float(input("Nhập a:"))
b = float(input("Nhập b:"))
if a==0 and b==0:
    print("Phương trình vô số nghiệm")
elif a==0 and b!=0:
    print("Phương trình vô nghiệm")
elif a!=0 and b!=0:
    print("Phương trình có một nghiệm duy nhất X=",-b/a)
else:
    print("Không hợp lệ")

