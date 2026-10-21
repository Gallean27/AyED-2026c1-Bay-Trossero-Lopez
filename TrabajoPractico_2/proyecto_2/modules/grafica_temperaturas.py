import matplotlib.pyplot as plt
from modules.temperaturas import Temperaturas_DB


db = Temperaturas_DB()

# Cargar datos desde archivo
with open("data/muestras.txt", "r") as archivo:
    for linea in archivo:
        fecha, temperatura = linea.strip().split(";")
        db.guardar_temperatura(float(temperatura), fecha)

# Obtener lista de strings en formato "dd/mm/aaaa: valor°C"
datos = db.devolver_temperaturas("01/01/2025", "31/01/2025")

# Convertir cada string en (fecha, temperatura)
datos_convertidos = []
for item in datos:
    partes = item.split(":")
    fecha = partes[0].strip()
    temperatura = float(partes[1].replace("°C", "").strip())
    datos_convertidos.append((fecha, temperatura))

# Nota: Mantenemos el orden cronológico original (o como prefieras) para ver la evolución temporal, 
# a diferencia del anterior que ordenaba por valor.
fechas = [d[0] for d in datos_convertidos]
temps = [d[1] for d in datos_convertidos]

# Encontrar extremos para resaltar
temp_min = min(temps)
temp_max = max(temps)
idx_min = temps.index(temp_min)
idx_max = temps.index(temp_max)

# Graficar
plt.figure(figsize=(14, 6))

# Línea de evolución temporal con estilo suavizado o punteado
plt.plot(fechas, temps, color="gray", linestyle="--", linewidth=1, alpha=0.7, label="Evolución temporal")

# Gráfico de dispersión donde el color de los puntos varía según la temperatura (colormap 'coolwarm')
scatter = plt.scatter(fechas, temps, c=temps, cmap="coolwarm", s=70, zorder=3)
cbar = plt.colorbar(scatter)
cbar.set_label("Temperatura (°C)")

# Resaltar puntualmente el mínimo y el máximo absoluto
plt.scatter(fechas[idx_min], temp_min, color="blue", s=150, marker="o", label=f"Mínimo: {temp_min}°C", zorder=4)
plt.scatter(fechas[idx_max], temp_max, color="red", s=150, marker="^", label=f"Máximo: {temp_max}°C", zorder=4)

plt.xticks(rotation=90, fontsize=8)
plt.xlabel("Fecha")
plt.ylabel("Temperatura (°C)")
plt.title("Evolución de Temperaturas con Mapa de Calor y Extremos Destacados")
plt.legend(loc="upper left")

plt.grid(True, linestyle=":", alpha=0.5)
plt.tight_layout()
plt.savefig("grafica_temperaturas_evolucion.png")
plt.show()