import random
class obj:
    def __init__(self, title, username, password):
        self.title = title
        self.username = username
        self.password = password

    def getVal(self):
        print('title: ', self.title)
        print('username: ', self.username, " | password is copied on clipboard")


def generate_passwordList():
    password_list = []
    leange = int(input("Bitte gib die Passwortlänge ein: "))
    grosse_buchstaben = input("Große Buchstaben Y/N: ")
    klein_buchstaben = input("Kleine Buchstaben Y/N: ")
    zahlen = input("Zahlen Y/N: ")
    zeichen = input("Zeichen Y/N: ")
    if grosse_buchstaben == 'Y':
        for char in range(65, 91):
            password_list.append(char)
    if klein_buchstaben == 'Y':
        for char in range(97, 123):
            password_list.append(char)
    if zahlen == 'Y':
        for char in range(48, 58):
            password_list.append(char)
    if zeichen == 'Y':
        for char in range(33, 48):
            password_list.append(char)
        for char in range(58, 97):
            password_list.append(char)
        for char in range(123, 127):
            password_list.append(char)
    return {
      "list" : password_list,
      "leange": leange 
    }
    


def generate_password(ascii_list, ammount):
    result = ''
    for item in range(ammount):
        index = random.randint(0, len(ascii_list) -1)
        charCode = ascii_list[index]
        result += chr(charCode)
    return result


p1 = obj("moodle", "uas000001", "sadj32ijksjdkasjdsa")

dd_list = generate_passwordList()
asd = generate_password(dd_list["list"], dd_list["leange"])

print("Passwort: " + asd)
