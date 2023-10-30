import math
import numpy as np

class Camera:

    def __init__(self,fov = 75,near = 0.0001,far = 10):
        self.hud = []
        self.world = []
        self.cameraAngles = [0, 0, 0]
        self.hfov = fov
        self.hfov = self.hfov * math.pi/180 # convert to radians
        self.vfov = 2*math.atan((height/width) * math.tan(self.hfov/2) )
        self.near = near
        self.far = far
        self.x = 0
        self.y = 0
        self.z = 0
  
    def addToWorld(self, object):
        
        self.world.append(object)

    def addToHud(self, hud):
        self.hud.append(object)

    def rotateCamera(
            self, angles
    ):  # angles is an array of length 3 for three angles in radians
        pass
    def draw(self,screen):
      pass
      
global width,height
width, height = 400,400

global cam 
cam = Camera()