
# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# %%
class SensorTF:
    def __init__(self, x, y, z, roll, pitch, yaw, radians=True):
        self._x     = x
        self._y     = y
        self._z     = z
        self._roll  = roll
        self._pitch = pitch
        self._yaw   = yaw

        if radians == False:
            self._roll  *= np.pi / 180.0
            self._pitch *= np.pi / 180.0
            self._yaw   *= np.pi / 180.0

        self._rot   = np.zeros([4,4])
        self._rotx  = np.zeros([4,4])
        self._roty  = np.zeros([4,4])
        self._rotz  = np.zeros([4,4])

        self.CreateXRotMat()
        self.CreateYRotMat()
        self.CreateZRotMat()



    def CreateXRotMat(self):
        self._rotx[0,0] = 1.0
        cos = np.cos(self._roll)
        sin = np.sin(self._roll)
        self._rotx[1,1] = cos
        self._rotx[1,2] = -sin
        self._rotx[2,1] = sin
        self._rotx[2,2] = cos
        #print(self._rotx)

    def CreateYRotMat(self):
        self._roty[1,1] = 1.0
        cos = np.cos(self._pitch)
        sin = np.sin(self._pitch)
        self._roty[0,0] = cos
        self._roty[2,2] = sin
        self._roty[2,0] = -sin
        self._roty[2,2] = cos
        #print(self._roty)

    def CreateZRotMat(self):
        self._rotz[2,2] = 1.0
        cos = np.cos(self._yaw)
        sin = np.sin(self._yaw)
        self._rotz[0,0] = cos
        self._rotz[0,1] = -sin
        self._rotz[1,0] = sin
        self._rotz[1,1] = cos
        #print(self._rotz)

    def CreateZYXEuler(self):
        self._rot = np.dot(self._rotz, np.dot(self._rotx,self._roty))
        #print(self._rot)
        return(self._rot)

    def CreateTFMat(self):
        self.CreateZYXEuler()
        self._rot[0,3] = self._x
        self._rot[1,3] = self._y
        self._rot[2,3] = self._z
        self._rot[3,3] = 1.0
        print(self._rot)
        return(self._rot)





# %%
s_tf = SensorTF( 1, 0, 0, 0.0, 0.0, 30, False)
#rot = s_tf.CreateZYXEuler()
rot = s_tf.CreateTFMat()


# %%
# range = 5.0 angle = 30
# sensor x = 7.0, y=-1.0 z = 0 heading = -45
# Truck x = 10, y = 10 z = 0 heading = 30deg

range = 5.0 #[m]
angle = 30.0 #[deg]
angle *= np.pi / 180.0

# Sensor Origin
x = range * np.cos(angle)
y = range * np.sin(angle)
z = 0
print("Sensor: (x,y,z)=(", x, ",", y, ",", z, ")")
raw_trgt_pos = np.zeros(4)
raw_trgt_pos[0] = x
raw_trgt_pos[1] = y
raw_trgt_pos[2] = z
raw_trgt_pos[3] = 1

sensor_tf = SensorTF( 10.0, 0.0, 0, 0, 0, -30, False)
rot = sensor_tf.CreateTFMat()

sensor_trgt_pos = np.dot(rot,raw_pos.T)
print("sensor_pos:")
print(sensor_trgt_pos)

truck_tf        = SensorTF( 0.0, 0.0, 0, 0, 0, 30, False)
truck_rot       = truck_tf.CreateTFMat()
truck_trgt_pos  = np.dot( truck_rot, sensor_trgt_pos.T)
print("Truck Target Pos:")
print(truck_trgt_pos)


# %%



