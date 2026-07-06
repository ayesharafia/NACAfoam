import sys
import os

# FORCE project root into Python path (ROBUST FIX)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt

from geometry.naca4_generator import NACA4Generator
from mesh.mesh_parameters import MeshParameters
from mesh.ogrid_generator import OGridGenerator
def main():

    # Generate airfoil
    geometry = NACA4Generator(
        digits="4418",
        chord=1.0,
        n_points=400
    ).generate()

    # Mesh parameters
    params = MeshParameters()

    # Generate O-grid
    grid = OGridGenerator(
        geometry,
        params
    ).generate()

    plt.figure(figsize=(10, 10))

    # Radial lines
    for j in range(grid.X.shape[1]):
        plt.plot(grid.X[:, j], grid.Y[:, j], 'b-', linewidth=0.3)

    # Circumferential lines
    for i in range(grid.X.shape[0]):
        plt.plot(grid.X[i, :], grid.Y[i, :], 'b-', linewidth=0.3)

    # Airfoil
    plt.plot(grid.airfoil_x, grid.airfoil_y, 'r', linewidth=2)

    # Outer boundary
    plt.plot(grid.outer_x, grid.outer_y, 'k')

    plt.axis("equal")
    plt.grid(True)
    plt.title("Prototype O-Grid")
    plt.show()


if __name__ == "__main__":
    main()
