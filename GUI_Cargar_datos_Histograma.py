import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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
            self.show_data()

    def load_excel_data(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
        if file_path:
            self.data = pd.read_excel(file_path)
            self.show_data()

    def show_data(self):
        top = tk.Toplevel(self.master)
        top.title("Datos Cargados")
        
        # Creamos una tabla de datos utilizando un widget Treeview de tkinter
        columns = list(self.data.columns)
        tree = tk.ttk.Treeview(top, columns=columns, show="headings")
        for col in columns:
            tree.heading(col, text=col)
        for row in self.data.itertuples():
            tree.insert("", "end", values=tuple(row[1:]))
        tree.pack(side="top", fill="both", expand=True)
        
        # Creamos un botón para mostrar el histograma
        button = tk.Button(top, text="Mostrar Histograma", command=self.show_histogram)
        button.pack(side="bottom")

    def show_histogram(self):
        fig, ax = plt.subplots()
        ax.hist(self.data.iloc[:, 0], bins=10)
        ax.set_xlabel(self.data.columns[0])
        ax.set_ylabel("Frecuencia")
        canvas = FigureCanvasTkAgg(fig, master=self.master)
        canvas.draw()
        canvas.get_tk_widget().pack(side="top", fill="both", expand=True)

root = tk.Tk()
app = App(master=root)
app.mainloop()
