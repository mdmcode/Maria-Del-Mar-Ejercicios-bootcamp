from cmu_graphics import *
from cmu_graphics import cmu_graphics

app.fondo = 'negro'

Label('*No a escala', 340, 370, relleno='blanco', tamaño=16)

sol = Star(200, 200, 35, 400, relleno=gradient('naranja', 'amarillo', 'rojoNaranja'))

luna = Group(
    Circle(200, 50, 20, relleno=None, borde='grisOscuro'),
    Circle(200, 30, 5, relleno='gris')
)

tierra = Group(
    Circle(200, 200, 150, relleno=None, borde='grisOscuro'),
    Circle(200, 50, 10, relleno=gradient('verde', 'azulReal', inicio='izquierda-superior')),
    luna
    )

cometa = Group(
    Circle(200, 200, 10, relleno='blanco'),
    Polygon(200, 190, 170, 200, 200, 210, 
             relleno=gradient('mocasín', 'amarilloClaro', 'blanco', 
                              inicio='izquierda-superior'),
                              opacidad=50)
)

cometa.rotarAngulo = 45
cometa.dx = 5
cometa.dy = 5
cometa.alFondo()
cometa.ancho = 30
cometa.altura = 15

marte = Group(
    Circle(200, 200, 100, relleno=None, borde='grisOscuro'),
    Circle(200, 100, 7, relleno=gradient('rojo', 'marron', inicio='izquierda-superior'))
    )

luna.dirección = 'sentido-horario'
tierra.dirección = 'sentido-horario'
marte.dirección = 'sentido-horario'

def enTeclaPresionada(tecla):
    # Cambie la dirección basado en la tecla.
    if (tecla == 'derecha'):
        tierra.dirección = 'sentido-horario'
    elif (tecla == 'izquierda'):
        tierra.dirección = 'sentido-antihorario'

def enPaso():
    # Si la dirección de la tierra es en sentido horario, agregue 3 al rotarÁngulo.
    # Si no, reste 3.
    if (tierra.dirección == 'sentido-horario'):
        tierra.rotarÁngulo += 3
        marte.rotarÁngulo += 5
        luna.rotarAngulo += 7
    else:
        marte.rotarÁngulo -= 5
        tierra.rotarÁngulo -= 3
        luna.rotarAngulo -= 7

    # Incremente el número de puntos del sol por 1.
    sol.puntos += 1

    #Mueve el cometa
    cometa.centroX += cometa.dx
    cometa.centroY += cometa.dy

    if cometa.superior >= 400:
        cometa.inferior = 0
        cometa.izquierda = -10

cmu_graphics.run()