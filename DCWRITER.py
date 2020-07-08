import asyncio
import time
import traceback
from os import system
from random import randint
from discord.ext import commands
import os
import discord
import random
import string
import platform
import ctypes
from configparser import ConfigParser

ctypes.windll.kernel32.SetConsoleTitleW(f"DCWRITER By Xubiz#0001/#1186 && 4NON#2491 | discord.gg/A4uw29W | ")

config = ConfigParser()

def create_config():
	config['settings'] = {'token': "", 'lang': "EN", 'msg_file': 'messages.txt', 'command': '$write', 'random': 'True'}
	with open("config.json", 'w') as f:
		config.write(f)

def read_config():
	global config
	config.read('config.json')

if os.path.exists('config.json'):
	read_config()
else:
	create_config()

if config['settings']['lang'] == "PL":
	PASTE_TOKEN = "Wklej swój token (bez ''): "
	LOGINING = "Logowanie..."
	CONNECTED_TO = "Połączono z"
	TURN_ON = "Włączono wiadomości"
	TURN_OFF = "Wyłączono wiadomości"
	CANT_FIND_MSG = f"Brak pliku {config['settings']['msg_file']}. Utworzono plik."
	CRITICAL_ERROR = "Aplikacja napotkała problem. Proszę zrestartować aplikacje"
	COMMAND = "Komenda to"
	RANDOM = "Losowe litery są"
	if config['settings']['random'] == 'True' or config['settings']['random'] == 'true':
		RANDOM_STATUS = RANDOM + ' włączone'
	elif config['settings']['random'] == 'False' or config['settings']['random'] == 'false':
		RANDOM_STATUS = RANDOM + ' wyłączone'
elif config['settings']['lang'] == "EN":
	PASTE_TOKEN = "Paste your token (without ''): "
	LOGINING = "Loggining..."
	CONNECTED_TO = "Connected to"
	TURN_ON = "Turned on news"
	TURN_OFF = "Turned off news"
	CANT_FIND_MSG = f"Can't find {config['settings']['msg_file']}. Was created a text file."
	CRITICAL_ERROR = "Application encountered a problem. Please restart apps"
	COMMAND = "Command this"
	RANDOM = "Random letters is"
	if config['settings']['random'] == 'True' or config['settings']['random'] == 'true':
		RANDOM_STATUS = RANDOM + ' enabled'
	elif config['settings']['random'] == 'False' or config['settings']['random'] == 'false':
		RANDOM_STATUS = RANDOM + ' disabled'


bot = commands.Bot(command_prefix=".", self_bot=True)
ready = False
writed_message = 0
write_status = True

def clear():
	if platform.system() == 'Windows':
		system("cls")
	elif platform.system() == 'Linux':
		system("clear")
	else:
		system("clear")

clear()
def intro():
	print("""
\t██████╗  ██████╗██╗    ██╗██████╗ ██╗████████╗███████╗██████╗
\t██╔══██╗██╔════╝██║    ██║██╔══██╗██║╚══██╔══╝██╔════╝██╔══██╗
\t██║  ██║██║     ██║ █╗ ██║██████╔╝██║   ██║   █████╗  ██████╔╝
\t██║  ██║██║     ██║███╗██║██╔══██╗██║   ██║   ██╔══╝  ██╔══██╗
\t██████╔╝╚██████╗╚███╔███╔╝██║  ██║██║   ██║   ███████╗██║  ██║
\t╚═════╝  ╚═════╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
""")

intro()

if config['settings']['token'] == '':
	token = input('\t' + time.strftime("[%H:%M:%S]", time.localtime()) + f" {PASTE_TOKEN}")
	config['settings']['token'] = token
	with open("config.json", 'w') as f:
		config.write(f)

time.sleep(2)
clear()
intro()
print('\t' + time.strftime("[%H:%M:%S]", time.localtime()) + f' {LOGINING}')

status = 0

while 1:
	try:
		@bot.event
		async def on_connect():
			print('\t' + time.strftime("[%H:%M:%S]", time.localtime()) + f" {CONNECTED_TO} {bot.user} ({bot.user.id})\n")
			time.sleep(2)
			print('\t' + time.strftime("[%H:%M:%S]", time.localtime()) + f" {COMMAND} '{config['settings']['command']}'")
			print('\t' + time.strftime("[%H:%M:%S]", time.localtime()) + f" {RANDOM_STATUS}\n")

		@bot.event
		async def on_message(message):
			global writed_message, status, config
			start = time.time()
			channel = message.channel
			if message.content.startswith(config['settings']['command']):
				if message.author == bot.user:
					if status == 0:
						print(time.strftime('\t' + "[%H:%M:%S]", time.localtime()) + f' {TURN_ON}')
						status = 1
					else:
						status = 0
						print(time.strftime('\t' + "[%H:%M:%S]", time.localtime()) + f' {TURN_OFF}')
					if status == 1:
						while True:
							if config['settings']['random'] == 'True' or config['settings']['random'] == 'true':
								while True:
									try:
										if status == 0:
											break
										time.sleep(0.75)
										randomnumber = random.randint(1,128)
										code = (('').join(random.choices(string.ascii_letters + string.digits, k=randomnumber)))
										await channel.send(code)
									except:
										pass
							elif os.path.exists(config['settings']['msg_file']):
								lins = 0
								with open(config['settings']['msg_file'], 'r') as f:
									for lins in f:
										try:
											if status == 0:
												break
											if not lins.strip():
												lins =+1
											else:
												time.sleep(0.75)
											await channel.send(lins)
											lins =+1
										except:
											continue
							else:
								with open(config['settings']['msg_file'], 'w') as f:
									print('\t' + time.strftime("[%H:%M:%S]", time.localtime()) + f" {CANT_FIND_MSG}")
									f.write("DCWRITER By Xubiz#0001/#1186 && 4NON#2491")
									f.close()
									f = open(config['settings']['msg_file'], 'r')
									for lins in f:
										try:
											time.sleep(0.75)
											await channel.send(lins)
											lins =+1
										except:
											pass
		bot.run(config['settings']['token'], bot=False)
	except:
		time.sleep(1)
		print(time.strftime('\t' + "[%H:%M:%S]", time.localtime()) + f" {CRITICAL_ERROR}")
		time.sleep(5)
		exit()

stop = time.time()
elapsed_time = time.time() - start
t = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
