import os

def get_files(path):
    files = []

    directory = os.listdir(path)
    directory.sort(reverse=True)

    for file in directory:
        if file.endswith('.txt'):
            files.append(file)
    return files

def remove_old_files(path, files):
    # Оставляет последние 5 файлов, остальные удаляет
    max_files = 5
    if len(files) < max_files:
        return
    i = 0
    for f in files:
        i += 1
        if i > max_files:
            os.remove(os.path.join(path, f))

name = os.getlogin()
path = f'C:/Users/{name}/AppData/Roaming/Mozilla/Firefox/Crash Reports/123'
files = get_files(path)
remove_old_files(path, files)