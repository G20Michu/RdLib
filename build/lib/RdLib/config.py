# config.py
import numpy as np
class Config:
    def __init__(self):

        self.Kalman = False #false value means kalman filter in turn off in all type measurement, True value means kalman filter is turn on in all type measurement
        self.Kalman_Chart_Path = '~/Documents/Kalman_Test' #Place where the graphs from kalman_test function are saved
        self.Kalman_Save_csv = False #False means program won't save masurement to the csv file located at the upper path.
        self.Kalman_Q =  np.diag([0.1, 0.1, 0.1, 0.1]) #By that value you can adjust kalman filter characteristic

        self.Serial_Port = '/dev/ttyS0' #that value referes to the raspberrypi serial port path
        self.Serial_Speed = '256000' #that value is set to communicate with Rd03d and Hlk-LD2450 radars.

        self.ctype = "Serial" #Serial/Gpio
        self.Detection_Mode = 'S' # S- single target M- multi target
        self.distance_units = "m" #in,ft,m,cm
        self.debug = False #True value allows to more output context in terminal 

    def set(self, **kwargs):
        for k, v in kwargs.items():
            if hasattr(self, k):
                setattr(self, k, v)

config = Config()
