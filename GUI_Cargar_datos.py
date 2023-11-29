import tkinter as tk
from tkinter import filedialog
import pandas as pd

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.load_csv_button = tk.Button(self, text="Cargar Datos CSV", command=self.load_csv_data)
        self.load_csv_button.pack(side="top")
        self.load_excel_button = tk.Button(self, text="Cargar Datos Excel", command=self.load_excel_data)
        self.load_excel_button.pack(side="top")
        self.quit_button = tk.Button(self, text="Salir", fg="red", command=self.master.destroy)
        self.quit_button.pack(side="bottom")

    def load_csv_data(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            self.data = pd.read_csv(file_path)
            print(self.data.head())

    def load_excel_data(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
        if file_path:
            self.data = pd.read_excel(file_path)
            print(self.data.head())

root = tk.Tk()
app = App(master=root)
app.mainloop()
