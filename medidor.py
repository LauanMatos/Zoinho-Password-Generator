from time import sleep

size = int(input("👽: How many characters do you want in your password?: "))
print("-" * 60)
sleep(1.5)

''' De Acordo com o size ele vai medir a força , nas proximas atualizações irei mudar a forma de medir a força , nao sera apenas por tamanho'''

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