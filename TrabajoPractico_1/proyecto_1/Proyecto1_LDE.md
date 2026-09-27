# 🐍 Proyecto 1: Implementación de Lista Doblemente Enlazada (TDA)

Este proyecto contiene la abstracción e implementación en Python de una **Lista Doblemente Enlazada**, una estructura de datos lineal y dinámica que permite gestionar colecciones de elementos con acceso e inserción bidireccional eficiente.

Permite:
- Insertar y eliminar elementos en los extremos (cabeza y cola) en tiempo constante O(1).
- Recorrer y manipular la estructura en ambas direcciones.
- Invertir los elementos *in-place* y realizar copias completas de la lista.
- Evaluar métricas de rendimiento y complejidad temporal (O(1) vs O(N)) mediante gráficos experimentales.

---

## 🏗 Arquitectura General

El código está organizado de manera modular en las siguientes capas y carpetas:

- **`modules/lde.py`**: Contiene la definición de las clases `Nodo` y `ListaDobleEnlazada` con sus respectivas operaciones críticas y excepciones.
- **`apps/graficar_lde.py`**: Script encargada del *benchmarking* que mide los tiempos de ejecución para las operaciones `len()`, `copiar()` e `invertir()`, generando curvas comparativas.
- **`tests/test_LDE.py`**: Suite de pruebas unitarias automatizadas (`unittest`) que evalúa escenarios normales y casos de borde.
- **`data/`**: Carpeta donde se exportan y almacenan las gráficas de rendimiento generadas (`.png`).
- **`docs/`**: Carpeta donde se aloja la documentación detallada del proyecto.

Las gráficas de los resultados están disponibles en la carpeta [data] del proyecto.

El informe completo está disponible en la carpeta [TrabajoPractico_1] del proyecto.

---

## 📑 Dependencias

1. **Python 3.x**
2. **matplotlib** (`pip install matplotlib`)
3. **coverage** (`pip install coverage`)
4. Dependencias listadas en `requirements.txt`

---

## 🚀 Cómo Ejecutar el Proyecto

1. **Clonar o descargar** el repositorio.
2. **Crear y activar** un entorno virtual (opcional).
3. **Instalar las dependencias**:
   ```bash
   pip install -r deps/requirements.txt
   

## 🙎🙎‍♂️ Autores

- Trossero Mateo Ignacio
- Bay Gabriel

