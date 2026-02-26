import string
from time import sleep
import random

size = int(input("👽: How many characters do you want in your password?: "))
print("-" * 60)
sleep(1.5)

characters = string.ascii_lowercase

uppercase = input("👽: Do You Want Capital Letters? S/N: ")
print("-" * 60)
sleep(1.5)

numbers = input("👽: Do You Want Numbers S/N: ")
print("-" * 60)
sleep(1.5)

simbols = input("👽: Do You Want Simbols S/N: ")
print("-" * 60)
sleep(1.5)

for i in range(size):
    password = password + random.choice(characters)


if uppercase.lower() == "s":
    characters = characters + string.ascii_uppercase
if numbers.lower() == "s":
        characters = characters + string.digits
if simbols.lower() == "s":
    characters = characters + string.punctuation

password = ""
