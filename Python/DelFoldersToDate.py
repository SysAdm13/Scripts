#================================================#
# Scripts by Python						         #
# Удаление папок и их содержимого с исключениями #
#										         #
# (C) 2022 Nogtev Vadim, Moscow, Russia          #
# Released under GNU Public License (GPL)        #
# email vadimnogtev16@gmail.com                  #  
#================================================#

import os, time
import datetime
import shutil

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
# путь где нужно удалить папки

#path2 = f'C:/Users/{name}/AppData/Roaming/Mozilla/Firefox/Crash Reports/321'
# раскомментить если требуется почистить более 1 папки.

path_for_logs = f'C:/Users/{name}/AppData/Roaming/Mozilla/Firefox/Crash Reports/123/DelFiles/'
create_dir(path_for_logs)
# путь до файлов и папки для логов, которая создастся если её нет.
file = os.listdir(path)
# получить список файлов

#file2 = os.listdir(path2)
# раскомментить если требуется почистить более 1 папки.

now = time.time()
# получить время
days = 0
# за какой период оставлять файлы(в днях)
seconds = days * 86400
# за какой период оставлять файлы(в секундах)
for f in file:
    fpatch = os.path.join(path, f)
    # преобразовать имя файла в полный путь
    if os.stat(fpatch).st_mtime < now - seconds:
    # если дата создания файла меньше сегодняшнего дня минус количество дней, которые нужно оставить
        try:
            if f == 'DelFiles': 
                continue
            # папка с именем DelFiles удалена не будет
            #elif f == '1':
            #    continue
            # папка с именем 1 удалена не будет
            else:    
                shutil.rmtree(fpatch)
                # удалить папку любую папку (пустую\не пустую)
                l = f'{date} for user {name} file {fpatch} was deleted'
                # создать сообщение о том когда кем и какой файл был удален
                fpatch = open(f'C:/Users/{name}/AppData/Roaming/Mozilla/Firefox/Crash Reports/123/DelFiles/text.txt', 'a')
                # Путь куда записывать логи удаления
                fpatch.write(l + '\n')
                # записать сообщение в файл
        except OSError as e:
            print("Ошибка: %s : %s" % (file, e.strerror))
            # ловец ошибок, чтобы программа не падала


# раскомментить если требуется почистить более 1 папки.
'''
for f in file2:
    fpatch = os.path.join(path2, f)
    # преобразовать имя файла в полный путь
    if os.stat(fpatch).st_mtime < now - seconds:
    # если дата создания файла меньше сегодняшнего дня минус количество дней, которые нужно оставить
        try:
            if f == 'DelFiles': 
                continue
            # папка с именем DelFiles удалена не будет
            elif f == '1':
                continue
            # папка с именем 1 удалена не будет
            else:    
                shutil.rmtree(fpatch)
                # удалить папку любую папку (пустую\не пустую)
                l = f'{date} for user {name} file {fpatch} was deleted'
                # создать сообщение о том когда кем и какой файл был удален
                fpatch = open(f'C:/Users/{name}/AppData/Roaming/Mozilla/Firefox/Crash Reports/123/DelFiles/text.txt', 'a')
                # Путь куда записывать логи удаления
                fpatch.write(l + '\n')
                # записать сообщение в файл
        except OSError as e:
            print("Ошибка: %s : %s" % (file, e.strerror))
            # ловец ошибок, чтобы программа не падала
'''