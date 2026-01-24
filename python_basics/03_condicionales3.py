# Vacaciones por antigüedad 2 eslpy Pide años de antigüedad y muestra días de vacaciones según:
# <5=10 >=5=15 <1=0 <3=3


antiguedad = float(input("¿Cuántos años de antigüedad tienes? "))

if antiguedad < 1:
    dias_vacaciones = 0
elif antiguedad >= 1 and antiguedad < 3:
    dias_vacaciones = 3
elif antiguedad >= 3 and antiguedad < 5:
    dias_vacaciones = 10
else:
    dias_vacaciones = 15

# Mostrar el resultado
print(f"Con {antiguedad} años de antigüedad, te corresponden {dias_vacaciones} días de vacaciones.")
