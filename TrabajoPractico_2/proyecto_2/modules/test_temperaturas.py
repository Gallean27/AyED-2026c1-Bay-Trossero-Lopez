from modules.temperaturas import Temperaturas_DB

db=Temperaturas_DB()

with open("data/muestras.txt", "r") as archivo:
    for linea in archivo:
        fecha, temperatura=linea.strip().split(";")
        db.guardar_temperatura(float(temperatura), fecha)

devolver_temperatura=db.devolver_temperatura("15/01/2025")
print(f"Temperatura del 15/01/2025: {devolver_temperatura}°C")

maxima=db.max_temp_rango("01/01/2025", "31/01/2025")
print(f"Temperatura máxima en enero de 2025: {maxima}°C")

minima=db.min_temp_rango("01/01/2025", "31/01/2025")
print(f"Temperatura mínima en enero de 2025: {minima}°C")

temperatura_extremos=db.temp_extremos_rango("01/01/2025", "31/01/2025")

# temp extremos devuelve una tupla (minimo, maximo) 
# [0] es el mínimo y [1] es el máximo

print(f"Temperatura máxima en enero de 2025: {temperatura_extremos[1]}°C")
print(f"Temperatura mínima en enero de 2025: {temperatura_extremos[0]}°C")

print(f"Temperatura del 15/01/2025 después de borrar: {db.devolver_temperatura('15/01/2025')}°C")

print("\nLista de temperaturas entre el 01/01/2025 y el 31/01/2025:")
devolver_lista_temp=db.devolver_temperaturas("01/01/2025", "31/01/2025")
for item in devolver_lista_temp:
    print(item)

borrar_temperatura=db.borrar_temperatura("15/01/2025")
print(f"\nTemperatura del 15/01/2025 después de borrar: {db.devolver_temperatura('15/01/2025')}°C")

cantidad=db.cantidad_muestras()
print(f"Cantidad de temperaturas almacenadas: {cantidad}")