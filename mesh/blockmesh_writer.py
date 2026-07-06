from pathlib import Path


class BlockMeshWriter:

    def __init__(self, ogrid, thickness=0.01):
        self.grid = ogrid
        self.thickness = thickness

    def write(self, filename):

        with open(filename, "w") as f:

            self.write_header(f)
            self.write_vertices(f)

    def write_header(self, f):

        f.write(
"""FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      blockMeshDict;
}

convertToMeters 1.0;

"""
        )

    def write_vertices(self, f):

        X = self.grid.X
        Y = self.grid.Y

        layers, n = X.shape

        f.write("vertices\n(\n")

        # Front plane (z = 0)
        for i in range(layers):
            for j in range(n):
                f.write(
                    f"    ({X[i,j]:.8f} {Y[i,j]:.8f} 0.0)\n"
                )

        # Back plane (z = thickness)
        for i in range(layers):
            for j in range(n):
                f.write(
                    f"    ({X[i,j]:.8f} {Y[i,j]:.8f} {self.thickness})\n"
                )

        f.write(");\n\n")
