# Semana 12: Modelos Avanzados de Clasificación

## Descripción

Este módulo enseña cómo combinar múltiples modelos de machine learning usando **ensemble learning** (votación por mayoría) para crear predicciones más robustas. Usamos el caso práctico del FC Barcelona para predecir qué jugadores deberían ser titulares.

## Estructura del Proyecto

```
semana-12/
├── generar_datos_liga.py              # Script de generación de datos sintéticos
├── datos_barcelona.csv                 # Dataset generado (no modificar manualmente)
├── modelos-avanzados-clasificacion.ipynb  # Notebook principal de análisis
└── README.md                           # Este archivo
```

## Workflow de Uso

### Paso 1: Generar Datos (solo la primera vez)

Antes de ejecutar el notebook, genera el dataset sintético:

```bash
# Desde la terminal, en el directorio semana-12:
python generar_datos_liga.py
```

**Salida esperada:**
```
======================================================================
Generador de Datos Sintéticos - FC Barcelona
======================================================================

Generando dataset de 15 jugadores...

Resumen del dataset generado:
  - Total de jugadores: 15
  - Titulares: 9
  - Suplentes: 6
  ...

Dataset guardado exitosamente en: datos_barcelona.csv
```

Esto creará el archivo `datos_barcelona.csv` con 15 jugadores sintéticos.

### Paso 2: Ejecutar el Análisis

Abre y ejecuta el notebook Jupyter:

```bash
jupyter notebook modelos-avanzados-clasificacion.ipynb
```

El notebook cargará automáticamente `datos_barcelona.csv` y realizará todo el análisis de modelos múltiples.

## Ventajas de Esta Estructura

### Separación de Responsabilidades

- **generar_datos_liga.py**: Responsable SOLO de generar datos
- **Notebook**: Responsable SOLO de análisis y modelado

### Beneficios Educativos

1. **Reproducibilidad**: Todos usan exactamente los mismos datos
2. **Realismo**: Refleja workflows profesionales de ciencia de datos
3. **Reutilización**: El CSV puede usarse en otros notebooks
4. **Versionado**: El CSV puede ser versionado con Git
5. **Claridad**: Cada archivo tiene una responsabilidad única

## Contenido del Dataset

El archivo `datos_barcelona.csv` contiene **100 registros** de jugadores:

- **Jugador**: Nombre con posición y temporada (ej: "Delantero_Centro_2022-23_32")
- **Goles_Temporada**: Goles marcados en la temporada (0-15)
- **Minutos_Jugados**: Minutos totales jugados (400-2200)
- **Edad**: Edad del jugador (18-35 años)
- **Es_Titular**: Variable objetivo (1 = titular, 0 = suplente)

**Posiciones incluidas**: Portero, Defensa Central, Lateral Derecho/Izquierdo, Mediocampista (Defensivo/Centro/Ofensivo), Extremo Derecho/Izquierdo, Delantero Centro

**Temporadas simuladas**: 2021-22, 2022-23, 2023-24

## Distribuciones Estadísticas

El generador usa distribuciones realistas:

- **Goles**: Exponencial (mayoría marca poco, pocos marcan mucho)
- **Minutos**: Uniforme (desde suplentes hasta titulares)
- **Edad**: Normal centrada en 25 años
- **Es_Titular**: Función de score = 60% minutos + 40% goles

## Conceptos Clave del Módulo

1. **Ensemble Learning**: Combinar múltiples modelos
2. **Votación por Mayoría**: Estrategia de combinación simple
3. **Separación de Datos**: Generación vs. Análisis
4. **Workflow Profesional**: Archivos CSV como interface
5. **Dataset Robusto**: 100 registros = evaluaciones más confiables
6. **Datos Multi-temporales**: Simulación de 3 temporadas históricas

## Sesiones del Notebook

### Sesión 1: Preparación de Datos (50 min)
- Carga de CSV
- División train/test

### Sesión 2: Entrenamiento Multi-Modelo (50 min)
- Regresión Logística (x2)
- Random Forest
- Comparación de predicciones

### Sesión 3: Ensemble y Evaluación (50 min)
- Votación por mayoría
- Evaluación comparativa
- Síntesis y reflexión

## Solución de Problemas

### Error: "No se encontró el archivo 'datos_barcelona.csv'"

**Solución:** Ejecuta primero el script generador:
```bash
python generar_datos_liga.py
```

### El notebook da resultados diferentes cada vez

**Verificación:** Asegúrate de que:
1. Estás usando el mismo `datos_barcelona.csv`
2. El script generador usa `np.random.seed(42)`
3. No modificaste manualmente el CSV

### Quiero generar datos diferentes

**Opción 1 - Diferentes jugadores (misma semilla):**
```bash
python generar_datos_liga.py  # Regenera con misma semilla
```

**Opción 2 - Modificar semilla en el script:**
Edita `generar_datos_liga.py` y cambia:
```python
semilla_aleatoria=42  # Cambia este número
```

## Requisitos

- Python 3.10+
- pandas
- numpy
- scikit-learn
- jupyter

Instalación:
```bash
pip install pandas numpy scikit-learn jupyter
```

## Autor

Equipo de Ciencia de Datos - Prepa Tec
Curso: PS5005 Programación Básica 1
Versión: 1.0

## Licencia

Material educativo para uso académico.
