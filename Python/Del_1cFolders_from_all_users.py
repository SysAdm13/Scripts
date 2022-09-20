
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
# путь до файлов и папки для логов, которая создастся если её нет.
# получить список файлов
#file2 = os.listdir(path2)
# раскомментить если требуется почистить более 1 папки.

now = time.time()
# получить время
days = 30
# за какой период оставлять файлы(в днях)
seconds = days * 86400

path = f'C:/Users'
file_list = os.listdir(path)
for i in file_list:

    if i == 'admin':
        continue    
    if i == 'All Users':
        continue 
    if i == 'Default User':
        continue 
    if i == 'DefaultAppPool':
        continue 
    if i == 'KlNagSvc':
        continue 
    if i == '.NET v4.5':
        continue 
    if i == '.NET v4.5 Classic':
        continue 
    if i == 'MSSQL$MICROSOFT##WID':
        continue 
    if i == 'USR1CV8':
        continue 
    if i == 'Default':
        continue 
    if i.endswith(('.txt', '.bmp', '.ini', '.dt')):
        continue 
    if i == 'Public':
        continue 
    else: 
        name = i
        path = f'C:/Users/{name}/AppData/Roaming/1C/1cv8'
        if os.path.exists(path):
            file = os.listdir(path)
            for f in file:
                fpatch = os.path.join(path, f)
    # преобразовать имя файла в полный путь
                if os.stat(fpatch).st_mtime < now - seconds:
    # если дата создания файла меньше сегодняшнего дня минус количество дней, которые нужно оставить
                    try:
                        if f == 'ExtCompT': 
                            continue
            # папка с именем DelFiles удалена не будет
                        elif f == 'conf':
                            continue
                        elif f == 'dumps':
                            continue
                        elif f == 'logs':
                            continue
            # папка с именем DelFiles удалена не будет
            #elif f == '1':
            #    continue
            # папка с именем 1 удалена не будет
                        else:    
                            shutil.rmtree(fpatch)
                # удалить папку любую папку (пустую\не пустую)
                            #l = f'{date} for user {name} file {fpatch} was deleted'
                # создать сообщение о том когда кем и какой файл был удален
                            #fpatch = open(f'C:/Users/{name}/AppData/Roaming/Mozilla/Firefox/Crash Reports/123/DelFiles/text.txt', 'a')
                # Путь куда записывать логи удаления
                            #fpatch.write(l + '\n')
                # записать сообщение в файл
                    except OSError as e:
                        print("Ошибка: %s : %s" % (file, e.strerror))
            # ловец ошибок, чтобы программа не падала
        else:
            continue


        path2 = f'C:/Users/{name}/AppData/Local/1C/1cv8'
        if os.path.exists(path2):
            file = os.listdir(path2)
            for f in file:
                fpatch = os.path.join(path2, f)
    # преобразовать имя файла в полный путь
                if os.stat(fpatch).st_mtime < now - seconds:
    # если дата создания файла меньше сегодняшнего дня минус количество дней, которые нужно оставить
                    try:
                        if f == 'ExtCompT': 
                            continue
            # папка с именем DelFiles удалена не будет
                        elif f == 'conf':
                            continue
                        elif f == 'dumps':
                            continue
                        elif f == 'logs':
                            continue
            # папка с именем 1 удалена не будет
                        else:    
                            shutil.rmtree(fpatch)
                # удалить папку любую папку (пустую\не пустую)
                            #l = f'{date} for user {name} file {fpatch} was deleted'
                # создать сообщение о том когда кем и какой файл был удален
                            #fpatch = open(f'C:/Users/{name}/AppData/Roaming/Mozilla/Firefox/Crash Reports/123/DelFiles/text.txt', 'a')
                # Путь куда записывать логи удаления
                            #fpatch.write(l + '\n')
                # записать сообщение в файл
                    except OSError as e:
                        print("Ошибка: %s : %s" % (file, e.strerror))
            # ловец ошибок, чтобы программа не падала
        else:
            continue