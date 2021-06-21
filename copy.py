import time
import sys
import json
import pyperclip
from tkinter import Tk
from pathlib import Path

# Wir öndern den sys path to HOME, damit der python file des Dateisystem finden kann.
home_path = str(Path.home())
sys.path.insert(1, home_path)
copier = Tk()

a_file = open(home_path + "\complete\db.json", "r")
json_obj = json.load(a_file)

arr = json_obj['pwrds']
title = sys.argv[1]

username = ""
password = ""
for item in arr:
  if item['title'] == title:
    username = item['username']
    password = item['password']

def clip(password):
  pyperclip.copy(password)
  print("---> You have 30 sek till i empty the clipboard")
  time.sleep(30)
  pyperclip.copy('empty')

print("Username: " + username + " | password copied to clipboard")
clip(password)
