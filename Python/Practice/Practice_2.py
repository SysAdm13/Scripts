#===============================================#
# Scripts by Python						        #
# Сумма всех чисел от введенного числа          #
#										        #
# (C) 2022 Nogtev Vadim, Moscow, Russia         #
# Released under GNU Public License (GPL)       #
# email vadimnogtev16@gmail.com                 #  
#===============================================#

N = int(input())
#your code goes here
i = 0
result = []
while i != N+1:
    result.append(i)
    i += 1
print(sum(result))

