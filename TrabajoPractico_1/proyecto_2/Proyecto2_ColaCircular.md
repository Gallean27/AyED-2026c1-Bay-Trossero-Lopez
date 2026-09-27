# 🐍 Proyecto 2: Simulación de Planificación de Procesos (Round Robin)

Este proyecto implementa un simulador de gestión de tiempo de CPU para un sistema operativo que aplica el algoritmo de planificación **Round Robin** utilizando una **Cola Circular** estática basada en arreglos de tamaño fijo.

Permite:
- Gestionar una cola de capacidad acotada con operaciones de encolado (`enqueue`) y desencolado (`dequeue`) en tiempo constante O(1) mediante aritmética modular.
- Simular la ejecución de una tanda de procesos concurrentes calculando sus tiempos de llegada, ráfaga, finalización, retorno (Turnaround Time) y espera (Waiting Time).
- Generar la salida formateada por consola con la tabla de métricas del scheduler para un *quantum* prefijado (q=2).

---

## 🏗 Arquitectura General

El código está organizado de manera modular en las siguientes capas y carpetas:

- **`modules/ColaCircular.py`**: Contiene la implementación de la clase `ColaCircular`, gestionando punteros de frente, final y envoltura de índices.
- **`apps/round_robin.py`**: Módulo que contiene la lógica de la simulación del *scheduler* y el cálculo de tiempos para cada proceso.
- **`main.py`**: Script ejecutable principal que corre la simulación para la tanda de procesos e imprime la tabla de resultados.
- **`tests/test_modulo1.py`**: Suite de pruebas unitarias automatizadas mediante `unittest` para validar la cola circular y el manejo de excepciones.
- **`data/`**: Carpeta reservada para exportación de registros o capturas de la simulación.
- **`docs/`**: Carpeta donde se aloja la documentación detallada del proyecto.

Las gráficas de los resultados están disponibles en la carpeta [data] del proyecto.

El informe completo está disponible en la carpeta [TrabajoPractico_1] del proyecto.

---

## 📑 Dependencias

1. **Python 3.x**
2. **tabulate** (`pip install tabulate`)
3. Dependencias listadas en `requirements.txt`

---

## 🚀 Cómo Ejecutar el Proyecto

1. **Clonar o descargar** el repositorio.
2. **Crear y activar** un entorno virtual (opcional).
3. **Instalar las dependencias**:
   ```bash
   pip install -r deps/requirements.txt