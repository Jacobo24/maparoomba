import tkinter as tk
class Habitacion:
    def __init__(self, longitud, ancho):
        self.longitud = longitud
        self.ancho = ancho

    def area(self):
        return self.longitud * self.ancho


class Mueble:
    def __init__(self, ancho, altura):
        self.ancho = ancho
        self.altura = altura

    def area(self):
        return self.ancho * self.altura


def calcular_area_limpiable(habitacion, mueble):
    area_total = habitacion.area()
    area_mueble = mueble.area()
    area_limpiable = area_total - area_mueble
    return area_limpiable
class Interfaz(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora de Área Limpiable")
        
        self.label_habitacion = tk.Label(self, text="Dimensiones de la habitación:")
        self.label_habitacion.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

        self.label_longitud = tk.Label(self, text="Longitud (metros):")
        self.label_longitud.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.entry_longitud = tk.Entry(self)
        self.entry_longitud.grid(row=1, column=1, padx=10, pady=5)

        self.label_ancho = tk.Label(self, text="Ancho (metros):")
        self.label_ancho.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.entry_ancho = tk.Entry(self)
        self.entry_ancho.grid(row=2, column=1, padx=10, pady=5)

        self.label_mueble = tk.Label(self, text="Dimensiones del mueble:")
        self.label_mueble.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)

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

    def calcular_area_limpiable(self):
        longitud = float(self.entry_longitud.get())
        ancho = float(self.entry_ancho.get())
        ancho_mueble = float(self.entry_ancho_mueble.get())
        altura_mueble = float(self.entry_altura_mueble.get())

        area_total = longitud * ancho
        area_mueble = ancho_mueble * altura_mueble
        area_limpiable = area_total - area_mueble

        self.label_resultado.config(text=f"Área limpiable: {area_limpiable:.2f} metros cuadrados")


if __name__ == "__main__":
    app = Interfaz()
    app.mainloop()