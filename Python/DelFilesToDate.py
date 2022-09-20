#================================================#
# Scripts by Python						         #
# Удаление файлов по определенному пути          #
#										         #
# (C) 2022 Nogtev Vadim, Moscow, Russia          #
# Released under GNU Public License (GPL)        #
# email vadimnogtev16@gmail.com                  #  
#================================================#

import os, time
import datetime

def datetime_normalview():
    date = datetime.datetime.now()
    date = str(date)
    date = list(date)
    date = date[0:19]
    a = ''
    for i in date:   
        a += i
    return a
# функция получения нормального вида даты, без милисекунд.

def create_dir(pathlogs):
    directory = os.path.dirname(pathlogs) 
    if not os.path.exists(directory): 
        os.makedirs(directory)
# функция создания директории если её нет.

date = datetime_normalview()
# получить текущую дату
name = os.getlogin()
# получить имя пользователя
path = f'C:/Users/{name}/AppData/Roaming/Mozilla/Firefox/Crash Reports/123'
# путь где нужно удалить файлы
path_for_logs = f'C:/Users/{name}/AppData/Roaming/Mozilla/Firefox/Crash Reports/123/DelFiles/'
create_dir(path_for_logs)
# путь до файлов и папки для логов, которая создастся если её нет.
file = os.listdir(path)
# получить список файлов
now = time.time()
# получить время
days = 365
# за какой период оставлять файлы(в днях)
seconds = days * 86400
# за какой период оставлять файлы(в секундах)
for f in file:
    f = os.path.join(path, f)
    # преобразовать имя файла в полный путь
    if os.stat(f).st_mtime < now - seconds:
        # если дата создания файла меньше сегодняшнего дня минус количество дней, которые нужно оставить
        try:
            os.remove(os.path.join(path, f))
            # удалить файлы по выбранному пути
            l = f'{date} for user {name} file {f} was deleted'
            # создать сообщение о том когда кем и какой файл был удален
            f = open(f'C:/Users/{name}/AppData/Roaming/Mozilla/Firefox/Crash Reports/123/DelFiles/text.txt', 'a')
            # Путь куда записывать логи удаления
            f.write(l + '\n')
            # записать сообщение в файл
        except OSError as e:
            print("Ошибка: %s : %s" % (file, e.strerror))
            # ловец ошибок, чтобы программа не падала
