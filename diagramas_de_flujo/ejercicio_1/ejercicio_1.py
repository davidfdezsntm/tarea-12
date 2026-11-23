# Ejercicio 1. Duración de un viaje
# David Fernández - Programación I
#
# Preguntas guía:
# 1. Datos que se leen: distancia (km) y velocidad media (km/h).
# 2. Resultados: horas y minutos restantes.
# 3. Cálculos: minutos totales, horas (//) y resto (%).
#
# ---------------- PSEUDOCÓDIGO ----------------
# ALGORITMO: DURACION_VIAJE
# ENTRADAS: distancia, velocidad
# SALIDA: horas, resto
#     LEER distancia, velocidad
#     minutos = round(distancia / velocidad * 60)
#     horas = minutos // 60
#     resto = minutos % 60
#     ESCRIBIR horas, resto
#
# Diagrama de flujo: diagrama_ejercicio_1.png


def duracion_viaje(distancia, velocidad):
    minutos = round(distancia / velocidad * 60)
    horas = minutos // 60
    resto = minutos % 60
    return minutos, horas, resto


# Prueba de escritorio
for distancia, velocidad in [(350, 100), (120, 80), (45, 90)]:
    minutos, horas, resto = duracion_viaje(distancia, velocidad)
    print(f"{distancia} km a {velocidad} km/h -> {minutos} min -> {horas} h {resto} min")

# ---------------- EJECUCIÓN ----------------
# 350 km a 100 km/h -> 210 min -> 3 h 30 min
# 120 km a 80 km/h -> 90 min -> 1 h 30 min
# 45 km a 90 km/h -> 30 min -> 0 h 30 min
