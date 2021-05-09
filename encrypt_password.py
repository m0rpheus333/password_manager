import bcrypt
import json
#TODO https://stackoverflow.com/questions/21318526/how-to-get-salt-from-a-password-and-use-it-to-validate-user



salt = bcrypt.hashpw(b'gabriel', bcrypt.gensalt())


pw1 = bcrypt.hashpw(b'123456', salt)
pw2 = bcrypt.hashpw(b'aksdjlkj33kj2l4k2w3e', salt)

print(pw1)
print(pw2)

