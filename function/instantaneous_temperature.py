from scipy.constants import Boltzmann
def instantaneous_temperature(npart:int,m:list,vxr:list,d:int):
    summvxr2 = 0
    for i in range(npart):
        summvxr2 += m[i]*(vxr[i]**2)
    nf = d*(npart-1)-1
    T = summvxr2/(nf*Boltzmann)
    return T