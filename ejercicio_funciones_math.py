from cmu_graphics import *
from cmu_graphics import cmu_graphics

app.fondo = rgb(60, 60, 60)

# anillo
Circle(200, 200, 110, relleno=None, borde='blancoFantasma', anchuraDeBorde=3, guión=(40, 1))
Circle(200, 200, 145, relleno=None, borde='blancoFantasma', anchuraDeBorde=3, guión=(80, 1))

# Labels de la brújula
Label('N', 200, 75, relleno='blancoFantasma', tamaño=30)
Label('S', 200, 325, relleno='blancoFantasma', tamaño=30)
Label('W', 75, 200, relleno='blancoFantasma', tamaño=30)
Label('E', 325, 200, relleno='blancoFantasma', tamaño=30)

# Star de fondo
Star(200, 200, 100, 12, relleno='blancoFantasma', redondez=20)
Star(200, 200, 100, 12, relleno=app.fondo, redondez=10)
Star(200, 200, 100, 12, relleno='blancoFantasma', redondez=5)

# Crea una aguja como una Line con el finalDeFlecha igual a Verdadero.
aguja = Line(200, 200, 200, 120, relleno='carmesí', anchuraDeLinea=8, finalDeFlecha=True)

def enRatónMovido(ratónX, ratónY):
    # Obtenga el ángulo entre el punto (200, 200) y la posición actual del cursor.
    ángulo = ánguloA(200, 200, ratónX, ratónY)

    # Use la función obtenerPuntoEnDir para obtener los valores nuevoX2, y nuevoY2 para la aguja.
    nuevoX2, nuevoY2 = obtenerPuntoEnDir(200, 200, ángulo, 80)

    # Establezca el x2 y el y2 de la aguja a los valores calculados arriba.
    aguja.x2 = nuevoX2
    aguja.y2 = nuevoY2


cmu_graphics.run()