import matplotlib.pyplot as plt

def plot_displacement_bars(x: list, xm: list, npart: int):
    """
    Grafica la diferencia (x - xm) como barras para visualizar
    la magnitud y dirección de las velocidades iniciales.
    """
    ids = range(npart)
    # Calculamos el desplazamiento (equivalente a v * dt)
    diff = [xi - xmi for xi, xmi in zip(x, xm)]
    
    plt.figure(figsize=(10, 6))
    
    # Asignamos colores: Verde si va a la derecha (+), Rojo si va a la izquierda (-)
    colors = ['green' if val >= 0 else 'red' for val in diff]
    
    plt.bar(ids, diff, color=colors, alpha=0.7)
    
    plt.axhline(0, color='black', linewidth=1)
    plt.ylabel('Desplazamiento Inicial ($x - x_m$)')
    plt.xlabel('Índice de la Partícula')
    plt.title('Inicialización de Velocidades (Visualizadas como Desplazamiento)')
    plt.grid(True, linestyle='--', alpha=0.5, axis='y')
    
    # Etiquetas explicativas
    max_val = max([abs(d) for d in diff]) if diff else 1.0
    plt.text(npart-1, max_val/2, "Velocidad (+)", color='green', ha='right', fontweight='bold')
    plt.text(npart-1, -max_val/2, "Velocidad (-)", color='red', ha='right', fontweight='bold')
    
    plt.tight_layout()
    plt.show()