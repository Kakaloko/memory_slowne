# -*- coding: utf-8 -*-
import random
import time
from operator import contains
import os

STATS_FILE = "statystyki.txt"

def zapisz_statystyki(punkty, bledy):
    suma_punktow = punkty
    suma_bledow = bledy
    liczba_gier = 1

    # Wczytaj istniejące dane, jeśli plik istnieje
    if os.path.exists(STATS_FILE):
        with open(STATS_FILE, "r") as plik:
            linie = plik.readlines()[2:]  # pomijamy nagłówek i separator
            for linia in linie:
                if "|" in linia:
                    nazwa, wartosc = linia.strip().split("|")
                    wartosc = wartosc.strip()
                    if "Liczba gier" in nazwa:
                        liczba_gier += int(wartosc)
                    elif "Suma punktów" in nazwa:
                        suma_punktow += int(wartosc)
                    elif "Suma błędów" in nazwa:
                        suma_bledow += int(wartosc)

    # Oblicz średnie
    srednie_punkty = suma_punktow / liczba_gier
    srednie_bledy = suma_bledow / liczba_gier

    # Zapisz nowy plik zaktualizowanymi danymi
    with open(STATS_FILE, "w") as plik:
        plik.write(f"{'Statystyka':<25} | Wartość\n")
        plik.write(f"{'-'*25}+{'-'*10}\n")
        plik.write(f"{'Liczba gier':<25} | {liczba_gier}\n")
        plik.write(f"{'Suma punktów':<25} | {suma_punktow}\n")
        plik.write(f"{'Suma błędów':<25} | {suma_bledow}\n")
        plik.write(f"{'Średnie punkty na grę':<25} | {srednie_punkty:.2f}\n")
        plik.write(f"{'Średnie błędy na grę':<25} | {srednie_bledy:.2f}\n")

    # Wyświetl też w konsoli
    print(f"\n📊 Statystyki ogólne:")
    print(f"- Liczba gier: {liczba_gier}")
    print(f"- Średnie punkty na grę: {srednie_punkty:.2f}")
    print(f"- Średnie błędy na grę: {srednie_bledy:.2f}")




def tryb_gry_na_czas(lista_slow):
    czas = int(input("Podaj czas potrzebny na zapamiętanie 5 słów: "))
    lista_do_wyswietlenia = random.sample(lista_slow, 5)
    lista_do_wyswietlenia = [s.lower() for s in lista_do_wyswietlenia]
    print("Wylosowane słowa:", lista_do_wyswietlenia)
    for i in range(czas, 0, -1):
        print(f"\rPozostały czas {i} s do rozpoczęcia gry", end='', flush=True)
        time.sleep(1)
    print("\n" * 15)
    lista_wpisana = [s.lower() for s in input("Wpisz zapamiętane słowa, oddzielone spacją: ").split()]
    punkty = 0
    bledy = 0
    for slowo in lista_wpisana:
        if slowo in lista_do_wyswietlenia:
            punkty += 1
        else:
            bledy += 1
    print("Koniec gry!")
    return punkty, bledy

def tryb_gry_na_ilosc(lista_slow):
    ilosc = int(input("Podaj ile słów chcesz zapamiętać w ciągu 10s: "))
    lista_do_wyswietlenia = random.sample(lista_slow, ilosc)
    print("Wylosowane słowa:", lista_do_wyswietlenia)
    for i in range(10, 0, -1):
        print(f"\rPozostały czas {i} s do rozpoczęcia gry", end='', flush=True)
        time.sleep(1)
    print("\n" * 15)
    lista_wpisana = [s.lower() for s in input("Wpisz zapamiętane słowa, oddzielone spacją: ").split()]
    punkty = 0
    bledy = 0
    for slowo in lista_wpisana:
        if slowo in lista_do_wyswietlenia:
            punkty += 1
        else:
            bledy += 1
    print("Koniec gry!")
    return punkty, bledy

def tryb_gry_do_pierwszego_bledu1(lista_slow):  # gra się kończy jeśli gracz poda mniejszą liczbę słów
    punkty = 0
    bledy = 0
    i = 1
    while True:
        lista_do_wyswietlenia = random.sample(lista_slow, i)
        print("Wylosowane słowa:", lista_do_wyswietlenia)
        for j in range(3 * i, 0, -1):
            print(f"\rPozostały czas {j} s do rozpoczęcia gry", end='', flush=True)
            time.sleep(1)
        print("\n" * 15)
        lista_wpisana = [s.lower() for s in input("Wpisz zapamiętane słowa, oddzielone spacją: ").split()]
        if (len(lista_wpisana) < len(lista_do_wyswietlenia)):
            print("Podałeś za mało słów!")
            break
        for slowo in lista_wpisana:
            if slowo in lista_do_wyswietlenia:
                punkty += 1
            else:
                bledy += 1
            if (bledy > 0):
                print("Pojawił się błąd!")
                break
        i += 1
    print("Koniec gry!")
    return punkty



def tworzenie_listy():
    tryb_gry = input("Wybierz tryb (easy, normal, hard) lub 'exit' by zakończyć: ").lower()

    if tryb_gry == "exit":
        print("Wyjście z programu")
        return None

    sciezka = f"../data/{tryb_gry}_level.csv"

    try:
        with open(sciezka, "r", encoding="utf-8") as plik:
            lista = plik.readline().strip().split(", ")
            return lista
    except FileNotFoundError:
        print("Nie znaleziono pliku dla tego trybu.")
        tworzenie_listy()


def wybor_trybu(lista):
    print("wybierz tryb gry: \n A <-- gra na czas \n B <-- gra na ilość \n C <-- gra do pierwszego błędu \n cofnij")
    wybor = input("Wybierz tryb A, B, C lub cofnij : ").lower()
    if wybor == "a":
        wynik1 = tryb_gry_na_czas(lista)
        print("Liczba punktów : ", wynik1[0],"Liczba błędów: ", wynik1[1] )
        zapisz_statystyki(wynik1[0], wynik1[1])

    elif wybor == "b":
        wynik2 = tryb_gry_na_ilosc(lista)
        print("Liczba punktów : ", wynik2[0], "Liczba błędów: ", wynik2[1])
        zapisz_statystyki(wynik2[0], wynik2[1])

    elif wybor == "c":
        wynik3 = tryb_gry_do_pierwszego_bledu1(lista)
        print("Liczba punktów : ", wynik3)

    elif wybor == "cofnij":
        print("Powrot do wyboru poziomu trudności")
        wybor_trybu(tworzenie_listy())

    else:
        print("Nie ma takiego trybu gry")

def main():
    while True:
        lista_slow = tworzenie_listy()
        if lista_slow is None:
            break
        wybor_trybu(lista_slow)

        decyzja = input("\nCzy chcesz zagrać ponownie? (tak/nie): ").lower()
        if decyzja != "tak":
            break

    # Po zakończeniu całej sesji
    decyzja_stat = input("\nCzy chcesz otworzyć plik ze statystykami? (tak/nie): ").lower()
    if decyzja_stat == "tak":
        try:
            os.system(f'notepad {STATS_FILE}')  # Windows
        except Exception as e:
            print("Nie udało się otworzyć pliku:", e)

if __name__ == "__main__":
    main()
