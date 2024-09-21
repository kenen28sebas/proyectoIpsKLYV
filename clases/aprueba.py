from customtkinter import *

class Sipi(CTkFrame):
    def __init__(self, master,titulo,ancho,largo,largo2):
        super().__init__(master, width=ancho,height=largo,fg_color="white")
        self.titulo=titulo
        tituloE = CTkLabel(self,text=self.titulo,font=("Papernotes",25),text_color="black")
        tituloE.place(x=20,y=12)
        self.caja=CTkEntry(self,border_color="#38184C",border_width=3,width=largo2,fg_color="white",text_color="black")
        self.caja.place(x=20,y=50)
    def getEntri(self):
        return self.caja.get()
ventana = CTk()
identificacionn = Sipi(ventana, "Número identificación:", 230, 80, 200)
identificacionn.pack()
btn = CTkButton(ventana,text="dassd",command=lambda:RegistrarP())
btn.pack()
def RegistrarP():
    global identificacionn
    print(identificacionn.getEntri())
    ventana.geometry("1250x700")

    perm=CTkFrame(ventana,width=1250,height=150,border_width=5,border_color="#2c6e49",fg_color="#ffc9b9")
    perm.place(x=0,y=0)

    lbltitulo=CTkLabel(perm,text="Registrar personal medico",text_color="black",font=("Ready For Fall",35))
    lbltitulo.place(x=410,y=50)

  

    frame1=CTkFrame(ventana,width=1250,height=550,fg_color="white")
    frame1.place(x=0,y=150)



    identificacionn = Sipi(frame1, "Número identificación:", 230, 80, 200)
    identificacionn.place(x=300,y=30)


    lugar_exp = Sipi(frame1, "Lugar expedición:", 250, 100, 200)
    lugar_exp.place(x=800,y=30)

    nombre = Sipi(frame1, "Nombres completos:", 230, 80, 200)
    nombre.place(x=50,y=140)

    apellido1 = Sipi(frame1, "Apellido 1:", 230, 80, 200)
    apellido1.place(x=300,y=140)
    apellido2 = Sipi(frame1, "Apellido 2:", 230, 80, 200)
    apellido2.place(x=550,y=140)

     



    email = Sipi(frame1, "Email:", 250, 100, 200)
    email.place(x=550,y=240)

    telefono = Sipi(frame1, "Teléfono:", 250, 100, 200)
    telefono.place(x=800,y=240)

    especialidad=Sipi(frame1,"Especialidad:",250,100,200)
    especialidad.place(x=50,y=340)
        
        

    btnguardar=CTkButton(frame1,border_width=5,border_color="#8338ec",text="Guardar",font=("Papernotes",25),width=120,height=40,fg_color="#e7c6ff",hover_color="#ff99c8",text_color="black",command=lambda:registrarMedico())
    btnguardar.place(x=70,y=480)

    reaca=CTkFrame(frame1,width=340,height=80,border_width=5,border_color="#fb6f92",fg_color="#ffd6ff")

    reaca.place(x=280,y=450)
    reaca.bind("<Button-1>",lambda v:(registrarMedico(especialidad.getEntri())))

    jijiji=CTkLabel(reaca,text="Registrar informacion academica",text_color="black",font=("Papernotes",25))
    jijiji.place(x=10,y=25)


        
        # ob=Medicos(tip_doc.getEntri)

    ob = None

        # ob.setExpLaboral()
    def registrarMedico(texto):
        print(texto)
            # global ob
            # ob=Medicos(tip_doc.getEntri(),identificacionn.getEntri(),fcha_exp.getEntri(),lugar_exp.getEntri(),nombre.getEntri(),apellido1.getEntri(),apellido2.getEntri(),fecha_na.getEntri(),"genero.getEntri()","sexo.getEntri()",telefono.getEntri(),email.getEntri(),especialidad.getEntri())
            # print(ob.getNombres())



            






        # imgfr1= Image.open("negrito.jpg")
        # imgfr1 = imgfr1.resize((150, 150))
        # imagen6 = CTkImage(light_image=imgfr1, size=(150, 150))

        # lblformulario3 = CTkLabel(
        #     master=perm, 
        #     image=imagen6,
        #     text=""
        # )
        # lblformulario3.place(x=900, y=20)



    # def reacademicos():
    #     # global framejose
    #     perm.destroy()
    #     frame1.destroy()
    #     ventana.geometry("1250x700")

    #     frame2=CTkFrame(ventana,width=1250,height=150,border_width=5,border_color="#ff758f",fg_color="#fff0f3")
    #     frame2.place(x=0,y=0)

    #     lbltitulo2=CTkLabel(frame2,text="Registrar informacion academica ",font=("Ready For Fall",30))
    #     lbltitulo2.place(x=330,y=50)

   

    #     framejose=CTkFrame(ventana,fg_color="white",width=1200,height=330,border_width=3,border_color="black")
    #     framejose.place(x=25,y=150)

    #     tituloa=Sipi(framejose,"Titulo:",250,100,200)
    #     tituloa.place(x=50,y=50)

    #     institucion=Sipi(framejose,"Institución:",250,100,200)
    #     institucion.place(x=300,y=50)

    #         # especialidad=Sipi(framejose,"Especialización",250,100,200)
    #         # especialidad.place(x=50,y=150)

    #     btnguardar=CTkButton(framejose,border_width=5,border_color="#8338ec",text="Guardar",font=("Papernotes",25),width=120,height=40,fg_color="#e7c6ff",hover_color="#ff99c8",text_color="black",command=lambda:(registrarAcdd()))
    #     btnguardar.place(x=550,y=260)

    #     reexl=CTkFrame(ventana,width=340,height=80,border_width=5,border_color="#0a9396",fg_color="#90e0ef")
    #     reexl.place(x=700,y=500)
    #     reexl.bind("<Button-1>","")

    #     titulo1=CTkLabel(reexl,text="Registrar experiencia laboral",text_color="black",font=("Papernotes",25))
    #     titulo1.place(x=10,y=25)

    #     #     def registrarAcdd():
    #     #         global ob
    #     #         ob.setAcademicos(tituloa.getEntri(),institucion.getEntri())
                
    #     #     def delreexl():
    #     #         reexl.destroy()
            
    #     # def registrarEl():

        #     # framejose.destroy()
        #     # frame2.destroy()

        #     framee=CTkFrame(ventana,width=1250,height=150,border_width=5,border_color="#ff758f",fg_color="#fff0f3")
        #     framee.place(x=0,y=0)

        #     lbltitulo4=CTkLabel(framee,text="Registrar experiencia laboral ",font=("Ready For Fall",30))
        #     lbltitulo4.place(x=330,y=50)

          

        #     frameel=CTkFrame(ventana,fg_color="white",width=1200,height=330,border_width=3,border_color="black")
        #     frameel.place(x=25,y=150)

        #     empresa=Sipi(frameel,"Empresa:",250,100,200)
        #     empresa.place(x=50,y=50)

        #     cargo=Sipi(frameel,"Cargo:",250,100,200)
        #     cargo.place(x=300,y=50)

 

        #     # especialidad1=Sipi(frameel,"Especialización:",250,100,200)
        #     # especialidad1.place(x=50,y=150)

        #     btnguardar1=CTkButton(frameel,border_width=5,border_color="#8338ec",text="Guardar",font=("Papernotes",25),width=120,height=40,fg_color="#e7c6ff",hover_color="#ff99c8",text_color="black",command=lambda:(registraExpl()))
        #     btnguardar1.place(x=550,y=260)
            
        #     reexl=CTkFrame(ventana,width=340,height=80,border_width=5,border_color="#0a9396",fg_color="#90e0ef")
        #     reexl.place(x=700,y=500)
        #     reexl.bind("<Button-1>",lambda v:confirmacion())
            
        #     titulo1=CTkLabel(reexl,text="Registrar Personal",text_color="black",font=("Papernotes",25))
        #     titulo1.place(x=10,y=25)
            
            
            
        #     def confirmacion ():
        #         global ventana_emergente
        #         try:
        #             print('Confirmacion0')
        #             # global ventana_emergente
        #             # ventana_emergente = CTkToplevel()
        #             # ventana_emergente.title("Ventana Emergente")
        #             # ventana_emergente.geometry("100x80")
        #             # ventana_emergente.lift()
        #             # ventana_emergente.attributes('-topmost', True)
        #             # mi_frame = CTkFrame(ventana_emergente)
        #             # mi_frame.pack(expand=True, fill="both", padx=20, pady=20)
        #             # etiqueta = CTkLabel(mi_frame, text="Përsonal cargado con exito!")
        #             # etiqueta.pack()
        #             # boton = CTkButton(mi_frame, text="Cerrar", command=ventana_emergente.destroy)
        #             # boton.place(x=40,y=40)
        #         except:
        #             # ventana_emergente.title("Ventana Emergente")
        #             # ventana_emergente.geometry("400x300")
        #             # ventana_emergente.lift()
        #             # ventana_emergente.attributes('-topmost', True)
        #             # mi_frame = CTkFrame(ventana_emergente)
        #             # mi_frame.pack(expand=True, fill="both", padx=20, pady=20)
        #             # etiqueta = CTkLabel(mi_frame, text="Error, intentelo nuevamente")
        #             # etiqueta.pack()
        #             # boton = CTkButton(mi_frame, text="Cerrar", command=ventana_emergente.destroy)
        #             # boton.place(x=40,y=40)
        #             print("error")
        

        #     def registraExpl():
        #         global ob

        #         ob.setExpLaboral(empresa.getEntri(),cargo.getEntri())



        #     # def actualizarhv():
        #     #     eduardo.destroy()
        #     #     frame2.destroy()




    

                







                





ventana.mainloop()