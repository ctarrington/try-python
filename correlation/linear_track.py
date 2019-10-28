import numpy as np

class LinearTrack():
    def __init__(self, box):
        self.box = box
        self.x = np.random.uniform(0, box.width)
        self.y = np.random.uniform(0, box.height)
        self.z = np.random.uniform(0, box.depth)
        self.dx = np.random.normal(40, 10)
        self.dy = np.random.normal(0, 2)
        self.dz = np.random.normal(40, 10)

    def tick(self, tick_size):
        # step by tick size in seconds
        # returns new x, y, z
        self.x = self.x + self.dx * tick_size
        self.y = self.y + self.dy * tick_size
        self.z = self.z + self.dz * tick_size

        return (self.x, self.y, self.z)






