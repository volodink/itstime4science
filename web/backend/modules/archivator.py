import zipfile
import os
def img_zip():
    z = zipfile.ZipFile('report.zip', 'w')        # Создание нового архива
    for root, dirs, files in os.walk('img'): # Список всех файлов и папок в директории folder
        for file in files:
           z.write(os.path.join(root,file))         # Создание относительных путей и запись файлов в архив

    z.close()