import random
import time
import os

#tryb_gry = input("Wybierz tryb (easy, normal, hard): ")
#
# # Tworzenie ścieżki do pliku
# sciezka = "../data/" + tryb_gry + "_level.csv"
#
# # Wczytanie linii z pliku i podzielenie jej na słowa
# with open(sciezka, "r") as plik:
#     linia = plik.readline().strip()         # usuń znaki nowej linii (\n)
#     lista = linia.strip().split(",")                # podziel po przecinkach

# Pobranie wyboru użytkownika
tryb_gry = input("Wybierz poziom trudności (easy, medium, hard): ").strip().lower()

# Mapowanie poziomu trudności na nazwę pliku
nazwa_pliku = "../data/" + tryb_gry + "_level.txt"

# Próba otwarcia pliku i wczytania słów
try:
    with open(nazwa_pliku, "r", encoding="utf-8") as plik:
        zawartosc = plik.read().strip()        # Wczytaj zawartość i usuń znaki nowej linii
        lista = zawartosc.split(",")           # Podziel po przecinkach

    print("Lista słów:", lista)

except FileNotFoundError:
    print(f"Plik '{nazwa_pliku}' nie został znaleziony.")
except Exception as e:
    print("Wystąpił błąd:", e)
# print("wybierz tryb gry: \n A <-- gra na czas \n B <-- gra na ilosc")
#
# Wybor = input("Wybierz tryb A lub B : ")
# if Wybor == "A":
#     liczba_s = int(input("Wybierz ile chcesz miec czasu na zadanie : "))
#     # lista = ["laptop", "lampa", "telefon", "okno", "zegarek", "butelka", "szalik", "sok", "plecak", "mysz"]
#
#     lista_do_wyswietlenia = random.sample(lista, 5)
#     print("Wylosowane słowa:", lista_do_wyswietlenia)
#     for i in range(liczba_s, 0, -1):
#         print(f"\rZniknie za {i} sekund...", end='', flush=True)
#         time.sleep(1)
#
#     # Czyszczenie linii i wiadomość końcowa
#     print("\r" + " " * 30 + "\rCzas minął!", end='', flush=True)
#     print("\n" * 10)
#     lista2 = input().split(" ")
#     punkty = 0
#     for slowo in lista2:
#         if slowo in lista_do_wyswietlenia:
#             punkty += 1
#     print(punkty)