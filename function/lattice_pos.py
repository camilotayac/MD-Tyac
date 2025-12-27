import random
def lattice_pos(i:int, a:float=1.0) -> float:
    """
    Genera la posición inicial de una partícula en una red unidimensional (1D).

    En este modelo de Dinámica Molecular, las partículas se colocan inicialmente
    sobre una red regular unidimensional (lattice 1D), es decir, todas las
    partículas se distribuyen a lo largo de una sola coordenada espacial (eje x),
    separadas por una distancia constante.

    La posición de cada partícula se define como:
        x_i = i * a

    donde:
    - i es el índice de la partícula (i = 0, 1, 2, ..., N−1)
    - a es el espaciamiento de la red (distancia fija entre partículas consecutivas)

    Este procedimiento se utiliza para:
    - Evitar solapamientos iniciales entre partículas
    - Proporcionar una configuración inicial ordenada y numéricamente estable
    - Permitir que el desorden y la dinámica emerjan posteriormente a partir
      de las velocidades iniciales y la integración de las ecuaciones de movimiento

    La red inicial no representa necesariamente una configuración física real,
    sino un punto de partida conveniente para la simulación, tal como se describe
    en Frenkel y Smit, Understanding Molecular Simulation.

    Parámetros
    ----------
    i : int
        Índice de la partícula en el sistema.
    a : float, opcional
        Espaciamiento de la red unidimensional (por defecto a = 1.0).

    Retorna
    -------
    float
        Posición inicial de la partícula i en el eje x.
    """
    x = i * a
    m = random.random()
    return x,m