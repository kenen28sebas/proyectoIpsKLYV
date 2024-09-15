from interfaz import *




nombre = Sipi(barra, "Nombres completos:", 230, 80, 200)
nombre.grid(row=1, column=0, padx=10, pady=10)

apellido1 = Sipi(barra, "Apellido 1:", 230, 80, 200)
apellido1.grid(row=1, column=1, padx=10, pady=10)

apellido2 = Sipi(barra, "Apellido 2:", 230, 80, 200)
apellido2.grid(row=2, column=0, padx=10, pady=10)

identificacion = Sipi(barra, "Número identificación:", 230, 80, 200)
identificacion.grid(row=2, column=1, padx=10, pady=10)
identificacion.validar()

fcha_exp = Date(barra, "Fecha de expedición:")
fcha_exp.grid(row=3, column=0, padx=10, pady=10)

tip_doc = Nopi(barra, "Tipo de documento:", 230, 100, ["CC", "TI"], 200)
tip_doc.grid(row=3, column=1, padx=10, pady=10)

lugar_exp = Sipi(barra, "Lugar expedición:", 250, 100, 200)
lugar_exp.grid(row=4, column=0, padx=10, pady=10)

fecha_na = Date(barra, "Fecha de Nacimiento:")
fecha_na.grid(row=4, column=1, padx=10, pady=10)

genero = Nopi(barra, "Género:", 250, 100, ["Masculino", "Femenino", "Otro"], 200)
genero.grid(row=5, column=0, padx=10, pady=10)

sexo = Sipi(barra, "Sexo:", 250, 100, 200)
sexo.grid(row=5, column=1, padx=10, pady=10)

telefono = Sipi(barra, "Teléfono:", 250, 100, 200)
telefono.grid(row=6, column=0, padx=10, pady=10)
telefono.validar()

email = Sipi(barra, "Email:", 250, 100, 200)
email.grid(row=6, column=1, padx=10, pady=10)

especialidad = Sipi(barra, "Especialidad:", 250, 100, 200)
especialidad.grid(row=7, column=0, padx=10, pady=10)


# h = None

# def cargarPm (th):
#     ob = th.crearPm(nombre.getEntri(),identificacion.getEntri(),fecha_exp.getEntri(),lugar_exp.getEntri(),nombre.getEntri(),apellido1.getEntri(),apellido2.getEntri(),genero.getEntri(),sexo.getEntri(),telefono.getEntri(),email.getEntri(),especialidad.getEntri())
#     return ob

# def hola (th):
#     ob = th.crearPm(nombre.getEntri(),identificacion.getEntri(),fecha_exp.getEntri(),lugar_exp.getEntri(),nombre.getEntri(),apellido1.getEntri(),apellido2.getEntri(),genero.getEntri(),sexo.getEntri(),telefono.getEntri(),email.getEntri(),especialidad.getEntri(),"s")
#     h = ob
#     print(h.getNombres())

# btn = CTkButton(ventana,text="vive la vida",command=lambda:hola(p1))
# btn.place(x=0,y=0)




ventana.mainloop()






# ejemplo = Sipi(ventana,"lina la mas bonita",100,200)
# ejemplo.place(x=10,y=10)

# ejmeplo2 = CTkLabel(ventana,text="kenen es menos bonito que lina")
# ejmeplo2.place(x=10,y=50)

# ejmeplo3 = Sipi(ventana,"yhoneida no se baña",200,300)
# ejmeplo3.place(x=10,y=80)