def check_center_of_mass_momentum(npart:int,m:list,vxr:list) -> str:
    summvxr = 0
    for i in range(npart):
        summvxr += m[i]*vxr[i]
    return print(f"Suma de velocidades ponderadas por la masa después de eliminar el centro de masa (≈ 0): {summvxr}")
