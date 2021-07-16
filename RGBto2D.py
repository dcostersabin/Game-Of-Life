import numpy as np
import os
import cv2


class RGBto2D:
    def __init__(self, name, save=False):
        self.path = os.getcwd() + '/images/' + name
        self.gray = None
        self.bw = None
        self.save = save

    def to_array(self):
        image = cv2.imread(self.path, cv2.IMREAD_GRAYSCALE)
        image = cv2.resize(image, dsize=(500, 500))
        self.gray = np.array(image)

    def to_bw(self):
        bw = np.array(self.gray).copy()
        bw[bw < 128] = 0
        bw[bw >= 128] = 1
        self.bw = bw

    def get_bw(self):
        self.to_array()
        self.to_bw()
        if self.save:
            bw = np.array(self.gray).copy()
            bw[bw < 128] = 0
            bw[bw >= 128] = 255
            cv2.imwrite(os.getcwd() + '/images/' + 'new.png', bw)
        return self.bw


if __name__ == '__main__':
    obj = RGBto2D('test.png', save=True)
    o = obj.get_bw()
