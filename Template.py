from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from mathutil import *
from graph import *
from mathutil import globVector
import mathutil
import sys
import thread
import popup

window_w, window_h = 800, 600
window_wG, window_hG = 640, 480
pontos = []
aux = []
vetores = []
index = 0
point_size = 13.0

PROMPT = ("F1 - Polygons On/Off","F2 - Control Points On/Off","F3 - Params(t) points On/Off","F5 - Reload Screen","Left Click - Insert Point", "Right Click - Remove Point")

ESC = '\x1b'
MODIFIED = -1
IDLE = -2
FPS = 30
castel = True
poligonal = True
control = True
params = True


def reset():
    global pontos

    pontos = []
    mathutil.curvatureK = []
    curvature = []
    glutPostRedisplay()


def display():
    global vetores
    global globVector
    globVector = []
    glClear(GL_COLOR_BUFFER_BIT)

    y = 20
    for s in PROMPT:
        glRasterPos(10.0, y)
        y+=20
        for c in s:
            glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ord(c))

    # print "Qtd Pontos:",len(pontos)
    # print pontos

    if len(pontos) > 0:
        # Desenho de pontos de controle
        glPointSize(point_size)
        glBegin(GL_POINTS)
        glColor3f(0.0, 1.0, 1.0)
        if control == True:
            for p in pontos:
                glVertex2f(p['x'], p['y'])
        glEnd()

        if len(pontos) > 1:

            # Desenha as linhas entre os pontos de controle
            glBegin(GL_LINE_STRIP)
            glColor3f(0.0,1.0,0.0)
            if poligonal == True:
                for p in pontos:
                    glVertex2f(p['x'], p['y'])
            glEnd()

            # Desenha a Curva
            glBegin(GL_LINE_STRIP)
            glColor3f(1.0,1.0,1.0)
            if castel == True:
                print popup.factor
                globVector = bezier(pontos,popup.factor)
            glEnd()

            glPointSize(5.0);
            # Desenha os pontos de parametro
            glBegin(GL_POINTS)
            glColor3f(1.0,0.0,0.0)
            if params == True:
                for p in globVector:
                    glVertex2d(p['x'], p['y'])
            glEnd()

        else:
            p = pontos[0]
            glVertex2d(p['x'], p['y'])

    glFlush()


def reshape (width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, window_w, window_h, 0.0, -5.0, 5.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def hadleKeyboard(*args):
    global castel

    if args[0] == ESC:
        sys.exit()
    elif args[0] == 'c':
        castel = True
        glutPostRedisplay()


def hadleSpecialKeyboard(key, x, y):
    global poligonal, control, params
    if key == GLUT_KEY_F1:
        if poligonal:
            poligonal = False
            glutPostRedisplay()
        else:
            poligonal = True
            glutPostRedisplay()
    elif key == GLUT_KEY_F2:
        if control:
            control = False
            glutPostRedisplay()
        else:
            control = True
            glutPostRedisplay()
    elif key == GLUT_KEY_F3:
        if params:
            params = False
            glutPostRedisplay()
        else:
            params = True
            glutPostRedisplay()
    elif key == GLUT_KEY_F5:
        print "Reloading"
        reset()


def handleMouseClick(button, state, x, y):
    global index
    exist = False
    vector_size = len(pontos)

    # Verifica se o ponto existe
    for p in range(0,vector_size): 
        if (x >= pontos[p]['x'] - point_size/2) and (x <= pontos[p]['x'] + point_size/2):
            if (y >= pontos[p]['y'] - point_size/2) and (y <= pontos[p]['y'] + point_size/2):
                exist = True
                index = p
                break
    
    # Adiciona pontos
    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN and exist == False:
            p = {'x':float(x),'y':float(y)}
            pontos.append(p)
            index = len(pontos)-1
            glutPostRedisplay()

    # Deleta pontos
    elif button == GLUT_RIGHT_BUTTON:
        if state == GLUT_DOWN and exist == True:
            pontos.pop(0 + index)
            glutPostRedisplay()


# movimentacao dos pontos
def move_point(x, y):
    global index
    pontos[index]['x'] = x
    pontos[index]['y'] = y 
    glutPostRedisplay()


def main():

    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(window_w,window_h)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("PG - Project 1")

    glClearColor(0.0, 0.0, 0.0, 0.0)
    glLineWidth(3.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Starting settings
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMouseFunc(handleMouseClick)
    glutMotionFunc(move_point)
    glutKeyboardFunc(hadleKeyboard)
    glutSpecialUpFunc(hadleSpecialKeyboard)
    glutMainLoop()
    window(window_wG, window_hG)
