from cmu_graphics import *

app.fondo = 'negro'

Label('*No a escala', 340, 370, relleno='blanco', tamaño=16)

sol = Star(200, 200, 35, 400, relleno=gradient('naranja', 'amarillo', 'rojoNaranja'))

tierra = Group(
    Círculo(200, 200, 150, relleno=None, borde='grisOscuro'),
    Círculo(200, 50, 10, relleno=gradient('verde', 'azulReal', inicio='izquierda-superior'))
    )

marte = Group(
    Círculo(200, 200, 120, relleno=None, borde='grisOscuro'),
    Círculo(200, 80, 7, relleno=gradient('rojo', 'marron', inicio='izquierda-superior'))
    )

tierra.dirección = 'sentido-horario'
marte.dirección = 'sentido-horario'

def enTeclaPresionada(tecla):
    # Cambie la dirección basado en la tecla.
    if (tecla == 'derecha'):
        tierra.dirección = 'sentido-horario'
        marte.dirección = 'sentido-horario'
    elif (tecla == 'izquierda'):
        marte.dirección = 'sentido-antihorario'
        tierra.dirección = 'sentido-antihorario'

def enPaso():
    # Si la dirección de la tierra es en sentido horario, agregue 3 al rotarÁngulo.
    # Si no, reste 3.
    if (tierra.dirección == 'sentido-horario'):
        tierra.rotarÁngulo += 3
        marte.rotarÁngulo += 5
    else:
        marte.rotarÁngulo -= 5
        tierra.rotarÁngulo -= 3

    # Incremente el número de puntos del sol por 1.
    sol.puntos += 1

cmu_graphics.run()