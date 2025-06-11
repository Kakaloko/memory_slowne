import random
import time
from operator import contains


def tryb_gry_na_czas(lista_slow):
    czas = int(input("Podaj czas potrzebny na zapamiętanie 10 słów: "))
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
        tworzenie_listy()


def wybor_trybu(lista):
    print("wybierz tryb gry: \n A <-- gra na czas \n B <-- gra na ilosc \n C <-- gra do pierwszego bledu \n cofnij")
    Wybor = input("Wybierz tryb A, B, C lub cofnij : ")
    if Wybor == "A":
        Wynik1 = tryb_gry_na_czas(lista)
        print("Liczba punktów : ", Wynik1[0],"Liczba błędów: ", Wynik1[1] )
        # liczba_SEC = int(input("Wybierz ile chcesz miec czasu na zadanie (w sekundach) : "))
        # lista_do_wyswietlenia = random.sample(lista, 5)
        # print("Wylosowane słowa:", lista_do_wyswietlenia)
        # for i in range(liczba_SEC, 0, -1):
        #     print(f"\rZniknie za {i} sekund...", end='', flush=True)
        #     time.sleep(1)

    elif Wybor == "B":
        Wynik2 = tryb_gry_na_ilosc(lista)
        print("Liczba punktów : ", Wynik2[0], "Liczba błędów: ", Wynik2[1])
        # liczba_SLOW = int(input("Wybierz ile słow chcesz wyswietlac do zapamietania : "))
        # lista_do_wyswietlenia = random.sample(lista, liczba_SLOW)
        # print("Wylosowane słowa:", lista_do_wyswietlenia)
        # for i in range(10, 0, -1):
        #     print(f"\rZniknie za {i} sekund...", end='', flush=True)
        #     time.sleep(1)
    elif Wybor == "C":
        Wynik3 = tryb_gry_do_pierwszego_bledu1(lista)
        print("Liczba punktów : ", Wynik3)

    elif Wybor == "cofnij":
        print("Powrot do wyboru poziomu trudnosci")
        wybor_trybu(tworzenie_listy())

    else:
        print("Nie ma takiego trybu gry")

def main():
    wybor_trybu(tworzenie_listy())
if __name__ == "__main__":
    main()
