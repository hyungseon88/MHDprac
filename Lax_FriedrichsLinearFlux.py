import numpy as np
import matplotlib.pyplot as plt

'''
CFL condition

lambda = dt/dx
next_u = 0.5*(right_u+left_u) - 0.5*lambda*(right_flux-left_flux)
       ~ 0.5*(right_u+left_u) - 0.5*lambda*dflux/du*(right_u-left_u)

Von-Neumann Analysis
A = cos(kdx) - i*lambda*dflux/du*sin(kdx)
A^2 = 1-((lambda*dflux/du)**2-1)*sin(kdx)**2 > 0
(lambda*dflux/du)**2-1 < 0
lambda*dflux/du < 1

monotonously growing Lipschitz continuous fluxes
oscillation generally arise
'''

# Define parameters
nx = 150  # number of grid points
L = 15 # length of domain
dx = L / nx  # grid spacing
c = 1.0   # wave speed
t_final = 0.1  # final time
dt = 0.2 * dx / abs(c)  # time step

# Define initial condition
x = np.linspace(0, L, nx)
u = np.zeros(nx)

# Initial condition
#u[(x>=3.5) & (x<=4)] = 1
u[(x>=3) & (x<=(4+dx))] = 1

# Lax–Friedrichs method
def update(u):
    return 0.5*(u[2:]+u[:-2])-0.5*dt/dx*(F(u[2:])-F(u[:-2]))

def F(u):
    return u

def plot(x, u):
    plt.clf()
    plt.plot(x,u)
    plt.xlim(3,4.5)
    plt.pause(0.1)

t = 0.0
plot(x,u)

while t < t_final:

    u[1:-1] = update(u)

    #Define boundary condition
    u[0] = 0
    u[-1] = 0

    t += dt
    plot(x,u)

plt.show()