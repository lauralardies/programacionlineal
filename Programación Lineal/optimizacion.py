# Import OR-Tools para programación lineal.
from ortools.linear_solver import pywraplp

class Ejercito():

    # Creamos un solucionador usando el backend de GLOP (Paquete de optimización lineal de Google).
    solucionador = pywraplp.Solver('Maximiza el poder del ejército', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

    # Variables que queremos optimizar (variables enteras)
    espadachines = solucionador.IntVar(0, solucionador.infinity(), 'espadachines')
    arqueros = solucionador.IntVar(0, solucionador.infinity(), 'arqueros')
    jinetes = solucionador.IntVar(0, solucionador.infinity(), 'jinetes')

    # Las restricciones de cada variable se añaden directamente a la instancia del solucionador.
    solucionador.Add(espadachines*60 + arqueros*80 + jinetes*140 <= 1200) # Comida.
    solucionador.Add(espadachines*20 + arqueros*10 <= 800)                # Madera.
    solucionador.Add(arqueros*40 + jinetes*100 <= 600)                    # Oro.

    def objetivo(self):
        # Definimos función objetivo : espadachines*70 + arqueros*95 + jinetes*230.
        # Maximizamos dicha función.
        return self.solucionador.Maximize(self.espadachines*70 + self.arqueros*95 + self.jinetes*230)

    def resolver(self):
        # Calculamos el problema.
        return self.solucionador.Solve() # Con esto podemos comprobar que verdaderamente sea óptima la solución.