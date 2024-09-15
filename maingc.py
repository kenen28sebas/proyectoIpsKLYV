from interfaz import*

ventana = CTk(fg_color="white")

ventana.geometry("1000x650")

header=CTkFrame(
    master=ventana,
    width=1000,
    height=100,
    fg_color="#44E3D3",
    corner_radius=0
)
secction1=CTkFrame(master=ventana,
    width=960,
    height=510,
    fg_color="#44E3D3")

secction1.place(x=20,y=120)
header.place(x=0, y=0)

vnVusuario = CTkToplevel(ventana, width=400, height=400)

titulo = CTkLabel(vnVusuario,text="Buscar paciente")
titulo.place(x=150,y=40)

cajaTexto = Sipi(vnVusuario,"No de documento",320, 80, 280)
cajaTexto.place(x=40,y=90) 





ventana.mainloop()