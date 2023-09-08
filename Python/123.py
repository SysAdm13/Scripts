
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
file_list = os.listdir(path)
# получить список файлов из папки удаления
file_for_extention = []
# пустой список для сравнения файлов
for files in file_list:
    # перебор файлов в папке удаления
    if files.endswith(('.txt', '.bmp')):
        # если есть файлы в определнном формате (.txt) (.bmp) 
        file_for_extention.append(files)
        # то добавить их к списку

list_folders = list(set(file_list) - set(file_for_extention))
# сравнение двух списков: разделение на файлы и папки
# файлы не трогать а в папку переходить и удалять в ней файлы
#

for files in list_folders:
    # получить список файлов из папки
    path_for_subfolder = os.path.join(path, files)
    # присвоенеие пути переменной
    file_list = os.listdir(path_for_subfolder)
    # получить список путей к папкам
    for file in file_list:
        # перебор файлов в папках
        file = os.path.join(path_for_subfolder, file)
        # присвоение путей файлам
        #if file.endswith('.txt'):
    #раскомментить если нужно исключить какое-то файлы из удаления в подпапках
        if os.stat(file).st_mtime < now - seconds:
        # если дата создания файла меньше сегодняшнего дня минус количество дней, которые нужно оставить
                try:
                    os.remove(os.path.join(path, file))
            # удалить файлы по выбранному пути
                    l = f'{date} for user {name} file {file} was deleted'
            # создать сообщение о том когда кем и какой файл был удален
                    f = open(f'C:/Users/{name}/AppData/Roaming/Mozilla/Firefox/Crash Reports/123/DelFiles/text.txt', 'a')
            # Путь куда записывать логи удаления
                    f.write(l + '\n')
            # записать сообщение в файл
                except OSError as e:
                    print("Ошибка: %s : %s" % (file_list, e.strerror))
            # ловец ошибок, чтобы программа не падала
       

            
