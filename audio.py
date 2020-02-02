import os
from tinytag import TinyTag
import shutil
import time
import subprocess

path = 'D:/target/'  # папка где лежит гора аудио кусков
target_dist = 'D:/dest/'  # папка где лежит mp3cat
end_dist = 'D:/audio/new/bleach/193-203/'  # папка где будут лежать итоговые файлы

list1 = os.walk(path)  # обходим все файлы папка path
folder = []  # выгружаем данные обхода
for i in list1:
    folder.append(i)
fi = []  # выбираем только имена файлов
for address, dirs, files in folder:
    fi.append(files)

x = fi[0]  # вычищаем имена до конца

fl = 0  # флаг остановки
while fl == 0:
    if len(x) <= 1:  # если в папке больше нет файлов то стоп
        fl = 1
        break

    name = x[0]  # берем имя первого файла в папке
    temp = name[8:10]  # определяем к какой серии он относится
    count = 0
    for i in x:  # считаем сколько файлов с этой серии
        count += 1
        if i[8:10] != temp:  # если попался с другой серии то стоп
            break

    q_count = count//4  # будем делить все файлы на 4 части
    count_points = [q_count, 2*q_count, 3*q_count, count-2]

    try:  # на всякий проверяем есть ли уже объединенный файл
        os.remove(target_dist+'combined.mp3')
    except FileNotFoundError:
        print('чистая папка')

    num = 0
    for i in count_points:
        while num <= i:
            shutil.move(path + x[num], target_dist)  # переносим первый транж файлов
            num += 1
        subprocess.call(target_dist + 'combiner.bat')  # запуск объединения
        shutil.move(target_dist + 'combined.mp3', end_dist)  # каждый файл после объединения перемещаем и меняем имя
        os.chdir(end_dist)
        os.rename('combined.mp3', '{}.{}.mp3'.format(name[8:10], i))
    x = x[count-1:]  # выкидываем из списка имен уже обработанные имена
