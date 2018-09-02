import sys
import pygame as pg 
import gtest2 as a

def run_game():
    x = 30
    y = 30

    ball = a.circle(x,y)
    
    done = False
    is_blue = True
    clock = pg.time.Clock()
    pg.init()
    screen = pg.display.set_mode((1200,800))
    pg.display.set_caption("first screen")
    print(clock)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        pressed = pg.key.get_pressed()
        if(pressed[pg.K_UP] or pressed[pg.K_DOWN] or pressed[pg.K_LEFT] or pressed[pg.K_RIGHT]):
            if pressed[pg.K_UP]: ball.impulse(0,-1)
            if pressed[pg.K_DOWN]: ball.impulse(0,1)
            if pressed[pg.K_LEFT]: ball.impulse(-1,0)
            if pressed[pg.K_RIGHT]: ball.impulse(1,0)
        else:
            ball.friction(1)
        if pressed[pg.K_SPACE]:
            print ball.velx,ball.vely,ball.ax,ball.ay
        x = (ball.px)
        y = (ball.py)
        
        
        screen.fill((0, 0, 0))
        if is_blue: color = (0, 128, 255)
        else: color = (255, 100, 0)
        pg.draw.circle(screen, color,[int(round(x)),int(round(y))],30,0)
        
        pg.display.flip()
        clock.tick(60)


run_game()
