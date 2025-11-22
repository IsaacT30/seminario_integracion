# Pide cuantos días registrarás y para cada día ingresa T (Tarde), O (Ok), P (Permiso).
# Cuenta y muestra las tardanzas totales.

dias = int(input("¿Cuántos días vas a cargar? "))
tardes = 0

for i in range(dias):
    marca = input(f"Día {i+1} (T=tarde, O=ok, P=permiso): ").strip().upper()
    if marca == "T":
        tardes += 1

print(f"Tardanzas totales: {tardes}")
 