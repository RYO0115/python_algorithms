
import random

from math import *
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.patches import Rectangle
from matplotlib.transforms import Affine2D

class Vehicle:
    def __init__(self, v, w, dt):
        self._v = v
        self._w = w
        self._dt = dt
        self._x_init = 0.0
        self._y_init = 0.0
        self._theta_init = 0.0
        self._x = 0.0
        self._y = 0.0
        self._theta = 0.0
        self._vx = 0.0
        self._vy = 0.0
        self._truck_width = 7.0
        self._truck_length= 12.0

        self.__truck = PlotVehicle(self._truck_width, self._truck_length)

        self._pos_noise = 1.0
        self._theta_noise = 0.05

        print("theta/dt = ", 180*(w * dt)/pi)

    
    def InitPosition(self, x, y, theta):
        self._x_init = x
        self._y_init = y
        self._theta_init = theta
        self._x = x
        self._y = y
        self._theta = theta

        self._true_x = x
        self._true_y = y
        self._true_theta = theta
    
    def SetNoise(self, pos_noise, theta_noise):
        self._pos_noise = pos_noise
        self._theta_noise = theta_noise
    
    def ChangeVelocity(self, v):
        self._v = v
    
    def ChangeAngularVelocity(self, w):
        self._w = w

    def UpdateOneStep(self):
        theta = self._theta
        self._true_theta = self._true_theta + self._w * self._dt
        self._theta = self._theta + self._w * self._dt + random.uniform(-self._theta_noise, self._theta_noise)

        self._vx = self._v * cos(theta)
        self._vy = self._v * sin(theta)
        self._true_vx = self._v * cos(self._true_theta)
        self._true_vy = self._v * sin(self._true_theta)

        self._true_x = self._true_x + self._true_vx * self._dt
        self._true_y = self._true_y + self._true_vy * self._dt
        self._x = self._true_x + self._vx * self._dt + random.uniform(-self._pos_noise, self._pos_noise)
        self._y = self._true_y + self._vy * self._dt + random.uniform(-self._pos_noise, self._pos_noise)

        return [self._x,self._y,self._theta], [self._true_x, self._true_y, self._true_theta]

    def GetAllState(self):
        return([self._x, self._y, self._theta, self._vx, self._vy, self._w])
    
    def GetAllTrueState(self):
        return([self._true_x, self._true_y, self._true_theta, self._true_vx, self._true_vy, self._w])

    


    def PlotCurrentVehiclePosition(self, ax, **kwargs):
        ax.scatter( self._true_x, self._true_y, color="black" )

        truck_x = self._true_x
        truck_y = self._true_y
        truck_theta = self._true_theta

        self.__truck.PlotCurrentVehiclePosition( ax, truck_x, truck_y, truck_theta, **kwargs)



class PlotVehicle():
    def __init__(self, truck_width, truck_length):
        self.__truck_width = truck_width
        self.__truck_length = truck_length
        self.__body_color = "yellow"
        self.__tyre_color = "black"
        self.__cab_color = "blue"
    
    def ChangeTruckSize(self, truck_length, truck_width):
        self.__truck_width = truck_width
        self.__truck_length = truck_length
    
    def ChangeTruckBodyColor(self, body_color):
        self.__body_color = body_color

    def ChangeTyreColor(self, tyre_color):
        self.__tyre_color = tyre_color
    
    def ChangeCabColor(self, cab_color):
        self.__cab_color = cab_color
    

    def RelativeRectangle(self, width, height, center_tf, **kwargs):
        rect_origin_to_center = Affine2D().translate(width/2 , height/2)
        return(Rectangle((0,0), width, height, transform=rect_origin_to_center.inverted() + center_tf, **kwargs))

    def PlotCurrentVehiclePosition(self, ax, truck_x, truck_y, truck_theta, **kwargs):

        rect_center_x = truck_x + self.__truck_length * 0.25 * cos(truck_theta)
        rect_center_y = truck_y + self.__truck_length * 0.25 * sin(truck_theta)

        to_rear_axle_tf   = Affine2D().rotate(truck_theta - radians(90)).translate(truck_x, truck_y) + ax.transData
        to_body_center_tf = Affine2D().rotate(truck_theta - radians(90)).translate(rect_center_x,rect_center_y) + ax.transData
        body = self.RelativeRectangle(self.__truck_width, self.__truck_length, to_body_center_tf, edgecolor="black", facecolor=self.__body_color, **kwargs)

        tyre_width = 1.0
        tyre_length = 3.0
        front_tyre_pos_x = 0.3 * self.__truck_width
        front_tyre_pos_y = 0.4 * self.__truck_length
        tyre_base_angle = 0
        body_center_to_left_front_tf = Affine2D().rotate(radians(tyre_base_angle)).translate( -0.4*self.__truck_width, 0.5*self.__truck_length) # ステアを切る場合はrotateをいじる
        body_center_to_right_front_tf = Affine2D().rotate(radians(tyre_base_angle)).translate( 0.4*self.__truck_width,  0.5*self.__truck_length)

        body_center_to_left_rear_tf = Affine2D().rotate(radians(tyre_base_angle)).translate( -0.4*self.__truck_width, 0)
        body_center_to_right_rear_tf = Affine2D().rotate(radians(tyre_base_angle)).translate( 0.4*self.__truck_width, 0)

        body_center_to_cab_tf = Affine2D().rotate(radians(tyre_base_angle)).translate( -0.3*self.__truck_width, 0.6*self.__truck_length)

        cab = self.RelativeRectangle( 2.0, 2.0, body_center_to_cab_tf + to_rear_axle_tf, facecolor=self.__cab_color, edgecolor="black", **kwargs)

        left_rear_wheel = self.RelativeRectangle( tyre_width, tyre_length, body_center_to_left_rear_tf     + to_rear_axle_tf, facecolor=self.__tyre_color, edgecolor="black", **kwargs)
        right_rear_wheel = self.RelativeRectangle( tyre_width, tyre_length, body_center_to_right_rear_tf   + to_rear_axle_tf, facecolor=self.__tyre_color, edgecolor="black", **kwargs)

        ax.add_patch(left_rear_wheel)
        ax.add_patch(right_rear_wheel)
        ax.add_patch(body)
        ax.add_patch(cab)
        


if __name__ == "__main__":        


    vehicle = Vehicle(10.0,0.05,0.1)

    vehicle.InitPosition(0, 0, 0)

    fig,ax = plt.subplots(figsize=[20,20])

    vehicle.PlotCurrentVehiclePosition(ax, alpha=0.5)

    for i in range(1,100,1):
        state, true_state = vehicle.UpdateOneStep()
        #print(i,":",state)

        ax.scatter(state[0], state[1], color="red")
        ax.scatter(true_state[0], true_state[1], color="blue")
        if i%20 == 0:
            print(i)
            vehicle.PlotCurrentVehiclePosition(ax, alpha=0.5)

    vehicle.PlotCurrentVehiclePosition(ax, alpha=0.5)

    ax.grid()
    ax.axis('auto')
    ax.set_aspect('equal')
    plt.show()
