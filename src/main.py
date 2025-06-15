from tkinter import ttk
import tkinter as tk
import time


class root(tk.Tk):
    def __init__(self, text="Memory słowne"):
        super().__init__()
        self.title(text)
        self.geometry("600x600")
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
        with open("../data/stats.txt", encoding="utf-8") as file_stats:
            stats = [line.strip().split(",") for line in file_stats]

        self.frame = tk.Frame(self)
        self.frame.configure(bg="#333446")

        table_stats = stats_table(self.frame, stats, len(stats), 2)

        back_button = ttk.Button(self, text="Wróć", command=self.menu_window)
        back_button.pack(anchor=tk.NW)

        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def game_window(self):
        self.clear()
       

        mode1_button = ttk.Button(self.frame, text="Na Czas ⏰", style= "TButton",command=self.game_choose_time,)
        mode1_button.pack()


        mode2_button = ttk.Button(self.frame, text="Na Ilość 📝", command= self.game_choose_amount)
        mode2_button.pack()
       
        mode3_button = ttk.Button(self.frame, text="Do pierwszego błedu ❌", style= "TButton",command=self.game_mistake,)
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
        self.level = str(self.level.get())
        self.amount = int(self.amount.get())

        self.clear()

        
        words = ttk.Label(self.frame,  text="tu będą słowa", style= "TButton")
        words.pack()
        
        ok_button = ttk.Button(self.frame, text="OK", command= self.write_words)
        ok_button.pack()

        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def game_choose_time(self, time = 5):
        self.clear()
        self.time = tk.IntVar()

        entry_label = ttk.Label(self.frame,  text="Wybierz czas w sekundach", style= "TButton")
        entry_label.pack()

        entry = ttk.Entry(self.frame, textvariable= self.time, style= "TButton", font=(20))
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

        words = ttk.Label(self.frame,  text="tu będą słowa", style= "TButton")
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
        self.clear()
        
 

    def write_words(self):
        self.clear()
        
        entry_label = ttk.Label(self.frame,  text="Podane słowa", style= "TButton")
        entry_label.pack()

        self.answer = tk.StringVar()

        entry = ttk.Entry(self.frame, textvariable= self.answer, style= "TButton", font=(20))
        entry.pack()

        ok_button = ttk.Button(self.frame, text="OK", command= self.game_result)
        ok_button.pack()

        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def game_result(self):
        self.clear()
        
        result_label= ttk.Label(self.frame,  text="Wynik", style= "TButton")
        result_label.pack()
        
        back_button = ttk.Button(self.frame, text="Wróć", command=self.menu_window)
        back_button.pack()

        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
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
                

if __name__ == "__main__":
    root_ = root()
    root_.mainloop()
    
