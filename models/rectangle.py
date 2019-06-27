import numpy as np


class Rectangle():
    center_x = 0
    center_y = 0
    width = 0
    height = 0
    e1 = [0, 0]
    e2 = [0, 0]
    e3 = [0, 0]
    e4 = [0, 0]

    r1 = [0, 0]
    r2 = [0, 0]
    r3 = [0, 0]
    r4 = [0, 0]

    def __init__(self, c_x, c_y, w, h):
        self.center_x = c_x
        self.center_y = c_y
        self.width = w
        self.height = h
        self.r1 = [0 - (self.width/2), 0 + (self.height / 2)]
        self.r2 = [0 - (self.width / 2), 0 - (self.height / 2)]
        self.r4 = [0 + (self.width / 2), 0 + (self.height / 2)]
        self.r3 = [0 + (self.width / 2), 0 - (self.height / 2)]
        self.updated_edges()

    def get_point_list(self):
        return [self.e1, self.e2, self.e3, self.e4]

    def move(self, x, y):
        self.center_x = x
        self.center_y = y
        self.updated_edges()

    def updated_edges(self):
        # newX = centerX + (point2x - centerX) * Math.cos(x) - (point2y - centerY) * Math.sin(x);

        # newY = centerY + (point2x - centerX) * Math.sin(x) + (point2y - centerY) * Math.cos(x);
        self.e1 = [self.center_x + self.r1[0], self.center_y + self.r1[1]]
        self.e2 = [self.center_x + self.r2[0], self.center_y + self.r2[1]]
        self.e4 = [self.center_x + self.r4[0], self.center_y + self.r4[1]]
        self.e3 = [self.center_x + self.r3[0], self.center_y + self.r3[1]]

    def rotate(self, deg):
        theta = np.radians(deg)
        c, s = np.cos(theta), np.sin(theta)
        R = np.array(((c, -s), (s, c)))

        v1 = np.array([[self.r1[0], self.r1[1]]])
        v1 = np.transpose(v1)
        v1_r = R.dot(v1)
        self.r1[0] = v1_r[0]
        self.r1[1] = v1_r[1]

        v2 = np.array([[self.r2[0], self.r2[1]]])
        v2 = np.transpose(v2)
        v2_r = R.dot(v2)
        self.r2[0] = v2_r[0]
        self.r2[1] = v2_r[1]

        v3 = np.array([[self.r3[0], self.r3[1]]])
        v3 = np.transpose(v3)
        v3_r = R.dot(v3)
        self.r3[0] = v3_r[0]
        self.r3[1] = v3_r[1]

        v4 = np.array([[self.r4[0], self.r4[1]]])
        v4 = np.transpose(v4)
        v4_r = R.dot(v4)
        self.r4[0] = v4_r[0]
        self.r4[1] = v4_r[1]

        self.updated_edges()
