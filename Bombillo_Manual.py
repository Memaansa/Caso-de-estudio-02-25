class Interruptor: 
    def __init__(self):
        self.state = False  #Estado inicial (apagado)
        print ("No hay luz")

    def señal (self,comando):
        if comando == "ON":  #Encendido 
            self.state = True
            print ("Se prendio el bombillo ☀️")          
        elif comando == "OFF":
            self.state = False  #Apagado
            print("Se apago el bombillo 🌑")

        else:
            print("Señal no recibida")

Bombillo = Interruptor()
while True:
    comnado =input ("Ingrece (ON/OFF):")
    Bombillo.señal(comnado)