import tkinter as tk


class Interfaz(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora de Área Limpiable")
        
        self.label_habitacion = tk.Label(self, text="Dimensiones de la habitación:")
        self.label_habitacion.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

        self.label_longitud = tk.Label(self, text="Longitud (metros):")
        self.label_longitud.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.entry_longitud = tk.Entry(self)
        self.entry_longitud.grid(row=1, column=1, padx=10, pady=5)

        self.label_ancho = tk.Label(self, text="Ancho (metros):")
        self.label_ancho.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.entry_ancho = tk.Entry(self)
        self.entry_ancho.grid(row=2, column=1, padx=10, pady=5)

        self.label_mueble = tk.Label(self, text="Dimensiones del mueble:")
        self.label_mueble.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

        self.label_ancho_mueble = tk.Label(self, text="Ancho (metros):")
        self.label_ancho_mueble.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
        self.entry_ancho_mueble = tk.Entry(self)
        self.entry_ancho_mueble.grid(row=4, column=1, padx=10, pady=5)

        self.label_altura_mueble = tk.Label(self, text="Altura (metros):")
        self.label_altura_mueble.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)
        self.entry_altura_mueble = tk.Entry(self)
        self.entry_altura_mueble.grid(row=5, column=1, padx=10, pady=5)

        self.button_calcular = tk.Button(self, text="Calcular Área Limpiable", command=self.calcular_area_limpiable)
        self.button_calcular.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        self.label_resultado = tk.Label(self, text="")
        self.label_resultado.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

        # Canvas para dibujar la habitación y el mueble
        self.canvas_dibujo = tk.Canvas(self, width=400, height=300, bg="white")
        self.canvas_dibujo.grid(row=0, column=2, rowspan=8, padx=10, pady=10)

    def calcular_area_limpiable(self):
        # Obtener dimensiones de la habitación y del mueble
        longitud = float(self.entry_longitud.get())
        ancho = float(self.entry_ancho.get())
        ancho_mueble = float(self.entry_ancho_mueble.get())
        altura_mueble = float(self.entry_altura_mueble.get())

        # Calcular coordenadas para dibujar la habitación centrada
        centro_x, centro_y = 200, 150
        mitad_longitud, mitad_ancho = (longitud * 20) / 2, (ancho * 20) / 2
        x1, y1 = centro_x - mitad_longitud, centro_y - mitad_ancho
        x2, y2 = centro_x + mitad_longitud, centro_y + mitad_ancho

        # Dibujar la habitación con un fondo gris claro
        self.canvas_dibujo.delete("habitacion")  # Limpiar dibujo anterior
        self.canvas_dibujo.create_rectangle(x1, y1, x2, y2, outline="blue", fill="#D3D3D3", width=2, tags="habitacion")

        # Calcular coordenadas para dibujar el mueble centrado dentro de la habitación
        x1_mueble, y1_mueble = centro_x - (ancho_mueble * 10), centro_y - (altura_mueble * 10)
        x2_mueble, y2_mueble = centro_x + (ancho_mueble * 10), centro_y + (altura_mueble * 10)

        # Dibujar el mueble con un fondo más oscuro
        self.canvas_dibujo.create_rectangle(x1_mueble, y1_mueble, x2_mueble, y2_mueble, outline="red", fill="#A9A9A9", width=2, tags="mueble")

        # Calcular área limpiable
        area_total = longitud * ancho
        area_mueble = ancho_mueble * altura_mueble
        area_limpiable = area_total - area_mueble

        # Mostrar el área limpiable
        self.label_resultado.config(text=f"Área limpiable: {area_limpiable:.2f} metros cuadrados")


if __name__ == "__main__":
    app = Interfaz()
    app.mainloop()