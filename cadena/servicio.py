# Modulo de servicio, contiene dos funciones, una para obtener
# el vector de estado estable para cierta cantidad de estados
# y otra para ver cual seria el porcentaje de clientes en
# un valor especifico de servicio.
import numpy as np
import pandas as pd


def probabilidad(lamda, nu, estados):
    """Esta funcion utiliza los valores que se pueden obtener con la
    funcion de analisis y genera los tiempos Omega y las
    probabilidades phi para la cantidad de estados solicitados y
    con ellos mostrar una tabla con el vector de estado estable.

    Parameters
    ----------
    lam : float
        Parámetro lambda deseado, que representa la intensidad de llegada.
    nu : float
        Parámetro Nu deseado, que representa la intensidad con la que salen
        los datos del proceso.
    estados : int
        Número de estados (cantidad de clientes) ingresado por el usuario.
    phi : float
        Probabilidad de quedar en el estado.
    Omega : float
        Tiempo de espera.
    Returns
    -------
    vee : float
        El vee representa el vector de estado estable para la cantidad de
        estados solicitados.
    """

    # A partir de los valores del modulo de analisis crea un array
    # con los valores de Omega y phi para el rango de estados definido
    phi = np.zeros(estados, dtype=float)
    phi[0] = 1
    total = phi[0]
    for i in range(estados-1):
        Omega = lamda + nu*i
        Omega1 = lamda + nu*(i+1)
        p = lamda/(lamda + nu*i)
        q1 = nu*(i+1) / (lamda + nu*(i+1))
        phi[i+1] = ((Omega*p)/(Omega1*q1))*phi[i]
        total = total + phi[i+1]

    phi[0] = 1/(total)

    # Crea un dataframe que contiene el vector de estado estable
    # para el rango de estados definido
    vee = np.zeros(estados, dtype=float)
    for j in range(estados):
        vee[j] = phi[j]*phi[0]
    vee[0] = phi[0]
    vee_d = {'Phi': vee}
    vee_df = pd.DataFrame(vee_d)

    return vee_df


def fila(clientes):
    """Esta función utiliza los datos del documento clientes.csv y realiza
    una consulta para dar como resultado si el numero de servicio existe
    y cual seria el porcentaje de clientes para ese.

    Parameters
    ----------
    serv :
        Dataframe con la cantidad de ocurrencias de un servicio.
    numero : int
        Numero del servicio a consultar.

    Returns
    -------
    servic :
        Al consultar los datos muestra cual es el servicio correspondiente
        con el porcentaje de clientes.
    """

    # Lee el archivo clientes y hacer un dataframe
    # clientes = pd.read_csv("clientes.csv")
    clientes_df = pd.DataFrame(clientes)

    # Extrae la columna de "servicio" y crea otor dataframe
    servicio = clientes_df["servicio"]
    servicio_df = pd.DataFrame(servicio)

    # Calcula ocurrencias de cada servicio
    serv = servicio_df.groupby(servicio_df.columns.tolist(),
                               as_index=False).size()

    # Total de clientes
    clientes_totales = len(clientes_df)

    # Calcula en la columna size el % de clientes
    serv["size"] = serv["size"].apply(lambda x: int(x)*100/clientes_totales)

    # Cambiar el nombre de la columna por algo mas entendible
    serv.rename(columns={"size": "% clientes"}, inplace=True)
    serv_df = pd.DataFrame(serv)
    serv_df.index = serv_df['servicio']
    serv_df.index.name = None

    numero = input("Número de servicio:")
    numero = int(numero)

    servic = 0

    if (numero < 0) or (numero > 141):
        print("Este número no se encuentra en el rango")

    if numero in serv_df["servicio"]:
        # Busca en el dataframe la fila correspondiente al input
        servic = serv_df[serv_df["servicio"] == numero]
        print(servic)

    if numero not in serv_df["servicio"]:
        print("Este número no corresponde a ningún servicio")

    return serv_df, servic
