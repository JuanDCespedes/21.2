from cartas import *
class Juego:
    def __init__(self):
        self.mazo=Mazo()
        self.casa=Mazo(True)
        self.jugador=Mazo(True)
    def iniciar_juego(self):
        self.casa.agregar_carta(self.mazo.dar_carta())
        self.casa.agregar_carta(self.mazo.dar_carta())
        self.jugador.agregar_carta(self.mazo.dar_carta())
        self.jugador.agregar_carta(self.mazo.dar_carta())
    def mostrar_juego(self):
        print("jugador:")
        self.jugador.mostrar_cartas()
        print("casa:")
        self.casa.mostrar_cartas() 
    def pedir(self, pide=True):
        while pide:
            turn=input("quieres otra carta? (s/n)\n")
            if turn == "s":
                self.jugador.agregar_carta(self.mazo.dar_carta())
                self.jugador.mostrar_cartas()
                print(self.jugador.dar_valor())
                if self.jugador.dar_valor() > 21:
                    print("una pena, te pasas, perdiste xd")
                    print("la casa gano")
                    break;
            else:
                print("tus cartas: ")
                self.jugador.mostrar_cartas(True)
                print(self.jugador.dar_valor())
                print("cartas de la casa: ")
                if self.jugador.dar_valor() <= 21:
                    while self.casa.dar_valor() < self.jugador.dar_valor():
                        self.casa.agregar_carta(self.mazo.dar_carta())
                        self.casa.mostrar_cartas()
                        print(self.casa.dar_valor())
                        if self.casa.dar_valor() >= self.jugador.dar_valor() and not(self.casa.dar_valor() > 21):
                            print("la casa gana xd, tuviste: "+ str(self.jugador.dar_valor()))
                            print("mientras que la casa: "+str(self.casa.dar_valor()))
                            break;
                        elif self.casa.dar_valor() > 21:
                            print("ganaste la casa se paso de 21 con: "+ str(self.casa.dar_valor()))
                            break;
                        elif self.casa.dar_valor() < self.jugador.dar_valor():
                            print("le ganaste a la casa con: "+str(self.jugador.dar_valor()))
                            print("mientras que la casa tuvo: "+str(self.casa.dar_valor()))
                elif self.jugador.dar_valor() > 21:
                    print("una pena, te pasas, perdiste xd")
                    print("la casa gano")
                    break;
                break;
if __name__ == "__main__":
    juego = Juego()
    juego.iniciar_juego()
    juego.mostrar_juego()
    juego.pedir()
