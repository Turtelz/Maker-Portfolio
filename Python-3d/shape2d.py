import pygame as pg 
import point 
from point import point as point
from random import randint
from copy import deepcopy


def projectArray(a):
    temp = []
    for i in a:
        temp.append(i.project())
    return temp

class triangle:
    def __init__(self,p1,p2,p3,color = (0,0,0)) -> None:
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.color = color
    
    def print(self):
        self.p1.print()
        self.p2.print()
        self.p3.print()
      
    def draw(self,screen):
        temp = projectArray([self.p1,self.p2,self.p3])
        


        pg.draw.polygon(screen,self.color,[temp[0],temp[1],temp[2]])
    def move(self,pos):
        self.p1.move(pos)
        self.p2.move(pos)   
        self.p3.move(pos)

    
    def rotate(self,angles,orgin):
      p1 = deepcopy(self.p1)
      p2 = deepcopy(self.p2)
      p3 = deepcopy(self.p3)
      p1.rotateAround(angles,orgin)
      p2.rotateAround(angles,orgin)
      p3.rotateAround(angles,orgin)

      
      return triangle(p1,p2,p3,self.color)
    
    def getCenter(self):
      return point([
        (self.p1.x + self.p2.x + self.p3.x) / 3, 
        (self.p1.y + self.p2.y + self.p3.y) / 3,
        (self.p1.z + self.p2.z + self.p3.z) / 3])
    
class square:
    def __init__(self,p1,p2,p3,p4,color = (0,0,0)):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.color = color
  
    def move(self,pos):
        self.p1.move(pos)
        self.p2.move(pos)   
        self.p3.move(pos)
        self.p4.move(pos)   

    def getCenter(self):
      return point([
        (self.p1.x + self.p2.x + self.p3.x + self.p4.x) / 4, 
        (self.p1.y + self.p2.y + self.p3.y + self.p4.y) / 4,
        (self.p1.z + self.p2.z + self.p3.z + self.p4.z) / 4])
    def print(self):
      self.p1.print()
      self.p2.print()
      self.p3.print()
      self.p4.print()
      
    def convert(self):

        p1 = self.p1
        p2 = self.p2
        p3 = self.p3
        tri = triangle(p1,p2,p3,self.color)

        p1 = self.p4
        p2 = self.p3
        p3 = self.p1
        tri2 = triangle(p1,p2,p3,self.color)

        return [tri,tri2]

    def draw(self,screen):
        temp = self.convert()

        temp[0].draw(screen)
        temp[1].draw(screen)