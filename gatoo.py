from interfaz import *
import customtkinter as ctk


class MyFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Ejemplo: Agregar un label y colocarlo usando coordenadas x e y
        self.label = ctk.CTkLabel(self, text="Nombre:")
        self.label.place(x=20, y=20)  # Colocando el label en x=20, y=20

        # Instanciar objetos de tus otras clases (como Sipi o Nopi)
        self.nombre = Sipi(self, "Nombres completos:", 230, 80, 200)
        self.nombre.place(x=100, y=50)  # Colocando en coordenadas x=100, y=50

        self.apellido1 = Sipi(self, "Apellido 1:", 230, 80, 200)
        self.apellido1.place(x=100, y=120)  # Colocando en coordenadas x=100, y=120

        self.apellido2 = Sipi(self, "Apellido 2:", 230, 80, 200)
        self.apellido2.place(x=100, y=190)  # Colocando en coordenadas x=100, y=190

        # Agregar más widgets con coordenadas específicas

# Inicializar la ventana principal y el frame desplazable
app = ctk.CTk()
app.geometry("500x400")

scrollable_frame = MyFrame(app, width=400, height=300)
scrollable_frame.grid(row=0, column=0, padx=20, pady=20)

app.mainloop()