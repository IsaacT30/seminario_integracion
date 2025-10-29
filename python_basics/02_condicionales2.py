# Sistema que pide pago por hora y horas trabajadas.
# Las primeras 40 horas son normales, las extras se pagan al 150%.
# Calcula y muestra el total semanal.

pago_por_hora = float(input("¿Cuál es el pago por hora? "))
horas_trabajadas = float(input("¿Cuántas horas trabajó esta semana? "))

if horas_trabajadas <= 40:
    total_semanal = horas_trabajadas * pago_por_hora
else:
    horas_extras = horas_trabajadas - 40
    total_semanal = (40 * pago_por_hora) + (horas_extras * pago_por_hora * 1.5)

print(f"El total semanal a pagar es: ${total_semanal:.2f}")