import json
import bcrypt
import sys
from getpass import getpass
from datetime import datetime
#NOTE use encode() to byte string and decode() to make normal string
from pathlib import Path



home_path = str(Path.home())
# Wir öndern den sys path to HOME, damit der python file des Dateisystem finden kann.
sys.path.insert(1, home_path)
data_now = datetime.now()
a_file = open(home_path + "\pmanager\db.json", "r")
json_obj = json.load(a_file)

#Funktion für Speicherung allen änderungen und manipulationen in JSON file
def write_to_db():
  a_file = open(home_path + "\pmanager\db.json", "w")
  json.dump(json_obj, a_file)
  a_file.close()

# Einstellung für die Passord Generator (mit Grossbuchstaben, Kleinbuchstaben usw.)
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

# Erstellen des Master Passworts
# Der passwort wird auch als salt generiert
# .decode, weil JSON File byte strings nicht akzeptiert
def write_new_master_password():
  pw = getpass("Neue Master Passowrd: ")
  password = getpass("Password wiederholen: ")
  if(pw == password):
    salt = bcrypt.hashpw(bytes(password, encoding='utf-8'), bcrypt.gensalt())
    pw1 = bcrypt.hashpw(bytes(password, encoding='utf-8'), salt)
    json_obj['mpw']['pw'] = pw1.decode()
    json_obj['mpw']['salt'] = salt.decode()
    print("Dein Muster Passwort ist erfolgreich erstellt!")
    return True
  else:
    print("Passwörte sind nicht gleich. Versuch Nochmals")
    write_new_master_password()


# Einstellung, wie oft soll Master Passwort abgefragt werden.
def choose_mode():
  def get_minutes():
    grenze = int(input('Wie viel Minuten: '))
    if(grenze >= 5 and grenze <= 1440):
      json_obj['mpw']['minutes'] = grenze
    else:
      print("Die Zeitangabe ist falsch. Bitte geben Sie in Zahlen zwischen 5 und 1440 Minuten ein")
      get_minutes()
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



#Eingabe des Passwortes durch getpass(), damit der nicht einfach in Command Line gezeigt wird
# bcrypt.checkpw() gibt Boolean aus, wenn das Encryptete Passwort mit eingegebenem Passwort übereinstimmt = True

def check_password():
  pw_input = getpass('Master-Password: ')
  if bcrypt.checkpw(pw_input.encode(), json_obj['mpw']['pw'].encode()):
    json_obj['mpw']['date'] = datetime.timestamp(datetime.now())
    write_to_db()
    print('---> Master ok')
  else:
    ask = input('Password ist falsh. Nochmals versuchen? y/n ')
    if ask == 'y':
      check_password()




# überprüft ob es übrhaupt User gibt
def new_user():
    if json_obj['mpw']['pw'] == None:
      print("Du bist neu hier \nLass uns neue Master Passwort erstellen")
      if write_new_master_password() and choose_mode():
        write_to_db()
      else:
        print("Es ist ein Fehler erstanden, versuchen Sie nochmals")


# Haupt Funktion. Überüft ob die Zeit und führt die Funktion Check_password aus
# wird bei jeder Befehl asugefuehrt
# 
def handle_password():
  new_user()
  if json_obj['mpw']['minutes'] != None:
    timestamp = datetime.fromtimestamp(json_obj['mpw']['date'])
    difference = data_now - timestamp
    if (difference.total_seconds() / 60) > int(json_obj['mpw']['minutes']):
      check_password()
    else:
      print("Minutes to ask a master password", difference.total_seconds / 60)

handle_password()
