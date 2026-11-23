# Ejercicio 3. Control de stock semanal
# David Fernández - Programación I
#
# Preguntas guía:
# 1. Se lee una vez el stock inicial; en cada vuelta, las ventas del día.
# 2. Antes del bucle: stock (se lee) y pedidos = 0.
# 3. Si quedan menos de 10: escribir "Reponer" y el día, sumar 50 al stock
#    y sumar 1 a pedidos.
#
# ---------------- PSEUDOCÓDIGO ----------------
# ALGORITMO: STOCK_SEMANAL
# ENTRADAS: stock, ventas
# SALIDA: stock, pedidos
#     LEER stock
#     pedidos = 0
#     PARA dia DESDE 1 HASTA 7:
#         LEER ventas
#         stock = stock - ventas
#         SI stock < 10:
#             ESCRIBIR "Reponer", dia
#             stock = stock + 50
#             pedidos = pedidos + 1
#     ESCRIBIR stock, pedidos
#
# Diagrama de flujo: diagrama_ejercicio_3.png


def stock_semanal(stock, ventas_semana):
    pedidos = 0
    for dia in range(1, 8):
        ventas = ventas_semana[dia - 1]
        stock = stock - ventas
        if stock < 10:
            print("Reponer el día", dia)
            stock = stock + 50
            pedidos = pedidos + 1
    return stock, pedidos


# Prueba de escritorio (stock inicial 40)
stock_final, pedidos = stock_semanal(40, [12, 15, 8, 20, 5, 18, 9])
print("Stock final:", stock_final)
print("Pedidos:", pedidos)

# ---------------- EJECUCIÓN ----------------
# Reponer el día 3
# Reponer el día 7
# Stock final: 53
# Pedidos: 2
