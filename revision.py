from cadena import analisis, dimensionamiento, servicio, simulacion
import pandas as pd

clientes = pd.read_csv('clientes.csv')

# Modulo de analisis
A1 = analisis.llegada(clientes)
print('El parámetro Lambda que define la intensidad de llegada es: ', A1, '\n')

A2 = analisis.servicio(clientes)
print('El parámetro nu que define la dureación del servicio es: ', A2, '\n')

A3 = analisis.parametros(A1, A2)
print('''Los parámetros solicitados # de estado, Omega, p y q son: ''',
      A3)

# Módulo de simulación
# 4. Simular una secuencia de llegadas y salidas de clientes al sistema
N = 200
A4 = simulacion.sistema(A1, A2, N)
print(A4[0])

# 5. Gráfica para observar un ejemplo del comportamiento del sistema
A5 = simulacion.visualizacion(A4, N)

# Modulo de servicio
# 6. Funcion para obtener el vector de estado estable
estados = 5
A6 = servicio.probabilidad(A1, A2, estados)
print('''El vector de estado estable es:''', '\n', A6)

# 7. Funcion para obtener el numero de servicio y el porcentaje de
# clientes en la fila
# Numero tiene que estar entre 0 y 140, y en algunos valores
# no existe un servicio correspondiente
A7 = servicio.fila(clientes)

# Modulo de dimensionamiento
P = 5
Lq = 5
# 8. Funcion para determinar el numero de servidores necesarios
A8 = dimensionamiento.servidores(A1, A2, N, P, Lq)
print(A8)

# 9. Funcion para determinar el tiempo necesario
A9 = dimensionamiento.tiempo(A1, N, P, Lq)
print(A9)

cerrar = input('Cerrar: ')
