#===============================================#
# Scripts by Python						        #
# Удаление данных из массива и вывод суммы      #
#										        #
# (C) 2022 Nogtev Vadim, Moscow, Russia         #
# Released under GNU Public License (GPL)       #
# email vadimnogtev16@gmail.com                 #  
#===============================================#

data = [7, 5, 6.9, 1, 8, 42, 33, 128, 1024, 2, 8, 11, 0.4, 1024, 66, 809, 11, 8.9, 1.1, 3.42, 9, 100, 444, 78]
#your code goes here
min_value = min(data)
print(min_value)
max_value = max(data)
print(max_value)
sum_del_value = min_value + max_value
data.remove(min_value)
data.remove(max_value)
print(sum_del_value)
print(sum(data))
