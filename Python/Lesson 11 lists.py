#===============================================#
# Scripts by Python						        #
# Работа с массивами                            #
#										        #
# (C) 2022 Nogtev Vadim, Moscow, Russia         #
# Released under GNU Public License (GPL)       #
# email vadimnogtev16@gmail.com                 #  
#===============================================#

mylist=list(range(0))

while True:
    a=input('Введите чило: ')
    
    if a=='stop':
        break
    else:mylist.append(int(a))
print('vi vveli stop slovo')
print(sum(mylist))










