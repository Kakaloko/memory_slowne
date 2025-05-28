<<<<<<< HEAD
import random
import time
import os
import csv

# Lista słów
with open("data/easy_level.csv", newline=" ") as csvfile:
    list = csvfile.reader()
lista = ["laptop", "lampa", "telefon", "okno", "zegarek", "butelka", "szalik", "sok", "plecak", "mysz"]

# Losowanie 5 słów
lista_do_wyswietlenia = random.sample(lista, 5)
print("Wylosowane słowa:", lista_do_wyswietlenia)

# Odczekaj 10 sekund
time.sleep(10)

# Wyczyść konsolę
os.system('cls')  # Dla Windows
=======
print("Hello World")
>>>>>>> f9026a8e26d443dc1516e3c3169fda9d14a0dcf4
