import numpy as np

class NACA4Generator:

    def __init__(self, digits="4418", chord=1.0, n_points=200):
        self.digits = digits
        self.chord = chord
        self.n_points = n_points

        self.m = 0.04
        self.p = 0.4
        self.t = 0.18

    def thickness(self, x):
        return 5*self.t*(0.2969*np.sqrt(x)
                         - 0.1260*x
                         - 0.3516*x**2
                         + 0.2843*x**3
                         - 0.1036*x**4)

    def camber(self, x):
        yc = np.where(x < self.p,
                      (self.m/self.p**2)*(2*self.p*x - x**2),
                      (self.m/(1-self.p)**2)*((1-2*self.p) + 2*self.p*x - x**2))
        return yc

    def generate(self):

        beta = np.linspace(0, np.pi, self.n_points)
        x = (1 - np.cos(beta)) / 2

        yt = self.thickness(x)
        yc = self.camber(x)

        xu = x - yt * np.sin(0)
        yu = yc + yt * np.cos(0)

        xl = x + yt * np.sin(0)
        yl = yc - yt * np.cos(0)

        x_loop = np.concatenate([xu, xl[::-1]])
        y_loop = np.concatenate([yu, yl[::-1]])

        return type("Geom", (), {
            "x": x_loop,
            "y": y_loop
        })
