import random
import time
import os

# Lista słów
lista = ["laptop", "lampa", "telefon", "okno", "zegarek", "butelka", "szalik", "sok", "plecak", "mysz"]

# Losowanie 5 słów
lista_do_wyswietlenia = random.sample(lista, 5)
print("Wylosowane słowa:", lista_do_wyswietlenia)

# Odczekaj 10 sekund
time.sleep(10)

# Wyczyść konsolę
os.system('cls')  # Dla Windows
