def initialize_previous_positions(x: list, vxrs: list, dt: float, npart: int) -> list:
    xm = [0.0] * npart
    for i in range(npart):
        xm[i] = x[i] - vxrs[i] * dt
    return xm