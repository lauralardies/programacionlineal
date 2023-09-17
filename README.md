# programacionlineal

Mi dirección de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/lauralardies/programacionlineal)
https://github.com/lauralardies/programacionlineal

## Tarea
Esta tarea consiste en la optimización de recursos mediante programación lineal. Debemos crear el ejército más poderoso posible teniendo en cuenta los recursos que tenemos.

Datos
| Recursos | 🗡️ Espadachines | 🏹 Arqueros | 🐎 Jinetes |
| --- | --- | --- | --- |
| 🌾 Comida (1200 en total) | 60 | 80 | 140 |
| 🪵 Madera (800 en total) | 20 | 10  | 0 |
| 🪙 Oro (600 en total) | 0 | 40 | 100 |
| 💪 Poder | 70 | 95 | 230 |

## Archivos

Todos los archivos de esta tarea se encuentran dentro de una carpeta llamada `Programación Lineal`. Dentro de ella te puedes encontrar con lo siguiente:

- Un archivo llamado `optimizacion.py` que cuenta con el código que realiza el algortimo de programación lineal para optimizar. 
- Un archivo llamado `main.py` en el que se ejecuta el algoritmo y muestra los resultados de la optimización. En caso de ser óptima la solución se imprime el resultado, de lo contrario se notifica de que no se ha podido encontrar una solución óptima.
- Un archivo llamado `run.py` mediante el cual se ejecuta el código.
- Un documento LaTeX llamado `Optimización de Recursos` en el que se resumen todos los procedimientos que he hecho para resolver el problema. Además se incluyen unas conclusiones sobre los resultados obtenidos.

## Código
### Código `optimizacion.py`
```
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
```

### Código `main.py`
```
from optimizacion import Ejercito
from ortools.linear_solver import pywraplp

def main():
    ejercito = Ejercito()

    ejercito.objetivo() # Definimos la función objetivo
    estado = ejercito.resolver() # Resolvemos el problema.

    # Vemos si el estado de la solución es óptimo.
    if estado == pywraplp.Solver.OPTIMAL:  
        print('================= Solución =================')  
        print(f'El problema se ha resuelto en {ejercito.solucionador.wall_time():.2f} milisegundos y en {Ejercito.solucionador.iterations()} iteraciones.')  
        print()  
        print(f'Valor del poder óptimo = {ejercito.solucionador.Objective().Value()} 💪 Poder')  
        print('Ejército:')
        print(f' - 🗡️ Espadachines = {ejercito.espadachines.solution_value()}')  
        print(f' - 🏹 Arqueros = {ejercito.arqueros.solution_value()}')  
        print(f' - 🐎 Jinetes = {ejercito.jinetes.solution_value()}')

    else: # En el caso en el que el programa no haya encontrado una solución óptima.
        print('El solucionador no ha podido encontrar una solución óptima.')
```

### Código `run.py`
```
from main import main

if '__main__' == __name__:
    main()
```
