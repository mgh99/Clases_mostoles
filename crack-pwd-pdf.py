# VERSION SIMPLE SOLO UNA LISTA DE CONTRASEÑAS
#import pikepdf
#from tqdm import tqdm
#
#passwords = [line.strip() for line in open("worldlist.txt")]
#
#for password in tqdm(passwords, "Decrypting PDF"):
#    try:
#        with pikepdf.open("sample1.pdf", password=password) as pdf:
#            print("\n[+] Password found: ", password)
#            break
#    except pikepdf._qpdf.PasswordError as e:
#        # contraseña incorrecta continua con el loop
#        continue
    

import os

# VERSION COMPLETA CON UNA LISTA DE MILLONES DE CONTRASEÑAS
import pikepdf
from tqdm import tqdm

# Lista de rutas a tus archivos .txt con contraseñas
password_files = [
    "pwd-list/worldlist1000000.txt",
    "pwd-list/100k-most-used-passwords-NCSC.txt",
    "pwd-list/1900-2020.txt",
    "pwd-list/500-worst-passwords.txt",
    "pwd-list/SplashData-2014.txt",
    "pwd-list/SplashData-2015-1.txt",
    "pwd-list/SplashData-2015-2.txt",
    "pwd-list/top-20-common-SSH-passwords.txt",
    "pwd-list/medical-devices.txt"
    "pwd-list/common-passwords-win.txt",
    "pwd-list/best1050.txt",
    "pwd-list/SplashData-2015-1.txt"
]

# Función para leer las contraseñas de todos los archivos
def load_passwords(password_files):
    passwords = []
    for file_path in password_files:
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    passwords.append(line.strip())
    return passwords

# Cargar todas las contraseñas de los archivos proporcionados
passwords = load_passwords(password_files)

# Intentar abrir el PDF con cada contraseña
for password in tqdm(passwords, "Decrypting PDF"):
    try:
        with pikepdf.open("sample3.pdf", password=password) as pdf:
            print("\n[+] Password found:", password)
            break
    except pikepdf.PasswordError:
        continue