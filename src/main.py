
import random
import time
from operator import contains


def tworzenie_listy():
    tryb_gry = input("Wybierz tryb (easy, normal, hard) lub 'exit' by zakończyć: ")

    if tryb_gry == "exit":
        print("Wyjście z programu")
        return None

    sciezka = f"../data/{tryb_gry}_level.csv"

    try:
        with open(sciezka, "r") as plik:
            lista = plik.readline().strip().split(", ")
            return lista  # Zwracamy listę tylko jeśli plik istnieje
    except FileNotFoundError:
        print("Nie znaleziono pliku dla tego trybu.")
        return None


def wybor_trybu(lista):
    print("wybierz tryb gry: \n A <-- gra na czas \n B <-- gra na ilosc \n cofnij")
    Wybor = input("Wybierz tryb A, B lub cofnij : ")

    if Wybor == "A":
        liczba_SEC = int(input("Wybierz ile chcesz miec czasu na zadanie (w sekundach) : "))
        lista_do_wyswietlenia = random.sample(lista, 5)
        print("Wylosowane słowa:", lista_do_wyswietlenia)
        for i in range(liczba_SEC, 0, -1):
            print(f"\rZniknie za {i} sekund...", end='', flush=True)
            time.sleep(1)

    elif Wybor == "B":
        liczba_SLOW = int(input("Wybierz ile słow chcesz wyswietlac do zapamietania : "))
        lista_do_wyswietlenia = random.sample(lista, liczba_SLOW)
        print("Wylosowane słowa:", lista_do_wyswietlenia)
        for i in range(10, 0, -1):
            print(f"\rZniknie za {i} sekund...", end='', flush=True)
            time.sleep(1)

    elif Wybor == "cofnij":
        print("Powrot do wyboru poziomu trudnosci")
        wybor_trybu(tworzenie_listy())

    else:
        print("Nie ma takiego trybu gry")

    print("\r" + " " * 30 + "\rCzas minął!", end='', flush=True)
    print("\n" * 10)
    lista2 = input().split(" ")
    punkty = 0
    for slowo in lista2:
        if slowo in lista_do_wyswietlenia:
            punkty += 1
    print(punkty)
    wybor_trybu(lista)



def main():
    wybor_trybu(tworzenie_listy())
if __name__ == "__main__":
    main()






"""import random
import time
import os

def tryb_gry_na_czas(lista_slow):
    czas = int(input("Podaj czas potrzebny na zapamiętanie 10 słów: "))
    lista_do_wyswietlenia = random.sample(lista_slow, 5)
    print("Wylosowane słowa:", lista_do_wyswietlenia)
    for i in range(czas, 0, -1):
        print(f"\rPozostały czas {i} s do rozpoczęcia gry", end='', flush=True)
        time.sleep(1)
   # print("\r" + " " * 30 + "\rCzas minął!", end='', flush=True)
    print("\n" * 10)
    lista_wpisana = input().split(" ")
    punkty = 0
    for slowo in lista_slow:
        if slowo in lista_do_wyswietlenia:
            punkty += 1
    return punkty

lista_latwych = ["laptop", "lampa", "telefon", "okno", "zegarek", "butelka", "szalik", "sok", "plecak", "mysz", "garnek", "długopis",
"nożyczki", "marker", "masło", "ryż", "makaron", "poduszka", "klapki", "gitara", "jabłko", "portfel", "słoik", "czajnik"]

def main():
    p = tryb_gry_na_czas(lista_latwych)
    print(p)

if __name__ == "__main__":
    main()
    
    
    
#pierwsza wersja:    
lista_do_wyswietlenia = random.sample(lista_latwych, 5)
print("Wylosowane słowa:", lista_do_wyswietlenia)

for i in range(3, 0, -1):
    print(f"\rZniknie za {i} sekund...", end='', flush=True)
    time.sleep(1)

print("\r" + " " * 30 + "\rCzas minął!", end='', flush=True)
print("\n" * 10)
lista_wpisana = input().split(" ")
punkty = 0
for slowo in lista2:
    if slowo in lista_do_wyswietlenia:
        punkty += 1
print(punkty)"""
