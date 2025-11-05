# Semana 13: Métricas Avanzadas de Evaluación

## Información General

**Bloque**: 3 - Modelado Predictivo y Machine Learning
**Semana**: 13 de 15
**Tema**: Métricas Avanzadas de Evaluación de Modelos
**Enfoque**: Análisis MICRO - Evaluación profunda de modelos (Tigres FC)
**Duración**: 1 sesión de 50 minutos
**Última actualización**: Octubre 2025

---

## Descripción

Esta semana profundiza en la **evaluación avanzada de modelos de clasificación**, enseñando a los estudiantes a ir más allá de la simple métrica de accuracy. Los estudiantes aprenden a usar la matriz de confusión, precision, recall y visualizaciones para evaluar profundamente el rendimiento de los modelos desarrollados en la Semana 12.

**Contexto en la narrativa unificada**: Continuamos trabajando con el **Tigres FC**, el equipo más fuerte de nuestra liga ficticia (85/100 en habilidad). Los estudiantes evalúan el modelo de predicción de titulares que construyeron en la Semana 12, aprendiendo a identificar qué tipos de errores comete y cómo compararlo con estrategias alternativas.

---

## Objetivos de Aprendizaje

Al finalizar esta semana, los estudiantes podrán:

1. **Construir y interpretar matrices de confusión**
   - Identificar verdaderos positivos, verdaderos negativos, falsos positivos y falsos negativos
   - Analizar qué tipos de errores comete un modelo

2. **Calcular métricas específicas de clasificación**
   - Precision: Confiabilidad de las predicciones positivas
   - Recall: Capacidad de detectar todos los casos positivos
   - Accuracy: Rendimiento general del modelo

3. **Visualizar resultados de evaluación**
   - Crear mapas de calor de matrices de confusión
   - Interpretar visualizaciones de rendimiento

4. **Comparar estrategias de predicción**
   - Evaluar múltiples enfoques (conservador, arriesgado, balanceado)
   - Elegir la estrategia óptima según el contexto

5. **Tomar decisiones basadas en métricas**
   - Entender cuándo priorizar precision vs. recall
   - Justificar elecciones de modelos con evidencia cuantitativa

---

## Estructura del Contenido

### Notebook Principal

**Archivo**: `metricas-avanzadas-evaluacion.ipynb`

#### Módulo 1: Construyendo la Matriz de Confusión (15 min)
- **Concepto**: Matriz de confusión y sus componentes (TP, TN, FP, FN)
- **Implementación**: Uso de `sklearn.metrics.confusion_matrix()`
- **Análisis**: Interpretación de cada tipo de acierto y error
- **Resultado**: Entender qué errores comete el modelo del Tigres FC

#### Módulo 2: Calculando Precisión y Recall (15 min)
- **Precision**: TP / (TP + FP) - Confiabilidad de predicciones positivas
- **Recall**: TP / (TP + FN) - Capacidad de detección
- **Cálculo manual**: Implementación desde componentes de la matriz
- **Interpretación**: Cuándo priorizar cada métrica

#### Módulo 3: Visualizando la Matriz de Confusión (10 min)
- **Herramienta**: Seaborn heatmap
- **Diseño**: Visualización profesional con anotaciones
- **Comunicación**: Presentación de resultados a audiencias no técnicas

#### Módulo 4: Comparando Estrategias de Predicción (10 min)
- **Baselines**: Estrategia conservadora vs. arriesgada
- **Comparación**: Análisis de accuracy, precision y recall
- **Decisión**: Selección de la mejor estrategia según contexto
- **Función reutilizable**: `calcular_metricas_completas()`

---

## Conexión con la Narrativa Unificada

### Progresión desde Semana 12

**Semana 12**: Construiste un modelo de ensemble (votación por mayoría) para el Tigres FC
**Semana 13**: Ahora evalúas profundamente ese modelo usando métricas avanzadas
**Semana 14**: Después mejorarás el modelo mediante feature engineering

### Contexto del Tigres FC

- **Equipo**: Tigres FC - El más fuerte de la liga ficticia (85/100)
- **Dataset**: 15 jugadores de ejemplo para análisis didáctico
- **Objetivo**: Predecir titulares vs. suplentes
- **Continuidad**: Mismo equipo y contexto que Semana 12

### Jugadores de Ejemplo

El notebook utiliza 15 jugadores ficticios del Tigres FC:
- Rodriguez G, Martinez L, Hernandez C, Garcia M, Lopez R
- Sanchez J, Gonzalez A, Perez D, Torres F, Ramirez E
- Flores H, Morales P, Castro S, Ortiz V, Mendoza I

**Nota**: Estos son datos sintéticos para propósitos didácticos, simplificados para facilitar el aprendizaje de las métricas.

---

## Conceptos Clave

### 1. Matriz de Confusión

```
                    Predicción
                Suplente  Titular
Realidad Suplente    TN       FP
         Titular     FN       TP
```

- **TP (True Positive)**: Predijo titular, fue titular - Acierto
- **TN (True Negative)**: Predijo suplente, fue suplente - Acierto
- **FP (False Positive)**: Predijo titular, fue suplente - Error Tipo 1
- **FN (False Negative)**: Predijo suplente, fue titular - Error Tipo 2

### 2. Métricas de Evaluación

**Precision (Confiabilidad)**:
```
Precision = TP / (TP + FP)
```
- ¿De los que predijimos como titulares, cuántos realmente lo fueron?
- Alta precision = pocas falsas alarmas

**Recall (Sensibilidad)**:
```
Recall = TP / (TP + FN)
```
- ¿De los titulares reales, a cuántos logramos identificar?
- Alto recall = nos perdemos pocos casos

**Accuracy (Precisión General)**:
```
Accuracy = (TP + TN) / Total
```
- ¿Cuántas predicciones fueron correctas en total?
- Métrica general, pero puede ser engañosa con datos desbalanceados

### 3. Trade-offs

No existe el modelo perfecto. Siempre hay un balance entre:
- **Alta Precision**: Menos falsas alarmas, pero nos perdemos casos
- **Alto Recall**: Capturamos todos los casos, pero con falsas alarmas
- **Balance óptimo**: Depende del costo de cada tipo de error

---

## Aplicaciones en Fútbol

### Sistemas de Scouting
- **Priorizar Precision**: No queremos recomendar jugadores que no funcionarán (fichajes costosos)
- **Priorizar Recall**: No queremos perdernos ningún talento emergente

### Prevención de Lesiones
- **Priorizar Recall**: Es crítico detectar todos los jugadores en riesgo
- Aceptamos algunas falsas alarmas (precaución extra)

### Predicción de Titulares
- **Balance**: Queremos confiabilidad (precision) y completitud (recall)
- Usado por el Tigres FC para optimizar alineaciones

---

## Archivos

```
semana-13/
├── metricas-avanzadas-evaluacion.ipynb  # Notebook principal
└── README.md                            # Este archivo
```

**Nota**: Esta semana no requiere datasets externos ni scripts de generación, ya que utiliza datos de ejemplo embebidos en el notebook para propósitos didácticos.

---

## Prerequisitos

### Conocimientos
- Conceptos de clasificación binaria (Semana 11)
- Modelos de ensemble y votación (Semana 12)
- Train/test split y evaluación básica con accuracy
- Uso básico de scikit-learn

### Librerías Python
```python
import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix, accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns
```

---

## Ejecución del Notebook

### Opción 1: Jupyter Notebook
```bash
cd contenido/bloque-3/semana-13
jupyter notebook metricas-avanzadas-evaluacion.ipynb
```

### Opción 2: JupyterLab
```bash
cd contenido/bloque-3/semana-13
jupyter lab metricas-avanzadas-evaluacion.ipynb
```

### Opción 3: VS Code
Abrir el archivo `.ipynb` directamente en VS Code con la extensión de Jupyter.

---

## Resultados Esperados

Al ejecutar el notebook completo, los estudiantes obtendrán:

1. **Matriz de confusión** del modelo del Tigres FC
   - 9 verdaderos positivos, 4 verdaderos negativos
   - 1 falso positivo, 1 falso negativo

2. **Métricas calculadas**:
   - Accuracy: 86.7%
   - Precision: 90.0%
   - Recall: 90.0%

3. **Visualización** profesional del heatmap de confusión

4. **Comparación de estrategias**:
   - Modelo original: Balance perfecto (90%/90%)
   - Estrategia conservadora: Alta precision (100%), recall 90%
   - Estrategia arriesgada: Baja precision (83.3%), recall perfecto (100%)

5. **Decisión informada**: El modelo original es el más balanceado para uso general

---

## Conexiones Pedagógicas

### Retrospectiva
- **Semana 11**: Introducción a ML con accuracy simple
- **Semana 12**: Construcción de modelos de ensemble para el Tigres FC
- **Semana 13**: Evaluación profunda con métricas avanzadas ← ESTAMOS AQUÍ

### Prospectiva
- **Semana 14**: Feature engineering para mejorar estas métricas
- **Semana 15**: Proyecto integrador aplicando todos los conceptos

---

## Metodología Socrática

El notebook utiliza preguntas guía como:

- "¿Por qué no basta con saber si el modelo acierta o falla?"
- "¿Cuándo preferirías alta precision vs. alto recall?"
- "¿Es peor predecir un suplente como titular, o un titular como suplente?"
- "¿Cómo comunicarías estos resultados al cuerpo técnico del Tigres FC?"

Estas preguntas fomentan el pensamiento crítico y la reflexión sobre el contexto de las decisiones basadas en datos.

---

## Notas para Instructores

### Tiempo Sugerido por Módulo
- Módulo 1 (Matriz de confusión): 15 minutos
- Módulo 2 (Precision y Recall): 15 minutos
- Módulo 3 (Visualización): 10 minutos
- Módulo 4 (Comparación): 10 minutos

### Puntos de Énfasis
1. **No todas las métricas son iguales**: Accuracy puede ser engañoso
2. **El contexto determina la métrica**: No hay una "mejor" métrica universal
3. **Visualización para comunicación**: Gráficos para audiencias no técnicas
4. **Comparación con baselines**: Validar que modelos complejos aportan valor

### Errores Comunes a Prevenir
- Confundir precision (métrica) con accuracy
- Pensar que un modelo con 90% accuracy es "perfecto"
- No considerar el costo diferencial de tipos de errores
- Olvidar que las métricas deben alinearse con objetivos de negocio

---

## Recursos Adicionales

### Documentación Oficial
- [sklearn.metrics.confusion_matrix](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html)
- [sklearn.metrics.accuracy_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html)
- [Seaborn heatmap](https://seaborn.pydata.org/generated/seaborn.heatmap.html)

### Conceptos Relacionados
- F1-Score: Media armónica de precision y recall
- ROC Curves y AUC: Evaluación gráfica de modelos
- Matrices de confusión multiclase: Extensión a más de 2 clases

---

## Estado de Actualización

### Cambios Realizados (Octubre 2025)

✅ **Actualización completa a narrativa unificada**:
- Cambio de FC Barcelona → Tigres FC en todo el contenido
- Nombres de jugadores actualizados a ficticios del Tigres FC
- Conexión explícita con Semana 12 agregada
- Contexto de la liga ficticia (85/100 habilidad) integrado
- README.md creado con documentación completa

### Próximos Pasos
- [ ] Considerar agregar ejemplos de ROC curves en versiones futuras
- [ ] Evaluar si agregar F1-Score en Módulo 2
- [ ] Validar tiempos de ejecución en sesión de 50 minutos

---

## Contacto y Contribuciones

**Proyecto**: PS5005 Programación Básica 1 - Ciencia de Datos Aplicada al Fútbol
**Institución**: Prepa Tec
**Propósito**: Educativo - Enseñanza de fundamentos de evaluación de modelos ML

Para reportar problemas o sugerir mejoras, consultar con el equipo de desarrollo del curso.

---

## Licencia

Material educativo para uso académico en Prepa Tec. Se permite su uso y adaptación con fines educativos citando la fuente.

---

**Última actualización**: Octubre 2025
**Versión**: 2.0 (con narrativa unificada del Tigres FC)
**Estado**: ✅ Actualizada y documentada
