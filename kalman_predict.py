import numpy as np


# Simulator options.
sim_opt = {}
sim_opt['FIG_SIZE'] = [8, 8]
sim_opt['ALLOW_SPEEDING'] = True

class KalmanFilter:
    def __init__(self):
        self.prev_t = 0.
        # Initial State [[pos_x], [pos_y], [velocity_x], [velocity_y]]
        self.x = np.array([[55.],
                           [3.],
                           [5.],
                           [0.]])

        self.Gu = np.array([[0.],
                            [0.],
                            [0.],
                            [0.]])

        # Uncertainity Matrix
        self.P = np.array([[0., 0., 0., 0.],
                           [0., 0., 0., 0.],
                           [0., 0., 0., 0.],
                           [0., 0., 0., 0.]])

        # Next State Function
        self.F = np.array([[1., 0., 0., 0.],
                           [0., 1., 0., 0.],
                           [0., 0., 1., 0.],
                           [0., 0., 0., 1.]])

        # Measurement Function
        self.H = np.array([[1., 0., 0., 0.],
                           [0., 1., 0., 0.]])

        # Measurement Uncertainty
        self.R = np.array([[5.0, 0.],
                           [0., 5.0]])

        # Identity Matrix [[1., 0., 0., 0.],
        #                  [0., 1., 0., 0.],
        #                  [0., 0., 1., 0.],
        #                  [0., 0., 0., 1.]]
        self.I = np.eye(4, )

    def predict(self, t):
        dt = t - self.prev_t
        self.F[0, 2] = dt
        self.F[1, 3] = dt
        self.x = self.F @ self.x
        self.P = self.F @ self.P @ np.transpose(self.F)
        self.P[0, 0] += 0.1
        self.P[1, 1] += 0.1
        self.P[2, 2] += 0.1
        self.P[3, 3] += 0.1
        return

    def update(self, measurements, t):
        Z = np.array([measurements])
        y = np.transpose(Z) - (self.H @ self.x)
        S = self.H @ self.P @ np.transpose(self.H) + self.R
        K = self.P @ np.transpose(self.H) @ np.linalg.inv(S)
        self.x = self.x + (K @ y)
        self.P = (self.I - (K @ self.H)) @ self.P
        self.prev_t = t
        return [self.x[0], self.x[1]]

    def predict_yellow_red(self, light_location):
        light_duration = 3
        F_new = np.copy(self.F)
        F_new[0, 2] = light_duration
        F_new[1, 3] = light_duration
        x_new = F_new @ self.x
        if x_new[0] < light_location:
            return [False, x_new[0]]
        else:
            return [True, x_new[0]]

    def predict_yellow_red_speeding(self, light_location):
        check = self.predict_yellow_red(light_location)
        if check[0]:
            return check
        light_duration = 3
        F_new = np.copy(self.F)
        Gu_new = np.copy(self.Gu)
        acc = 1.25 
        Gu_new[0] = 0.5 * acc  # accelerating for one second
        Gu_new[2] = acc  # accelerating for one second
        F_new[0, 2] = 1
        F_new[1, 3] = 1
        x_new = F_new @ self.x + Gu_new  

        F_new[0, 2] = light_duration - 1
        F_new[1, 3] = light_duration - 1
        x_new = F_new @ x_new
        if x_new[0] < light_location:
            return [False, x_new[0]]
        else:
            return [True, x_new[0]]

