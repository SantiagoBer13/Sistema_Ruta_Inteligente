# 📍 Algoritmo de Búsqueda de Rutas en un Sistema de Transporte
Este proyecto implementa un sistema de búsqueda de rutas óptimas en un transporte masivo local utilizando [Kanren](https://github.com/logpy/logpy) para lógica relacional y [NetworkX](https://networkx.org/) para visualización de grafos.

## 🚀 Características
- Desarrollo de un sistema inteligente que, a partir de una base de conocimiento escrita en reglas lógicas, determina la mejor ruta para moverse desde un punto A hasta un punto B en el sistema de transporte masivo local.
- Encuentra la mejor ruta entre dos puntos.
- Considera costos (pesos) en las conexiones.
- Visualiza gráficamente el sistema de transporte.

## 📋 Requisitos

1. Editor de Codigo (VS Code o PyCharm)
2. Python 3.6 o superior
3. Bibliotecas:
    - Kanren (lógica relacional)
    - NetworkX (representación y visualización de grafos)
    - Matplotlib (visualización)

## 🛠️ Instalación
1. Clona este repositorio:
   ```sh
   git clone https://github.com/SantiagoBer13/Sistema_Ruta_Inteligente.git
   cd Sistema_Ruta_Inteligente
   ```
2. Crea y activa un entorno virtual
    ```
    python -m venv venv
    source venv/bin/activate  # En macOS/Linux
    venv\Scripts\activate  # En Windows
    ```

3. Instala las librerias
    ```
    pip install matplotlib kanren networkx
    ```

## 📌 Uso
1. Ejecuta el script principal:
    ```
    python SI_Sistema_Transporte.py
    ```
    Se mostrará la mejor ruta entre los puntos definidos y una representación gráfica.
## 📝 Autor
    Santiago Bernal Tinjacá


