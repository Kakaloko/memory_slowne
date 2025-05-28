import random
import time
import os

tryb_gry = input("Wybierz tryb(easy, normal, hard)")

plik = open("../data/"+ tryb_gry +"_level.csv","r")
lista = plik.readline().split(",")
plik.close()


# Losowanie 5 słów
lista_do_wyswietlenia = random.sample(lista, 5)
print("Wylosowane słowa:", lista_do_wyswietlenia)

# Odczekaj 10 sekund
time.sleep(10)

# Wyczyść konsolę
os.system('cls')  # Dla Windows
