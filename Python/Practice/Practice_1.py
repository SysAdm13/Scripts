#===============================================#
# Scripts by Python						        #
# Переворот строки                              #
#										        #
# (C) 2022 Nogtev Vadim, Moscow, Russia         #
# Released under GNU Public License (GPL)       #
# email vadimnogtev16@gmail.com                 #  
#===============================================#

string = input()
new_string = ''
for i in string:
    new_string = string[::-1]
print(new_string)