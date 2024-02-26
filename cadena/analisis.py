# import pandas as pd
from statistics import mean

# clientes = pd.read_csv('clientes.csv')
# print(clientes.head(10))


# %%
def llegada(clientes):
    """Descripción de la función.
    El parámetro :math:`\lambda` es de la distribución exponencial:
    .. math:: f_X(x) = \lambda e^{-\lambda x}
    Parameters
    ----------
    clientes : dataframe
        Dataframe que contiene el número de clientes y los diferentes
        tiempos necesarios para llevar acabo el estudio
    prom_lam : float
        Promedio de la columna de 'intervalo' necesario para calcular el
        parámetro lambda
    Returns
    -------
    lamda : float
        Parámetro lambda deseado, que representa la intensidad de llegada
    """
    prom_lam = mean(clientes['intervalo'])

    lamda = 1/prom_lam

    return lamda


def servicio(clientes):
    """Descripción de la función.
    Parameters
    ----------
    clientes : dataframe
        Dataframe que contiene el número de clientes y los diferentes
        tiempos necesarios para llevar acabo el estudio

    prom_nu : float
        Promedio de la columna de 'servicio' necesario para calcular el
        parámetro Nu
    Returns
    -------
    nu : float
        Parámetro Nu deseado, que representa la intensidad con la que salen
        los datos del proceso
    """
    prom_nu = mean(clientes['servicio'])

    nu = 1/prom_nu

    return nu


def parametros(A1, A2):
    """Descripción de la función.
    Parameters
    ----------
    lamda : float
        Parámetro lambda deseado, que representa la intensidad de llegada.
    nu : float
        Parámetro Nu deseado, que representa la intensidad con la que salen
        los datos del proceso.
    Returns
    -------
    i : int
        El ususario escoge este valor para definir en cuál estado quiere
        averiguar los parámetros

    Omega : float
        Parámetro de permanencia.

    p : float
        Probabilidad de pasar al siguiente estado superior.

    q: float
        Probabilidad de pasar al siguiente estado inferior.
    """

    lamda = A1
    nu = A2
    i = input('Número de estado para los parametros: ')
    i = int(i)

    Omega = lamda + nu*i
    p = lamda/(lamda + nu*i)
    q = nu*i / (lamda + nu*i)

    return i, Omega, p, q
