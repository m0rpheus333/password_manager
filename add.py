import os
import sys
import json
import random
from pathlib import Path

# Wir öndern den sys path to HOME, damit der python file des Dateisystem finden kann.
home_path = str(Path.home())
sys.path.insert(1, home_path)


#Die Funktion für Speicherung allen geänderten, maipulierten Daten.
def write_to_db():
  a_file = open(home_path + "\complete\db.json", "w")
  json.dump(json_obj, a_file)
  a_file.close()

#Eröffnung der db.json file und konvertierung in Python Dictinary
a_file = open(home_path + "\complete\db.json", "r")
json_obj = json.load(a_file)


# Alle Daten werden von JSON file gezogen.
# Ertellung des Data Dictinory mit lange und Array mit ASCII Codes (zB. 65-91 sind Grossbuchstaben),
# die von user abgefragt wurden
def generate_passwordList():
  password_list = []
  mode = json_obj['mpw']['generator']
  lenght = mode['len']
  for key in mode:
    if key == 'gb' and mode[key] == True:
      for char in range(65, 91):
        password_list.append(char)
    if key == 'kb' and mode[key] == True:
      for char in range(97, 123):
        password_list.append(char)
    if key == 'zh' and mode[key] == True:
      for char in range(33, 48):
        password_list.append(char)
      for char in range(58, 97):
        password_list.append(char)
      for char in range(123, 127):
        password_list.append(char)
    if key == 'zf' and mode[key] == True:
      for char in range(48, 58):
        password_list.append(char)
      return {
      "list" : password_list,
      "leange": lenght 
    }

# Generiert Passwort nach laenge und ascii array, diw wir mit oberen funktion erstellen
def generate_password(ascii_list, ammount):
    result = ''
    for item in range(ammount):
        index = random.randint(0, len(ascii_list) -1)
        charCode = ascii_list[index]
        result += chr(charCode)
    return result

pw_list = generate_passwordList()
pw = generate_password(pw_list["list"], pw_list["leange"])


def create_obj(title, username, password):
  acc_obj = {
  "title": title,
  "username" : username,
  "password" : password
  }
  return acc_obj


def check_repeat(title, key):
  for item in json_obj['pwrds']:
    if item[key] == title:
      return False
  return True

try:
  arguments = sys.argv
  new_pw = create_obj(arguments[1], arguments[2],pw)
  if check_repeat(arguments[1], "title") == False:
    print("Error: Der eingegebene Titel ist bereits vorhanden, bitte ändern Sie den Titel")
  elif check_repeat(arguments[2], "username"):
    print("Error: Der eingegebene Username ist bereits vorhanden, bitte ändern Sie den Username")
  else:
    json_obj['pwrds'].append(new_pw)
except:
  print("Es ist ein Error erstanden. Bitte geben sie 'passman usage' ein.")


write_to_db()