from typing import Any, Tuple
from customtkinter import *
from PIL import Image
from tkcalendar import *
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
myDb=myclient["proyecto_IPS"]
historias=myDb["Historias"]



def main():
    ventana=CTk(fg_color="white")
    ventana.title ("Menu principal del paciente")
    ventana.geometry("900x500")


    frametl=CTkFrame(ventana,width=900,height=100,border_color="#5603ad",fg_color="#c2f8cb",border_width=5)
    frametl.place(x=0,y=0)

    tituloframe=CTkLabel(frametl,text="Menu principal",font=("Ready For Fall",30),text_color="black")
    tituloframe.place(x=350,y=30)









        


    opcion1=Opciones(ventana,"Consultar HC","eduardo.png")
    opcion1.place(x=50,y=180)
    opcion1.bind("<Button-1>",lambda v:consultarhc())

    opcion2=Opciones(ventana,"Crear HC","buscar.png")
    opcion2.place(x=500,y=180)
    opcion2.bind("<Button-1>",lambda v:CrearHc())


    # opcion3=Opciones(ventana,)
    

    def consultarhc():
        opcion1.destroy()
        opcion2.destroy()
        frametl.destroy()
        

        ventana.geometry("900x500")



        frmtitulo=CTkFrame(ventana,width=900,height=120,border_width=5,border_color="#00c49a",fg_color="#72ddf7")
        frmtitulo.place(x=0,y=0)

        lbltitulo=CTkLabel(frmtitulo,text="Consultar historia clinica",font=("Ready For Fall",30))
        lbltitulo.place(x=280,y=30)

        caja=CTkEntry(ventana,border_width=3,border_color="#0fa3b1",width=300,placeholder_text="Digite su numero de identificacion",height=40)
    
        caja.place(x=50,y=150)
        caja.get()

        j=caja.get()


        boton2=CTkButton(ventana,border_width=3,border_color="#60d394",fg_color="#d9fff8",text="Buscar",height=40,text_color="black",font=("Ready For Fall",20),command=lambda:buscarhc(caja.get()))
        boton2.place(x=350,y=150)
    
        def buscarhc(identificacion):
            ventana.geometry("900x500")
            documentos=historias.find({"numero_identificacion":identificacion})

            mostrardatos=CTkFrame(ventana,width=320,height=150,border_width=5,border_color="#5a189a",fg_color="#dbcae9")
            mostrardatos.place(x=50,y=250)
            mostrardatos.bind("<Button-1>",lambda v:opcionesc())

            texto=CTkLabel(mostrardatos, text=f'Nombre: {documentos[0]["nombres"]}', text_color="black", font=("Ready For Fall",22))

            texto.place(x=30,y=90)


            img2=Image.open("señora.png")
            img2=img2.resize((80,80))
            imagen2=CTkImage(light_image=img2,size=(80,80))

            lblimg2=CTkLabel(
                master=mostrardatos,
                image=imagen2,
                text=""
            )
            lblimg2.place(x=120,y=10)

            def opcionesc():
                mostrardatos.destroy()
                frmtitulo.destroy()
                caja.destroy()
                boton2.destroy()

                ventana.geometry("800x500")

                framerlt=CTkFrame(ventana,width=800,height=100,border_width=5,border_color="#5a189a",fg_color="#b8b8ff")
                framerlt.place(x=0,y=0)

                titulo=CTkLabel(framerlt,text="Seleccione una opcion",font=("Ready For Fall",25),text_color="black")
                titulo.place(x=250,y=30)

                opcionhc1=CrearHistoriac(ventana,"#ff5d8f","#ffcad4","Consultar anamnesis","anamnesis.png",18)
                opcionhc1.place(x=50,y=120)
                opcionhc1.bind("<Button-1>",lambda v:consultaranamnesis())

                # opcionhc2=CrearHistoriac(ventana,"#006600","#80ffdb","Consultar signos vitales","signos.png",18)
                # opcionhc2.place(x=50,y=280)

                opcionhc3=CrearHistoriac(ventana,"#00a8e8","#b8f2e6","Consultar Diagnosticos","anamnesis 2.webp",18)
                opcionhc3.place(x=350,y=120)
                opcionhc3.bind("<Button-1>",lambda v:diagnostico())



                opcionhc4=CrearHistoriac(ventana,"#fe6d73","white","Consultar Formulas M","anamnesis 2.webp",18)
                opcionhc4.place(x=350,y=280)
                opcionhc4.bind("<Button-1>",lambda v:formulaM())
                

                def consultaranamnesis():
                    framerlt.destroy()

                    opcionhc1.destroy()
                    opcionhc3.destroy()
                    opcionhc4.destroy()
                    ventana.geometry("600x700")
                    y=50

                    frametitulo=CTkFrame(ventana,width=600,height=100,border_width=5,border_color="#247ba0",fg_color="#e2e2e2")
                    frametitulo.place(x=0,y=0)

                    lbltitulo2=CTkLabel(frametitulo,text="Consultas medicas",font=("Ready For Fall",30),text_color="black")
                    lbltitulo2.place(x=150,y=30)


                    for i in documentos[0]["consulta_medica"]:
                    
                        consulta=CTkFrame(ventana,width=500,height=200,border_width=3,border_color="#fe6d73",fg_color="#f4dbd8")
                        consulta.place(x=50,y=y)


                        acatlo=CTkLabel(consulta,text=f"Enfermedad actual:{i["enfermedad_actual"]}",text_color="black",font=("Ready For Fall",18))
                        acatlo.place(x=20,y=20)

                        fechac=CTkLabel(consulta,text=f"Fecha Consulta:{i["fecha_consulta"]}",text_color="black",font=("Ready For Fall",18))
                        fechac.place(x=20,y=50)


                        anexo=CTkLabel(consulta,text=f"Anexo:{i["anexo"]}",text_color="black",font=("Ready For Fall",18))
                        anexo.place(x=20,y=80)

                        med=CTkLabel(consulta,text=f"Medico consulta:{i["medico_consulta"]}",text_color="black",font=("Ready For Fall",18))
                        med.place(x=20,y=110)

                        y =y+150
                        boton=CTkButton(ventana,text="Atras",border_width=3,border_color="black",text_color="black",hover_color="#ffb3c6",fg_color="#a9def9",font=("Ready For Fall",25),width=150,height=70)
                        boton.place(x=1100,y=170)

                def formulaM():
                    framerlt.destroy()

                    opcionhc1.destroy()
                    opcionhc3.destroy()
                    opcionhc4.destroy()
                    ventana.geometry("1100x700")
                    frametitulo=CTkFrame(ventana,width=1100,height=100,border_width=5,border_color="#247ba0",fg_color="#e2e2e2")
                    frametitulo.place(x=0,y=0)
                    x=20

                    lbltitulo2=CTkLabel(frametitulo,text="Formulas medicas",font=("Ready For Fall",30),text_color="black")
                    lbltitulo2.place(x=400,y=30)


                    for i in documentos[0]["formula_medica"]:
                    
                        consulta=CTkFrame(ventana,width=500,height=400,border_width=3,border_color="#fe6d73",fg_color="#f4dbd8")
                        consulta.place(x=x,y=150)


                        med2=CTkLabel(consulta,text=f"Medicamento:{i["medicamento"]}",text_color="black",font=("Ready For Fall",18))
                        med2.place(x=20,y=20)

                        concentracion=CTkLabel(consulta,text=f"Concentracion:{i["concentracion"]}",text_color="black",font=("Ready For Fall",18))
                        concentracion.place(x=20,y=50)


                        forma=CTkLabel(consulta,text=f"Forma farmaceutica:{i["forma_farmaceutica"]}",text_color="black",font=("Ready For Fall",18))
                        forma.place(x=20,y=80)

                        dosis=CTkLabel(consulta,text=f"Dosis:{i["dosis"]}",text_color="black",font=("Ready For Fall",18))
                        dosis.place(x=20,y=110)

                        via=CTkLabel(consulta,text=f"Via de administracion:{i["via_administracion"]}",text_color="black",font=("Ready For Fall",18))
                        via.place(x=20,y=140)

                        frec=CTkLabel(consulta,text=f"Frecuencia:{i["frecuencia"]}",text_color="black",font=("Ready For Fall",18))
                        frec.place(x=20,y=170)

                        time=CTkLabel(consulta,text=f"Tiempo de tratamiento:{i["tiempo_tratamiento"]}",text_color="black",font=("Ready For Fall",18))
                        time.place(x=20,y=200)

                        cant=CTkLabel(consulta,text=f"Cantidad:{i["cantidad"]}",text_color="black",font=("Ready For Fall",18))
                        cant.place(x=20,y=230)

                        cantl=CTkLabel(consulta,text=f"Cantidad en letras:{i["cantidad_letras"]}",text_color="black",font=("Ready For Fall",18))
                        cantl.place(x=20,y=260)

                        posologia=CTkLabel(consulta,text=f"Posologia:{i["posologia"]}",text_color="black",font=("Ready For Fall",18))
                        posologia.place(x=20,y=290)

                        x =x+550
                        boton=CTkButton(ventana,text="Atras",border_width=3,border_color="black",text_color="black",hover_color="#ffb3c6",fg_color="#a9def9",font=("Ready For Fall",25),width=150,height=70)
                        boton.place(x=1100,y=170)


                def diagnostico():
                    framerlt.destroy()

                    opcionhc1.destroy()
                    opcionhc3.destroy()
                    opcionhc4.destroy()
                    ventana.geometry("1100x400")
                    frametitulo2=CTkFrame(ventana,width=1100,height=100,border_width=5,border_color="#247ba0",fg_color="#e2e2e2")
                    frametitulo2.place(x=0,y=0)

                    x=20

                    lbltitulo2=CTkLabel(frametitulo2,text="Diagnosticos",font=("Ready For Fall",30),text_color="black")
                    lbltitulo2.place(x=400,y=30)

                    
                    for i in documentos[0]["diagnostico"]:
                    
                        consulta=CTkFrame(ventana,width=500,height=200,border_width=3,border_color="#fe6d73",fg_color="#f4dbd8")
                        consulta.place(x=x,y=150)


                        cod=CTkLabel(consulta,text=f"Codigo:{i["codigo"]}",text_color="black",font=("Ready For Fall",18))
                        cod.place(x=20,y=20)

                        nombre=CTkLabel(consulta,text=f"Nombre:{i["nombre"]}",text_color="black",font=("Ready For Fall",18))
                        nombre.place(x=20,y=50)


                        hallazgos=CTkLabel(consulta,text=f"Hallazgos:{i["hallazgos"]}",text_color="black",font=("Ready For Fall",18))
                        hallazgos.place(x=20,y=80)

                        descripcion=CTkLabel(consulta,text=f"Descripción:{i["descripcion"]}",text_color="black",font=("Ready For Fall",18))
                        descripcion.place(x=20,y=110)

                        # via=CTkLabel(consulta,text=f"Via de administracion:{i["via_administracion"]}",text_color="black",font=("Ready For Fall",18))
                        # via.place(x=20,y=140)

                        # frec=CTkLabel(consulta,text=f"Frecuencia:{i["frecuencia"]}",text_color="black",font=("Ready For Fall",18))
                        # frec.place(x=20,y=170)

                        # time=CTkLabel(consulta,text=f"Tiempo de tratamiento:{i["tiempo_tratamiento"]}",text_color="black",font=("Ready For Fall",18))
                        # time.place(x=20,y=200)

                        # cant=CTkLabel(consulta,text=f"Cantidad:{i["cantidad"]}",text_color="black",font=("Ready For Fall",18))
                        # cant.place(x=20,y=230)

                        # cantl=CTkLabel(consulta,text=f"Cantidad en letras:{i["cantidad_letras"]}",text_color="black",font=("Ready For Fall",18))
                        # cantl.place(x=20,y=260)

                        # posologia=CTkLabel(consulta,text=f"Posologia:{i["posologia"]}",text_color="black",font=("Ready For Fall",18))
                        # posologia.place(x=20,y=290)

                        x =x+550
                        boton=CTkButton(ventana,text="Atras",border_width=3,border_color="black",text_color="black",hover_color="#ffb3c6",fg_color="#a9def9",font=("Ready For Fall",25),width=150,height=70)
                        boton.place(x=1100,y=170)














    













        # tip_doc=Nopi(ventana,"Tipo de documento:", 230, 100, ["CC", "TI","Cedula de extrangeria","Registro civil"], 200)
        # tip_doc.place(x=50,y=20)


        # numero_id=Sipi(ventana,"Numero de identificación:",270,80,200)
        # numero_id.place(x=300,y=20)

        # fecha_exp=Date(ventana,"Fecha de Expedición:")
        # fecha_exp.place(x=580,y=20)

        # nombres=Sipi(ventana,"Nombres Completos",270,80,200)
        # nombres.place(x=50,y=120)

        # apllido1=Sipi(ventana,"Apellido 1:",270,80,200)
        # apllido1.place(x=300,y=120)



        
        # ventana.geometry("1250x500")
        
        # documentos=historias.find({"identificacion":numero_id})
            # for i in documentos:
            #     print(i)
            

        # global frame2
        # frame2=CTkFrame(ventana,width=320,height=150,border_width=5,border_color="#5a189a",fg_color="#dbcae9")
        # frame2.place(x=50,y=250)
            
        # texto=CTkLabel(frame2,text=f'Nombre:{documentos[0]["nombres"]}',text_color="black",font=("Ready For Fall",22))
        # texto.place(x=50,y=90)



        # apllido2=Sipi(frameob,"Apellido 2:",270,80,200)
        # apllido2.place(x=580,y=120)

        # fecha_nc=Date(frameob,"Fecha de nacimiento")
        # fecha_nc.place(x=50,y=220)

        # email=Sipi(frameob,"Email",270,80,200)
        # email.place(x=300,y=220)

        # telefono=Sipi(frameob,"Telefono",270,80,200)
        # telefono.place(x=50,y=220)

        # sexo = Nopi(frameob, "Sexo:", 250, 100, ["Masculino","Femenino"],200)
        # sexo.place(x=580,y=220)

        # genero = Nopi(frameob, "Género:", 250, 100, ["Hetero","Gay","Lesbiana","Bisexual"], 200)
        # genero.place(x=50,y=320)

        # rh=Sipi(frameob,"Tipo de sangre:",270,80,200)
        # rh.place(x=300,y=320)

        # tpAtencion=Nopi(frameob,"Tipo de Atención especial",280,100,["seleccione","Adultos mayores"," Población habitante de calle", "Comunidades indígenas", " Víctimas del conflicto armado" ],200)
        # tpAtencion.place(x=580,y=320)

        # ocupacion=Sipi(frameob,"Ocupacion",270,80,200)
        # ocupacion.place(x=50,y=420)

        # tpafiliacion=Nopi(frameob,"Tipo de afiliación",250,100,["seleccione","Cotizante", "Beneficiario"],200)
        # tpafiliacion.place(x=300,y=420)

        # regimen =Nopi(frameob,"Regimen",280,100,["seleccione","Contributivo", "Subsidiado"],200)
        # regimen.place(x=580,y=420)

        # btnguardar=CTkButton(frameob,text="Guardar",width=150,height=50,border_color="#5a189a",fg_color="#ffeedd",font=("Ready For Fall",20),text_color="black",border_width=5)
        # btnguardar.place(x=330,y=530)


    def CrearHc():
        opcion1.destroy()
        opcion2.destroy()
        frametl.destroy()
        ventana.geometry("700x500")

        frametl2=CTkFrame(ventana,border_width=5,height=100,width=700,border_color="#008000",fg_color="#d0f4de")
        frametl2.place(x=0,y=0)

        titulofr=CTkLabel(frametl2,text="Crear Historia Clinica",font=("Ready For Fall",30),text_color="black")
        titulofr.place(x=200,y=30)

        opcion1hc=CrearHistoriac(ventana,"#dc136c","#f7d6e0","Anamnesis","anamnesis.png",25)
        opcion1hc.place(x=50,y=150)
        opcion1hc.bind("<Button-1>",lambda v:anamnesisfml())

        opcion2hc=CrearHistoriac(ventana,"#3c096c","#e4c1f9","Formula M","formula medica.webp",25)
        opcion2hc.place(x=50,y=300)
        opcion2hc.bind("<Button-1>",lambda v:formulaM())

        opicion3hc=CrearHistoriac(ventana,"#2B60E3","#79DDE6","Signos vitales","signos.png",25)
        opicion3hc.place(x=350,y=150)
        opicion3hc.bind("<Button-1>",lambda v:signosVitales())


        opcion4hc=CrearHistoriac(ventana,"#20A944","#80ed99","Diagnostico","diagnostico.png",25)
        opcion4hc.place(x=350,y=300)
        opcion4hc.bind("<Button-1>",lambda v:diagnostico())



        def anamnesisfml():
            opcion1hc.destroy()
            opcion2hc.destroy()
            opicion3hc.destroy()
            opcion4hc.destroy()
            frametl2.destroy()
            ventana.geometry("1200x690")

            frametl3=CTkFrame(ventana,border_width=5,height=100,width=1200,border_color="#008000",fg_color="#d0f4de")
            frametl3.place(x=0,y=0)

            titulofr3=CTkLabel(frametl3,text="Anamnesis",font=("Ready For Fall",30),text_color="black")
            titulofr3.place(x=500,y=30)

            frameanamnesis=CTkFrame(ventana,border_color="black",border_width=3,width=350,height=550,fg_color="white")
            frameanamnesis.place(x=50,y=120)

            titulofrm=CTkFrame(frameanamnesis,width=340,height=60,fg_color="#ffb3c1",border_width=3,border_color="#f72585")
            titulofrm.place(x=5,y=5)

            lbltl=CTkLabel(titulofrm,text="Consulta",font=("Ready For Fall",25),text_color="black")
            lbltl.place(x=120,y=10)
            mtvconsulta=Sipi(frameanamnesis,"Motivo de consulta:",230,80,200)
            mtvconsulta.place(x=10,y=80)

            enfermedadatl=Sipi(frameanamnesis,"Enfermedad actual:",230,80,200)
            enfermedadatl.place(x=10,y=160)

            fechacon=Date(frameanamnesis,"Fecha de consulta:")
            fechacon.place(x=10,y=240)

            anexo=Sipi(frameanamnesis,"Anexo",230,80,200)
            anexo.place(x=10,y=320)

            medicoconsul=Sipi(frameanamnesis,"Medico consulta",230,80,200)
            medicoconsul.place(x=10,y=400)

            botonguardar=CTkButton(frameanamnesis,width=100,height=30,border_width=3,border_color="#f15bb5",fg_color="#ffc9b9",font=("Ready For Fall",15),text="Guardar",text_color="black")
            botonguardar.place(x=120,y=500)

#antecedentes personales 

            frameanamnesis2=CTkFrame(ventana,border_color="black",border_width=3,width=350,height=300,fg_color="white")
            frameanamnesis2.place(x=420,y=120)

            titulofrm2=CTkFrame(frameanamnesis2,width=340,height=60,fg_color="#90e0ef",border_width=3,border_color="#0096c7")
            titulofrm2.place(x=5,y=5)

            lbltl2=CTkLabel(titulofrm2,text="Antecedentes personales",font=("Ready For Fall",25),text_color="black")
            lbltl2.place(x=20,y=10)

            alergia=Sipi(frameanamnesis2,"Alergias",230,80,200)
            alergia.place(x=10,y=80)

            enfermedades=Sipi(frameanamnesis2,"Enfermedades",230,80,200)
            enfermedades.place(x=10,y=160)

            botonguardar2=CTkButton(frameanamnesis2,width=100,height=30,border_width=3,border_color="#0096c7",fg_color="#90e0ef",font=("Ready For Fall",15),text="Guardar",text_color="black")
            botonguardar2.place(x=120,y=250)


#antecedentes familiares 
            
            frameanamnesis3=CTkFrame(ventana,border_color="black",border_width=3,width=350,height=300,fg_color="white")
            frameanamnesis3.place(x=800,y=120)

            titulofrm3=CTkFrame(frameanamnesis3,width=340,height=60,fg_color="#e0aaff",border_width=3,border_color="#7209b7")
            titulofrm3.place(x=5,y=5)

            lbltl3=CTkLabel(titulofrm3,text="Antecedentes personales",font=("Ready For Fall",25),text_color="black")
            lbltl3.place(x=20,y=10)

            alergia2=Sipi(frameanamnesis3,"Alergias",230,80,200)
            alergia2.place(x=10,y=80)

            enfermedades2=Sipi(frameanamnesis3,"Enfermedades",230,80,200)
            enfermedades2.place(x=10,y=160)

            botonguardar3=CTkButton(frameanamnesis3,width=100,height=30,border_width=3,border_color="#7209b7",fg_color="#e0aaff",font=("Ready For Fall",15),text="Guardar",text_color="black")
            botonguardar3.place(x=120,y=250)

        def formulaM():
            opcion1hc.destroy()
            opcion2hc.destroy()
            opicion3hc.destroy()
            opcion4hc.destroy()
            frametl2.destroy()
            ventana.geometry("700x700")

            frametl4=CTkFrame(ventana,border_width=5,height=100,width=700,border_color="#008000",fg_color="#d0f4de")
            frametl4.place(x=0,y=0)

            titulofr4=CTkLabel(frametl4,text="Formula medica",font=("Ready For Fall",30),text_color="black")
            titulofr4.place(x=220,y=30)

            medicamento=Sipi(ventana,"Medicamento:",230,80,200)
            medicamento.place(x=50,y=120)

            concentracion=Sipi(ventana,"Concentracion:",230,80,200)
            concentracion.place(x=350,y=120)

            formaf=Sipi(ventana,"Forma farmaceutica:",230,80,200)
            formaf.place(x=50,y=220)

            dosis=Sipi(ventana,"Dosis:",230,80,200)
            dosis.place(x=350,y=220)

            viaadm=Sipi(ventana,"Via de administración",240,80,200)
            viaadm.place(x=50,y=320)

            frecuencia=Sipi(ventana,"Frecuencia:",230,80,200)
            frecuencia.place(x=350,y=320)

            tratamiento=Sipi(ventana,"Tiempo de tratamiento",260,80,200)
            tratamiento.place(x=50,y=420)

            cantidad=Sipi(ventana,"Cantidad",230,80,200)
            cantidad.place(x=350,y=420)

            cantidadL=Sipi(ventana,"Cantidad en letras",230,80,200)
            cantidadL.place(x=50,y=520)

            posologia=Sipi(ventana,"Posologia",230,80,200)
            posologia.place(x=350,y=520)

        def diagnostico():
            opcion1hc.destroy()
            opcion2hc.destroy()
            opicion3hc.destroy()
            opcion4hc.destroy()
            frametl2.destroy()
            ventana.geometry("500x600")

            frametl5=CTkFrame(ventana,border_width=5,height=100,width=500,border_color="#008000",fg_color="#d0f4de")
            frametl5.place(x=0,y=0)

            titulofr5=CTkLabel(frametl5,text="Diagnostico",font=("Ready For Fall",30),text_color="black")
            titulofr5.place(x=150,y=30)

            codigo=Sipi(ventana,"Codigo de diagnostico:",250,80,200)
            codigo.place(x=100,y=120)

            nombre=Sipi(ventana,"Nombre del diagnostico:",270,80,200)
            nombre.place(x=100,y=220)

            hallazgos=Sipi(ventana,"Hallazgos:",230,80,200)
            hallazgos.place(x=100,y=320)

            descripcion=Sipi(ventana,"Descripcion:",230,80,200)
            descripcion.place(x=100,y=420)

        def signosVitales():

            opcion1hc.destroy()
            opcion2hc.destroy()
            opicion3hc.destroy()
            opcion4hc.destroy()
            frametl2.destroy()
            ventana.geometry("700x750")

            frametl6=CTkFrame(ventana,border_width=5,height=100,width=700,border_color="#008000",fg_color="#d0f4de")
            frametl6.place(x=0,y=0)

            titulofr6=CTkLabel(frametl6,text="Signos vitales",font=("Ready For Fall",30),text_color="black")
            titulofr6.place(x=250,y=30)

            frecuenciaC=Sipi(ventana,"Frecuencia cardiaca",230,80,200)
            frecuenciaC.place(x=30,y=120)

            frecuenciaR=Sipi(ventana,"Frecuencia respiratoria",260,80,200)
            frecuenciaR.place(x=350,y=120)

            tensionad=Sipi(ventana,"Tension arterial diastolica",300,80,200)
            tensionad.place(x=30,y=220)

            tensionas=Sipi(ventana,"Tension arterial sistolica",300,80,200)
            tensionas.place(x=350,y=220)

            tensaionam=Sipi(ventana,"Tension arterial media",300,80,200)
            tensaionam.place(x=30,y=320)

            pulsoximetria=Sipi(ventana,"Pulsoximetria",230,80,200)
            pulsoximetria.place(x=350,y=320)

            temperatura=Sipi(ventana,"Temperatura",230,80,200)
            temperatura.place(x=30,y=420)

            peso=Sipi(ventana,"Peso",230,80,200)
            peso.place(x=350,y=420)

            talla=Sipi(ventana,"Talla",230,80,200)
            talla.place(x=30,y=520)

            masa=Sipi(ventana,"Masa",230,80,200)
            masa.place(x=350,y=520)

            boton=CTkButton(ventana,text="Guardar",font=("Ready For Fall",20),width=200,height=50,text_color="black",border_width=5,border_color="#ff006e",fg_color="#ffcad4",hover_color="#e4c1f9")
            boton.place(x=200,y=650)





            
            





















        

    
    ventana.mainloop()


class CrearHistoriac(CTkFrame):
    def __init__(self, master,colorb,colorf,titulo,imagen,tamaño):
        super().__init__(master,width=250,height=120,border_width=5,border_color=colorb,fg_color=colorf)
        self.titulo=titulo
        image=Image.open(imagen)
        image=image.resize((60,60))

        self.ctkImg= CTkImage(light_image=image,size=(60,60))
        lblimg=CTkLabel(self,image=self.ctkImg,text="")
        lblimg.place(x=100,y=45)
        self.titlo=CTkLabel(self,text=titulo,font=("Ready For Fall",tamaño))
        self.titlo.place(x=40,y=10)



class Opciones(CTkFrame):


    def __init__(self, master,titulo,imagen):
        super().__init__(master,width=300,height=180,fg_color="#bdb2ff",border_color="#0582ca",border_width=5)
        self.titulo=titulo
        # # self.titulo.place(x=50,y=45)
        image = Image.open(imagen)
        image = image.resize((100, 100)) 
        
        
        self.ctk_image = CTkImage(light_image=image, size=(100, 100))
        
    
        lblimg = CTkLabel(self, image=self.ctk_image, text="")
        lblimg.place(x=100, y=55)

        self.title_label = CTkLabel(self, text=titulo,font=("Ready For Fall",25))
        self.title_label.place(x=60, y=10)



class Sipi(CTkFrame):
    def __init__(self, master,titulo,ancho,largo,largo2):
        super().__init__(master, width=ancho,height=largo,fg_color="white")
        self.titulo=titulo
        tituloE = CTkLabel(self,text=self.titulo,font=("Ready For Fall",20),text_color="black")
        tituloE.place(x=20,y=12)
        self.caja=CTkEntry(self,border_color="#38184C",border_width=3,width=largo2,fg_color="white",text_color="black")
        self.caja.place(x=20,y=50)
    def getEntri(self):
        return self.caja.get()
    







class Nopi(CTkFrame):
    def __init__(self, master, titulo,ancho,largo,opciones,largo2):
        super().__init__(master,width=ancho,height=largo,fg_color="white")
        self.titulo=titulo
        ttlo=CTkLabel(self,text=self.titulo,font=("Ready For Fall",20))
        ttlo.place(x=20,y=12)
        self.combo=CTkComboBox(self,values=opciones,border_color="#38184C",border_width=3,width=largo2,font=("coolvetica rg",18),dropdown_fg_color="#fae0e4",button_hover_color="#ff7096",button_color="#e7c6ff")
        self.combo.place(x=20,y=50)

    def getEntri(self):
        return self.combo.get()
    





class Date(CTkFrame):
    def __init__(self, master, titulo):
        super().__init__(master, width=250, height=100, fg_color="white")
        self.titulo = titulo
    
        ttlD = CTkLabel(self, text=self.titulo, font=("Ready For Fall", 20))
        ttlD.place(x=20,y=12)
        
        self.j = DateEntry(self, width=20, background='#ff8fab', foreground='black', borderwidth=3, font=('Papernotes', 12))
        self.j.place(x=40,y=70)
    def getEntri(self):
        return self.j.get()




main()
    