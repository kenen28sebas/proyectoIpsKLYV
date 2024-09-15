class Persona :
    def __init__(self,nombre,ap,doc):   
        self.nombre = nombre
        self.ap = ap
        self.doc = doc
    
    def regalar (self):
        return "jose"
    
lina = Persona("lina","alarcon",123)

# print(lina.regalar())

kenen=lina.regalar()
# print(kenen)

class A:
    def __init__(self,id,rango) :
        self.id = id
        self.rango = rango
    def crearOb(self):
        objeto =B(1234)
        return objeto
        
class B:
    def __init__(self,id) :
        self.id = id      
        

jose = A(1234, "capitan")
print(jose.id)

martha=B(456)
print(martha.id)

nancuy =jose.crearOb()

print(nancuy.id)