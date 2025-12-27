import math
from function.box_muller import box_muller
from function.center_of_mass_velocity import center_of_mass_velocity
from function.remove_center_of_mass_velocity import remove_center_of_mass_velocity
from function.check_center_of_mass_momentum import check_center_of_mass_momentum
from function.instantaneous_temperature import instantaneous_temperature
from function.scale_velocities import scale_velocities
from function.initialize_previous_positions import initialize_previous_positions
from function.plot_displacement_bars import plot_displacement_bars

def initv(npart:int,temp:float,d:int,dt:float,graf:bool) -> tuple[list,list,list]:
    m, x, vx = box_muller(npart)
    vcm = center_of_mass_velocity(npart,m,vx)
    vxr = remove_center_of_mass_velocity(vx,vcm,npart)
    check_center_of_mass_momentum(npart,m,vxr)
    T = instantaneous_temperature(npart,m,vxr,d)
    fs = math.sqrt(temp / T)
    vxrs = scale_velocities(npart,vxr,fs)
    xm = initialize_previous_positions(x,vxrs,dt,npart)
    if graf:
        plot_displacement_bars(x,xm,npart)
    return x, vx, xm


