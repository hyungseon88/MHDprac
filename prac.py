import numpy as np
import matplotlib.pyplot as plt

# Define simulation parameters
nx = 50 # number of grid points in x-direction
ny = 50 # number of grid points in y-direction
dx = 0.1 # grid spacing in x-direction
dy = 0.1 # grid spacing in y-direction
dt = 0.01 # time step
tmax = 2.0 # maximum simulation time

# Define fluid properties
rho = 1.0 # density
mu = 0.1 # viscosity
gamma = 1.4 # adiabatic index
B0 = 1.0 # magnetic field strength

# Define initial conditions
u = np.zeros((nx,ny)) # x-velocity
v = np.zeros((nx,ny)) # y-velocity
p = np.ones((nx,ny)) # pressure
Bx = np.zeros((nx,ny)) # x-component of magnetic field
By = np.zeros((nx,ny)) # y-component of magnetic field

# Define boundary conditions
u[:,0] = 1.0 # left boundary
u[:,-1] = 0.0 # right boundary
v[0,:] = 0.0 # bottom boundary
v[-1,:] = 0.0 # top boundary

# Initialize variables
t = 0.0

# Define plot parameters
fig, ax = plt.subplots()
im = ax.imshow(u, cmap='jet', origin='lower', extent=[0, nx*dx, 0, ny*dy])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('2D Fluid Flow Simulation')

# Define finite volume method
while t < tmax:
    # Calculate fluxes
    Fx = rho*u**2 + p + Bx**2 - B0**2
    Fy = rho*u*v + By*Bx
    Gx = rho*u*v + By*Bx
    Gy = rho*v**2 + p + By**2 - B0**2

    # Calculate gradients
    dFx_dx = np.gradient(Fx,dx,axis=0)
    dFy_dy = np.gradient(Fy,dy,axis=1)
    dGx_dx = np.gradient(Gx,dx,axis=0)
    dGy_dy = np.gradient(Gy,dy,axis=1)

    # Calculate time derivatives
    du_dt = -(1/rho)*dFx_dx - (1/rho)*dFy_dy
    dv_dt = -(1/rho)*dGx_dx - (1/rho)*dGy_dy
    dp_dt = -gamma*p*(dFx_dx + dGy_dy) - gamma*p*(u*dFx_dx + v*dFy_dy)
    dBx_dt = np.zeros((nx,ny))
    dBy_dt = np.zeros((nx,ny))

    # Update variables
    u += dt*du_dt
    v += dt*dv_dt
    p += dt*dp_dt
    Bx += dt*dBx_dt
    By += dt*dBy_dt

    # Update time
    t += dt

    # Update plot
    im.set_data(u)
    plt.pause(0.01)
    plt.draw()
    #plt.clf()