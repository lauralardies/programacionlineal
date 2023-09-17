from optimizacion import Ejercito
from ortools.linear_solver import pywraplp

def main():
    ejercito = Ejercito()

    ejercito.objetivo() # Definimos la función objetivo
    estado = ejercito.resolver() # Resolvemos el problema.

    # Vemos si el estado de la solución es óptimo.
    if estado == pywraplp.Solver.OPTIMAL:  
        print('================= Solución =================')  
        print(f'El problema se ha resuelto en {ejercito.solucionador.wall_time():.2f} milisegundos y en {ejercito.solucionador.iterations()} iteraciones.')  
        print()  
        print(f'Valor del poder óptimo = {ejercito.solucionador.Objective().Value()} 💪 Poder')  
        print('Ejército:')
        print(f' - 🗡️ Espadachines = {ejercito.espadachines.solution_value()}')  
        print(f' - 🏹 Arqueros = {ejercito.arqueros.solution_value()}')  
        print(f' - 🐎 Jinetes = {ejercito.jinetes.solution_value()}')

    else: # En el caso en el que el programa no haya encontrado una solución óptima.
        print('El solucionador no ha podido encontrar una solución óptima.')