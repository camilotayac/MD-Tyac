import math
import random
from function.lattice_pos import lattice_pos

def box_muller(npart: int) -> tuple[list, list, list]:
    """
    Inicializa posiciones y velocidades en un sistema unidimensional (1D)
    utilizando una red regular para las posiciones y el método de Box–Muller
    para generar velocidades con distribución normal.

    Esta función realiza tres tareas principales:
    1. Asigna posiciones iniciales en una red 1D.
    2. Genera velocidades aleatorias con distribución gaussiana (media cero).
    3. Calcula la suma de las velocidades, necesaria para eliminar posteriormente
       el movimiento del centro de masa.

    Parámetros
    ----------
    npart : int
        Número de partículas del sistema.
    x : list
        Lista donde se almacenan las posiciones (1D).
    vx : list
        Lista donde se almacenan las velocidades (1D).

    Retorna
    -------
    x : list
        Posiciones iniciales de las partículas.
    vx : list
        Velocidades iniciales generadas aleatoriamente.
    sumv : float
        Suma de las velocidades (proporcional a la velocidad del centro de masa).
    """
    m = [0.0] * npart
    x = [0.0] * npart
    vx = [0.0] * npart
    for i in range(npart):
        # Posición inicial en una red 1D
        x[i], m[i] = lattice_pos(i)

        # Generación de velocidad aleatoria (Box–Muller)
        R1 = random.random()
        R2 = random.random()
        vx[i] = math.sqrt(-math.log(R1)) * math.cos(2.0 * math.pi * R2)
    return m, x, vx