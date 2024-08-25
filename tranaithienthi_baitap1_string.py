# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 09:57:32 2024

@author: Student
"""

chuoi="Đại học quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM"
chuoi1=chuoi.split(" , ")
chuoi2=chuoi.replace("P. ","").replace("Q. ","").split(",")
print(chuoi1)
print(chuoi2)
