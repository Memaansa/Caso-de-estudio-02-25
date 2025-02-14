import sys

class Interruptor: 
    def __init__(self, test_mode=True):
        self.state = False  #Estado inicial (apagado)
        self.test_mode = test_mode  # Modo de prueba 
        if not self.test_mode:  
            print ("No hay luz")

    def señal (self,comando):
        if comando == "ON":  #Encendido 
            self.state = True
            if not self.test_mode:
                print ("Se prendio el bombillo ☀️")          
        elif comando == "OFF":
            self.state = False  #Apagado
            if not self.test_mode:
                print("Se apago el bombillo 🌑")

        else:
            if not self.test_mode:
                print("Señal no recibida")

Bombillo = Interruptor()
if __name__ == "__main__":
    while True:
        comnado =input ("Ingrece (ON/OFF):")
        Bombillo.señal(comnado)