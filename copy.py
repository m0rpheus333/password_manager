import time
import sys
import json
import pyperclip
from tkinter import Tk
from pathlib import Path
from signal import signal, SIGINT


# Wir öndern den sys path to HOME, damit der python file des Dateisystem finden kann.
home_path = str(Path.home())
sys.path.insert(1, home_path)
copier = Tk()

a_file = open(home_path + "\pmanager\db.json", "r")
json_obj = json.load(a_file)

arr = json_obj['pwrds']
title = sys.argv[1]



username = ""
password = ""
for item in arr:
  if item['title'] == title:
    username = item['username']
    password = item['password']
#Wenn das Programm durch Ctrl+C abgebrochen wird
#sollen wir den Clipboard leeren
#  source: https://www.devdungeon.com/content/python-catch-sigint-ctrl-c

def handler(signal_received, frame):
    print('CTRL-C detected. Passwort in Clipboard wird gelöscht')
    pyperclip.copy(' ')
    sys.exit(1)

def clip(password):
  pyperclip.copy(password)
  print("---> You have 30 sec, untill I empty the clipboard")
  signal(SIGINT, handler)
  time.sleep(30)
  pyperclip.copy(' ')

print("Username: " + username + " | password copied to clipboard")
clip(password)
