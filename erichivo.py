# Import OR-Tools para programación lineal.
from ortools.linear_solver import pywraplp

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

# Definimos función objetivo : espadachines*70 + arqueros*95 + jinetes*230.
# Maximizamos dicha función.
solucionador.Maximize(espadachines*70 + arqueros*95 + jinetes*230)

# Calculamos el problema.
estado = solucionador.Solve() # Con esto podemos comprobar que verdaderamente sea óptima la solución.

# En el caso que esta solución sea óptima, mostramos en pantalla los resultados.
if estado == pywraplp.Solver.OPTIMAL:  
    print('================= Solución =================')  
    print(f'El problema se ha resuelto en {solucionador.wall_time():.2f} milisegundos y en {solucionador.iterations()} iteraciones.')  
    print()  
    print(f'Valor del poder óptimo = {solucionador.Objective().Value()} 💪 Poder')  
    print('Ejército:')
    print(f' - 🗡️ Espadachines = {espadachines.solution_value()}')  
    print(f' - 🏹 Arqueros = {arqueros.solution_value()}')  
    print(f' - 🐎 Jinetes = {jinetes.solution_value()}')
else:  
    print('El solucionador no ha podido encontrar una solución óptima.')