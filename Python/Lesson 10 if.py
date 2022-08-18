#===============================================#
# Scripts by Python						        #
# угадываем число введенное с клавиатуры        #
#										        #
# (C) 2022 Nogtev Vadim, Moscow, Russia         #
# Released under GNU Public License (GPL)       #
# email vadimnogtev16@gmail.com                 #  
#===============================================#


x = 0
while(x!=25):
    x = int(input())
    if x<25:print("You need more")
    elif x>25:print("You need menshe")
    else: print("YES IT IS!!")    
print('===========================EOF===========================')