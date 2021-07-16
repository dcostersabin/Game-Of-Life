import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from RGBto2D import RGBto2D


class GameOfLife:
    def __init__(self, dpi=10, size=50, save=False, image=None):
        self.dpi = dpi
        self.grid = None
        self.fig = None
        self.ax = None
        self.im = None
        self.ON = 1
        self.OFF = 0
        self.fig_size = None
        self.size = size
        self.save = save
        self.image = image

    def create_grid(self):
        if self.image is not None:
            img = RGBto2D(self.image, save=True).get_bw()
            self.size = img.shape[0]
            self.grid = img
        else:
            self.grid = np.zeros((self.size, self.size))

    def randomize(self):
        random = np.random.random((2, 2))
        self.grid[0:2, 0:2] = (random > 0.75)

    def set_fig(self):
        self.fig, self.ax = plt.subplots()
        self.im = self.ax.imshow(self.grid, interpolation='nearest')

    def count_neighbors(self, x, y):
        count = 0
        for i in range(-1, 2, 1):
            for j in range(-1, 2, 1):
                if (i != 0) or (j != 0):
                    row = (x + i) % self.size
                    col = (y + i) % self.size
                    count += self.grid[row, col]
        return count

    def animate(self, frame):
        print(frame)
        new_grid = self.grid.copy()
        for row in range(self.size):
            for col in range(self.size):
                neigh = self.count_neighbors(row, col)

                if self.grid[row, col] == self.ON:
                    if (neigh < 2) or (neigh > 3):
                        new_grid[row, col] = self.OFF
                else:
                    if neigh == 3:
                        new_grid[row, col] = self.ON

        self.im.set_data(new_grid)
        self.grid = new_grid
        return self.im,

    def start(self):
        self.create_grid()
        if self.image is None:
            self.randomize()
        self.set_fig()
        ani = animation.FuncAnimation(self.fig, self.animate, frames=300, interval=300,
                                      save_count=10)
        if self.save:
            ani.save('demo.mp4', fps=60, extra_args=['-vcodec', 'libx264'])


if __name__ == '__main__':
    obj = GameOfLife(size=100, save=True, )
    obj.start()
