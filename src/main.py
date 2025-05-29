import random
import time
import os
#from asyncio.unix_events import can_use_pidfd


def tryb_gry_na_czas(lista_slow):
    czas = int(input("Podaj czas potrzebny na zapamiętanie 10 słów: "))
    lista_do_wyswietlenia = random.sample(lista_slow, 5)
    lista_do_wyswietlenia = [s.lower() for s in lista_do_wyswietlenia]
    print("Wylosowane słowa:", lista_do_wyswietlenia)
    for i in range(czas, 0, -1):
        print(f"\rPozostały czas {i} s do rozpoczęcia gry", end='', flush=True)
        time.sleep(1)
   # print("\r" + " " * 30 + "\rCzas minął!", end='', flush=True)
    print("\n" * 15)
    lista_wpisana = [s.lower() for s in input("Wpisz zapamiętane słowa, oddzielone spacją: ").split()]
    punkty = 0
    bledy = 0
    for slowo in lista_wpisana:
        if slowo in lista_do_wyswietlenia:
            punkty += 1
        else:
            bledy += 1
    #punkty = sum(1 for slowo in lista_wpisana if slowo in lista_do_wyswietlenia) # inny sposób na zliczanie pkt
    print("Koniec gry!")
    return punkty, bledy


def tryb_gry_na_ilosc(lista_slow):
    ilosc = int(input("Podaj ile słów chcesz zapamiętać w ciągu 10s: "))
    lista_do_wyswietlenia = random.sample(lista_slow, ilosc)
    print("Wylosowane słowa:", lista_do_wyswietlenia)
    for i in range(10, 0, -1):
        print(f"\rPozostały czas {i} s do rozpoczęcia gry", end='', flush=True)
        time.sleep(1)
    # print("\r" + " " * 30 + "\rCzas minął!", end='', flush=True)
    print("\n" * 15)
    lista_wpisana = [s.lower() for s in input("Wpisz zapamiętane słowa, oddzielone spacją: ").split()]
    punkty = 0
    bledy = 0
    for slowo in lista_wpisana:
        if slowo in lista_do_wyswietlenia:
            punkty += 1
        else:
            bledy += 1
    # punkty = sum(1 for slowo in lista_wpisana if slowo in lista_do_wyswietlenia) # inny sposób na zliczanie pkt
    print("Koniec gry!")
    return punkty, bledy

def tryb_gry_do_pierwszego_bledu(lista_slow): #na razie nie działa
    punkty = 0
    bledy = 0
    i = 1
    while (bledy != 0): #inna pętla
        lista_do_wyswietlenia = random.sample(lista_slow, i)
        print("Wylosowane słowa:", lista_do_wyswietlenia)
        for j in range(10, 0, -1):
            print(f"\rPozostały czas {j} s do rozpoczęcia gry", end='', flush=True)
            time.sleep(1)
        # print("\r" + " " * 30 + "\rCzas minął!", end='', flush=True)
        print("\n" * 15)
        lista_wpisana = [s.lower() for s in input("Wpisz zapamiętane słowa, oddzielone spacją: ").split()]
        for slowo in lista_wpisana:
            if slowo in lista_do_wyswietlenia:
                punkty += 1
            else:
                bledy += 1
        # punkty = sum(1 for slowo in lista_wpisana if slowo in lista_do_wyswietlenia) # inny sposób na zliczanie pkt
        i += 1
    print("Koniec gry!")
    return punkty

lista_latwych = ["laptop", "lampa", "telefon", "okno", "zegarek", "butelka", "szalik", "sok", "plecak", "mysz", "garnek", "długopis",
                 "nożyczki", "marker", "masło", "ryż", "makaron", "poduszka", "klapki", "gitara", "jabłko", "portfel", "słoik", "czajnik"]

lista_srednich = ["komputer", "rowerzysta", "kalendarz", "dynastia", "przyjaciel", "ogródek", "śniadanie", "zapałki", "torbieli",
                  "ekranowy", "domownik", "zegarowy", "kamizelka", "cukiernia", "kapelusz", "biblioteka", "wędkarstwo", "telefonia",
                  "parasolka", "artysta", "narzędzia", "motylek", "podróżnik", "światło", "zeszytowy"]

lista_trudnych = ["przeziębienie", "oświadczenie", "pożądliwość", "zatrzęsienie", "prześladowca", "żółciopędny", "przysięgający",
                  "błyskotliwość", "współdziałanie", "niewyjaśniony", "półksiężyc", "świadomość", "złożoność", "przemyślenie",
                  "dźwięczność", "łagodniejszy", "niezależność", "zaprzyjaźnić", "zażenowanie", "źreniczność", "nadziejość",
                  "koleżeństwo", "uprzedzenie", "namiętność", "miękkość"]


def main():
    lista =""
    while True:
        poziom_trudności = input("Wpisz poziom trudności (łatwy, średni, trudny): ")
        match poziom_trudności:
            case "łatwy":
                lista = lista_latwych
                break
            case "średni":
                lista = lista_srednich
                break
            case "trudny":
                lista = lista_trudnych
                break
            case _:
                print("Niepoprawny poziom trudności. Wpisz ponownie.")
    tryb_gry = ""
    punkty = 0
    bledy = 0
    while True:
        tryb_gry = input("Wybierz tryb gry (na czas, na ilość, do pierwszego błędu): ")
        match tryb_gry:
            case "na czas":
                punkty, bledy = tryb_gry_na_czas(lista)
                break
            case "na ilość":
                punkty, bledy = tryb_gry_na_ilosc(lista)
                break
            case "do pierwszego błędu":
                punkty, bledy = tryb_gry_do_pierwszego_bledu(lista)
                break
            case _:
                print("Niepoprawny tryb gry. Wpisz ponownie.")
    print("Liczba zdobytych punktów: ", punkty)
    print("Liczba błędów: ", bledy)

if __name__ == "__main__":
    main()

#pierwsza wersja:
"""
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
