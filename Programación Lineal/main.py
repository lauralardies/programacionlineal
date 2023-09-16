from optimizacion import Ejercito
from ortools.linear_solver import pywraplp

def main():
    ejercito = Ejercito()
    ejercito.objetivo()
    estado = ejercito.resolver()

    if estado == pywraplp.Solver.OPTIMAL:  
        print('================= Solución =================')  
        print(f'El problema se ha resuelto en {ejercito.solucionador.wall_time():.2f} milisegundos y en {Ejercito.solucionador.iterations()} iteraciones.')  
        print()  
        print(f'Valor del poder óptimo = {ejercito.solucionador.Objective().Value()} 💪 Poder')  
        print('Ejército:')
        print(f' - 🗡️ Espadachines = {ejercito.espadachines.solution_value()}')  
        print(f' - 🏹 Arqueros = {ejercito.arqueros.solution_value()}')  
        print(f' - 🐎 Jinetes = {ejercito.jinetes.solution_value()}')
    else:  
        print('El solucionador no ha podido encontrar una solución óptima.')