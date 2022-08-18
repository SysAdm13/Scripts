#===============================================#
# Scripts by Python						        #
# Работа с функциями                            #
#										        #
# (C) 2022 Nogtev Vadim, Moscow, Russia         #
# Released under GNU Public License (GPL)       #
# email vadimnogtev16@gmail.com                 #  
#===============================================#

inputfile1 = "C:/Projects/Files/File1.txt"
inputfile2 = "C:/Projects/Files/rockyou.txt"

myfile = open(inputfile1, mode='r', encoding='utf8')

for num, line in enumerate(myfile):
    print('Line№ '+ str(num) + ' : ' + line.strip())