from dataclasses import dataclass


@dataclass
class MeshParameters:
    """
    Parameters controlling the O-grid mesh generation.
    All dimensions are normalized by chord length.
    """

    # Airfoil
    chord: float = 1.0

    # Farfield
    farfield_radius: float = 20.0

    # O-grid resolution
    airfoil_points: int = 400
    radial_layers: int = 80

    # Growth ratio from airfoil to farfield
    growth_rate: float = 1.05

    # Wake refinement (reserved for future C-grid support)
    wake_length: float = 10.0

    # Spanwise thickness for 2D OpenFOAM mesh
    span: float = 0.01
