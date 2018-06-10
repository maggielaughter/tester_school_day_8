import os
from datetime import datetime



if __name__=='__main__':
    print(os.name)
    print(os.uname())
    print(os.listdir('.')) #podajemy katalog w nawiasach a on nam zwraca to samo co ls w bash
    print(os.stat('data.json')[6]) # wywołanie linuxowe statu - zwraca informacje o pliku/węźle
    #st_size - w bajtach, st_atime - czas ostatniego dostaępu, st_mtime - czas ostatniej modyfikacji, st_ctime - czas creation
    stat = os.stat('data.json')
    print('Rozmiar :',stat.st_size)
    atime = datetime.fromtimestamp(stat.st_atime)
    print('Ostatni dostęp :', atime)


    for file_name in os.listdir('.'):
        stat = os.stat(file_name)
        print(file_name, ' :', stat.st_size, datetime.fromtimestamp(stat.st_atime))


