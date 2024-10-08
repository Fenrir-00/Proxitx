#!/usr/bin/env python
import requests
import random
import os
import time
import re  # Importar el módulo re para expresiones regulares
from colores import colorverde,colorazul,colorclasic,colormorado,colornaraja,coloramarillo

class color:
    morado = '\033[95m'
    blanco = '\033[97m'
    cyan = '\033[96m'
    azul = '\033[94m'
    verde = '\033[92m'
    amarillo = '\033[93m'
    rojo = '\033[91m'
    fin = '\033[0m'

def lista():
 url = 'https://free-proxy-list.net/'  # Cambia esta URL por la que desees
 response = requests.get(url)

# Extraer direcciones IP y puertos con una expresión regular
 ip_port_list = re.findall(r'[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+:[0-9]+', response.text)
 with open('resultados.txt', 'w') as f:
    for ip_port in ip_port_list:
        f.write(ip_port + '\n')

def banner():
 os.system("clear")
 print(f"""{color.cyan}
██████╗ ██████╗  █████╗ ██╗  ██╗██╗   ██╗████████╗██╗  ██╗
██╔══██╗██╔══██╗██╔══██╗╚██╗██╔╝╚██╗ ██╔╝╚══██╔══╝╚██╗██╔╝
██████╔╝██████╔╝██║  ██║ ╚███╔╝  ╚████╔╝    ██║    ╚███╔╝
██╔═══╝ ██╔══██╗██║  ██║ ██╔██╗   ╚██╔╝     ██║    ██╔██╗
██║     ██║  ██║╚█████╔╝██╔╝╚██╗   ██║      ██║   ██╔╝╚██╗
╚═╝     ╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝""")
 print(f"{color.fin}")

def version():
 texto ="""
 |=======================================================|
 | Script by              : #FENRIR-00                   |
 | Version                : Version  2.5                 |
 | Follow me on Github    : https://github.com/Fenrir-00 |
 | Contact me on Telegram : @Ritorito1990                |
 ========================================================= 
""" 

 suerte = random.randint(0,5)
 if suerte == 0:
   coloramarillo(texto)
 elif suerte == 1:
   colorazul(texto)
 elif suerte == 2 :
   colorclasic(texto)
 elif suerte == 3 :
   colormorado(texto)
 elif suerte == 4 :
   colornaraja(texto)
 elif suerte == 5:
   colorverde(texto)      

# Leer la lista de proxies desde el archivo resultados.txt
def cargar_proxies(archivo):
    proxies_list = []
    try:
        with open(archivo, 'r') as f:
            for linea in f:
                # Eliminar espacios en blanco y saltos de línea
                proxy = linea.strip()
                if proxy:  # Asegurarse de que la línea no esté vacía
                    proxies_list.append({"http": proxy, "https": proxy})
    except FileNotFoundError:
        print(f"El archivo {archivo} no fue encontrado.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
    return proxies_list

def is_valid_ip(ip):
    """Verifica si la IP es válida (números y puntos)"""
    pattern = r'^\d{1,3}(\.\d{1,3}){3}$'
    return re.match(pattern, ip) is not None

def change_ip_with_proxy(proxies):
    """Realiza una solicitud HTTP utilizando un proxy"""
    for proxy in proxies:
        try:
            print(f"{color.verde}Usando el proxy: {proxy}")
            response = requests.get("http://ifconfig.me", proxies=proxy, timeout=5)
            ip_publica = response.text.strip()

            if is_valid_ip(ip_publica):
                print(f"{color.azul}IP pública: {ip_publica}")
            else:
                print(f"{color.rojo}fallo[×] - IP no válida")
                
            time.sleep(5)  # Cambia cada 5 segundos
        except requests.exceptions.RequestException as e:
            print(f"{color.rojo}fallo[×] - IP no válida")

# Cargar proxies desde resultados.txt
lista()
proxies_list = cargar_proxies('resultados.txt')

# Cambiar IP con proxies
if proxies_list:  # Solo ejecutar si hay proxies cargados
    banner()
    version()
    change_ip_with_proxy(proxies_list)
else:
    print("No se encontraron proxies para usar.")
