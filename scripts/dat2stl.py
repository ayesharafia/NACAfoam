import numpy as np
import os

dat_file = "constant/geometry/NACA4418.dat"
stl_file = "constant/triSurface/NACA4418.stl"

os.makedirs("constant/triSurface", exist_ok=True)

data = np.loadtxt(dat_file, skiprows=1)
x = data[:,0]
y = data[:,1]

with open(stl_file, "w") as f:
    f.write("solid naca4418\n")

    for i in range(len(x)-1):
        x1, y1 = x[i], y[i]
        x2, y2 = x[i+1], y[i+1]

        z1, z2 = 0.0, 0.1

        # triangle 1
        f.write("facet normal 0 0 1\nouter loop\n")
        f.write(f"vertex {x1} {y1} {z1}\n")
        f.write(f"vertex {x2} {y2} {z1}\n")
        f.write(f"vertex {x2} {y2} {z2}\n")
        f.write("endloop\nendfacet\n")

        # triangle 2
        f.write("facet normal 0 0 1\nouter loop\n")
        f.write(f"vertex {x1} {y1} {z1}\n")
        f.write(f"vertex {x2} {y2} {z2}\n")
        f.write(f"vertex {x1} {y1} {z2}\n")
        f.write("endloop\nendfacet\n")

    f.write("endsolid naca4418\n")

print("STL created:", stl_file)

