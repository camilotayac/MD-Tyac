def center_of_mass_velocity(npart: int,m: list, vx:list) -> float:
    summ = 0
    sumvm = 0
    for i in range(npart):
        summ += m[i]
        sumvm += m[i]*vx[i]
    vcm = sumvm/summ
    return vcm