# Crea una grafica con arcos que muestre los porcentajes de las distintas religiones alrededor del 
# mundo
from cmu_graphics import *
from cmu_graphics import cmu_graphics

poblacionMundial = 7600

def obtenerAngulo(personas):
    frecuenciaRelativa = personas/poblacionMundial

    angulo = 360 * frecuenciaRelativa
    return angulo

# Circulo de fondo
Circle(200, 200, 150)

cristianos = 2300
islam = 1900
hinduismo = 1200
budismo = 520
chinos = 394
ateos = 1200
afros = 100

# Dibuja el arco de porcentaje cristiano
arcoCristianos = Arc(200, 200, 280, 280, 0, obtenerAngulo(cristianos), relleno='azulCielo')
cristianosFinal = arcoCristianos.startAngle + arcoCristianos.sweepAngle

# Dibuja el arco de porcentaje del islam
arcoIslam = Arc(200, 200, 280, 280, cristianosFinal, obtenerAngulo(islam), relleno='rojo')
islamFinal = arcoIslam.startAngle + arcoIslam.sweepAngle

# Dibuja el arco del hinduismo
arcoHinduismo = Arc(200, 200, 280, 280, islamFinal, obtenerAngulo(hinduismo), relleno='verde')
hinduismoFinal = arcoHinduismo.startAngle + arcoHinduismo.sweepAngle

# Dibuja el arco del budismo
arcoBudismo = Arc(200, 200, 280, 280, hinduismoFinal, obtenerAngulo(budismo), relleno='naranja')
budismoFinal = arcoBudismo.startAngle + arcoBudismo.sweepAngle

# Dibuja el arco de las religiones chinas
arcoChino = Arc(200, 200, 280, 280, budismoFinal, obtenerAngulo(chinos), relleno='violetaOscuro')
chinosFinal = arcoChino.startAngle + arcoChino.sweepAngle

# Dibuja el arco de las religiones africanas
arcoAfro = Arc(200, 200, 280, 280, chinosFinal, obtenerAngulo(afros), relleno='marrónRosado')
afrosFinal = arcoAfro.startAngle + arcoAfro.sweepAngle

# Dibuja el arco de los no religiosos
arcoAteos = Arc(200, 200, 280, 280, afrosFinal, obtenerAngulo(ateos), relleno='blanco')
ateosFinal = arcoAteos.startAngle + arcoAteos.sweepAngle

cmu_graphics.run()