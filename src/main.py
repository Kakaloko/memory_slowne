from tkinter import ttk
import tkinter as tk

class Root(tk.Tk):
    def __init__(self, text="Memory słowne"):
        super().__init__()
        self.title(text)
        self.geometry("600x600")
        self.configure(bg="#333446")
       
        self.menu_window()
        
        
    def menu_window(self):
        self.clear()

        self.frame = tk.Frame(self)
        self.frame.configure(bg="#333446")

        play_button = tk.Button(self.frame, text="Graj", bg="#7F8CAA",borderwidth=0, command=self.game_window,)
        play_button.pack()


        statistics_button = tk.Button(self.frame, text="Statystyki",bg="#7F8CAA", command= self.statistics_window)
        statistics_button.pack()
       

        option_button = tk.Button(self.frame, text="Opcje",bg="#7F8CAA", command=self.option_window)
        option_button.pack()
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


    def statistics_window(self):
        self.clear()


    def game_window(self):
        self.clear()

    def option_window(self):
        self.clear()

    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = Root()
    root.mainloop()