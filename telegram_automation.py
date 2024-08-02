#!/usr/bin/env python3

import pyautogui
from termcolor import colored
from telethon import TelegramClient
import argparse
import os
import datetime
import signal
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import time

def def_handler(signal, def_handler):
    print(colored("[!] Saliendo del programa...", 'red'))
    exit(1)

signal.signal(signal.SIGINT, def_handler)

def create_client():
    # Tus credenciales API de telegram (si no sabes como crearlas búscalo)
    api_id = 'example_id'
    api_hash = 'example_hash'

    # Número de teléfono con el que inicias sesión en Telegram
    global phone_number
    phone_number = 'example_number'

    # Crear el cliente de Telethon
    return TelegramClient('session_name', api_id, api_hash)


firefox_abierto = None

def iniciar_firefox():

    geckodriver_path = "/home/ezirion/.fzf/bin/geckodriver"
    profile_path = "/home/ezirion/Desktop/python_projects/MyProjects/sesion_firefox"  # Asegúrate de que el path sea correcto

    options = Options()
    options.profile = profile_path

    # Configura el servicio de Firefox
    service = Service(geckodriver_path)
  
    # Inicia una instancia de Firefox si no está ya abierta
    firefox = webdriver.Firefox(service=service, options=options)

    firefox.get('https://www.youtube.com')

    time.sleep(7)

    try:
        sign_in_btn = WebDriverWait(firefox, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[3]/div[2]/ytd-button-renderer/yt-button-shape/a"))
        )
        sign_in_btn.click()
    except Exception as e:
        pass

    return firefox


def like_video(firefox_abierto, url):

    # Vamos a la url del video
    firefox_abierto.get(video_url)

    time.sleep(7)

# Encuentra el botón de like y haz clic en él
    try:
        sign_in_btn = WebDriverWait(firefox_abierto, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[3]/div[2]/ytd-button-renderer/yt-button-shape/a"))
        )
        sign_in_btn.click()
    except Exception as e:
        pass


    # Espera a que la página del video cargue
    time.sleep(5)

    # Encuentra el botón de like y haz clic en él
    try:
        like_button = WebDriverWait(firefox_abierto, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[2]/div/div/ytd-menu-renderer/div[1]/segmented-like-dislike-button-view-model/yt-smartimation/div/div/like-button-view-model/toggle-button-view-model/button-view-model/button"))
        )
        like_button.click()
    except Exception as e:
        print("Error al intentar encontrar o hacer clic en el botón de 'like':", e)
        return

    # Espera un momento para asegurarse de que el like se registre
    time.sleep(3)
  
    # Hace captura de pantalla despues de dar el like
    take_cap() 

    try:
        like_button = WebDriverWait(firefox_abierto, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[2]/div/div/ytd-menu-renderer/div[1]/segmented-like-dislike-button-view-model/yt-smartimation/div/div/like-button-view-model/toggle-button-view-model/button-view-model/button"))
        )
        like_button.click()
    except Exception as e:
        print("Error al intentar encontrar o hacer clic en el botón de 'like':", e)
        return


async def __get_dialogs():
    
    await client.start(phone=phone_number)
    
    # Obtener todos los diálogos
    dialogs = await client.get_dialogs()
    
    
    # Iterar sobre los diálogos y mostrar información de los grupos
    for dialog in dialogs:
            print(f"Nombre del grupo: {dialog.name}")
            print(f"ID del grupo: {dialog.id}")
            print(f"Access hash: {dialog.entity.access_hash}")
            print(f"Enlace del grupo: https://t.me/{dialog.entity.username}" if dialog.entity.username else "No tiene enlace")
            print("-" * 40)


video_url = None
used_urls = ['https://www.youtube.com',]

async def get_messages():

    global video_url
    global used_urls

    await client.start(phone=phone_number)
    
    # ID y access hash del grupo
    group_id = -1002027619250
    access_hash = -7539049283132133995 # Este es el grupo en el que lo hice no me importa compartirlo
    # NOTA: Si quieres probarlo, informar que yo solo gané 20€ hasta que me dijeron que no pagaban más si no les ingresaba dinero,
    # por lo cual ahi paré, justo donde saco mas beneficio de manera segura, recomiendo hacer lo mismo, ya que estas cosas suelen
    # ser estafas, aunque en este caso nos aprovechamos un poco :D
    
    # Obtener la entidad del grupo usando el ID y el access hash
    group = await client.get_input_entity(group_id)

    loop = True

    while loop:
        # Obtener los últimos 10 mensajes del grupo
        messages = await client.get_messages(group, limit=50)
        # Imprimir los mensajes
        for message in reversed(messages):
            if not message.text:
                continue
            elif 'https://youtu.be/' in message.text and message.text not in used_urls:
                print(f"De: {message.sender_id}, Mensaje: {message.text}")
                video_url = message.text
                used_urls.append(video_url)
                loop = False
                break

def take_cap():

    screenshot = pyautogui.screenshot()
    screenshot.save('/home/ezirion/Desktop/python_projects/MyProjects/screenshot.png')


async def send_cap():
# Iniciar sesión en Telegram
    try:
        for i in range(2):
            await client.start(phone=phone_number)
        
            # Obtener el usuario al que quieres enviar el mensaje (por número de teléfono)
            recipient = await client.get_entity("@Lucia5451")

            # Enviar el mensaje
            await client.send_file(recipient, "/home/ezirion/Desktop/python_projects/MyProjects/screenshot.png")
    
            print(colored(f"\n[+] Mensaje enviado correctamente ({datetime.datetime.now()})'.'", 'green'))
            
            time.sleep(400)

    except Exception as e:
        print(colored(f"\n[!] Algo ha fallado: {str(e)}.", 'red'))



async def main():
    global video_url
    firefox = iniciar_firefox()

    while True:
        # Recibimos los mensajes del grupo de telegram buscando si hay alguna url de video de youtube
        await get_messages() 
        # Se busca el enlace del video, se inicia sesion en yt si es necesario, y da like al video
        like_video(firefox, video_url) # Se da like al video y se llama a la fn 'take_cap'
        await send_cap() # Manda la captura al bot que chequea las capturas
        ahora = datetime.datetime.now()
        time.sleep(1200)
        if ahora.hour >= 21 and ahora.minute >= 10: # A determinada hora apaga el equipo para que no consuma tanta energía
            os.system("poweroff")
            exit(1)


# Ejecutar el cliente de Telethon

with create_client() as client:
    client.loop.run_until_complete(main())
