from point import point as point
import math


class Renderer:

    def __init__(self):
        self.world = []
        self.hud = []

    def draw(self, obj):
        self.world.append(obj)

    def sortByZValue(self,cam):  # sorts the squares by z value in order to render them
                                # should only be triangles but lazy
        centerPoints = []
        tris = []
        
        for obj in self.world:
            '''
            for square in obj.getSquares():
                
                squares.append(square)
                centerPoints.append(square.getCenter())
            '''
            for tri in obj.polygons:
                tris.append(tri)
                centerPoints.append(tri.getCenter())

        centerWithSquare = []  # should be [square,its distance]

        
        centerWithSquare = []
        for i in range(len(tris)):
            a = (centerPoints[i].x - cam.x) * (centerPoints[i].x - cam.x)
            b = (centerPoints[i].y - cam.y) * (centerPoints[i].y - cam.y)
            c = (centerPoints[i].z - cam.z) * (centerPoints[i].z - cam.z)

            d = math.sqrt(a + b + c)
            centerWithSquare.append([tris[i], d])

        temp = sorted(centerWithSquare, key=lambda x: x[1], reverse=True)




        self.world = list(map(lambda x: x[0], temp))

    def render(self, screen,camera):
        self.sortByZValue(camera)

        for obj in self.world:
            if type(obj).__name__ == "square":
                obj.draw(screen)
            if type(obj).__name__ == "triangle":
                obj.draw(screen)


        self.world = []


global render
render = Renderer()
