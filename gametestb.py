import sys
import pygame as pg 
import gtest2

def run_game():
    x = 30
    y = 30
    dirx = 0
    diry  = 0
    velx = 0
    vely = 0
    vmod = 0
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
        if pressed[pg.K_UP]: diry = -1
        elif pressed[pg.K_DOWN]: diry = 1
        else: diry = 0
        if pressed[pg.K_LEFT]: dirx = -1
        elif pressed[pg.K_RIGHT]: dirx = 1
        else: dirx = 0
        
        if (dirx*diry == 0): vmod = 10
        elif (dirx or diry): vmod = 7
        else: vmod = 0
        
        x += dirx*vmod
        y += diry*vmod
        
        screen.fill((0, 0, 0))
        if is_blue: color = (0, 128, 255)
        else: color = (255, 100, 0)
        pg.draw.circle(screen, color,[x,y],30,0)
        
        pg.display.flip()
        clock.tick(60)


run_game()
