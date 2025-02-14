class Sensores:
    def __init__(self):
        self.luz_on = False
        print ("No hay luz")
    
    def hay_persona(self,Persona):
        if Persona:
            self.luz_on = True
            print ("Persona detectada. Bombillo encendido.")
        else:
            self.luz_on = False
            print ("No hay nadie. Bombillo apagado.")

sensor = Sensores()
while True:
    Persona = input("¿Hay alguien?").strip().lower()
    if Persona == "si":
        sensor.hay_persona(True)
    elif Persona == "no":
        sensor.hay_persona(False)
    else:
        print ("Entrada no válida. Use 'si' o 'no'.")
 