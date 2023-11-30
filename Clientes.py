class Clientes:
    def __init__(self, nombre:str, apellido:str, email:str, region:str) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.region = region
    
    def __str__(self):
        return f"La información de este cliente es: \n{self.nombre} {self.apellido}\n{self.email}\n{self.region}"

    def cobertura(self): #Cobertura valida que la tienda ficticia tenga cobertura a la región en la que vive el cliente colombiano
        reg = ("Caribe","Andina")
        if self.region in reg:
            return "Nuestra tienda tiene cobertura para ti ;)"
        else:
            return "Lo sentimos, nuestra tienda no tiene cobertura para ti :(" 

    def condiciones(self): #Condiciones simula el popup de términos y condiciones al inscribirnos en algo, pero en este caso el cliente acepta o rechaza ingresando una respuesta numérica 1 o 2
        print(f"Estimado/a {self.nombre} {self.apellido}, ¿acepta usted los términos y condiciones de la tienda referentes al tratamiento de su información personal?")
        respuesta = input("Escribe 1 para aceptar o 2 para rechazar ")
        while respuesta != "1" and respuesta != "2":
                respuesta = input("Respuesta no válida, por favor escriba 1 para aceptar o 2 para rechazar ")
        if respuesta == "1":
            return "Gracias por aceptar!!"
        else:
            return "Lamentamos y respetamos su decisión"
             

cliente1 = Clientes("Alberto","González","hola@gmail.com","Caribe")
#print(cliente1.cobertura())
#print(cliente1)
#print(cliente1.condiciones())
