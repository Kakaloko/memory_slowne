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

for i in range(3, 0, -1):
    print(f"\rZniknie za {i} sekund...", end='', flush=True)
    time.sleep(1)

# Czyszczenie linii i wiadomość końcowa
print("\r" + " " * 30 + "\rCzas minął!", end='', flush=True)
print("\n" * 10)
lista2 = input().split(" ")
punkty = 0
for slowo in lista2:
    if slowo in lista_do_wyswietlenia:
        punkty += 1
print(punkty)