import subprocess


def get_profiles():
    try:
        # Intenta obtener los datos usando UTF-8, y si falla, usa cp1252
        data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'], encoding='utf-8', errors='ignore')
    except UnicodeDecodeError:
        data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'], encoding='cp1252', errors='ignore')
    return data

data = get_profiles()

# Filtrar y limpiar los nombres de los perfiles de las líneas relevantes
profiles = [i.split(":")[1][1:-1] for i in data.split('\n') if "All User Profile" in i]

for i in profiles:
    try:
        # Intenta recuperar información de perfil, ignorando errores de decodificación
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear'], encoding='utf-8', errors='ignore')
        
        # Busca la clave de contenido si es posible
        key_content = [b.split(":")[1][1:-1] for b in results.split('\n') if "Key Content" in b]
        
        try:
            print("{:<30}| {:<}".format(i, key_content[0]))
        except IndexError:
            print("{:<30}| {:<}".format(i, "No key found"))
    except subprocess.CalledProcessError:
        print("{:30}| {:<}".format(i, "Failed to retrieve profile info"))

input("Press Enter to exit...")
