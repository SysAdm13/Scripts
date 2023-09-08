import datetime

def datetime_normalview()
date = datetime.datetime.now()
#date_now = date.strftime
date = str(date)
date = list(date)
date = date[0:19]
a = ''
for i in date:   
    a += i
print(a)

