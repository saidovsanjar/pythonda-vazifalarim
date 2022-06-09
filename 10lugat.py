# -*- coding: utf-8 -*-
"""
Created on Thu May 26 10:34:34 2022

@author: Санжар
"""

# otam = {'t_yil':1971,'ism':'ulugbek'.title(),'yosh':53}
# print(f"otamning ismi {otam['ism']} , yoshi {otam['yosh']} , {otam['t_yil']} da tugilgan ")

# taom = {'onam':'osh','otam':'shashlik','akam':'shurva','ukam':'manti','men':'norin'}
# print(f"Onamning sevimli taomi {taom['onam']} \
#  otamning sevimli taomi {taom['otam']} \
#  akamning sevimli taomi {taom['akam']}") 


python_izohli_lugati = {
    'integer':"Butun son",
    'float':"O'nlik son",
    'string':"Matn",
    'list':"Ro'yxat",
    'tuple':"O'zgarmas ro'yxat"}
# # print(python_izohli_lugati['tuple'])

# kalit = input("Kalit so'z kiriting:").lower()
# print(python_izohli_lugati.get(kalit,"Bunday so'z mavjud emas"))

kalit = input('kalit suz kiriting: ').lower()
tarjima = python_izohli_lugati.get(kalit)
if tarjima==None:
    print('bunday suz mavjud emas')
else:
    print(f"{kalit.title()} suzi {tarjima} deb ataladi")
    



















