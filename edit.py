import sys
import json
from typing import ItemsView
import bcrypt
from pathlib import Path


home_path = str(Path.home())
sys.path.insert(1, home_path)

a_file = open(home_path + "\complete\db.json", "r")
json_obj = json.load(a_file)

array = json_obj['pwrds']


def eintrag_loeschen():
  best = input("Bitte bestätige, dass du den Eintrag löschen willst. (Y/N)")
  if best.lower() == 'y':
    try:
      title = sys.argv[1]
      print("Ertrag mit Titel: " + title + "| wird gelöscht")
      for elem in array:
        if elem['title'] == title:
          json_obj['pwrds'].pop(array.index(elem))
        write_to_db()
      print("Eintrag wurde erfolgteich gelöscht")
    except:
      print("Die Eingabe ist falsch. Bitte geben sie 'passman usage' ein.")


def write_to_db():
  a_file = open(home_path + "\complete\db.json", "w")
  json.dump(json_obj, a_file)
  a_file.close()

def write_new_master_password():
  pw = input("Neue Master Passowrd: ")
  password = input("Password wiederholen: ")
  if(pw == password):
    salt = bcrypt.hashpw(bytes(password, encoding='utf-8'), bcrypt.gensalt())
    pw1 = bcrypt.hashpw(bytes(password, encoding='utf-8'), salt)
    json_obj['mpw']['pw'] = pw1.decode()
    json_obj['mpw']['salt'] = salt.decode()
    write_to_db()
    print("Dein Muster Passwort ist erfolgreich erstellt!")
  else:
    print("Passwörte sind nicht gleich. Versuch Nochmals")
    write_new_master_password()

print('Wilkommen in Settings. Bitte wählen sie enine Option: ')
print("1. Master-Passwort ändern \n2. Eintrag löschen\n3. Alle Einträge auflisten")
mode = int(input("--> Nummer: "))
if mode == 1:
  best = input("Bitte bestätige, dass du dein Master-Passwort ändern willst. (Y/N)")
  if best.lower() == 'y':
    write_new_master_password()
elif mode == 2:
  eintrag_loeschen()
elif mode == 3:
  main_array = []
  for elem in array:
    main_array.append([elem['title'],elem['username']])
  print ("{:<10} {:<10} {:<10}".format("Titel     |","Username |", "Passwort   |"))
  for item in main_array:
    titel, username = item
    print ("{:<10} {:<10} {:<10}".format(titel,username, "***********"))
else:
  print("Die Eingabe ist falsch. Bitte geben sie 'passman usage' ein.")