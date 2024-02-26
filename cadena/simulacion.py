'''
Módulo de simulación:
Este módulo es encargado de simular y visualizar un sistema M/M/1 
con parámetros encontrados del módulo de análisis, el mismo trabaja con método 
rvs(), haciendo que cada vez que corra se obtenga un resultado diferente, además
se pueden alterar varios valores como N, P, el exceso.
'''
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt


def sistema(lam, nu, N):
    """Simula una secuencia de llegadas y salidas de
    clientes al sistema, según los parámetros encontrados
     del inciso anterior.

    Parameters
    ----------
    lam : float
        Parámetro lambda deseado, que representa la intensidad de llegada.

    nu : float
        Parámetro Nu deseado, que representa la intensidad con la que salen
        los datos del proceso.

    N : int
        Número de clientes ingresado por el usuario.

    Returns
    -------
    simul_df : float
        Simulación de una secuencia de llegadas y
        salidas de clientes al sistema.

    t_llegadas : float
        Calcula el tiempo de llegada entre clientes.

    t_atencion : float
        Calcula el tiempo de atención entre clientes
        y cuando puede ser atendido el siguiente.

    t_servicio : float
        Con la función rvs() se genera un tiempo
        de servicio aleatorio usado para los demás datos.

    t_salida : float
        Tiempo de salida de cada cliente.
    """

    # Distribución de los tiempos de llegada entre cada cliente
    X = stats.expon(scale=1/lam)

    # Distribución de los tiempos de servicio de cada cliente
    Y = stats.expon(scale=1/nu)

    # Intervalos entre llegadas (segundos desde el último cliente)
    t_intervalos = np.ceil(X.rvs(N)).astype('int')

    # Tiempos de llegadas (segundos desde el inicio)
    t_llegadas = [t_intervalos[0]]
    # Aquí se calcula el intervalo de tiempo entre
    # el cliente anterior y el siguiente
    for i in range(1, len(t_intervalos)):
        siguiente = t_llegadas[i-1] + t_intervalos[i]
        t_llegadas.append(siguiente)

    # Tiempos de servicio (segundos desde inicio de servicio)
    t_servicio = np.ceil(Y.rvs(N)).astype('int')

    # Inicialización del tiempo de incio y de fin de atención
    inicio = t_llegadas[0]  # Primera llegada
    fin = inicio + t_servicio[0]    # Primera salida

    # Tiempos de atención de todos los clientes
    t_atencion = [inicio]
    t_salida = np.zeros(N, dtype=int)
    t_salida[0] = fin
    # Determina cuando se puede atender el cliente
    for i in range(1, N):
        inicio = np.max((t_llegadas[i], fin))
        fin = inicio + t_servicio[i]
        t_atencion.append(inicio)
        t_salida[i] = fin

    clientes = np.zeros(N, dtype=int)
    for v in range(N):
        clientes[v] = v+1

    simul = {
            'Cliente': clientes, 'T_Llegada': t_llegadas,
            'T_Atención': t_atencion,
            'T_Servicio': t_servicio, 'T_Salida': t_salida
            }
    simul_df = pd.DataFrame(data=simul)

    return simul_df, t_llegadas, t_atencion, t_servicio


def visualizacion(A4, N):
    '''Realiza una visualización de la simulación de clientes que hay
        para observar un ejemplo del comportamiento del sistema con
        los parámetros encontrados contra el tiempo.

    Parameters
    ----------
    A4 : float
        Obtiene el lamda y nu del inciso 4.

    N : int
        Número de clientes del sistema.

    Xt : int
        Cantidad de clientes en un tiempo determinado.

    t : float
        Vector temporal de tiempo en el que se estudian
        la cantidad de clientes.

    P : int
        Cantidad de personas máximas que pueden estar sin que estén en espera.

    Returns
    -------
    visualizacion() : gráfica de los clientes actuales contra tiempo.
    '''

    t_llegadas = A4[1]
    t_atencion = A4[2]
    t_servicio = A4[3]

    # Inicialización del vector temporal para registrar eventos
    t = np.zeros(t_atencion[-1] + t_servicio[-1] + 1)

    # Asignación de eventos de llegada (+1) de clientes
    for c in range(N):
        i = t_llegadas[c]
        t[i] += 1
        j = t_atencion[c] + t_servicio[c]
        t[j] -= 1

    # Umbral de P o más personas en el sistema (hay P-1 en fila)
    P = 5

    # Instantes (segundos) de tiempo con P o más solicitudes en sistema
    exceso = 0

    # Proceso aleatorio (estado n = {0, 1, 2, ...})
    Xt = np.zeros(t.shape)

    # Inicialización de estado n
    n = 0

    # Recorrido del vector temporal y conteo de clientes (estado n)
    for i, c in enumerate(t):
        n += c  # Esta es la suma o resta al estado, es decir el cambio
        Xt[i] = n
        if Xt[i] >= P:
            exceso += 1

    plt.plot(Xt)
    plt.xlabel('Tiempo t (s)')
    plt.ylabel('Clientes en el sistema, n')
    plt.axhline(P, color='r', linestyle='--')
    plt.show()

    return 'Visualización'
