from time import sleep
import time


def loadingbar(time_total=5, size2=50):
    print("👽: Password Generator...")
    print("-" * 60)
    sleep(2.0)

    for i in range(size2 + 1):
        porcentagem = int((i / size2) * 100)

        barra = "█" * i + "░" * (size2 - i)
        print(f"\r[{barra}] {porcentagem}%", end="", flush=True)
        time.sleep(time_total / size2)

loadingbar(5)
