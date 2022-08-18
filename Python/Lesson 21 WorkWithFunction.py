#===============================================#
# Scripts by Python						        #
# Работа с функциями                            #
#										        #
# (C) 2022 Nogtev Vadim, Moscow, Russia         #
# Released under GNU Public License (GPL)       #
# email vadimnogtev16@gmail.com                 #  
#===============================================#

def get_hidden_card(num_card, stars=4):
    num_card_new = num_card[-4:]
    value_stars = stars * "*"
    return(f'{value_stars}{num_card_new}') 

num_card = str(1234567812345678)
print(get_hidden_card(num_card,7))