from typing import Any, Tuple
from customtkinter import *
from PIL import Image,ImageTk

import pymongo
# from interfaz import *
from tkcalendar import *
from interfaz import *
from clases.paciente import *
from clases.personalM import *
from clases.persona import *




myclient = pymongo.MongoClient("mongodb://localhost:27017/")
myDb=myclient["proyecto_IPS"]
medico=myDb["Medico"]

# documentos=medico.find({"identificacion":"1233506312"})
# h = documentos[0]["academicos"]
# print(documentos[0]["academicos"][0]["titulo"])








def main():
    ventana = CTk(fg_color="white")
    ventana.title("personal medico")
    ventana.geometry("1250x500")
    cuadrito = CTkFrame(
        master=ventana,
        width=1250,
        height=120,
        fg_color="#f5cac3",
        border_width=5,
        border_color="#fb6f92"

    )

    cuadrito.place(x=0, y=0)  


    titulo = CTkLabel(
        master=cuadrito, 
        text="Menu principal",
        text_color="black",
        font=("Ready For Fall", 30)
    )
    titulo.place(x=500, y=40) 



    global formularioIm2,imagen
    formularioIm2= Image.open("hp.png")
    formularioIm2 = formularioIm2.resize((100, 100))
    imagen = CTkImage(light_image=formularioIm2, size=(100, 100))

    lblformulario2 = CTkLabel(
        master=cuadrito, 
        image=imagen,
        text=""
    )
    lblformulario2.place(x=40, y=10)

    

    boton=CTkButton(ventana,width=300,height=50,border_width=5,border_color="#7209b7",fg_color="#e7c6ff",text="Salir",text_color="black",font=("Ready For Fall",20),hover_color="#ff85a1",command=lambda:Salir())
    boton.place(x=470,y=400)

    jose2=Menu(ventana,"Registrar personal medico",350,170,"frm2.png")
    jose2.place(x=50,y=150)
    jose2.bind("<Button-1>",lambda v:RegistrarP())




    
    def atrasM():
        main()

    def Salir():
        ventana.destroy()

    


    
    def consultarhv():
        jose2.destroy()
        martha.destroy()
        # eduardo.destroy()
        cuadrito.destroy()
        
        
        
        # titulo.destroy()
        frame=CTkFrame(ventana,width=1250,height=500,fg_color="white")
        frame.place(x=0,y=0)

        cuadrito2=CTkFrame(frame,width=1250,height=130,border_width=5,border_color="#685634",fg_color="#ffc9b9")
        cuadrito2.place(x=0,y=0)


        titulo2 = CTkLabel(
        master=cuadrito2, 
        text="Consultar hoja de vida",
        text_color="black",
        font=("Ready For Fall", 30)
        )
        titulo2.place(x=450, y=40)

        caja=CTkEntry(frame,border_width=3,border_color="#0fa3b1",width=300,placeholder_text="Digite su numero de identificacion",height=40)
        # caja.bind("<Button-1>",lambda v:jose())
        caja.place(x=50,y=150)
        caja.get()

        j=caja.get()


        boton2=CTkButton(frame,border_width=3,border_color="#60d394",fg_color="#d9fff8",text="Buscar",height=40,text_color="black",font=("Ready For Fall",20),command=lambda:buscarhv(caja.get()))
        boton2.place(x=350,y=150)

        # boton3=CTkButton(frame,text="Atras",border_width=3,border_color="black",text_color="black",hover_color="#ffb3c6",fg_color="#a9def9",font=("Ready For Fall",25),width=150,height=70,command=lambda:atrasM())
        # boton3.place(x=1000,y=40)

        # atras=Image.open("atras.jpg")
        # atras=atras.resize((80,80))
        # atrass=CTkImage(light_image=atras,size=(80,80))

        # lblatras=CTkLabel(
        #     master=boton3,
        #     image=atrass,
        #     text=""

        # )
        # lblatras.place(x=40,y=15)


        # img2=Image.open("jose.png")
        # img2=img2.resize((100,100))
        # imagen2=CTkImage(light_image=img2,size=(100,100))

        # lblimg2=CTkLabel(
        #     master=cuadrito2,
        #     image=imagen2,
        #     text=""
        # )
        # lblimg2.place(x=40,y=15)

        # def actualizar_hv():
        #     eduardo.destroy()
        #     cuadrito2.destroy()





    def buscarhv(identificacion):
        # frame2.destroy()
        ventana.geometry("1250x500")
        
        documentos=medico.find({"identificacion":identificacion})
        # for i in documentos:
        #     print(i)
        


        frame2=CTkFrame(ventana,width=320,height=150,border_width=5,border_color="#5a189a",fg_color="#dbcae9")
        frame2.place(x=50,y=250)
        
        texto=CTkLabel(frame2,text=f'Nombre:{documentos[0]["nombres"]}',text_color="black",font=("Ready For Fall",22))
        texto.place(x=50,y=90)
        
        

        marta=Image.open("marta.png")
        marta=marta.resize((80,80))
        img=CTkImage(light_image=marta,size=(80,80))

        lblimg=CTkLabel(master=frame2,image=img,text="")
        lblimg.place(x=110,y=10)
        
        # boton3=CTkButton(frame2,text="Consultar",border_width=3,border_color="#a06cd5",fg_color="#e2cfea",text_color="black",font=("Ready For Fall",20))
        # boton3.place(x=90,y=80)
        frame2.bind("<Button-1>",lambda v:jose())








        
        

        def jose():
            
            frame2.destroy()

            ventana.geometry("1250x650")

            

            frame3=CTkFrame(ventana,width=500,height=450,fg_color="white")
            frame3.place(x=0,y=200)
            frame3.bind("<Button-1>",lambda v:academicos())

            # hv=CTkFrame(frame3,width=500,height=400,border_width=3,border_color="black",fg_color="white")
            # hv.place(x=0,y=20)

            tp_id=CTkLabel(frame3,text=f"Tipo de identificacion:{documentos[0]["tipo_documento"]}",text_color="black",font=("Ready For Fall",20))
            tp_id.place(x=40,y=30)
            

            ide=CTkLabel(frame3,text=f"Identificacion:{documentos[0]["identificacion"]}",text_color="black",font=("Ready For Fall",20))
            ide.place(x=40,y=60)
            
            
            
            

            fechaE=CTkLabel(frame3,text=f"Fecha de expedicion:{documentos[0]["fecha_expedicion"]}",text_color="black",font=("Ready For Fall",20))
            fechaE.place(x=40,y=90)

            lugarE=CTkLabel(frame3,text=f"Lugar de expedicion:{documentos[0]["lugar_expedicion"]}",text_color="black",font=("Ready For Fall",20))
            lugarE.place(x=40,y=120)

            nombres=CTkLabel(frame3,text=f"Nombres:{documentos[0]["nombres"]}",text_color="black",font=("Ready For Fall",20))
            nombres.place(x=40,y=150)

            apellido1=CTkLabel(frame3,text=f"Apellido 1:{documentos[0]["apellido1"]}",text_color="black",font=("Ready For Fall",20))
            apellido1.place(x=40,y=180)

            apellido2=CTkLabel(frame3,text=f"Apellido 2:{documentos[0]["apellido2"]}",text_color="black",font=("Ready For Fall",20))
            apellido2.place(x=40,y=210)

            fechaNa=CTkLabel(frame3,text=f"Fecha de nacimiento:{documentos[0]["fecha_nacimiento"]}",text_color="black",font=("Ready For Fall",20))
            fechaNa.place(x=40,y=240)

            genero=CTkLabel(frame3,text=f"Genero:{documentos[0]["genero"]}",text_color="black",font=("Ready For Fall",20))
            genero.place(x=40,y=270)

            sexo=CTkLabel(frame3,text=f"Sexo:{documentos[0]["sexo"]}",text_color="black",font=("Ready For Fall",20))
            sexo.place(x=40,y=300)

            telefono=CTkLabel(frame3,text=f"Telefono:{documentos[0]["telefono"]}",text_color="black",font=("Ready For Fall",20))
            telefono.place(x=40,y=330)

            email=CTkLabel(frame3,text=f"Email:{documentos[0]["email"]}",text_color="black",font=("Ready For Fall",20))
            email.place(x=40,y=360)

            # direccion=CTkLabel(frame3,text=f"Direccion:{documentos[0]["direccion"]}",text_color="black",font=("Ready For Fall",20))
            # direccion.place(x=40,y=390)

            # nacionalidad=CTkLabel(frame3,text=f"Nacionalidad:{documentos[0]["nacionalidad"]}",text_color="black",font=("Ready For Fall",20))
            # nacionalidad.place(x=40,y=390)

            frame4=CTkFrame(ventana,width=350,height=150,border_width=5,border_color="black",fg_color="#ffc2d1")
            frame4.bind("<Button-1>",lambda v:academicos())
            frame4.place(x=600,y=200)
            # frame4.bind("<Button-1>",lambda v:academicos())




            aca=CTkLabel(frame4,text=" Consultar Academicos",text_color="black",font=("Ready For Fall",22))
            
            aca.place(x=50,y=10)


            global img3
            img3= Image.open("academicos.png")
            img3 = img3.resize((80, 80))
            imagen3 = CTkImage(light_image=img3, size=(80, 80))

            lblimg3 = CTkLabel(
                master=frame4, 
                image=imagen3,
                text=""
            )
            lblimg3.place(x=140, y=50)

            # jose()


            

            # acatlo=CTkLabel(frame4,text=f"Titulo:{documentos[0]["academicos"]["titulo"]}",text_color="black",font=("Ready For Fall",18))
            # acatlo.place(x=20,y=50)

            # acains=CTkLabel(frame4,text=f"Institución:{documentos[0]["academicos"]["institución"]}",text_color="black",font=("Ready For Fall",18))
            # acains.place(x=20,y=80)


            # fechaini=CTkLabel(frame4,text=f"Fecha inicio:{documentos[0]["academicos"]["fechaInicio"]}",text_color="black",font=("Ready For Fall",18))
            # fechaini.place(x=20,y=110)

            # fechafn=CTkLabel(frame4,text=f"Fecha fin:{documentos[0]["academicos"]["fechaFin"]}",text_color="black",font=("Ready For Fall",18))
            # fechafn.place(x=20,y=140)

            expL=CTkFrame(ventana,width=350,height=150,border_width=5,border_color="black",fg_color="#ffc2d1")
            expL.place(x=600,y=400)
            expL.bind("<Button-1>",lambda v:experienciaL())


            experiencia=CTkLabel(expL,text=" Consultar Experiencia",text_color="black",font=("Ready For Fall",22))
            experiencia.place(x=50,y=10)


            img4= Image.open("experiencial.png")
            img4 = img4.resize((80, 80))
            imagen4 = CTkImage(light_image=img4, size=(80, 80))

            lblimg4 = CTkLabel(
                master=expL, 
                image=imagen4,
                text=""
            )
            lblimg4.place(x=140, y=50)



#boton atras
            # atras=CTkButton(frame3,width=150,height=80,border_width=5,border_color="black",fg_color="white",text="Atras",font=("Ready For Fall",20),text_color="black")
            # atras.place(x=150,y=300)

            def academicos():
                frame4.destroy()
                ventana.geometry("1250x700")
                # frame4.destroy()
                expL.destroy()
                # frame3.destroy()
                y = 200
                for i in documentos[0]["academicos"]:
                    
                    acadm=CTkFrame(ventana,width=500,height=200,border_width=3,border_color="black",fg_color="white")
                    acadm.place(x=550,y=y)


                    acatlo=CTkLabel(acadm,text=f"Titulo:{i["titulo"]}",text_color="black",font=("Ready For Fall",18))
                    acatlo.place(x=20,y=20)

                    acains=CTkLabel(acadm,text=f"Institución:{i["institucion"]}",text_color="black",font=("Ready For Fall",18))
                    acains.place(x=20,y=50)


                    fechaini=CTkLabel(acadm,text=f"Fecha inicio:{i["fecha_inicio"]}",text_color="black",font=("Ready For Fall",18))
                    fechaini.place(x=20,y=80)

                    fechafn=CTkLabel(acadm,text=f"Fecha fin:{i["fecha_fin"]}",text_color="black",font=("Ready For Fall",18))
                    fechafn.place(x=20,y=110)

                    especialidad=CTkLabel(acadm,text=f"Especialidad:{i["especialidad"]}",text_color="black",font=("Ready For Fall",18))
                    especialidad.place(x=20,y=140)
                    y =y+250
                    boton=CTkButton(ventana,text="Atras",border_width=3,border_color="black",text_color="black",hover_color="#ffb3c6",fg_color="#a9def9",font=("Ready For Fall",25),width=150,height=70)
                    boton.place(x=1100,y=170)
                
            def experienciaL():
                frame4.destroy()
                expL.destroy()
                ventana.geometry("1250x700")
                y=200
                for e in documentos[0]["experiencias_laborales"]:

                    experiencias=CTkFrame(ventana,width=500,height=200,border_width=3,border_color="black",fg_color="white")
                    experiencias.place(x=500,y=y)

                    
                    empresa=CTkLabel(experiencias,text=f"Empresa:{e["empresa"]}",text_color="black",font=("Ready For Fall",18))
                    empresa.place(x=20,y=50)

                    cargo=CTkLabel(experiencias,text=f"Cargo:{e["cargo"]}",text_color="black",font=("Ready For Fall",18))
                    cargo.place(x=20,y=80)

                    FechaI=CTkLabel(experiencias,text=f"Fecha inicio:{e["fecha_inicio"]}",text_color="black",font=("Ready For Fall",18))
                    FechaI.place(x=20,y=110)

                    FechaF=CTkLabel(experiencias,text=f"Fecha fin:{e["fecha_fin"]}",text_color="black",font=("Ready For Fall",18))
                    FechaF.place(x=20,y=140)

                    y=y+250

                    boton2=CTkButton(ventana,text="Atras",border_width=3,border_color="black",text_color="black",hover_color="#ffb3c6",fg_color="#c8b6ff",font=("Ready For Fall",25),width=150,height=70)
                    boton2.place(x=1100,y=170)

    def RegistrarP():
        jose2.destroy()
        martha.destroy()
        eduardo.destroy()
        boton.destroy()
        cuadrito.destroy()
        ventana.geometry("1250x700")

        perm=CTkFrame(ventana,width=1250,height=150,border_width=5,border_color="#2c6e49",fg_color="#ffc9b9")
        perm.place(x=0,y=0)
        perm.bind("<Button-1>",lambda v:reacademicos())

        lbltitulo=CTkLabel(perm,text="Registrar personal medico",text_color="black",font=("Ready For Fall",35))
        lbltitulo.place(x=410,y=50)

        # imgfr= Image.open("personita.png")
        # imgfr = imgfr.resize((120, 120))
        # imagen5 = CTkImage(light_image=imgfr, size=(120, 120))

        # lblformulario2 = CTkLabel(
        #     master=perm, 
        #     image=imagen5,
        #     text=""
        # )
        # lblformulario2.place(x=70, y=10)

        frame1=CTkFrame(ventana,width=1250,height=550,fg_color="white")
        frame1.place(x=0,y=150)
        frame1.bind("<Button-1>",lambda v:reacademicos())

        tip_doc = Nopi(frame1, "Tipo de documento:", 230, 100, ["CC", "TI","Cedula de extrangeria","Registro civil"], 200)
        tip_doc.place(x=50,y=30)

        identificacionn = Sipi(frame1, "Número identificación:", 230, 80, 200)
        identificacionn.place(x=300,y=30)

        fcha_exp = Date(frame1, "Fecha de expedición:")
        fcha_exp.place(x=550,y=30)

        lugar_exp = Sipi(frame1, "Lugar expedición:", 250, 100, 200)
        lugar_exp.place(x=800,y=30)

        nombre = Sipi(frame1, "Nombres completos:", 230, 80, 200)
        nombre.place(x=50,y=140)

        apellido1 = Sipi(frame1, "Apellido 1:", 230, 80, 200)
        apellido1.place(x=300,y=140)

        apellido2 = Sipi(frame1, "Apellido 2:", 230, 80, 200)
        apellido2.place(x=550,y=140)

        fecha_na = Date(frame1, "Fecha de Nacimiento:")
        fecha_na.place(x=800,y=140)

        sexo = Nopi(frame1, "Sexo:", 250, 100, ["Masculino","Femenino"],200)
        sexo.place(x=50,y=240)

        genero = Nopi(frame1, "Género:", 250, 100, ["Hetero","Gay","Lesbiana","Bisexual"], 200)
        genero.place(x=300,y=240)

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
        reaca.bind("<Button-1>",lambda v:reacademicos())

        jijiji=CTkLabel(reaca,text="Registrar informacion academica",text_color="black",font=("Papernotes",25))
        jijiji.place(x=10,y=25)


        # ob=Medicos(tip_doc.getEntri)

        ob = None

        # ob.setExpLaboral()
        def registrarMedico():
            global ob
            ob=Medicos(tip_doc.getEntri(),identificacionn.getEntri(),fcha_exp.getEntri(),lugar_exp.getEntri(),nombre.getEntri(),apellido1.getEntri(),apellido2.getEntri(),fecha_na.getEntri(),genero.getEntri(),sexo.getEntri(),telefono.getEntri(),email.getEntri(),especialidad.getEntri())
            print(ob.getNombres())



            






        # imgfr1= Image.open("negrito.jpg")
        # imgfr1 = imgfr1.resize((150, 150))
        # imagen6 = CTkImage(light_image=imgfr1, size=(150, 150))

        # lblformulario3 = CTkLabel(
        #     master=perm, 
        #     image=imagen6,
        #     text=""
        # )
        # lblformulario3.place(x=900, y=20)



        def reacademicos():
            # global framejose
            perm.destroy()
            frame1.destroy()
            ventana.geometry("1250x700")

            frame2=CTkFrame(ventana,width=1250,height=150,border_width=5,border_color="#ff758f",fg_color="#fff0f3")
            frame2.place(x=0,y=0)

            lbltitulo2=CTkLabel(frame2,text="Registrar informacion academica ",font=("Ready For Fall",30))
            lbltitulo2.place(x=330,y=50)

            imgfra= Image.open("hp.png")
            imgfra = imgfra.resize((100, 100))
            imagenn = CTkImage(light_image=imgfra, size=(100, 100))

            lblformulario3 = CTkLabel(
                master=frame2, 
                image=imagenn,
                text=""
            )
            lblformulario3.place(x=900, y=20)

            framejose=CTkFrame(ventana,fg_color="white",width=1200,height=330,border_width=3,border_color="black")
            framejose.place(x=25,y=150)

            tituloa=Sipi(framejose,"Titulo:",250,100,200)
            tituloa.place(x=50,y=50)

            institucion=Sipi(framejose,"Institución:",250,100,200)
            institucion.place(x=300,y=50)

            fehcaini=Date(framejose,"Fecha inicio:")
            fehcaini.place(x=600,y=50)

            fechafin=Date(framejose,"Fecha de finalización")
            fechafin.place(x=800,y=50)

            # especialidad=Sipi(framejose,"Especialización",250,100,200)
            # especialidad.place(x=50,y=150)

            btnguardar=CTkButton(framejose,border_width=5,border_color="#8338ec",text="Guardar",font=("Papernotes",25),width=120,height=40,fg_color="#e7c6ff",hover_color="#ff99c8",text_color="black",command=lambda:registrarAcdd())
            btnguardar.place(x=550,y=260)

            reexl=CTkFrame(ventana,width=340,height=80,border_width=5,border_color="#0a9396",fg_color="#90e0ef")
            reexl.place(x=700,y=500)
            reexl.bind("<Button-1>",lambda v:registrarEl())

            titulo1=CTkLabel(reexl,text="Registrar experiencia laboral",text_color="black",font=("Papernotes",25))
            titulo1.place(x=10,y=25)

            def registrarAcdd():
                global ob

                ob.setAcademicos(tituloa.getEntri(),institucion.getEntri(),fehcaini.getEntri(),fechafin.getEntri(),)

            def registrarEl():
                # reexl.destroy()
                framejose.destroy()
                frame2.destroy()

            framee=CTkFrame(ventana,width=1250,height=150,border_width=5,border_color="#ff758f",fg_color="#fff0f3")
            framee.place(x=0,y=0)

            lbltitulo4=CTkLabel(framee,text="Registrar experiencia laboral ",font=("Ready For Fall",30))
            lbltitulo4.place(x=330,y=50)

            imgfra= Image.open("hp.png")
            imgfra = imgfra.resize((100, 100))
            imagenn = CTkImage(light_image=imgfra, size=(100, 100))

            lblformulario3 = CTkLabel(
                master=framee, 
                image=imagenn,
                text=""
            )
            lblformulario3.place(x=900, y=20)

            frameel=CTkFrame(ventana,fg_color="white",width=1200,height=330,border_width=3,border_color="black")
            frameel.place(x=25,y=150)

            empresa=Sipi(frameel,"Empresa:",250,100,200)
            empresa.place(x=50,y=50)

            cargo=Sipi(frameel,"Cargo:",250,100,200)
            cargo.place(x=300,y=50)

            fehcaini1=Date(frameel,"Fecha inicio:")
            fehcaini1.place(x=600,y=50)

            fechafin1=Date(frameel,"Fecha de finalización:")
            fechafin1.place(x=800,y=50)

            # especialidad1=Sipi(frameel,"Especialización:",250,100,200)
            # especialidad1.place(x=50,y=150)

            btnguardar1=CTkButton(frameel,border_width=5,border_color="#8338ec",text="Guardar",font=("Papernotes",25),width=120,height=40,fg_color="#e7c6ff",hover_color="#ff99c8",text_color="black",command=lambda:registraExpl())
            btnguardar1.place(x=550,y=260)

            def registraExpl():
                global ob

                ob.setExpLaboral(empresa.getEntri(),cargo.getEntri(),fechafin1.getEntri(),fechafin1.getEntri())



            # def actualizarhv():
            #     eduardo.destroy()
            #     frame2.destroy()




    

                







                





            

    martha=Menu(ventana,"Consultar hoja de vida",350,170,"C:\\Users\\linit\\OneDrive\\Escritorio\\proyectoIpsKLYV\\fml m.png")
    martha.place(x=450,y=150)
    martha.bind("<Button-1>",lambda v:consultarhv())

    eduardo=Menu(ventana,"Actualizar hoja de vida",350,170,"C:\\Users\\linit\\OneDrive\\Escritorio\\proyectoIpsKLYV\\eduardo.png")
    eduardo.place(x=850,y=150)
    # eduardo.bind("<Button-1>",lambda v:actualizar_hv())






        



    ventana.mainloop()




class Menu(CTkFrame):


    def __init__(self, master,titulo,ancho,largo,imagen):
        super().__init__(master,width=ancho,height=largo,fg_color="#BBF5BF",border_color="#386641",border_width=5)
        self.titulo=titulo
        # self.titulo.place(x=50,y=45)
        # self.image = Image.open(imagen)
        # self.image = self.image.resize((100, 100)) 
        
        
        # self.ctk_image = CTkImage(light_image=self.image, size=(100, 100))
        
    
        # self.lblimg = CTkLabel(self, image=self.ctk_image, text="")
        # self.lblimg.place(x=125, y=55)

        # self.title_label = CTkLabel(self, text=titulo,font=("Ready For Fall",25))
        # self.title_label.place(x=17, y=10)





#jose tu papa 
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




class Nopi(CTkFrame):
    def __init__(self, master, titulo,ancho,largo,opciones,largo2):
        super().__init__(master,width=ancho,height=largo,fg_color="white")
        self.titulo=titulo
        ttlo=CTkLabel(self,text=self.titulo,font=("Papernotes",25))
        ttlo.place(x=20,y=12)
        self.combo=CTkComboBox(self,values=opciones,border_color="#38184C",border_width=3,width=largo2,font=("coolvetica rg",18),dropdown_fg_color="#fae0e4",button_hover_color="#ff7096",button_color="#e7c6ff")
        self.combo.place(x=20,y=50)

    def getEntri(self):
        return self.combo.get()
    





class Date(CTkFrame):
    def __init__(self, master, titulo):
        super().__init__(master, width=250, height=100, fg_color="white")
        self.titulo = titulo
    
        ttlD = CTkLabel(self, text=self.titulo, font=("Papernotes", 25))
        ttlD.place(x=20,y=12)
        
        self.j = DateEntry(self, width=20, background='#ff8fab', foreground='black', borderwidth=3, font=('Papernotes', 12))
        self.j.place(x=40,y=70)
    def getEntri(self):
        return self.j.get()






#         def crearpm():
#             jose.destroy

# nombre = Sipi(barra, "Nombres completos:", 230, 80, 200)
# nombre.grid(row=1, column=0, padx=10, pady=10)

# apellido1 = Sipi(barra, "Apellido 1:", 230, 80, 200)
# apellido1.grid(row=1, column=1, padx=10, pady=10)

# apellido2 = Sipi(barra, "Apellido 2:", 230, 80, 200)
# apellido2.grid(row=2, column=0, padx=10, pady=10)

# identificacion = Sipi(barra, "Número identificación:", 230, 80, 200)
# identificacion.grid(row=2, column=1, padx=10, pady=10)
# identificacion.validar()

# fcha_exp = Date(barra, "Fecha de expedición:")
# fcha_exp.grid(row=3, column=0, padx=10, pady=10)

# tip_doc = Nopi(barra, "Tipo de documento:", 230, 100, ["CC", "TI"], 200)
# tip_doc.grid(row=3, column=1, padx=10, pady=10)

# lugar_exp = Sipi(barra, "Lugar expedición:", 250, 100, 200)
# lugar_exp.grid(row=4, column=0, padx=10, pady=10)

# fecha_na = Date(barra, "Fecha de Nacimiento:")
# fecha_na.grid(row=4, column=1, padx=10, pady=10)

# genero = Nopi(barra, "Género:", 250, 100, ["sdkn","jndckj","jsdndjn"], 200)
# genero.grid(row=5, column=0, padx=10, pady=10)

# sexo = Nopi(barra, "Sexo:", 250, 100, ["Masculino","Femenino"],200)
# sexo.grid(row=5, column=1, padx=10, pady=10)

# telefono = Sipi(barra, "Teléfono:", 250, 100, 200)
# telefono.grid(row=6, column=0, padx=10, pady=10)
# telefono.validar()

# email = Sipi(barra, "Email:", 250, 100, 200)
# email.grid(row=6, column=1, padx=10, pady=10)

# especialidad = Sipi(barra, "Especialidad:", 250, 100, 200)
# especialidad.grid(row=7, column=0, padx=10, pady=10)


# h = None

# def cargarPm (th):
#     ob = th.crearPm(nombre.getEntri(),identificacion.getEntri(),fcha_exp.getEntri(),lugar_exp.getEntri(),nombre.getEntri(),apellido1.getEntri(),apellido2.getEntri(),genero.getEntri(),sexo.getEntri(),telefono.getEntri(),email.getEntri(),especialidad.getEntri())
#     return ob

# def hola (th):
#     ob = th.crearPm(nombre.getEntri(),identificacion.getEntri(),fcha_exp.getEntri(),lugar_exp.getEntri(),nombre.getEntri(),apellido1.getEntri(),apellido2.getEntri(),genero.getEntri(),sexo.getEntri(),telefono.getEntri(),email.getEntri(),especialidad.getEntri(),"s")
#     h = ob
#     print(h.getNombres())
#     print(h.getFechaExp())

# botonS=CTkButton(barra,width=300,height=50,fg_color="#deaaff",border_width=3,border_color="#5a189a",text="Guardar",font=("Ready For Fall",20),text_color="black",command=lambda:hola())
# botonS.place(x=300,y=730)




if __name__ == '__main__':
    ejemplo = main()
    ejemplo.mainloop()
