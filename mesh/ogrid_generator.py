from dataclasses import dataclass
import numpy as np

from mesh.mesh_parameters import MeshParameters


@dataclass
class OGrid:

    # Airfoil boundary
    airfoil_x: np.ndarray
    airfoil_y: np.ndarray

    # Outer boundary
    outer_x: np.ndarray
    outer_y: np.ndarray

    # Radial grid
    X: np.ndarray
    Y: np.ndarray


class OGridGenerator:

    def __init__(self, geometry, params: MeshParameters):

        self.geometry = geometry
        self.params = params

    def generate(self):

        # Airfoil boundary
        airfoil_x = self.geometry.x
        airfoil_y = self.geometry.y

        n = len(airfoil_x)

        # Uniform angle distribution
        theta = np.linspace(0, 2*np.pi, n, endpoint=False)

        R = self.params.farfield_radius * self.params.chord

        outer_x = R * np.cos(theta)
        outer_y = R * np.sin(theta)

        layers = self.params.radial_layers

        X = np.zeros((layers, n))
        Y = np.zeros((layers, n))

        for i in range(layers):

            s = i / (layers - 1)

            X[i] = (1 - s) * airfoil_x + s * outer_x
            Y[i] = (1 - s) * airfoil_y + s * outer_y

        return OGrid(
            airfoil_x,
            airfoil_y,
            outer_x,
            outer_y,
            X,
            Y
        )
