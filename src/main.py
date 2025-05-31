from tkinter import ttk
import tkinter as tk

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
       

        option_button = ttk.Button(self.frame, text="Opcje", command=self.option_window)
        option_button.pack()
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

    def option_window(self):
        self.clear()

    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()


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
    
