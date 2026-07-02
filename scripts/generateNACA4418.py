import numpy as np

# NACA 4418
m = 0.04      # maximum camber
p = 0.4       # location of maximum camber
t = 0.18      # thickness
c = 1.0       # chord

n = 201

beta = np.linspace(0, np.pi, n)
x = 0.5 * c * (1 - np.cos(beta))

yt = 5*t*c*(
    0.2969*np.sqrt(x/c)
    -0.1260*(x/c)
    -0.3516*(x/c)**2
    +0.2843*(x/c)**3
    -0.1015*(x/c)**4
)

yc = np.zeros_like(x)
dyc = np.zeros_like(x)

for i, xx in enumerate(x):
    xc = xx/c
    if xc < p:
        yc[i] = m*(2*p*xc - xc**2)/p**2
        dyc[i] = 2*m*(p-xc)/p**2
    else:
        yc[i] = m*((1-2*p)+2*p*xc-xc**2)/(1-p)**2
        dyc[i] = 2*m*(p-xc)/(1-p)**2

theta = np.arctan(dyc)

xu = x - yt*np.sin(theta)
yu = yc + yt*np.cos(theta)

xl = x + yt*np.sin(theta)
yl = yc - yt*np.cos(theta)

X = np.concatenate((xu[::-1], xl[1:]))
Y = np.concatenate((yu[::-1], yl[1:]))

with open("constant/geometry/NACA4418.dat", "w") as f:
    f.write("NACA4418\n")
    for xx, yy in zip(X, Y):
        f.write(f"{xx:.8f} {yy:.8f}\n")

print("Generated NACA4418.dat")
