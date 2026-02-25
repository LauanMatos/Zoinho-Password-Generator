import random
import string
from time import sleep
import time

VERSAO = "1.0"
print(f"👽 Zoinho Password Generator - v{VERSAO}")

print("=" * 60)
print("           👽 Zoinho Password Generator 👽 ")
print("=" * 60)
while True:
    size = int(input("👽: How many characters do you want in your password?: "))
    print("-" * 60)
    sleep(1.5)

    characters = string.ascii_lowercase

    uppercase = input("👽: Do You Want Capital Letters? S/N: ")
    print("-" * 60)
    sleep(1.5)

    Numbers = input("👽: Do You Want Numbers S/N: ")
    print("-" * 60)
    sleep(1.5)

    simbols = input("👽: Do You Want Simbols S/N: ")
    print("-" * 60)
    sleep(1.5)

    if uppercase.lower() == "s":
        characters = characters + string.ascii_uppercase
    if Numbers.lower() == "s":
        characters = characters + string.digits
    if simbols.lower() == "s":
        characters = characters + string.punctuation

    password = ""

    for i in range(size):
        password = password + random.choice(characters)

    def password_generator(time_total=5, size2=50):
        print("👽: Password Generator...")
        print("-" * 60)
        sleep(2.0)
        for i in range(size2 + 1):
            porcentagem = int((i / size2) * 100)

            barra = "█" * i + "░" * (size2 - i)
            print(f"\r[{barra}] {porcentagem}%", end="", flush=True)
            time.sleep(time_total / size2)
        print("")
        print("-" * 60)
        print("👽: Generated Password ")
        print("-" * 60)
        sleep(2.0)
        print(f"👽: Password: {password}")
        print("-" * 60)

    password_generator(5)

    def force_meter(size):
        if size < 11:
            return "Weak"
        elif size < 21:
            return "Medium"
        elif size < 31:
            return "Strong"
        else:
            return "Very Strong"
    force = force_meter(size)
    print(f"👽: Stregth Level: {force}")
    print("-" * 60)
    sleep(1.5)

    continuar = input("👽: Deseja Continuar? S/N: ")
    print("-" * 60)
    if continuar.lower() != "s":
        sleep(1.5)
        print("👽: Obrigado Por Ter Passado Aqui! Volte Logo!...")
        print("-" * 60)
        break

print("=" * 60)