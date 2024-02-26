import random
class Carta:
    def __init__(self, valor, pinta):
        self.valor=valor
        self.pinta=pinta
    def dar_valor(self):
        if self.valor in ("J", "Q", "K"):
            return 10
        if self.valor=="A":
            return 1
        return int(self.valor)
    def mostrar(self):
        return self.valor + " de "+ self.pinta
class Mazo:
    def __init__(self, jugador =False):
        
        if jugador:
            self.cartas=[]
        else:
            self.cartas=[Carta(v, p)for v in ["A","J", "Q", "K"]+[str(x) for x in range(2, 11)] for p in ["picas", "treboles", "corazones", "diamantes"]]
            random.shuffle(self.cartas)   
    def dar_valor(self, todas=False):
        valor=0
        for c in self.cartas:
            valor+=c.dar_valor()
        if self.tiene_as() and valor <=11:
            valor+=10
        return valor
    def tiene_as(self):
        for c in self.cartas:
            if c.valor=="A":
                return True
        return False
    def dar_carta(self):
        return self.cartas.pop()
    def agregar_carta(self,carta):
        self.cartas.append(carta)
    def mostrar_cartas(self, todas=False):
        if todas:
            print(self.cartas[0].mostrar())
        else:
            print(" ")
        for c in self.cartas[1:]:
            print(c.mostrar())
