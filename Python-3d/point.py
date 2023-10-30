import numpy as np
import math
from camera import cam,width,height

class point:
  def __init__(self,xyz):
    self.x = xyz[0]
    self.y = xyz[1]
    self.z = xyz[2]
    self.w = 1
  def print(self):
    print(self.x,self.y,self.z,self.w)
    
  @classmethod
  def arrayToPoint(self,a):
    return point(a)
  def __add__(self, o):
    if type(o).__name__ == "point":
      return point([self.x - o.x,self.y - o.y,self.z - o.z])
    else:
      print("not correct type")

  def __truediv__(self,o):
    return point([self.x/o,self.y/o,self.z/o])
  def move(self,movement): # movement is also a point
    self.x += movement.x
    self.y += movement.y
    self.z += movement.z
  
  def convertToArray(self):
    return [self.x/self.w,self.y/self.w,self.z/self.w]
  def convertToHomo(self):
    return [self.x,self.y,self.z,self.w]

  
  
  def rotateAround(self,angle,orgin): # angle is a array of 3 angles
    x = orgin.x - self.x
    y = orgin.y - self.y 
    z = orgin.z - self.z 

    ax = angle[0]
    ay = angle[1]
    az = angle[2]

    m = [x,y,z]
    mx = [
          [1 , 0 ,0],
          [0,math.cos(ax),-math.sin(ax)],
          [0,math.sin(ax),math.cos(ax)]
          ]
    my = [
          [math.cos(ay),0,math.sin(ay)],
          [0,1,0],
          [-math.sin(ay),0,math.cos(ay)]
          ]
    mz = [
          [math.cos(az),-math.sin(az),0],
          [math.sin(az),math.cos(az),0],
          [0,0,1]
          ]
    
    m = np.matmul(np.matmul(np.matmul(my,mx), mz),m)
    self.x = m[0]
    self.y = m[1]
    self.z = m[2]
    
    self.x += orgin.x
    self.y += orgin.y
    self.z += orgin.z
    
    
  def project(self):

      a1 = [
            [1/((width/height)*math.tan(cam.vfov/2)),0,0,0],
            [0,1/(math.tan(cam.vfov/2)),0,0],
            [0,0,cam.far/(cam.far-cam.near),(-cam.near*cam.far)/(cam.far-cam.near)],
            [0,0,1,0]
           ]
      pos = np.matmul(a1,self.convertToHomo())
      pos = self.viewVolumeToScreen(pos)

      return pos  
  def viewVolumeToScreen(self,point):
      #print(point[0],point[1])
      temp = [point[0]/point[3],point[1]/point[3]]
      temp[0] *= width/2
      temp[1] *= height/2
    
      temp[0] += width/2
      temp[1] += height/2
      
      return temp
  def print(self):
    print(self.x,self.y,self.z)