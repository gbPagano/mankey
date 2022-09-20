from pathlib import Path
import csv, os

from mankey.data.master import master_encrypted
from mankey.utils.crypto import encrypt2

path = Path(__file__).absolute().parent.parent
archive = path / "data" / "personal_data" / "data.csv"


def save_new_pwd(name, url, user, pwd):
    
    pwd = encrypt2(user, os.getenv("pwd_mankey"), pwd)

    row = [name, url, user, pwd]

    with open(archive,'a') as file:
        writer = csv.writer(file) 
        writer.writerow(row)
    
    print("Sucesso!")
    return


def search_pwd(keyword):
    with open(archive,'r') as file:       
        for row in csv.reader(file):
            if keyword in row[0] or keyword in row[1]:
                print(row)
