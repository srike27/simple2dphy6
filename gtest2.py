import sys
import math
import pygame as pg 

class circle:

    px = 30
    py = 30
    mflag = 0

    def updatestate(self):
        tmvx = self.velx
        tmvy = self.vely
        self.px+=self.velx
        self.py+=self.vely
        self.velx = self.velx + self.ax
        self.vely = self.vely + self.ay
        self.speed =math.sqrt(self.velx*self.velx+self.vely*self.vely)
        if self.ax==0:
            self.velx = tmvx
        if self.ay==0:
            self.vely = tmvy

    def impulse(self,acx,acy):
        self.ax = acx
        self.ay = acy
        self.updatestate()
        self.ax = 0
        self.ay = 0

    def frictiony(self,nu):
        self.mtest()
        if self.speed != 0: 
            #print(self.velx,self.vely)
            self.ax = -round((self.velx/self.speed)*nu)
            #self.ay = -round((self.vely/self.speed)*nu)
            #print(self.ax)
            #print(self.ay)
            self.updatestate()
            #print("velx",self.velx)
            #print("vely",self.vely)
            self.ax = 0
            #self.ay = 0
        else:
            self.ax=0
            #self.ay=0
            self.mtest()



    def frictionx(self,nu):
        self.mtest()
        if self.speed != 0: 
            #print(self.velx,self.vely)
            #self.ax = -round((self.velx/self.speed)*nu)
            self.ay = -round((self.vely/self.speed)*nu)
            #print(self.ax)
            #print(self.ay)
            self.updatestate()
            #print("velx",self.velx)
            #print("vely",self.vely)
            #self.ax = 0
            self.ay = 0
        else:
            #self.ax=0
            self.ay=0
            self.mtest()

    def friction(self,nu):
        self.mtest()
        if self.speed != 0: 
            #print(self.velx,self.vely)
            self.ax = -round((self.velx/self.speed)*nu)
            self.ay = -round((self.vely/self.speed)*nu)
            #print(self.ax)
            #print(self.ay)
            self.updatestate()
            #print("velx",self.velx)
            #print("vely",self.vely)
            self.ax = 0
            self.ay = 0
        else:
            self.ax=0
            self.ay=0
            self.mtest()

        

    def mtest(self):
        if self.velx != 0 and self.vely != 0:
            self.mflag = 1
        else:
            self.mflag = 0
    

    def __init__(self,x,y):
        self.px = x
        self.py = y
        self.velx = 0
        self.vely = 0
        self.ax = 0
        self.ay = 0
        self.speed =math.sqrt(self.velx*self.velx+self.vely*self.vely)
        self.mtest()
        self.vthresh = 10

    
