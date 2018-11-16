import sys
import pygame as pg 
import gtest2 as a
import math

def run_game():
    x = 20
    y = 20
    k =1
    radius  =20
    prod = 0.055
    kpp = 0.1
    kpv = prod/kpp
    i= 0
    j=0

    ball = a.circle(x,y)
    
    done = False
    is_blue = False
    clock = pg.time.Clock()
    pg.init()
    screen = pg.display.set_mode((1000,1000))
    pg.display.set_caption("first screen")
    xtga = [100 , 150 , 200, 250, 300, 350]
    ytga = [100 , 100 , 100, 100, 100, 100]
    xtg = xtga[0]
    ytg = ytga[0]
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        x = (ball.px)
        y = (ball.py)
        vx = ball.velx
        vy = ball.vely

        vrx = int(kpp*(xtg - x))
        vry = int(kpp*(ytg - y))
 
        kx = int(kpv*(vrx - vx))
        ky = int(kpv*(vry - vy))

        if(vx>0):
            dirx =1
        elif vx<0:
            dirx =-1
        else:
            dirx =0
        if vy>0:
            diry =1
        elif vy<0:
            diry =-1
        else:
            diry =0
        
        ball.impulse(kx,ky)

        if(dirx ==0 and diry ==0):
            ball.friction(1)
        elif (diry == 0 and dirx!=0):
            ball.frictionx(1)
        elif (dirx == 0 and diry!=0):
            ball.frictiony(1)
         
        


        
        if (x>1000-radius or x<radius):
            ball.velx = -int(0.5*ball.velx)
            #ball.ax = -1*ball.ax
            if(x>1000 -radius):
                ball.px = 1000 - radius
            else: ball.px = radius
        if (y>1000 -radius or y<radius):
            ball.vely = -int(0.5*ball.vely)
            #ball.ay =-1*ball.ay
            if(y>1000-radius):
                ball.py = 1000 -radius
            else: ball.py = radius    
        screen.fill((0, 0, 0))
        pg.draw.circle(screen, (0, 128 , 255) ,[xtg,ytg],radius,0)
        if is_blue: color = (0, 128, 255)
        else: color = (255, 100, 0) 
        pg.draw.circle(screen, color,[int(round(x)),int(round(y))],radius,0)
        
        if(i == 120):
            xtg = xtga[j]
            ytg = (j+1)*ytga[j]
            j = j+1
            if(j==6):
                j=0
            i =0
        i = i+1
        pg.display.flip()
        clock.tick(60)


run_game()