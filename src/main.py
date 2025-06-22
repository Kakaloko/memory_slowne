import tkinter as tk
from tkinter import ttk
import random
import time
from operator import contains
import os

STATS_FILE = "statystyki.txt"

class root(tk.Tk):
    def __init__(self, text="Memory słowne"):
        super().__init__()
        self.title(text)
        self.geometry("800x800")
        self.configure(bg="#333446")
        ttk.Style().configure("TButton", 
                                padding=[10,5,10,5],
                                margins=[20,10,20,10],
                                background="#7F8CAA",
                                foreground = "black",
                                borderwidth=2,
                                font=("Impact", 25,))
        self.menu_window()
        
        
    def menu_window(self):
        self.clear()
        
        self.frame = tk.Frame(self)
        self.frame.configure(bg="#333446")

        play_button = ttk.Button(self.frame, text="Graj", style= "TButton",command=self.game_window,)
        play_button.pack()


        statistics_button = ttk.Button(self.frame, text="Statystyki", command= self.statistics_window)
        statistics_button.pack()
      
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def statistics_window(self):
        self.clear()

        stats = []
        with open(STATS_FILE, encoding="windows-1250") as file_stats:
            lines = file_stats.readlines()[2:]  # pomijamy nagłówek i separator
            for line in lines:
                if "|" in line:
                    kolumny = [s.strip() for s in line.strip().split("|")]
                    stats.append(kolumny)

        self.frame = tk.Frame(self)
        self.frame.configure(bg="#333446")

        table_stats = stats_table(self.frame, stats, len(stats), 2)

        back_button = ttk.Button(self, text="Wróć", command=self.menu_window)
        back_button.pack(anchor=tk.NW)

        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def game_window(self):
        self.clear()
        self.amount = 0
        self.mistake = False
        self.level = "Łatwy"
        mode1_button = ttk.Button(self.frame, text="Na Czas ⏰", style= "TButton",command=self.game_choose_time)
        mode1_button.pack()


        mode2_button = ttk.Button(self.frame, text="Na Ilość 📝", command= self.game_choose_amount)
        mode2_button.pack()
       
        mode3_button = ttk.Button(self.frame, text="Do pierwszego błedu ❌", style= "TButton",command=self.game_mistake)
        mode3_button.pack()

        

        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def game_choose_amount(self):
        self.clear()
        self.amount = tk.IntVar()

        entry_label = ttk.Label(self.frame,  text="Wybierz ilość słów", style= "TButton", width= 20)
        entry_label.pack()

        entry = ttk.Entry(self.frame, textvariable= self.amount, style= "TButton", font=(50), width= 20)
        entry.pack()

        self.level_list = ["Łatwy", "Łatwy", "Średni", "Trudny"] #Nie wiem czemu musi być tak ale dziąła dobrze xD
        self.level = tk.StringVar(value="Łatwy")
        level_menu = ttk.OptionMenu(self.frame, self.level , *self.level_list, style="TButton")

        level_menu.pack()

        ok_button = ttk.Button(self.frame, text="OK", command= self.game_amount)
        ok_button.pack()

        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def game_amount(self):
        if self.mistake == False:
            self.level = str(self.level.get())
            self.amount = int(self.amount.get())

        self.clear()

        self.word_list = tworzenie_listy(self.level, self.amount)


        words = tk.Text(self.frame,  height = 4, width = 50)
        words.config(font= ("Arial", 15))
        words.insert(tk.END, self.word_list)
        words.pack(expand=True)
        
        ok_button = ttk.Button(self.frame, text="OK", command= self.write_words)

        ok_button.pack()

        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def game_choose_time(self, time = 5):
        self.clear()
        self.time = tk.IntVar()

        entry_label = ttk.Label(self.frame,  text="Wybierz czas w sekundach", style= "TButton")
        entry_label.pack()

        entry = ttk.Entry(self.frame, textvariable= self.time, style= "TButton", font=(30))
        entry.pack()

        self.level_list = ["Łatwy", "Łatwy", "Średni", "Trudny"] #Nie wiem czemu musi być tak ale dziąła dobrze xD
        self.level = tk.StringVar(value="Łatwy")
        level_menu = ttk.OptionMenu(self.frame, self.level , *self.level_list, style="TButton")
        level_menu.pack()

        ok_button = ttk.Button(self.frame, text="OK", command= self.game_time)
        ok_button.pack()


        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def game_time(self):
        self.clear()
        self.level = str(self.level.get())
        time_left = int(self.time.get())

        self.word_list = tworzenie_listy(self.level)

        words = tk.Text(self.frame,  height = 4, width = 50)
        words.config(font= ("Arial", 15))
        words.insert(tk.END, self.word_list)
        words.pack()
        time_label = ttk.Label(self.frame, text=str(time_left), style= "TButton")
        time_label.pack()
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        while True:
            if time_left <= 0:
                self.write_words()
                break
            else:
                time_label.config(text= time_left)
                self.update()
                time.sleep(1)
                time_left -= 1

    def game_mistake(self):
        
     
  
        self.amount += 1
        self.mistake = True
        if (self.amount > 6 and self.level == "Łatwy") or self.level == "Średni" :
            self.level = "Średni"
        
        if (self.amount > 6 and self.level == "Średni") or self.level == "Trudny":
            self.level = "Trudny"
        else:
            self.level = "Łatwy"
        

        self.game_amount()

  
        


 

    def write_words(self):
        self.clear()
        
        entry_label = ttk.Label(self.frame,  text="Wpisz słowa", style= "TButton")
        entry_label.pack()

        self.answer = tk.StringVar()

        entry = ttk.Entry(self.frame, textvariable= self.answer, style= "TButton", font=(20))
        entry.pack()

        ok_button = ttk.Button(self.frame, text="OK", command= self.game_result)
        ok_button.pack()

        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def game_result(self):
        self.clear()

        # Porównaj odpowiedzi i uzyskaj punkty i błędy
        punkty, bledy = porownanie(self.word_list, str(self.answer.get()))

        
        # Wyświetl wynik gracza
        if self.mistake == False:
        
            result_label = ttk.Label(
                self.frame,
                text=f"Wynik:\n✅ Poprawne: {punkty}\n❌ Błędy: {bledy}",
                style="TButton"
            )
            result_label.pack(pady=10)
            back_button = ttk.Button(self.frame, text="Wróć do menu", command=self.menu_window)
            back_button.pack(pady=10)

            self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
            

        else:
            result_label = ttk.Label(
                self.frame,
                text=f"Przetrwano:\n {self.amount} rundy",
                style="TButton"
            )
            result_label.pack(pady=10)
             # Przycisk powrotu do menu
            back_button = ttk.Button(self.frame, text="Wróć do menu", command=self.menu_window)
            back_button.pack(pady=10)

            self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
  
        
        if bledy == 0 :
            self.game_mistake()

    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.frame = tk.Frame(self)
        self.frame.configure(bg="#333446")

class stats_table:
    def __init__(self, root, list, rows, columns):
        
        # code for creating table
        for i in range(rows):
            for j in range(columns):
                
                self.e = tk.Label(root, width=20, 
                                  text=list[i][j].strip(),
                                fg='#EAEFEF', 
                                bg='#333446',
                                font=('Arial',16,'bold'))
                
                self.e.grid(row=i, column=j)
                
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


def porownanie(wyswietlone, odpowiedz_var):
    odpowiedzi = odpowiedz_var.strip().lower().split()
    odpowiedzi = [s.strip() for s in odpowiedzi if s.strip()]  # usuń puste

    # Tworzymy kopię listy wyświetlonych słów (wszystko małymi literami)
    poprawne_slowa = [s.lower() for s in wyswietlone]

    punkty = 0
    bledy = 0

    for slowo in odpowiedzi:
        if slowo in poprawne_slowa:
            punkty += 1
            poprawne_slowa.remove(slowo)  # usuwamy, by nie liczyć dwa razy tego samego
        else:
            bledy += 1  # słowo nie pasuje

    # Dodaj błędy za pominięte słowa
    bledy += len(poprawne_slowa) - bledy

    zapisz_statystyki(punkty, bledy)

    return punkty, bledy


def tworzenie_listy(tryb="Łatwy", ilosc=5):
    # Mapowanie nazw trybów
    match tryb:
        case "Łatwy":
            tryb = "easy"
        case "Normalny":
            tryb = "normal"
        case "Trudny":
            tryb = "hard"

    sciezka = f"../data/{tryb}_level.csv"

    try:
        with open(sciezka, "r", encoding="utf-8") as plik:
            # Załaduj wszystkie słowa z pliku
            zawartosc = plik.read()
            wszystkie_slowa = [slowo.strip() for slowo in zawartosc.replace('\n', ',').split(',') if slowo.strip()]

            # Losuj `ilosc` słów bez powtórzeń
            if len(wszystkie_slowa) < ilosc:
                print("Zbyt mało słów w pliku!")
                return wszystkie_slowa
            else:
                return random.sample(wszystkie_slowa, ilosc)

    except FileNotFoundError:
        print("Nie znaleziono pliku dla tego trybu.")
        return []


if __name__ == "__main__":
    root_ = root()
    root_.mainloop()