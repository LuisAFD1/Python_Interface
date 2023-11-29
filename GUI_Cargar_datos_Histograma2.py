import tkinter as tk
from tkinter import filedialog
import pandas as pd
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(fill='both', expand=True)
        self.create_widgets()

    def create_widgets(self):
        self.load_button = tk.Button(self, text="Cargar Datos", command=self.load_data)
        self.load_button.grid(row=0, column=0, sticky='w')
        self.quit_button = tk.Button(self, text="Salir", fg="red", command=self.master.destroy)
        self.quit_button.grid(row=0, column=1, sticky='e')

        self.frame_table = tk.Frame(self)
        self.frame_table.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

    def load_data(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv"), ("Excel Files", "*.xlsx")])
        if file_path:
            if file_path.endswith('.csv'):
                self.data = pd.read_csv(file_path)
            else:
                self.data = pd.read_excel(file_path)
            self.create_table()

    def create_table(self):
        # Limpiar la tabla existente
        for widget in self.frame_table.winfo_children():
            widget.destroy()

        # Crear un scrollbar
        scrollbar = tk.Scrollbar(self.frame_table)
        scrollbar.grid(row=0, column=1, sticky='ns')

        # Crear un treeview
        tree = ttk.Treeview(self.frame_table, yscrollcommand=scrollbar.set)
        tree['columns'] = list(self.data.columns)
        for col in tree['columns']:
            tree.heading(col, text=col)
        for index, row in self.data.iterrows():
            tree.insert('', index, text=index, values=list(row))

        # Configurar scrollbar
        scrollbar.config(command=tree.yview)

        # Colocar treeview en el frame
        tree.grid(row=0, column=0, sticky='nsew')
        self.frame_table.rowconfigure(0, weight=1)
        self.frame_table.columnconfigure(0, weight=1)

        # Crear botón para histograma
        self.hist_button = tk.Button(self, text="Mostrar Histograma", command=self.show_histogram)
        self.hist_button.grid(row=2, column=0, padx=10, pady=10, sticky='w')

    def show_histogram(self):
        # Crear la figura y el gráfico de barras
        fig, ax = plt.subplots()
        ax.hist(self.data.iloc[:, 0])

        # Colocar el gráfico en un widget de tkinter
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().grid(row=3, column=0, padx=10, pady=10, sticky='nsew')

        # Crear botón para cerrar el histograma
        self.close_button = tk.Button(self, text="Cerrar Histograma", command=lambda: canvas.get_tk_widget().destroy())
        self.close_button.grid(row=2, column=1, padx=10, pady=10, sticky='e')


root = tk.Tk()
app = App(master=root)
app.mainloop()
