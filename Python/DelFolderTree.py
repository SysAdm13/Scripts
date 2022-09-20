
import os, datetime, time

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

name = os.getlogin()
# получить имя пользователя

path_for_logs = f'C:/Users/{name}/AppData/Roaming/Mozilla/Firefox/Crash Reports/123/DelFiles/'
create_dir(path_for_logs)
# путь до файлов и папки для логов, которая создаётся если её нет.

date = datetime_normalview()
# получить дату
now = time.time()
# получить время
days = 0
# за какой период оставлять файлы(в днях)
seconds = days * 86400
# за какой период оставлять файлы(в секундах)

path = f'C:\\Users\\{name}\\AppData\\Roaming\\Mozilla\\Firefox\\Crash Reports\\123'
# путь от куда удалять файлы
file = os.listdir(path)
# получить список файлов из папки удаления
file_not_use = []
folder_not_use = []
# два пустых списка для сравнения файлов
for i in file:
    # перебор файло в папке удаления
    if i.endswith('.txt'):
        # если есть файлы в определнном формате (.txt) 
        file_not_use.append(i)
        # то добавить их к списку
    elif i.endswith('.bmp'):
        # если есть файлы в определнном формате (.bmp) 
        file_not_use.append(i)
        # то добавить их к списку
    result = list(set(file) - set(file_not_use))
# сравнение двух списков: разделение на файлы и папки
# файлы не трогать а в папку переходить и удалять в ней файлы
#

for i in result:
    # получить список файлов из папки
    i = os.path.join(path, i)
    # преобразование имени папки в её путь
    path1 = i
    # присвоенеие пути переменной
    file = os.listdir(path1)
    # получить список путей к папкам
    for b in file:
        # перебор файлов в папках
        b = os.path.join(path1, b)
        # присвоение путей файлам
        #if b.endswith('.txt'):
    #раскомментить если нужно исключить какое-то файлы из удаления в подпапках
        if os.stat(b).st_mtime < now - seconds:
        # если дата создания файла меньше сегодняшнего дня минус количество дней, которые нужно оставить
                try:
                    os.remove(os.path.join(path, b))
            # удалить файлы по выбранному пути
                    l = f'{date} for user {name} file {b} was deleted'
            # создать сообщение о том когда кем и какой файл был удален
                    f = open(f'C:/Users/{name}/AppData/Roaming/Mozilla/Firefox/Crash Reports/123/DelFiles/text.txt', 'a')
            # Путь куда записывать логи удаления
                    f.write(l + '\n')
            # записать сообщение в файл
                except OSError as e:
                    print("Ошибка: %s : %s" % (file, e.strerror))
            # ловец ошибок, чтобы программа не падала
    #for     
    
