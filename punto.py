import math

class punto:

    def __init__(self):
        self.x=5
        self.y=9

    def calcular_distancia (self):
        
        distancia=math.hypot(self.x,self.y)

        print(distancia)


