#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Programa para levantar y detener SSH en un host a traves de un bot de telegram
# Se ha utilizado como codigo base el echobot2.py de https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/echobot2.py
import logging
import telegram
import subprocess
from telegram.error import NetworkError, Unauthorized
from time import sleep


update_id = None

def main():
    global update_id
    # Add here your Telegram Bot Authorization Token
    bot = telegram.Bot('#Token#')

    # get the first pending update_id, this is so we can skip over it in case
    # we get an "Unauthorized" exception.
    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    while True:
        try:
            echo(bot)
        except NetworkError:
            sleep(1)
        except Unauthorized:
            # The user has removed or blocked the bot.
            update_id += 1


def echo(bot):
    global update_id
    # Request updates after the last update_id
    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1
        msg = update.message.text
        #Add here your chat id
        if update.message and update.message.chat.id==#ChatID#:  
            # Proccess message
            a=0
            if msg == "/Arriba":
                subprocess.call(["./start"])
                update.message.reply_text("SSH arriba")
                a=1
            if msg == "/Abajo":
                subprocess.call(["./stop"])
                update.message.reply_text("SSH abajo")
                a=1
            if msg == "/Status":
                out = subprocess.check_output(["systemctl status sshd|tail -n 1"],shell=True)
                update.message.reply_text(out)
                a=1
            if msg == "/Temperatura":
                out = subprocess.check_output(["sensors"])
                update.message.reply_text(out)
                a=1
                
            if a == 0:
                update.message.reply_text("Comando no reconocido, comandos válidos:\n\n/Ayuda - Muestra este mensaje\n\n/Arriba - Levanta el servicio SSH\n\n/Abajo - Detiene el servicio SSH\n\n/Status - Muestra el estado actual del servicio SSH\n\n/Temperatura - Muestra la temperatura del dispositivo")
                

if __name__ == '__main__':
    main()
