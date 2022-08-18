#===============================================#
# Scripts by Python						        #
# Работа с файлами                              #
#										        #
# (C) 2022 Nogtev Vadim, Moscow, Russia         #
# Released under GNU Public License (GPL)       #
# email vadimnogtev16@gmail.com                 #  
#===============================================#

inputfile2 = "C:/Projects/Files/rockyou.txt"
outputfile2 = 'C:/Projects/Files/rockyou(out).txt'

myfile = open(inputfile2, mode='r', encoding='latin_1')
myfile2= open(outputfile2, mode='a', encoding='latin_1')

for num, line in enumerate(myfile):
    if "petya" in line:
        print('Line№ '+ str(num) + ' : ' + line.strip())
        myfile2.write(line)
        
myfile.close()
myfile2.close()
