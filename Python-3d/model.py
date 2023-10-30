from copy import deepcopy
from point import point as p
from shape2d import triangle
from random import randint

class Model:
  def __init__(self):
    self.points = []
    self.pointOrder = []
    self.polygons = []
    self.orgin = p([0,0,0])

  def print(self):
    for p in self.points:
      p.print()
    

  @staticmethod
  def createFromFileName(fileName):
    self = Model()
    o = open(fileName)
    
    # start of reading
    line = o.readline().split()
    while len(line) != 0:

      if line[0] == "v":
        self.points.append(p([float(line[1]),float(line[2]),float(line[3])]))
      line = o.readline()
      line = line.split()

    
    line = o.readline().split()
    while len(line) != 0:

      if line[0] == "f":
        self.pointOrder.append([int(line[1]),int(line[2]),int(line[3])])
      line = o.readline()
      line = line.split() 

    # turning points into polygons and saving it
    for listOfPoints in self.pointOrder:
      p1 = deepcopy(self.points[listOfPoints[0] - 1])
      p2 = deepcopy(self.points[listOfPoints[1] - 1])
      p3 = deepcopy(self.points[listOfPoints[2] - 1])
      tri = triangle(p1,p2,p3,color = (randint(0,255),randint(0,255),randint(0,255)))
      self.polygons.append(tri)
   # print(f"polys: {self.polygons}")     # points: {self.points}        pointOrder: {self.pointOrder}")
    return self

      
  @staticmethod
  def createFromPolygons(polys):
    temp = Model()
    pol = deepcopy(polys)
    temp.polygons = pol
    temp.orgin = p([0,0,0])
    return temp

    
  def move(self,point): # temp  p is an array
    point = p(point)
    for tri in self.polygons:
      tri.move(point)


    self.orgin.x += point.x
    self.orgin.y += point.y
    self.orgin.z += point.z

  def rotate(self,angles,orgin = p([0,0,0])):
    rotatedPolygons = []
    for tri in self.polygons:
      rotatedPolygons.append(tri.rotate(angles,orgin))

    m = Model.createFromPolygons(rotatedPolygons)
    return m
    
  def draw(self,screen): # temperary 
    for tri in self.polygons:
       tri.draw(screen)
    #self.polygons[0].draw(screen)
    
