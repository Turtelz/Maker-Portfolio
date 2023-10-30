from shape2d import *
import numpy as np
from copy import deepcopy
from point import point as point



class cube:
    def __init__(self, x, y, z, width, height, depth):
        self.p1 = point([1, 1, 1])
        self.p2 = point([1, -1, 1])
        self.p3 = point([-1, -1, 1])
        self.p4 = point([-1, 1, 1])
        self.p5 = point([1, 1, -1])
        self.p6 = point([1, -1, -1])
        self.p7 = point([-1, -1, -1])
        self.p8 = point([-1, 1, -1])
        self.orgin = point([0,0,0])
        self.points = [
            self.p1, self.p2, self.p3, self.p4, self.p5, self.p6, self.p7,
            self.p8
        ]
        self.newSquares(changeColor=True)

    def newSquares(self,changeColor = False):
      if changeColor == True:
          self.c1 = (randint(0,255),randint(0,255),randint(0,255))
          self.c2 = (randint(0,255),randint(0,255),randint(0,255))
          self.c3 = (randint(0,255),randint(0,255),randint(0,255))
          self.c4 = (randint(0,255),randint(0,255),randint(0,255))
          self.c5 = (randint(0,255),randint(0,255),randint(0,255))
          self.c6 = (randint(0,255),randint(0,255),randint(0,255))
      self.s1 = square(self.p1, self.p2, self.p3, self.p4,self.c1)
      self.s2 = square(self.p1, self.p2, self.p6, self.p5,self.c2)
      self.s3 = square(self.p1, self.p4, self.p8, self.p5,self.c3)
      self.s4 = square(self.p7, self.p8, self.p5, self.p6,self.c4)
      self.s5 = square(self.p7, self.p8, self.p4, self.p3,self.c5)
      self.s6 = square(self.p7, self.p6, self.p2, self.p3,self.c6)


    def draw(self, screen):
        self.s1.draw(screen)
        self.s2.draw(screen)
        self.s3.draw(screen)
        self.s4.draw(screen)
        self.s5.draw(screen)
        self.s6.draw(screen)

    def getSquares(self):
      return [self.s1,self.s2,self.s3,self.s4,self.s5,self.s6]
  
    def move(self, pos=[0, 0, 0]):
        pos = point.arrayToPoint(pos)
        self.p1.move(pos)
        self.p2.move(pos)
        self.p3.move(pos)
        self.p4.move(pos)
        self.p5.move(pos)
        self.p6.move(pos)
        self.p7.move(pos)
        self.p8.move(pos)
        self.orgin.move(pos)
        self.newSquares()

    def rotate(self, angles,orgin):
        tempSquare = deepcopy(self)
        
        tempSquare.p1.rotateAround(angles,orgin)
        tempSquare.p2.rotateAround(angles,orgin)
        tempSquare.p3.rotateAround(angles,orgin)
        tempSquare.p4.rotateAround(angles,orgin)
        tempSquare.p5.rotateAround(angles,orgin)
        tempSquare.p6.rotateAround(angles,orgin)
        tempSquare.p7.rotateAround(angles,orgin)
        tempSquare.p8.rotateAround(angles,orgin)

        return tempSquare

    def setPValues(self):
        self.p1 = self.points[0]
        self.p2 = self.points[1]
        self.p3 = self.points[2]
        self.p4 = self.points[3]
        self.p5 = self.points[4]
        self.p6 = self.points[5]
        self.p7 = self.points[6]
        self.p8 = self.points[7]



    def print(self):
        self.orgin.print()