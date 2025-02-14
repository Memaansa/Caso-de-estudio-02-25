class Sensores:
    def __init__(self, test_mode=True):
        self.luz_on = False
        self.test_mode = test_mode
        if not self.test_mode:
            print ("No hay luz")
    
    def hay_persona(self,Persona):
        if Persona:
            self.luz_on = True
            if not self.test_mode:
                print ("Persona detectada. Bombillo encendido.")
        else:
            self.luz_on = False
            if not self.test_mode:
                print ("No hay nadie. Bombillo apagado.")

sensor = Sensores()
if __name__ == "__main__":
    while True:
        Persona = input("¿Hay alguien?").strip().lower()
        if Persona == "si":
            sensor.hay_persona(True)
        elif Persona == "no":
            sensor.hay_persona(False)
        else:
            print ("Entrada no válida. Use 'si' o 'no'.")
 