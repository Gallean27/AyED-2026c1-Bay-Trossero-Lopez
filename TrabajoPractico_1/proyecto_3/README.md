# 🐍 Proyecto 3: Algoritmos de Ordenamiento y Benchmark de Rendimiento

Este proyecto contiene la implementación de distintos algoritmos de ordenamiento en Python (tanto basados en comparaciones como no comparativos) y un script de análisis empírico que evalúa su tiempo de ejecución frente a la función nativa `sorted()` (*Timsort*).

Permite:
- Ordenar listas de elementos mediante **Burbuja**, **Quicksort** y **Radix Sort**.
- Generar listas de enteros aleatorios de tamaño variable N para pruebas de rendimiento.
- Evaluar y comparar empíricamente los tiempos de ejecución de cada algoritmo.
- Exportar gráficas comparativas de rendimiento (N vs. Tiempo) en formato de imagen.

---

## 🏗 Arquitectura General

El código está organizado de manera modular en las siguientes capas y carpetas:

- **`modules/ordenamientos.py`**: Contiene las funciones puras que implementan la lógica de cada algoritmo (`ordenamiento_burbuja`, `quicksort`, `ordenamiento_radix` y sus auxiliares de conteo por dígito).
- **`apps/graficar_ordenamiento.py`**: Script ejecutable encargada del *benchmarking*. Mide los tiempos de ejecución para distintos tamaños de entrada $N$ y genera las curvas comparativas con `matplotlib`.
- **`tests/test_ordenamiento.py`**: Suite de pruebas unitarias automatizadas mediante el módulo `unittest`.
- **`data/`**: Carpeta donde se exportan y almacenan las gráficas de rendimiento generadas (`.png`).
- **`docs/`**: Carpeta donde se aloja la documentación detallada del proyecto.

Las gráficas de los resultados están disponibles en la carpeta [data] del proyecto.

El informe completo está disponible en la carpeta [TrabajoPractico_1] del proyecto.

---

## 📑 Dependencias

1. **Python 3.x**
2. **matplotlib** (`pip install matplotlib`)
3. Dependencias listadas en `requirements.txt`

---

## 🚀 Cómo Ejecutar el Proyecto

1. **Clonar o descargar** el repositorio.
2. **Crear y activar** un entorno virtual (opcional).
3. **Instalar las dependencias**:
   ```bash
   pip install -r deps/requirements.txt
