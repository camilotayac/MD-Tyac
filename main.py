from function.initv import initv
if __name__ == "__main__":
    n_particulas = 10
    temperatura = 300
    dimension = 1
    delta_t = 0.005 
    grafica_initv = True
    x,vx,xm = initv(n_particulas,temperatura,dimension,delta_t,grafica_initv)
