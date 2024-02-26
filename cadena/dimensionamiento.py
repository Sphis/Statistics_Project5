# Modulo de dimensionamiento, el cual contiene dos funciones,
# una para modificar el numero de servidores y otra para
# modificar el tiempo de atencion, ambas con el objetivo de
# reducir la fila que se genera.

import numpy as np
from scipy import stats


def servidores(lam, nu, N, P, Lq):
    """Esta funcion utiliza los limitantes que se le asignan N y P ademas
    de los parametros que se obtienen del modulo de analisis y mediante
    varias pruebas calcula la cantidad de servidores necesarios para un
    funcionamiento optimo del sistema evitando una larga cola de espera.

    Parameters
    ----------
    lam : float
        Parámetro lambda deseado, que representa la intensidad de llegada.
    nu : float
        Parámetro Nu deseado, que representa la intensidad con la que salen
        los datos del proceso.
    N : int
        Parametro dado para la cantidad de clientes que llegaran y deben
        ser atendidos.
    P : int
        Parametro establecido, que representa la cantidad maxima deseada
        de clientes en la fila.

    Returns
    -------
    s : int
        Numero de servidores, resultado de multiples comparaciones hasta
        lograr que el numero de personas en la fila no sobrepase el valor
        de P, osea la cantidad maxima.
    """

    # Estado de la fila (0 = mal, 1 = bien)
    fila = 0

    # Cantidad de servidores
    s = 1

    while fila == 0:

        # Distribución de los tiempos de llegada entre cada cliente
        X = stats.expon(scale=1/lam)

        # Distribución de los tiempos de servicio de cada cliente
        Y = stats.expon(scale=1/(nu*s))

        # Intervalos entre llegadas (segundos desde el último cliente)
        t_intervalos = np.ceil(X.rvs(N)).astype('int')

        # Tiempos de llegadas (segundos desde el inicio)
        t_llegadas = [t_intervalos[0]]
        # Aquí se calcula el intervalo de tiempo entre el cliente anterior
        # y el siguiente
        for i in range(1, len(t_intervalos)):
            siguiente = t_llegadas[i-1] + t_intervalos[i]
            t_llegadas.append(siguiente)

        # Tiempos de servicio (segundos desde inicio de servicio)
        t_servicio = np.ceil(Y.rvs(N)).astype('int')

        # Inicialización del tiempo de incio y de fin de atención
        inicio = t_llegadas[0]  # Primera llegada
        fin = inicio + t_servicio[0]    # Primera salida
        T = Lq

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
            T = T+1

        # Descripción de la función.
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

        # Cuando existen mas personas de las deseadas se genera exceso entonces
        # se modifica la cantidad de servidores para intentar reducirlo, al no
        # tener exceso se da por finalizado y entrega el numero de servidores.
        if exceso >= 1:
            s = s + 1
        else:
            return "Servidores necesarios:", s+1
    return


def tiempo(lam, N, P, Lq):
    """Esta funcion utiliza los limitantes que se le asignan N y P ademas
    de los parametros que se obtienen del modulo de analisis y mediante
    varias pruebas calcula velocidad de atencion necesaria para un
    funcionamiento optimo del sistema evitando una larga cola de espera.

    Parameters
    ----------
    lam : float
        Parámetro lambda deseado, que representa la intensidad de llegada.
    N : int
        Parametro dado para la cantidad de clientes que llegaran y deben
        ser atendidos.
    P : int
        Parametro establecido, que representa la cantidad maxima deseada
        de clientes en la fila.

    Returns
    -------
    v1 : float
        Derivador del tiempo de atencion, resultado de multiples comparaciones
        hasta lograr que el numero de personas en la fila no sobrepase el valor
        de P, osea la cantidad maxima.
    """

    # Estado de la fila (0 = mal, 1 = bien)
    fila = 0

    # Tiempo de atencion inicial
    v1 = 0.001

    while fila == 0:

        # Distribución de los tiempos de llegada entre cada cliente
        X = stats.expon(scale=1/lam)

        # Distribución de los tiempos de servicio de cada cliente
        Y = stats.expon(scale=1/v1)

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
        T = Lq

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
            T = T+1

        # Descripción de la función.
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

        # Cuando existen mas personas de las deseadas se genera exceso entonces
        # se modifica el tiempo para intentar reducirlo, al no existir exceso
        # se da por finalizado y se entrega el valor de tiempo.
        if exceso >= 1:
            v1 = v1 + 0.001
        else:
            return "Tiempo necesario:", v1
    return
