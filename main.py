#!/usr/bin/env python3
import sys
import numpy as np
from glfw.GLFW import *
from OpenGL.GL import *
from OpenGL.GLU import *


def startup():
    update_viewport(None, 800, 800)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)


def spin(angle):
    glRotatef(angle,1.0,0.0,0.0)
    glRotatef(angle,0.0,1.0,0.0)
    glRotatef(angle,0.0,0.0,1.0)


def shutdown():
    pass


def axes():
    glBegin(GL_LINES)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-5.0, 0.0, 0.0)
    glVertex3f(5.0, 0.0, 0.0)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, -5.0, 0.0)
    glVertex3f(0.0, 5.0, 0.0)

    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, -5.0)
    glVertex3f(0.0, 0.0, 5.0)

    glEnd()

def plane():
    global map, dim
    dim=100
    distance=30
    move=15
    map=np.zeros((dim,dim,3))
    for i in range (steps):
        for n in range (steps):
            map[i][n]=[(i-move)*distance,(n-move)*distance,0]

def color():
    global color_map
    color_map=np.zeros((steps,steps,3))
    for i in range (steps):
        for n in range (steps):
            color_map[i][n]=[np.random.rand(),np.random.rand(),np.random.rand()]

def calc():
    global steps,egg
    steps=30
    egg=np.zeros((steps,steps,3))
    u=0
    for u_start in range (steps):
        v=0
        for v_start in range (steps):
            x=(-90*u**5+225*u**4-270*u**3+180*u**2-45*u)*np.cos(np.pi*v)
            y=160*u**4-320*u**3+160*u**2-5
            z=(-90*u**5+225*u**4-270*u**3+180*u**2-45*u)*np.sin(np.pi*v)
            egg[u_start][v_start]=[x,y,z]
            v+=1/(steps-1)
        u+=1/(steps-1)

def zad1():
    for u_start in range (steps):
        for v_start in range (steps):
            glBegin(GL_POINTS)          
            glColor3ub(255, 255, 0)
            glVertex3f(egg[u_start,v_start][0],egg[u_start,v_start][1],egg[u_start,v_start][2])
            glEnd()


def zad2():
    glBegin(GL_LINES)
    for u_start in range (steps):
        for v_start in range (steps):
            if u_start!=steps-1:
                glVertex3f(egg[u_start][v_start][0],egg[u_start][v_start][1],egg[u_start][v_start][2])
                glVertex3f(egg[u_start+1][v_start][0],egg[u_start+1][v_start][1],egg[u_start+1][v_start][2])
            if v_start!=steps-1:
                glVertex3f(egg[u_start][v_start][0],egg[u_start][v_start][1],egg[u_start][v_start][2])
                glVertex3f(egg[u_start][v_start+1][0],egg[u_start][v_start+1][1],egg[u_start][v_start+1][2]) 
    glEnd()


def zad3():
    
    glBegin(GL_TRIANGLES)
    for u_start in range (steps-1):
        for v_start in range (steps-1):
            glColor3f(color_map[u_start][v_start][0],color_map[u_start][v_start][1],color_map[u_start][v_start][2])
            glVertex3f(egg[u_start][v_start][0],egg[u_start][v_start][1],egg[u_start][v_start][2])
            glColor3f(color_map[u_start+1][v_start][0],color_map[u_start+1][v_start][1],color_map[u_start+1][v_start][2])
            glVertex3f(egg[u_start+1][v_start][0],egg[u_start+1][v_start][1],egg[u_start+1][v_start][2])
            glColor3f(color_map[u_start][v_start+1][0],color_map[u_start][v_start+1][1],color_map[u_start][v_start+1][2])
            glVertex3f(egg[u_start][v_start+1][0],egg[u_start][v_start+1][1],egg[u_start][v_start+1][2])
            glColor3f(color_map[u_start+1][v_start][0],color_map[u_start+1][v_start][1],color_map[u_start+1][v_start][2])
            glVertex3f(egg[u_start+1][v_start][0],egg[u_start+1][v_start][1],egg[u_start+1][v_start][2])
            glColor3f(color_map[u_start+1][v_start][0],color_map[u_start+1][v_start][1],color_map[u_start+1][v_start][2])
            glVertex3f(egg[u_start][v_start+1][0],egg[u_start][v_start+1][1],egg[u_start][v_start+1][2])
            glColor3f(color_map[u_start+1][v_start+1][0],color_map[u_start+1][v_start+1][1],color_map[u_start+1][v_start+1][2])
            glVertex3f(egg[u_start+1][v_start+1][0],egg[u_start+1][v_start+1][1],egg[u_start+1][v_start+1][2])
    glEnd()


def zad4():
    glBegin(GL_TRIANGLE_STRIP)
    for u_start in range (steps-1):
        for v_start in range (steps-1):
            glColor3f(color_map[u_start][v_start][0],color_map[u_start][v_start][1],color_map[u_start][v_start][2])
            glVertex3f(egg[u_start][v_start][0],egg[u_start][v_start][1],egg[u_start][v_start][2])
            glVertex3f(egg[u_start][v_start+1][0],egg[u_start][v_start+1][1],egg[u_start][v_start+1][2])
            glVertex3f(egg[u_start+1][v_start][0],egg[u_start+1][v_start][1],egg[u_start+1][v_start][2])
            glVertex3f(egg[u_start+1][v_start+1][0],egg[u_start+1][v_start+1][1],egg[u_start+1][v_start+1][2])
    glEnd()

def zad5():
    glRotatef(0,0,0,0)
    for u_start in range (dim-1):
        glBegin(GL_LINE_STRIP)
        for v_start in range (dim-1):
            glVertex3f(map[u_start][v_start][0]/dim,map[u_start][v_start][1]/dim,map[u_start][v_start][2])
            glVertex3f(map[u_start][v_start+1][0]/dim,map[u_start][v_start+1][1]/dim,map[u_start][v_start][2])
            glVertex3f(map[u_start+1][v_start][0]/dim,map[u_start+1][v_start][1]/dim,map[u_start][v_start][2])
            glVertex3f(map[u_start+1][v_start+1][0]/dim,map[u_start+1][v_start+1][1]/dim,map[u_start][v_start][2])
        glEnd()



def render(time):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    

    zad5()
    
    glLoadIdentity()
    #spin(time * 90 / 3.14)
    axes()
    glFlush()


def update_viewport(window, width, height):
    if width == 0:
        width = 1
    if height == 0:
        height = 1
    aspect_ratio = width / height

    glMatrixMode(GL_PROJECTION)
    glViewport(0, 0, width, height)
    glLoadIdentity()

    if width <= height:
        glOrtho(-7.5, 7.5, -7.5 / aspect_ratio, 7.5 / aspect_ratio, 7.5, -7.5)
    else:
        glOrtho(-7.5 * aspect_ratio, 7.5 * aspect_ratio, -7.5, 7.5, 7.5, -7.5)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():
    calc()
    color()
    plane()
    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(800, 800, __file__, None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSwapInterval(1)

    startup()
    while not glfwWindowShouldClose(window):
        render(glfwGetTime())
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()
