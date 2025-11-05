# Diccionario de Datos - Evaluación Tigres FC

## Información General del Dataset

**Nombre del archivo**: `datos_evaluacion_tigres_fc.csv`
**Registros**: 15 jugadores
**Columnas**: 9 variables
**Propósito**: Dataset didáctico para enseñar métricas avanzadas de evaluación de modelos
**Contexto**: Semana 13 - Evaluación de predicciones de titularidad en el Tigres FC
**Generación**: Script `generar_datos_tigres.py` (semilla: 42)

---

## Descripción del Contexto

Este dataset representa las predicciones de un modelo de machine learning que intenta predecir qué jugadores del Tigres FC serán titulares en un partido, comparadas con la realidad de quiénes efectivamente fueron titulares.

El Tigres FC es el equipo más fuerte de nuestra liga ficticia (85/100 en habilidad), introducido en la Semana 11. Este dataset está diseñado específicamente para producir métricas de evaluación que faciliten el aprendizaje de conceptos como matriz de confusión, precision y recall.

---

## Estructura del Dataset

### Métricas de Evaluación Resultantes

El dataset está diseñado para producir:
- **Verdaderos Positivos (TP)**: 9 jugadores
- **Verdaderos Negativos (TN)**: 4 jugadores
- **Falsos Positivos (FP)**: 1 jugador
- **Falsos Negativos (FN)**: 1 jugador

**Métricas resultantes**:
- **Accuracy**: 86.7% (13 aciertos de 15 predicciones)
- **Precision**: 90.0% (9 TP de 10 predicciones positivas)
- **Recall**: 90.0% (9 TP de 10 casos positivos reales)

---

## Diccionario de Variables

### 1. jugador
- **Tipo**: String (texto)
- **Descripción**: Nombre del jugador del Tigres FC (formato: Apellido + Inicial)
- **Valores únicos**: 15 jugadores
- **Ejemplo**: "Rodriguez G", "Martinez L", "Hernandez C"
- **Notas**: Nombres ficticios creados para propósitos educativos
- **Valores nulos**: No permitidos

### 2. goles_por_partido
- **Tipo**: Float (decimal)
- **Descripción**: Promedio de goles anotados por partido en la temporada
- **Rango**: 0.0 - 1.0 goles por partido
- **Distribución**:
  - Titulares: 0.3 - 0.8 goles/partido (más productivos)
  - Suplentes: 0.0 - 0.3 goles/partido (menos oportunidades)
- **Ejemplo**: 0.49, 0.69, 0.38
- **Notas**: Generado con distribución uniforme + ruido aleatorio
- **Valores nulos**: No permitidos

### 3. minutos_promedio
- **Tipo**: Integer (entero)
- **Descripción**: Promedio de minutos jugados por partido
- **Rango**: 20 - 90 minutos
- **Distribución**:
  - Titulares: 70-90 minutos (juegan casi todo el partido)
  - Suplentes: 20-50 minutos (entran de cambio)
- **Ejemplo**: 80, 87, 73
- **Notas**: Los partidos de fútbol son de 90 minutos
- **Valores nulos**: No permitidos

### 4. edad
- **Tipo**: Integer (entero)
- **Descripción**: Edad del jugador en años
- **Rango**: 20 - 35 años
- **Distribución**:
  - Titulares: 24-30 años (edad ideal de rendimiento)
  - Suplentes: 20-35 años (mayor variabilidad)
- **Ejemplo**: 28, 26, 25
- **Notas**: Distribución realista para fútbol profesional
- **Valores nulos**: No permitidos

### 5. prediccion_modelo
- **Tipo**: Integer (binario)
- **Descripción**: Predicción del modelo de machine learning
- **Valores posibles**:
  - `1`: El modelo predice que será titular
  - `0`: El modelo predice que será suplente
- **Distribución**: 10 predicciones de titular (1), 5 de suplente (0)
- **Ejemplo**: 1, 1, 0
- **Notas**: Variable objetivo predicha por el modelo de la Semana 12
- **Valores nulos**: No permitidos

### 6. titular_real
- **Tipo**: Integer (binario)
- **Descripción**: Realidad del partido - si el jugador fue titular o no
- **Valores posibles**:
  - `1`: El jugador fue titular en el partido
  - `0`: El jugador fue suplente en el partido
- **Distribución**: 10 titulares reales (1), 5 suplentes reales (0)
- **Ejemplo**: 1, 1, 0
- **Notas**: Variable ground truth (verdad absoluta)
- **Valores nulos**: No permitidos

### 7. prediccion_texto
- **Tipo**: String (categórico)
- **Descripción**: Versión legible de la predicción del modelo
- **Valores posibles**:
  - `"Titular"`: Corresponde a prediccion_modelo = 1
  - `"Suplente"`: Corresponde a prediccion_modelo = 0
- **Ejemplo**: "Titular", "Suplente"
- **Notas**: Derivada de prediccion_modelo para facilitar visualización
- **Valores nulos**: No permitidos

### 8. realidad_texto
- **Tipo**: String (categórico)
- **Descripción**: Versión legible de la realidad del partido
- **Valores posibles**:
  - `"Titular"`: Corresponde a titular_real = 1
  - `"Suplente"`: Corresponde a titular_real = 0
- **Ejemplo**: "Titular", "Suplente"
- **Notas**: Derivada de titular_real para facilitar visualización
- **Valores nulos**: No permitidos

### 9. tipo_resultado
- **Tipo**: String (categórico)
- **Descripción**: Clasificación del resultado de la predicción
- **Valores posibles**:
  - `"TP"`: True Positive (Verdadero Positivo) - Predijo titular, fue titular
  - `"TN"`: True Negative (Verdadero Negativo) - Predijo suplente, fue suplente
  - `"FP"`: False Positive (Falso Positivo) - Predijo titular, fue suplente
  - `"FN"`: False Negative (Falso Negativo) - Predijo suplente, fue titular
- **Distribución**: 9 TP, 4 TN, 1 FP, 1 FN
- **Ejemplo**: "TP", "FN", "TN"
- **Notas**: Derivada de prediccion_modelo y titular_real
- **Valores nulos**: No permitidos

---

## Casos Especiales

### Falso Positivo (FP)
- **Jugador**: Flores H
- **Predicción**: Titular (1)
- **Realidad**: Suplente (0)
- **Interpretación**: El modelo pensó que sería titular, pero no lo fue (falsa alarma)

### Falso Negativo (FN)
- **Jugador**: Lopez R
- **Predicción**: Suplente (0)
- **Realidad**: Titular (1)
- **Interpretación**: El modelo no lo identificó como titular, pero sí lo fue (se le escapó)

---

## Relaciones entre Variables

### Variables de Entrada (Features)
- `goles_por_partido`: Indicador de productividad ofensiva
- `minutos_promedio`: Indicador de tiempo de juego
- `edad`: Indicador de experiencia/rendimiento

**Relación con titularidad**: Jugadores con más goles, más minutos y edad ideal (24-30) tienden a ser titulares.

### Variables de Salida (Targets)
- `prediccion_modelo`: Lo que el modelo predice
- `titular_real`: La verdad absoluta
- `tipo_resultado`: Clasificación de acierto/error

### Variables Derivadas
- `prediccion_texto`: Derivada de `prediccion_modelo`
- `realidad_texto`: Derivada de `titular_real`
- `tipo_resultado`: Derivada de `prediccion_modelo` + `titular_real`

---

## Validación de Datos

### Reglas de Integridad

1. **Unicidad**: Cada jugador debe aparecer exactamente una vez
2. **Coherencia binaria**: prediccion_modelo y titular_real solo pueden ser 0 o 1
3. **Coherencia textual**: prediccion_texto y realidad_texto deben corresponder a sus versiones numéricas
4. **Coherencia de resultados**: tipo_resultado debe derivarse correctamente de prediccion_modelo y titular_real
5. **Rangos válidos**:
   - goles_por_partido: [0.0, 1.0]
   - minutos_promedio: [20, 90]
   - edad: [20, 35]

### Conteos Esperados

- Total de registros: 15
- Predicciones positivas: 10 (titular)
- Predicciones negativas: 5 (suplente)
- Casos positivos reales: 10 (titular)
- Casos negativos reales: 5 (suplente)
- TP + TN + FP + FN = 15

---

## Uso Pedagógico

### Objetivo Educativo
Este dataset está diseñado para que los estudiantes aprendan a:
1. Construir matrices de confusión
2. Calcular precision, recall y accuracy
3. Interpretar tipos de errores (FP vs FN)
4. Visualizar matrices de confusión con heatmaps
5. Comparar diferentes estrategias de predicción

### Características Didácticas
- **Tamaño manejable**: 15 registros permiten análisis manual
- **Balance de clases**: 10 titulares, 5 suplentes (no extremadamente desbalanceado)
- **Balance de errores**: 1 FP y 1 FN para mostrar ambos tipos
- **Métricas bonitas**: 86.7%, 90%, 90% son fáciles de interpretar
- **Casos especiales**: Flores H y Lopez R son casos de estudio

---

## Generación de Datos

### Script de Generación
```bash
python generar_datos_tigres.py
```

### Parámetros de Generación
- **Semilla aleatoria**: 42 (garantiza reproducibilidad)
- **Distribuciones**:
  - Goles titulares: Uniforme(0.3, 0.8)
  - Goles suplentes: Uniforme(0.0, 0.3)
  - Minutos titulares: Uniforme(70, 90)
  - Minutos suplentes: Uniforme(20, 50)
  - Edad titulares: Entero(24, 30)
  - Edad suplentes: Entero(20, 35)

### Reproducibilidad
El uso de `np.random.seed(42)` garantiza que cada ejecución del script genere exactamente los mismos datos, esencial para propósitos educativos.

---

## Limitaciones

### Limitaciones Metodológicas
1. **Datos sintéticos**: No representan jugadores reales
2. **Simplicidad**: Solo 3 características de entrada (en realidad hay muchas más)
3. **Tamaño pequeño**: 15 jugadores (en realidad se analizan cientos)
4. **Distribuciones simplificadas**: No capturan toda la complejidad del fútbol

### Propósito Educativo
Estas limitaciones son **intencionales** para facilitar el aprendizaje de los conceptos sin abrumar a estudiantes de preparatoria.

---

## Conexión con Otras Semanas

### Semana 11
- Se introduce la liga ficticia de 8 equipos
- Tigres FC identificado como el más fuerte (85/100)

### Semana 12
- Se desarrolla modelo de ensemble para predecir titulares del Tigres FC
- Dataset de 100 jugadores para entrenamiento

### Semana 13 (Este Dataset)
- Se evalúa el modelo usando 15 jugadores de ejemplo
- Enfoque en métricas de evaluación (precision, recall, matriz de confusión)

### Semana 14
- Se mejorará el modelo mediante feature engineering
- Se crearán nuevas variables derivadas

---

## Referencias

### Documentación Técnica
- Script generador: `generar_datos_tigres.py`
- Notebook de análisis: `metricas-avanzadas-evaluacion.ipynb`
- README del módulo: `README.md`

### Conceptos Relacionados
- Matriz de confusión
- Precision (confiabilidad)
- Recall (sensibilidad)
- Accuracy (precisión general)
- Verdaderos/Falsos Positivos/Negativos

---

**Versión del diccionario**: 1.0
**Última actualización**: Octubre 2025
**Autor**: Equipo PS5005 - Prepa Tec
**Propósito**: Material educativo para enseñanza de evaluación de modelos ML
