import sys
import pygame as pg 
import gtest2 as a

def run_game():
    x = 300
    y = 300
    k =1
    radius  =20

    ball = a.circle(x,y)
    
    done = False
    is_blue = False
    clock = pg.time.Clock()
    pg.init()
    screen = pg.display.set_mode((1200,800))
    pg.display.set_caption("first screen")
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        pressed = pg.key.get_pressed()
        dirx = 0
        diry = 0
        if(pressed[pg.K_UP] or pressed[pg.K_DOWN] or pressed[pg.K_LEFT] or pressed[pg.K_RIGHT]):
            
            if pressed[pg.K_UP]:
                ball.impulse(0,-k)
                diry = -1
            if pressed[pg.K_DOWN]:
                ball.impulse(0,k)
                diry = 1
            if pressed[pg.K_LEFT]:
                ball.impulse(-k,0)
                dirx = -1
            if pressed[pg.K_RIGHT]:
                ball.impulse(k,0)
                dirx = 1
        
        if(dirx ==0 and diry ==0):
            ball.friction(1)
        elif (diry == 0 and dirx!=0):
            ball.frictionx(1)
        elif (dirx == 0 and diry!=0):
            ball.frictiony(1)
         

        if pressed[pg.K_SPACE]:
            print ball.velx,ball.vely,ball.ax,ball.ay

        print screen
        x = (ball.px)
        y = (ball.py)
        if (x>1200-radius or x<radius):
            ball.velx = -int(0.5*ball.velx)
            #ball.ax = -1*ball.ax
            if(x>1200 -radius):
                ball.px = 1200 - radius
            else: ball.px = radius
        if (y>800 -radius or y<radius):
            ball.vely = -int(0.5*ball.vely)
            #ball.ay =-1*ball.ay
            if(y>800-radius):
                ball.py = 800 -radius
            else: ball.py = radius    
        screen.fill((0, 0, 0))
        if is_blue: color = (0, 128, 255)
        else: color = (255, 100, 0)
        pg.draw.circle(screen, color,[int(round(x)),int(round(y))],radius,0)
        
        pg.display.flip()
        clock.tick(60)


run_game()
