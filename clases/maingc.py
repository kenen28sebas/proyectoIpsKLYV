from customtkinter import*

ventana = CTk()
ventana.geometry("500x500")

class Sipi(CTkFrame):
    def __init__(self, master,titulo,ancho,largo,largo2):
        super().__init__(master, width=ancho,height=largo,fg_color="white")
        self.titulo=titulo
        tituloE = CTkLabel(self,text=self.titulo,font=("coolvetica rg",20),text_color="black")
        tituloE.place(x=20,y=0)
        self.caja=CTkEntry(self,border_color="#38184C",border_width=3,width=largo2,fg_color="white",text_color="black")
        self.caja.place(x=20,y=30)
    
    def getEntri(self):
        return self.caja.get()   


sipi1 = Sipi(ventana,"Identificacion",150,70,120)
sipi1.place(x=0,y=0)



ventana.mainloop()