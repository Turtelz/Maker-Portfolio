from shape3d import *
import numpy as np
import math
from camera import Camera, width,height,cam
from renderer import render
from model import Model as m

cam.vfov = 40 * math.pi/180

screen = pg.display.set_mode((width, height))
clock = pg.time.Clock()
degreeScaler =  180 / math.pi

c = cube(0, 0, 0, 0, 0, 0)
c.move([0, 0, 10])
x = 0
y = 0
z = 0 

dx = 0.01
dy = 0.01
dz = 0.01

#teapot = m.createFromFileName("Cube.obj")  #Comment out for Cube
teapot = m.createFromFileName("teapot.obj")  #Comment out for Teapot
#teapot = m.createFromFileName("filename.obj")  #if you want to use own obj file replace "filename" with the actual name of the file

teapot.move([0, 0, 10])
while True:
    screen.fill((255, 255, 255))
    clock.tick(60)
    keys = pg.key.get_pressed()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()



    x += dx
    y += dy
    z += dz
    temp = c.rotate([x,y,z],c.orgin)
    rotatedTeapot = teapot.rotate([x,y,z], orgin = teapot.orgin)
    render.draw(rotatedTeapot)
    
    if keys[pg.K_s]:
       teapot.move([0, -1, 0])
       pass
    if keys[pg.K_w]:
        teapot.move([0, 1, 0])
        pass
    if keys[pg.K_a]:
        teapot.move([1, 0, 0])
        pass
    if keys[pg.K_d]:
        teapot.move([-1, 0, 0])
        pass
    #rotatedTeapot.draw(screen)
    
    render.render(screen,cam)
    pg.display.flip()