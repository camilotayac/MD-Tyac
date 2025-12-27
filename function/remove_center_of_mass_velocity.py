def remove_center_of_mass_velocity(vx:list,vcm:float,npart:int) -> list:
    vxr = [0.0] * npart
    for i in range(npart):
        vxr[i] = vx[i] - vcm
    return vxr
