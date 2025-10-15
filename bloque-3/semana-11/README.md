# Semana 11: Introducción al Modelado Predictivo

## Descripción

Esta libreta introduce a los estudiantes al mundo del modelado predictivo usando datos de fútbol. Los estudiantes aprenden a crear y evaluar su primer modelo de predicción usando datos sintéticos de una liga ficticia.

## Archivos del proyecto

### Libreta principal
- **[modelado-predictivo-introduccion.ipynb](modelado-predictivo-introduccion.ipynb)**: Libreta interactiva con las 3 sesiones de la semana

### Datos
- **[datos_liga_futbol.csv](datos_liga_futbol.csv)**: Datos sintéticos de una temporada completa de la liga ficticia (56 partidos, 14 columnas)

### Script de generación de datos
- **[generar_datos_liga.py](generar_datos_liga.py)**: Generador de datos sintéticos de liga de fútbol con características realistas (solo necesario si quieres regenerar los datos)

## Generador de datos sintéticos

### Características del generador

El generador crea datos realistas de una liga de fútbol ficticia con:

- **8 equipos** con diferentes niveles de habilidad (60-85 puntos)
- **Ventaja de jugar en casa** (15% adicional de probabilidad)
- **Efecto de racha de victorias** (10% bonus por victoria consecutiva, máx 3)
- **Variabilidad realista** (20% de factor aleatorio)
- **Distribución de goles** usando Poisson (común en fútbol)

### Equipos de la liga ficticia

1. Tigres FC (85) - Equipo muy fuerte
2. Águilas United (82) - Equipo fuerte
3. Leones SC (78) - Equipo medio-fuerte
4. Halcones City (75) - Equipo medio
5. Lobos Atlético (72) - Equipo medio
6. Pumas CF (68) - Equipo medio-débil
7. Zorros FC (65) - Equipo débil
8. Cóndores United (60) - Equipo muy débil

### Uso básico en la libreta

La libreta lee directamente el archivo CSV:

```python
import pandas as pd

# Cargar datos
datos_partidos = pd.read_csv('datos_liga_futbol.csv')

# Explorar datos
print(datos_partidos.head())
print(datos_partidos.info())
```

### Regenerar datos (opcional)

Solo es necesario si quieres modificar los datos o crear una nueva temporada:

```bash
# Activar entorno virtual
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# Ejecutar generador (sobrescribirá datos_liga_futbol.csv)
python generar_datos_liga.py
```

El script genera:
- Archivo CSV con 56 partidos
- Número de jornadas
- Tabla de resultados en consola
- Tabla de posiciones en consola
- Análisis de ventaja local en consola

### Columnas generadas

Cada partido incluye:

- `Temporada`: Número de temporada (1, 2, 3...)
- `Jornada`: Número de jornada (1-14 para liga de 8 equipos)
- `Equipo_Local`: Equipo que juega en casa
- `Equipo_Visitante`: Equipo visitante
- `Goles_Local`: Goles marcados por el equipo local
- `Goles_Visitante`: Goles marcados por el equipo visitante
- `Resultado`: "Victoria Local", "Victoria Visitante", "Empate"
- `Ganador`: Nombre del equipo ganador o "Empate"
- `Juega_En_Casa`: Siempre True para el equipo local
- `Probabilidad_Victoria_Local`: Probabilidad calculada (0.0-1.0)
- `Habilidad_Local`: Nivel de habilidad del equipo local (60-85)
- `Habilidad_Visitante`: Nivel de habilidad del equipo visitante (60-85)
- `Racha_Local`: Victorias consecutivas del equipo local
- `Racha_Visitante`: Victorias consecutivas del equipo visitante

## Estructura pedagógica

### Sesión 1: ¿Qué significa "predecir" usando datos? (50 min)
**Objetivos:**
- Diferenciar entre opinión y predicción basada en datos
- Descubrir la ventaja de jugar en casa mediante análisis
- Entender cómo los datos históricos informan predicciones

**Actividades:**
- Generación de datos de liga ficticia
- Análisis exploratorio de resultados
- Visualización de ventaja local

### Sesión 2: ¿Cómo le enseñamos a la computadora a predecir? (50 min)
**Objetivos:**
- Comprender qué es un modelo de machine learning
- Preparar datos para entrenar un modelo
- Entrenar un modelo de regresión logística
- Hacer predicciones sobre nuevos partidos

**Actividades:**
- Preparación de características numéricas
- División train/test
- Entrenamiento del modelo
- Primeras predicciones

### Sesión 3: ¿Qué tan buenas son nuestras predicciones? (50 min)
**Objetivos:**
- Medir la precisión de un modelo predictivo
- Interpretar métricas de evaluación
- Identificar características importantes
- Entender limitaciones de los modelos

**Actividades:**
- Cálculo de accuracy
- Análisis de matriz de confusión
- Visualización de importancia de características
- Reflexión crítica sobre limitaciones

## Metodología Socrática

La libreta utiliza preguntas guía constantes:

- **Preguntas de apertura**: Activan conocimiento previo
- **Preguntas reflexivas**: Promueven pensamiento crítico
- **Preguntas de conexión**: Relacionan con experiencias reales
- **Preguntas de síntesis**: Consolidan aprendizaje

## Tecnologías utilizadas

- **pandas**: Manipulación de datos
- **numpy**: Operaciones numéricas
- **matplotlib**: Visualización
- **seaborn**: Visualización estadística
- **scikit-learn**: Modelado predictivo
  - `LogisticRegression`: Modelo de clasificación binaria
  - `train_test_split`: División de datos
  - `accuracy_score`: Métrica de evaluación
  - `classification_report`: Reporte detallado
  - `confusion_matrix`: Matriz de confusión

## Conceptos clave

### Machine Learning
- **Modelo**: Algoritmo que aprende patrones de datos
- **Entrenamiento**: Proceso de aprendizaje con datos históricos
- **Predicción**: Aplicación del modelo a casos nuevos
- **Evaluación**: Medición del rendimiento del modelo

### Preparación de datos
- **Features (X)**: Variables de entrada para predicción
- **Target (y)**: Variable que queremos predecir
- **Train/Test split**: División para entrenamiento y evaluación

### Métricas de evaluación
- **Accuracy**: Porcentaje de predicciones correctas
- **Precision**: De las predicciones positivas, cuántas fueron correctas
- **Recall**: De los casos positivos reales, cuántos se predijeron
- **F1-score**: Media armónica de precision y recall
- **Confusion Matrix**: Tabla de aciertos y errores por clase

## Tiempo de ejecución estimado

- **Sesión 1**: 15-20 minutos
- **Sesión 2**: 20-25 minutos
- **Sesión 3**: 15-20 minutos
- **Total**: ~50-65 minutos (ajustable según profundidad de discusión)

## Extensiones posibles

### Para estudiantes avanzados
1. Agregar más características al modelo (clima, lesiones, historial)
2. Probar diferentes algoritmos (Random Forest, SVM)
3. Predecir cantidad de goles en lugar de solo ganador
4. Implementar validación cruzada
5. Optimizar hiperparámetros del modelo

### Para proyectos finales
1. Crear una liga personalizada con equipos favoritos
2. Construir un sistema de recomendación de alineaciones
3. Predecir probabilidades de campeonato por equipo
4. Analizar efecto de cambios de entrenador
5. Simular toda una temporada con Monte Carlo

## Notas para instructores

### Puntos de atención
- El generador usa semilla 42 para reproducibilidad
- Los datos son sintéticos pero estadísticamente realistas
- La libreta se ejecuta completamente en ~10 minutos
- Incluye checkpoints de reflexión cada 10-15 minutos

### Adaptaciones recomendadas
- Ajustar número de partidos según tiempo disponible
- Modificar equipos según preferencias regionales
- Agregar ejemplos de equipos reales en discusiones
- Conectar con eventos deportivos actuales

### Conexión con curriculum
- **Semana 10**: Análisis estadístico descriptivo
- **Semana 11**: Introducción a modelado predictivo (esta libreta)
- **Semana 12**: Modelos de clasificación avanzados
- **Semana 13**: Métricas avanzadas de evaluación
- **Semana 14**: Feature engineering
- **Semana 15**: Proyecto integrador final

## Limitaciones y consideraciones éticas

### Limitaciones técnicas
- Modelo simplificado (solo 3 características)
- Datos sintéticos (no reflejan complejidad real)
- Sin factores externos (clima, árbitros, lesiones)
- Asume independencia entre partidos

### Consideraciones éticas
- Los modelos NO garantizan resultados futuros
- Importante mantener pensamiento crítico
- No usar para apuestas o decisiones financieras
- Reconocer valor humano más allá de predicciones

## Recursos adicionales

### Documentación oficial
- [scikit-learn: Logistic Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)
- [pandas: DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- [matplotlib: pyplot](https://matplotlib.org/stable/api/pyplot_summary.html)

### Lectura complementaria
- "An Introduction to Statistical Learning" - James et al.
- "Python Data Science Handbook" - Jake VanderPlas
- "Soccermatics" - David Sumpter (aplicaciones de matemáticas al fútbol)

## Licencia y uso

Este material está diseñado para uso educativo en el curso PS5005 - Programación Básica 1 de Prepa Tec. Se permite su uso y adaptación con fines educativos citando la fuente.

---

**Última actualización**: Octubre 2025
**Versión**: 2.0 (refactorizada con datos sintéticos)
