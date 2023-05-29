from Funcion import f
from tabulate import tabulate

class Iteracion():
    def __init__(self, t):
        self.t = t
        self.P = None
        self.k1 = None
        self.k2 = None
        self.k3 = None
        self.k4 = None
        
    def calculark1(self, h, Pn):
        self.k1 = h * f(Pn)
        
    def calculark2(self, h, Pn):
        self.k2 = h * f(Pn + self.k1/2)
        
    def calculark3(self, h, Pn):
        self.k3 = h * f(Pn + self.k2/2)
        
    def calculark4(self, h, Pn):
        self.k4 = h * f(Pn + self.k3)
        
    def calcularP(self, Pn):
        self.P = Pn + (self.k1 + 2*self.k2 + 2*self.k3 + self.k4) / 6
        
    def calcular(self, h, Pn):
        self.calculark1(h, Pn)
        self.calculark2(h, Pn)
        self.calculark3(h, Pn)
        self.calculark4(h, Pn)
        self.calcularP(Pn)
        
    def __str__(self):
        data = [
            ["t", self.t],
            ["P", self.P],
            ["k1", self.k1],
            ["k2", self.k2],
            ["k3", self.k3],
            ["k4", self.k4]
        ]
        
        table = tabulate(data, headers=["Variable", "Valor"], tablefmt="fancy_grid", floatfmt=".8f")
        return table
