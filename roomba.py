import tkinter as tk

class Interfaz(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mapa de Roomba")

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

        self.label_velocidad = tk.Label(self, text="Velocidad de la Roomba (km/h):")
        self.label_velocidad.grid(row=6, column=0, padx=10, pady=5, sticky=tk.W)
        self.entry_velocidad = tk.Entry(self)
        self.entry_velocidad.grid(row=6, column=1, padx=10, pady=5)

        self.button_calcular = tk.Button(self, text="Calcular Área Limpiable y Tiempo", command=self.calcular_area_tiempo)
        self.button_calcular.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

        self.label_resultado_area = tk.Label(self, text="")
        self.label_resultado_area.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

        self.label_resultado_tiempo = tk.Label(self, text="")
        self.label_resultado_tiempo.grid(row=9, column=0, columnspan=2, padx=10, pady=5)

        self.canvas_dibujo = tk.Canvas(self, width=400, height=300, bg="white")
        self.canvas_dibujo.grid(row=0, column=2, rowspan=10, padx=10, pady=10)
        self.canvas_dibujo.create_text(200, 20, text="Mapa de Roomba", font=("Arial", 14), fill="black")

    def calcular_area_tiempo(self):
        longitud = float(self.entry_longitud.get())
        ancho = float(self.entry_ancho.get())
        ancho_mueble = float(self.entry_ancho_mueble.get())
        altura_mueble = float(self.entry_altura_mueble.get())

        velocidad_roomba = float(self.entry_velocidad.get())

        centro_x, centro_y = 200, 150
        mitad_longitud, mitad_ancho = (longitud * 20) / 2, (ancho * 20) / 2
        x1, y1 = centro_x - mitad_longitud, centro_y - mitad_ancho
        x2, y2 = centro_x + mitad_longitud, centro_y + mitad_ancho

        self.canvas_dibujo.delete("habitacion")
        self.canvas_dibujo.create_rectangle(x1, y1, x2, y2, outline="blue", fill="#ADD8E6", width=2, tags="habitacion")

        x1_mueble, y1_mueble = centro_x - (ancho_mueble * 10), centro_y - (altura_mueble * 10)
        x2_mueble, y2_mueble = centro_x + (ancho_mueble * 10), centro_y + (altura_mueble * 10)

        self.canvas_dibujo.create_rectangle(x1_mueble, y1_mueble, x2_mueble, y2_mueble, outline="red", fill="#8B4513", width=2, tags="mueble")

        area_total = longitud * ancho
        area_mueble = ancho_mueble * altura_mueble
        area_limpiable = area_total - area_mueble

        tiempo_limpiar_segundos = area_limpiable / (velocidad_roomba / 3600)
        horas = int(tiempo_limpiar_segundos / 3600)
        minutos = int((tiempo_limpiar_segundos % 3600) / 60)
        segundos = int(tiempo_limpiar_segundos % 60)

        self.label_resultado_area.config(text=f"Área limpiable: {area_limpiable:.2f} metros cuadrados")
        self.label_resultado_tiempo.config(text=f"Tiempo necesario para limpiar: {horas} horas, {minutos} minutos y {segundos} segundos")


if __name__ == "__main__":
    app = Interfaz()
    app.mainloop()