def scale_velocities(npart:int,vxr:list,fs:float) -> list:
    vxrs = [0.0] * npart
    for i in range(npart):
        vxrs[i] = vxr[i]*fs
    return vxrs