# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 07:29:57 2024

@author: Le Pham Nhu Y
"""
distance = float(input("Nhập độ dài đoạn đường đến trường(m):"))
if distance < 300:
    print("Đường đến trường quá gần. Thôi!Đi bộ")
elif distance >=300 and distance <=700:
    print("Đường đến trường không xa. Thôi!Đi xe đạp")
else:
    print("Không xác định")
