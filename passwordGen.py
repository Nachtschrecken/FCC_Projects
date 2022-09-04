import string
import random


characters = list(string.ascii_letters + string.digits)

def generate_password(length):

    random.shuffle(characters)
    password = []
    for x in range(length):
        password.append(random.choice(characters))
    random.shuffle(password)
    password = "".join(password)

    return password


generate_password(50)