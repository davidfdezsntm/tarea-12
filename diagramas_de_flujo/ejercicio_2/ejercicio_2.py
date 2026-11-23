# Ejercicio 2. Gastos de envío
# David Fernández - Programación I
#
# Preguntas guía:
# 1. Datos que se leen: importe del pedido y peso del paquete.
# 2. Dos decisiones: primero ¿importe >= 50? (si es Sí, envío gratis y no se
#    pregunta más); si es No, ¿peso > 5? para elegir 9.95 o 4.95.
# 3. Cálculo que se hace siempre: total = importe + envio.
#
# ---------------- PSEUDOCÓDIGO ----------------
# ALGORITMO: GASTOS_ENVIO
# ENTRADAS: importe, peso
# SALIDA: envio, total
#     LEER importe, peso
#     SI importe >= 50:
#         envio = 0
#     SI NO SI peso > 5:
#         envio = 9.95
#     SI NO:
#         envio = 4.95
#     total = importe + envio
#     ESCRIBIR envio, total
#
# Diagrama de flujo: diagrama_ejercicio_2.png


def gastos_envio(importe, peso):
    if importe >= 50:
        envio = 0
    elif peso > 5:
        envio = 9.95
    else:
        envio = 4.95
    total = importe + envio
    return envio, total


# Prueba de escritorio
for importe, peso in [(60, 8), (30, 8), (30, 2), (50, 1)]:
    envio, total = gastos_envio(importe, peso)
    print(f"Importe {importe}, peso {peso} -> envío {envio:.2f}, total {total:.2f}")

# ---------------- EJECUCIÓN ----------------
# Importe 60, peso 8 -> envío 0.00, total 60.00
# Importe 30, peso 8 -> envío 9.95, total 39.95
# Importe 30, peso 2 -> envío 4.95, total 34.95
# Importe 50, peso 1 -> envío 0.00, total 50.00
