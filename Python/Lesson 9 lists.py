#===============================================#
# Scripts by Python						        #
# Создание и копирование Массивов               #
#										        #
# (C) 2022 Nogtev Vadim, Moscow, Russia         #
# Released under GNU Public License (GPL)       #
# email vadimnogtev16@gmail.com                 #  
#===============================================#

cars = ['bmw','vw','seat','skoda','Lexus','Audi','Ford','Mersedes','Toyota']
Japan_motors=['Toyota','Lexus']
Germany_motors=['bmw','Mersedes']
Vag_motors=['vw','Audi','skoda']
for x in cars:
    if x in Japan_motors:
        print(x+" Is Japan Motors!")
    elif x in Germany_motors:
        print(x+" Is Germany Motors")
    else:print(x+" Vag Motors")    