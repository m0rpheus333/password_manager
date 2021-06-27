import sys
import json
from typing import ItemsView
import bcrypt
from pathlib import Path
from datetime import datetime

home_path = str(Path.home())
sys.path.insert(1, home_path)

a_file = open(home_path + "\pmanager\db.json", "r")
json_obj = json.load(a_file)

array = json_obj['pwrds']


def eintrag_loeschen():
  best = input("Bitte bestätige, dass du den Eintrag löschen willst. (Y/N) ")
  if best.lower() == 'y':
    try:
      title = sys.argv[1]
      print("Ertrag mit Titel: " + title + " wird gelöscht")
      for elem in array:
        if elem['title'] == title:
          json_obj['pwrds'].pop(array.index(elem))
        write_to_db()
      print("Eintrag wurde erfolgteich gelöscht")
    except:
      print("Die Eingabe ist falsch. Bitte geben sie 'passman usage' ein.")


def write_to_db():
  a_file = open(home_path + "\pmanager\db.json", "w")
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

def password_generator_sett():
  def set_pw_mode(mode, string):
    str = 'Soll Passwort ' + string + ' haben? Y/N '
    a = input(str).lower()
    if a == "y":
      json_obj['mpw']['generator'][mode] = True
    elif a == "n":
      json_obj['mpw']['generator'][mode] = False
    else:
      print("eingabe ist falsch.")
  print("Automatisch generierte Passwort Einstellungen: \n")
  laenge = int(input("Geben sie die Laenge des Passworts: "))
  json_obj['mpw']['generator']["len"] = laenge;
  set_pw_mode('gb','große Buchstaben')
  set_pw_mode('kb','kleine Buchstaben')
  set_pw_mode('zh','Zeichen')
  set_pw_mode('zf','Zahlen')

def choose_mode():
  def get_minutes():
    grenze = int(input('Wie viel Minuten: '))
    if(grenze >= 5 and grenze <= 1440):
      json_obj['mpw']['minutes'] = grenze
    else:
      print("Die Zeitangabe ist falsch. Bitte geben Sie in Zahlen zwischen 5 und 1440 Minuten ein")
      get_minutes
  print("--> Wie oft soll Master-Password abgefragt werden? Wählen sie Nummer. Minimum 5 Minuten, Maximum 24 Stunden (1440 min)")
  print('1. In minuten \n2. Bei jeder Abfrage')
  mode = int(input("Nummer: "))
  if mode == 1 or mode == 2:
    if mode == 1:
      json_obj['mpw']['mode'] = 'minutes'
      get_minutes()
      json_obj['mpw']['date'] = datetime.timestamp(datetime.now())
    elif mode == 2:
      json_obj['mpw']['mode'] = None
    print("Alle Eingaben sind gespeichert und verschluessert")
    password_generator_sett()
    return True
  else:
    print('---> Unbekannte Input. Versuchen Sie nochmal')
    choose_mode()


print('Wilkommen in Settings. Bitte wählen sie enine Option: ')
print("1. Master-Passwort ändern \n2. Eintrag löschen\n3. Alle Einträge auflisten \n4. Passwort Generator Modus ändern")
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
elif mode == 4:
  if choose_mode():
    write_to_db()
else:
  print("Die Eingabe ist falsch. Bitte geben sie 'passman usage' ein.")