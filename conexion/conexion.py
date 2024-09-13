def llenarArchivo (objeto):
        archivo = {
            "tipo_documento" : objeto.getTipoDoc(),
            "fecha_expedicion" : objeto.getFechaExp(),
            "lugar_expedicion" : objeto.getLugar(),
            "nombres" : objeto.getNombres(),
            "apellido1" : objeto.getApellido1(),
            "apellido2" : objeto.getApellido2(),
            "fecha_nacimiento" : objeto.getFechaN(),
            "genero": objeto.getGenero(),
            "sexo" : objeto.getSexo(),
            "email" : objeto.getEmail(), 
            "teléfono": objeto.getTelefono()
                
            }
        return archivo
    
print("hola")