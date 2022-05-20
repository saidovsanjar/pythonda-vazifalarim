# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 10:11:38 2022

@author: Санжар

mavzu:list
"""

ismlar = ['abror' , 'mahmud' , 'ali']
print(f"salom {ismlar[0]} bugun choyxonaga borasanmi".capitalize())
print(f"salom {ismlar[1]} bugun choyxona bor".title())
print(f"salom {ismlar[2]} bugun choyxona bor".upper())

sonlar = [2,5,1.5,12,-9,-4,]
# son = sonlar[0] + sonlar[3]
# print(son)

# son = sonlar[2] * sonlar[5]
# print(son)

# son = sonlar[1] - sonlar[-1]
# print(son)

# t_shaxslar = ['imom buxoriy', ' amir temur ',' imom shofeiy']
# z_shaxslar = ['bill gates ' ,' elon mask ' ,' sanjar'] 
# h_shaxs = t_shaxslar.pop(1)
# f_shaxs = z_shaxslar.pop(2)
# print(f"Men tarixiy shaxslardan {h_shaxs.title()} bilan suhbatlashishni xoxlar edim , zamonaviy shaxslardan esa {f_shaxs.title()} bilan suhbatlashishni xoxlar edim")


friends = []
friends.append('ali')
friends.append('sardor')
friends.append('davron')
friends.append('mahmud')
friends.append('anvar')
print(friends)

friends.remove('davron')
friends.remove('ali')
(friends)
friends.append('Hasan')
friends.insert(0, 'Husan')
friends.insert(2, 'shavkat')
print(friends)


mehmonlar = []
mehmonlar.append(friends.pop(3))
mehmonlar.append(friends.pop(-1))
mehmonlar.append(friends.pop(0))
print("\nKelgan mehmonlar: ", mehmonlar)





















































