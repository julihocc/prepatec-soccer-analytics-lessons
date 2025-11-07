# Bloque 3: Modelado Predictivo y Machine Learning

## Descripción General

El Bloque 3 introduce a los estudiantes de preparatoria al mundo del modelado predictivo y machine learning mediante el contexto del fútbol. Utilizando una **liga de fútbol ficticia** de 8 equipos, los estudiantes aprenden a predecir resultados de partidos mediante diferentes técnicas de clasificación.

**Público objetivo**: Estudiantes de preparatoria (15-18 años) sin experiencia previa en machine learning
**Duración**: 7 sesiones de 1 hora cada una
**Enfoque pedagógico**: Aprendizaje progresivo y modular con código reutilizable
**Herramientas**: Python, pandas, numpy, matplotlib, seaborn, scikit-learn, xgboost

## Objetivo del Bloque

**Pregunta central**: ¿Podemos predecir el resultado de un partido de fútbol (Victoria Local, Victoria Visitante o Empate)?

**Enfoque**: Construir y comparar múltiples modelos de clasificación, desde los más simples hasta los más sofisticados.

---

## Narrativa Unificada: La Liga Ficticia

El Bloque 3 utiliza una **narrativa progresiva y coherente** basada en una liga de fútbol ficticia de 8 equipos. Esta liga fue diseñada específicamente para proporcionar contexto realista y continuidad a lo largo de todas las semanas del bloque.

### Los 8 Equipos de la Liga

| Equipo | Habilidad | Nivel | Uso en el Curso |
|--------|-----------|-------|-----------------|
| **Tigres FC** | 85/100 | Muy fuerte | ⭐ Análisis detallado en Semanas 12-14 |
| Águilas United | 82/100 | Fuerte | Análisis de liga (Semana 11) |
| Leones SC | 78/100 | Medio-fuerte | Análisis de liga (Semana 11) |
| Halcones City | 75/100 | Medio | Análisis de liga (Semana 11) |
| Lobos Atlético | 72/100 | Medio | Análisis de liga (Semana 11) |
| Pumas CF | 68/100 | Medio-débil | Análisis de liga (Semana 11) |
| Zorros FC | 65/100 | Débil | Análisis de liga (Semana 11) |
| Cóndores United | 60/100 | Muy débil | Análisis de liga (Semana 11) |

**Contexto**: El Tigres FC es el equipo más fuerte de la liga (85 puntos), lo que justifica el análisis profundo de sus jugadores individuales en las semanas posteriores.

---

## Estructura Modular del Curso

### Organización de Archivos

```
bloque-3/
├── README.md                          # Este archivo - Plan general del curso
├── PROGRESO.md                        # Registro de avance (actualizar después de cada sesión)
│
├── data/                              # 📊 Datasets centralizados
│   ├── datos_liga_futbol.csv         # Dataset principal: 281 partidos de 5 temporadas
│   ├── generar_datos_liga.py         # Script para generar datos sintéticos
│   └── DICCIONARIO_DATOS.md          # Documentación completa del dataset
│
├── src/                               # 🔧 Código reutilizable
│   ├── __init__.py                   # Inicializar como módulo Python
│   ├── features.py                   # 🎯 Feature engineering (usar en todos los notebooks)
│   ├── evaluacion.py                 # 📊 Funciones de evaluación y visualización
│   └── utils.py                      # 🛠️ Utilidades generales
│
└── notebook/                          # 📓 Notebooks de trabajo (1 hora cada uno)
    ├── 01-eda.ipynb                  # ✅ Sesión 1: Análisis Exploratorio
    ├── 02-feature-engineering.ipynb  # ⏳ Sesión 2: Creación de características
    ├── 03-regresion-logistica.ipynb  # ⏳ Sesión 3: Modelo baseline
    ├── 04-arboles-decision.ipynb     # ⏳ Sesión 4: Árboles de decisión
    ├── 05-random-forest.ipynb        # ⏳ Sesión 5: Bosques aleatorios
    ├── 06-xgboost.ipynb              # ⏳ Sesión 6: Gradient boosting
    └── 07-comparacion-modelos.ipynb  # ⏳ Sesión 7: Comparación final
```

---

## Plan de Trabajo: 7 Sesiones de 1 Hora

### 📊 Sesión 1: Análisis Exploratorio de Datos (EDA)
**Estado**: ✅ Completada
**Archivo**: `notebook/01-eda.ipynb`
**Duración**: ~50-60 minutos

**Objetivos de aprendizaje**:
- Comprender la estructura del dataset de la liga
- Identificar patrones en victorias locales vs visitantes
- Analizar distribución de goles y resultados
- Visualizar relaciones entre variables clave

**Contenido**:
- Carga y exploración inicial de datos
- Estadísticas descriptivas básicas
- Visualizaciones de distribuciones
- Análisis de correlaciones
- Identificación de ventaja de jugar en casa

**Entregables**:
- Dataset limpio y comprendido
- 5-7 visualizaciones clave
- Lista de insights principales

---

### 🎯 Sesión 2: Ingeniería de Características
**Estado**: ⏳ Pendiente
**Archivo**: `notebook/02-feature-engineering.ipynb`
**Duración**: ~60 minutos

**Objetivos de aprendizaje**:
- Entender qué es feature engineering y por qué es importante
- Crear características derivadas del dataset base
- Guardar funciones reutilizables para otros notebooks

**Contenido**:
1. **Features básicas** (15 min):
   - Diferencia de habilidades entre equipos
   - Ventaja de jugar en casa (binaria)
   - Diferencia de rachas

2. **Features avanzadas** (20 min):
   - Ratio de habilidades
   - Momentum del equipo (racha normalizada)
   - Interacciones entre variables

3. **Módulo reutilizable** (15 min):
   - Crear funciones en `src/features.py`
   - Documentar cada función
   - Probar con dataset completo

4. **Preparación para modelado** (10 min):
   - Split train/test (80/20)
   - Guardar datasets procesados
   - Verificar no hay data leakage

**Entregables**:
- `src/features.py` con funciones documentadas
- Dataset con nuevas características
- Train/test split guardados

**Código ejemplo** (features.py):
```python
def crear_features_basicas(df):
    """Crea características básicas para predicción."""
    df['Diferencia_Habilidad'] = df['Habilidad_Local'] - df['Habilidad_Visitante']
    df['Diferencia_Racha'] = df['Racha_Local'] - df['Racha_Visitante']
    return df

def crear_features_avanzadas(df):
    """Crea características avanzadas."""
    df['Ratio_Habilidad'] = df['Habilidad_Local'] / (df['Habilidad_Visitante'] + 1)
    df['Momentum_Local'] = df['Racha_Local'] * df['Habilidad_Local'] / 100
    return df
```

---

### 🎯 Sesión 3: Regresión Logística (Modelo Baseline)
**Estado**: ⏳ Pendiente
**Archivo**: `notebook/03-regresion-logistica.ipynb`
**Duración**: ~60 minutos

**Objetivos de aprendizaje**:
- Entender qué es clasificación multiclase
- Construir un modelo baseline simple
- Evaluar métricas básicas (accuracy, matriz de confusión)

**Contenido**:
1. **Introducción a clasificación** (10 min):
   - ¿Qué es clasificación multiclase?
   - Diferencia con clasificación binaria
   - ¿Por qué regresión logística como baseline?

2. **Construcción del modelo** (20 min):
   - Importar features desde `src/features.py`
   - Entrenar modelo con sklearn
   - Predicciones en test set

3. **Evaluación** (20 min):
   - Accuracy general
   - Matriz de confusión
   - Accuracy por clase (Local, Visitante, Empate)
   - ¿Qué clase predice mejor/peor?

4. **Interpretación** (10 min):
   - Coeficientes del modelo
   - Features más importantes
   - Discusión de resultados

**Entregables**:
- Modelo entrenado y guardado
- Reporte de métricas baseline
- Interpretación de coeficientes

**Métricas esperadas**:
- Accuracy: ~50-60%
- Clase mejor predicha: Victoria Local
- Clase peor predicha: Empate

---

### 🌳 Sesión 4: Árboles de Decisión
**Estado**: ⏳ Pendiente
**Archivo**: `notebook/04-arboles-decision.ipynb`
**Duración**: ~60 minutos

**Objetivos de aprendizaje**:
- Comprender cómo funcionan los árboles de decisión
- Visualizar reglas de decisión
- Comparar con regresión logística

**Contenido**:
1. **Teoría básica** (15 min):
   - ¿Qué es un árbol de decisión?
   - Analogía con preguntas de sí/no
   - Ventajas: interpretabilidad, no linealidad

2. **Entrenamiento** (15 min):
   - DecisionTreeClassifier de sklearn
   - Hiperparámetros básicos (max_depth, min_samples_split)
   - Entrenar con mismos datos que Sesión 3

3. **Visualización del árbol** (15 min):
   - Dibujar árbol de decisión
   - Interpretar reglas principales
   - ¿Qué features usa primero?

4. **Evaluación y comparación** (15 min):
   - Mismas métricas que Sesión 3
   - Comparar con regresión logística
   - Discusión: ¿Cuál es mejor y por qué?

**Entregables**:
- Árbol de decisión entrenado
- Visualización del árbol
- Tabla comparativa con modelo baseline

**Conceptos clave**:
- Overfitting vs underfitting
- Importancia de features
- Trade-off interpretabilidad vs precisión

---

### 🌲 Sesión 5: Bosques Aleatorios (Random Forest)
**Estado**: ⏳ Pendiente
**Archivo**: `notebook/05-random-forest.ipynb`
**Duración**: ~60 minutos

**Objetivos de aprendizaje**:
- Entender ensemble learning
- Implementar Random Forest
- Mejorar predicciones mediante votación

**Contenido**:
1. **Concepto de ensemble** (10 min):
   - Analogía: "consultar a varios expertos"
   - Votación por mayoría
   - ¿Por qué funciona mejor?

2. **Random Forest** (15 min):
   - Múltiples árboles aleatorios
   - Parámetros: n_estimators, max_features
   - Entrenar con sklearn

3. **Evaluación** (20 min):
   - Métricas completas
   - Feature importance
   - Comparar con modelos anteriores

4. **Análisis de errores** (15 min):
   - ¿Qué partidos predice mal?
   - ¿Hay patrones en los errores?
   - Ideas para mejorar

**Entregables**:
- Random Forest entrenado
- Gráfico de feature importance
- Tabla comparativa (3 modelos)

**Métricas esperadas**:
- Accuracy: ~60-70%
- Mejor que modelos anteriores
- Empates aún difíciles de predecir

---

### 🚀 Sesión 6: XGBoost (Gradient Boosting)
**Estado**: ⏳ Pendiente
**Archivo**: `notebook/06-xgboost.ipynb`
**Duración**: ~60 minutos

**Objetivos de aprendizaje**:
- Introducción a gradient boosting
- Usar XGBoost para clasificación
- Optimizar hiperparámetros básicos

**Contenido**:
1. **Teoría de boosting** (10 min):
   - Diferencia con Random Forest
   - Aprendizaje secuencial
   - Corregir errores de modelos anteriores

2. **XGBoost implementation** (20 min):
   - Instalación y configuración
   - Parámetros básicos: n_estimators, learning_rate, max_depth
   - Entrenar modelo

3. **Evaluación** (15 min):
   - Métricas completas
   - Feature importance
   - Comparar con 3 modelos anteriores

4. **Tuning básico** (15 min):
   - Probar 2-3 configuraciones
   - Grid search simple
   - Seleccionar mejor modelo

**Entregables**:
- XGBoost entrenado y optimizado
- Feature importance de XGBoost
- Tabla comparativa (4 modelos)

**Métricas esperadas**:
- Accuracy: ~65-75%
- Posiblemente el mejor modelo
- Mejor predicción de empates

---

### 📊 Sesión 7: Comparación y Conclusiones
**Estado**: ⏳ Pendiente
**Archivo**: `notebook/07-comparacion-modelos.ipynb`
**Duración**: ~60 minutos

**Objetivos de aprendizaje**:
- Comparar todos los modelos de manera sistemática
- Entender trade-offs entre modelos
- Presentar recomendaciones finales

**Contenido**:
1. **Carga de modelos** (10 min):
   - Cargar 4 modelos entrenados
   - Verificar métricas guardadas

2. **Comparación sistemática** (25 min):
   - Tabla resumen con todas las métricas
   - Gráficos comparativos:
     - Accuracy por modelo
     - Accuracy por clase (Local/Visitante/Empate)
     - Matriz de confusión de cada modelo
     - Feature importance comparada
   - Análisis de tiempo de entrenamiento

3. **Casos de estudio** (15 min):
   - Seleccionar 5 partidos "difíciles"
   - Ver predicciones de cada modelo
   - Analizar por qué difieren

4. **Conclusiones y recomendaciones** (10 min):
   - ¿Qué modelo es mejor?
   - ¿Depende del contexto?
   - ¿Qué aprendimos sobre predicción de fútbol?
   - Próximos pasos para mejorar

**Entregables**:
- Dashboard comparativo completo
- Reporte ejecutivo (1-2 páginas)
- Recomendación de modelo final

**Visualizaciones clave**:
```python
# Comparación de accuracy
modelos = ['Reg. Logística', 'Árbol', 'Random Forest', 'XGBoost']
accuracy = [0.56, 0.62, 0.69, 0.72]

# Comparación por clase
resultados = {
    'Victoria Local': [0.65, 0.71, 0.78, 0.80],
    'Victoria Visitante': [0.58, 0.64, 0.70, 0.73],
    'Empate': [0.35, 0.42, 0.50, 0.58]
}
```

---

## Principios Clave del Curso

### 🎯 Modularidad y Reutilización
- **Un módulo, un objetivo**: Cada notebook cubre un modelo específico
- **Código DRY**: Feature engineering en `src/features.py` reutilizable en todos los notebooks
- **Progresión clara**: De modelos simples (logística) a complejos (XGBoost)

### ⏱️ Sesiones de 1 Hora
- **50-60 minutos** de contenido efectivo
- **10 minutos** al final para preguntas y resumen
- **Entregables claros** al final de cada sesión

### 📊 Evaluación Consistente
- **Mismas métricas** en todos los modelos (accuracy, matriz confusión)
- **Mismo train/test split** para comparación justa
- **Visualizaciones estandarizadas** usando `src/evaluacion.py`

### 🎓 Enfoque Didáctico
- **Teoría mínima necesaria**: 10-15 minutos por sesión
- **Práctica inmediata**: Código ejecutable desde el primer minuto
- **Aprendizaje activo**: Estudiantes ejecutan y modifican código
- **Comparación constante**: ¿Es mejor que el modelo anterior?

---

## Próximos Pasos Inmediatos

### 🔴 Prioridad 1: Simplificar EDA (Sesión 1)
**Estado actual**: El notebook `01-eda.ipynb` es demasiado extenso (15 secciones)
**Acción requerida**: Reducir a 6-8 secciones esenciales para 1 hora

**Secciones a mantener**:
1. Carga de datos e inspección inicial
2. Calidad de datos (nulos, duplicados)
3. Análisis de resultados (Victoria L/V/Empate)
4. Análisis de goles
5. Ventaja de jugar en casa
6. Correlaciones básicas
7. Resumen ejecutivo

**Secciones a mover/eliminar**:
- Análisis por temporada (mover a apéndice)
- Análisis exhaustivo de equipos (innecesario para predicción)
- Análisis detallado de rachas (ver en feature engineering)
- Probabilidades de victoria (demasiado avanzado)
- Tabla general de equipos (mover a apéndice)

### 🟡 Prioridad 2: Crear Módulo de Features
**Archivo**: `src/features.py`
**Contenido**:
```python
"""
Feature Engineering para Predicción de Resultados de Fútbol
Bloque 3: Modelado Predictivo
"""

import pandas as pd
import numpy as np

def crear_features_basicas(df):
    """
    Crea características básicas para predicción.

    Args:
        df: DataFrame con datos de partidos

    Returns:
        DataFrame con nuevas columnas de features
    """
    df = df.copy()

    # Diferencia de habilidades
    df['Diferencia_Habilidad'] = df['Habilidad_Local'] - df['Habilidad_Visitante']

    # Diferencia de rachas
    df['Diferencia_Racha'] = df['Racha_Local'] - df['Racha_Visitante']

    # Ventaja de casa (ya existe como Juega_En_Casa)

    return df

def crear_features_avanzadas(df):
    """
    Crea características avanzadas (interacciones, ratios).

    Args:
        df: DataFrame con features básicas

    Returns:
        DataFrame con features avanzadas adicionales
    """
    df = df.copy()

    # Ratio de habilidades (evitar división por cero)
    df['Ratio_Habilidad'] = df['Habilidad_Local'] / (df['Habilidad_Visitante'] + 1)

    # Momentum (racha * habilidad normalizada)
    df['Momentum_Local'] = df['Racha_Local'] * df['Habilidad_Local'] / 100
    df['Momentum_Visitante'] = df['Racha_Visitante'] * df['Habilidad_Visitante'] / 100

    # Diferencia de momentum
    df['Diferencia_Momentum'] = df['Momentum_Local'] - df['Momentum_Visitante']

    return df

def preparar_datos_modelado(df, test_size=0.2, random_state=42):
    """
    Prepara datos para modelado: features, target, train/test split.

    Args:
        df: DataFrame con todas las features
        test_size: Proporción para test set
        random_state: Semilla aleatoria

    Returns:
        X_train, X_test, y_train, y_test
    """
    from sklearn.model_selection import train_test_split

    # Features a usar
    feature_columns = [
        'Habilidad_Local', 'Habilidad_Visitante',
        'Racha_Local', 'Racha_Visitante',
        'Probabilidad_Victoria_Local',
        'Diferencia_Habilidad', 'Diferencia_Racha',
        'Ratio_Habilidad',
        'Momentum_Local', 'Momentum_Visitante', 'Diferencia_Momentum'
    ]

    X = df[feature_columns]
    y = df['Resultado']  # 'Victoria Local', 'Victoria Visitante', 'Empate'

    return train_test_split(X, y, test_size=test_size, random_state=random_state, stratify=y)
```

### 🟡 Prioridad 3: Crear Módulo de Evaluación
**Archivo**: `src/evaluacion.py`
**Contenido**: Funciones para visualizar métricas de manera consistente

### 🟢 Prioridad 4-7: Crear Notebooks de Modelos
Seguir el plan detallado en Sesiones 3-7

---

## Calendario Sugerido de Implementación

### Fase 1: Fundamentos (Semana 1)
- [ ] Día 1: Simplificar EDA notebook
- [ ] Día 2: Crear `src/features.py`
- [ ] Día 3: Crear `src/evaluacion.py`
- [ ] Día 4: Crear notebook feature engineering
- [ ] Día 5: Testing y revisión

### Fase 2: Modelos Básicos (Semana 2)
- [ ] Día 1-2: Notebook regresión logística
- [ ] Día 3-4: Notebook árboles de decisión
- [ ] Día 5: Testing y ajustes

### Fase 3: Modelos Avanzados (Semana 3)
- [ ] Día 1-2: Notebook Random Forest
- [ ] Día 3-4: Notebook XGBoost
- [ ] Día 5: Testing y ajustes

### Fase 4: Integración (Semana 4)
- [ ] Día 1-3: Notebook comparación de modelos
- [ ] Día 4-5: Documentación final y README

---

## Compatibilidad con Estructura Anterior

Este nuevo enfoque modular **complementa** (no reemplaza) la estructura de semanas 10-15 existente:

- **Nueva estructura**: Enfoque modular para enseñanza práctica (7 sesiones de 1 hora)
- **Estructura anterior**: Material de referencia y contexto narrativo más amplio

Ambas coexisten en `bloque-3/` y los instructores pueden elegir cuál usar según el contexto.

---

## Progresión Pedagógica por Semanas (Estructura Anterior)

*Nota: Esta sección mantiene la estructura original para referencia.*

### Semana 10: Análisis Estadístico Descriptivo
**Estado**: ⚠️ Por revisar para narrativa unificada
**Enfoque**: Introducción a estadística básica
**Datos**: (Por determinar - posiblemente introducción a los equipos)

---

### Semana 11: Introducción al Modelado Predictivo ✅
**Estado**: ✅ Actualizada con narrativa unificada
**Enfoque**: Análisis **MACRO** - Nivel de liga completa
**Última actualización**: Octubre 2025

#### Contenido
- **Dataset**: `datos_liga_futbol.csv` - 56 partidos de la liga
- **Objetivo**: Predecir ganadores de partidos usando características del equipo
- **Técnica ML**: Regresión Logística simple
- **Resultados clave**: Identificación del Tigres FC como equipo más fuerte (85/100)

#### Archivos principales
```
semana-11/
├── modelado-predictivo-introduccion.ipynb  # Notebook principal (3 sesiones)
├── datos_liga_futbol.csv                   # Dataset de 56 partidos
├── generar_datos_liga.py                   # Generador de datos sintéticos
├── DICCIONARIO_DATOS.md                    # Documentación del dataset
└── README.md                               # Guía de uso
```

#### Conceptos enseñados
- ¿Qué es un modelo predictivo?
- Preparación de datos (features y target)
- Train/test split
- Evaluación con accuracy
- Ventaja de jugar en casa
- Efecto de rachas de victorias

#### Conexión narrativa
Esta semana establece la liga ficticia y presenta los 8 equipos. Los estudiantes analizan 56 partidos para entender qué factores predicen victorias. El análisis revela al **Tigres FC como el equipo más exitoso**, preparando el terreno para el análisis detallado en Semana 12.

---

### Semana 12: Modelos Avanzados de Clasificación ✅
**Estado**: ✅ Actualizada con narrativa unificada (Tigres FC)
**Enfoque**: Análisis **MICRO** - Nivel de jugadores individuales
**Última actualización**: Octubre 2025

#### Contenido
- **Dataset**: `datos_tigres_fc.csv` - 100 jugadores del Tigres FC
- **Objetivo**: Predecir si un jugador debería ser titular o suplente
- **Técnica ML**: Ensemble Learning (votación por mayoría)
- **Modelos**: Regresión Logística (×2) + Random Forest

#### Archivos principales
```
semana-12/
├── modelos-avanzados-clasificacion.ipynb  # Notebook principal (3 sesiones)
├── datos_tigres_fc.csv                    # Dataset de 100 jugadores
├── generar_datos_liga.py                  # Generador de datos sintéticos
├── DICCIONARIO_DATOS.md                   # Documentación del dataset
└── README.md                              # Guía de uso
```

#### Conceptos enseñados
- Ensemble Learning (aprendizaje en conjunto)
- Votación por mayoría
- Combinación de múltiples modelos
- Ventajas de datasets más grandes (100 vs 15 registros)
- Separación de generación de datos y análisis
- Evaluación comparativa de modelos

#### Conexión narrativa
Esta semana profundiza en el **Tigres FC**, el equipo más fuerte identificado en Semana 11. El análisis pasa de nivel macro (equipos) a nivel micro (jugadores individuales), mostrando cómo el éxito del equipo se refleja en las estadísticas de sus jugadores. Se analizan 100 jugadores de 3 temporadas para construir un sistema robusto de selección de titulares.

#### Cambios realizados
- ✅ Cambio de "FC Barcelona" → "Tigres FC" en todo el contenido
- ✅ Dataset actualizado: `datos_barcelona.csv` → `datos_tigres_fc.csv`
- ✅ Conexión explícita con la liga ficticia de Semana 11
- ✅ 100 jugadores del equipo más fuerte de la liga
- ✅ Diccionario de datos completo creado
- ✅ README actualizado con nueva narrativa

---

### Semana 13: Métricas Avanzadas de Evaluación ⏳
**Estado**: ⏳ Pendiente de actualización
**Enfoque**: Análisis **MICRO** - Evaluación avanzada de modelos
**Actualización pendiente**: Usar Tigres FC

#### Contenido planificado
- Continuar con datos del Tigres FC
- Métricas avanzadas: Precision, Recall, F1-Score
- Matriz de confusión avanzada
- ROC curves y AUC
- Evaluación de modelos desbalanceados

#### Tareas pendientes
- [ ] Revisar notebook actual
- [ ] Verificar si usa Barcelona o datos genéricos
- [ ] Actualizar a Tigres FC si es necesario
- [ ] Conectar con análisis de Semana 12
- [ ] Agregar referencias a la liga ficticia

---

### Semana 14: Feature Engineering ⏳
**Estado**: ⏳ Pendiente de actualización
**Enfoque**: Análisis **MICRO** - Optimización de características
**Actualización pendiente**: Usar Tigres FC

#### Contenido planificado
- Continuar con datos del Tigres FC
- Creación de nuevas características
- Transformación de variables
- Normalización y estandarización
- Feature importance
- Selección de características

#### Tareas pendientes
- [ ] Revisar notebook actual
- [ ] Verificar si usa Barcelona o datos genéricos
- [ ] Actualizar a Tigres FC si es necesario
- [ ] Conectar con análisis de Semanas 12-13
- [ ] Agregar variables derivadas del contexto de la liga

---

### Semana 15: Proyecto Integrador Final ⏳
**Estado**: ⏳ Pendiente de actualización
**Enfoque**: Análisis **MACRO + MICRO** - Proyecto completo
**Actualización pendiente**: Usar liga ficticia completa

#### Contenido planificado
- Análisis comparativo de equipos de la liga
- Predicción de campeón de liga
- Análisis de jugadores destacados por equipo
- Simulación de temporada completa
- Presentación de resultados

#### Tareas pendientes
- [ ] Revisar proyecto actual
- [ ] Integrar liga ficticia de 8 equipos
- [ ] Permitir análisis comparativo entre equipos
- [ ] Incluir datos del Tigres FC como caso de estudio
- [ ] Crear rúbrica de evaluación actualizada

---

## Flujo Narrativo del Bloque

### Análisis Progresivo: De lo General a lo Específico

```
SEMANA 10
   ↓
   Introducción a estadística
   ↓
SEMANA 11: PRESENTACIÓN DE LA LIGA
   ↓
   8 equipos | 56 partidos
   Análisis MACRO (equipos)
   Resultado: Tigres FC es el más fuerte (85/100)
   ↓
SEMANA 12: ENFOQUE EN EL MEJOR EQUIPO
   ↓
   Tigres FC | 100 jugadores
   Análisis MICRO (individuos)
   Pregunta: ¿Qué hace a un jugador titular en el mejor equipo?
   ↓
SEMANA 13: EVALUACIÓN PROFUNDA
   ↓
   Tigres FC | Métricas avanzadas
   Pregunta: ¿Qué tan buenos son nuestros modelos realmente?
   ↓
SEMANA 14: OPTIMIZACIÓN
   ↓
   Tigres FC | Feature engineering
   Pregunta: ¿Podemos mejorar las predicciones?
   ↓
SEMANA 15: PROYECTO INTEGRADOR
   ↓
   Liga completa | Análisis comparativo
   Pregunta: ¿Cómo se comparan los equipos y sus jugadores?
```

---

## Datasets Principales

### Dataset de Liga (Semana 11)
**Archivo**: `semana-11/datos_liga_futbol.csv`
- **Registros**: 56 partidos
- **Variables**: 14 columnas
- **Objetivo**: Predecir ganador de partido
- **Características clave**: Habilidad equipo, ventaja casa, rachas

### Dataset de Jugadores (Semanas 12-14)
**Archivo**: `semana-12/datos_tigres_fc.csv`
- **Registros**: 100 jugadores
- **Variables**: 5 columnas
- **Objetivo**: Predecir titular vs suplente
- **Características clave**: Goles, minutos, edad

### Dataset Integrador (Semana 15)
**Archivo**: (Por determinar)
- **Contenido planificado**: Datos de múltiples equipos para análisis comparativo

---

## Estructura de Archivos

```
bloque-3/
├── README.md                          # Este archivo
├── semana-10/                         # ⚠️ Por revisar
│   └── [archivos de estadística descriptiva]
│
├── semana-11/                         # ✅ Actualizada
│   ├── modelado-predictivo-introduccion.ipynb
│   ├── datos_liga_futbol.csv
│   ├── generar_datos_liga.py
│   ├── DICCIONARIO_DATOS.md
│   └── README.md
│
├── semana-12/                         # ✅ Actualizada
│   ├── modelos-avanzados-clasificacion.ipynb
│   ├── datos_tigres_fc.csv
│   ├── generar_datos_liga.py
│   ├── DICCIONARIO_DATOS.md
│   └── README.md
│
├── semana-13/                         # ⏳ Pendiente
│   └── [por actualizar con Tigres FC]
│
├── semana-14/                         # ⏳ Pendiente
│   └── [por actualizar con Tigres FC]
│
└── semana-15/                         # ⏳ Pendiente
    └── [por actualizar con liga completa]
```

---

## Registro de Cambios

### Octubre 2025 - Unificación de Narrativa

#### Cambios Completados ✅

**Semana 11: Introducción al Modelado Predictivo**
- ✅ README actualizado con lista correcta de equipos y habilidades
- ✅ Tigres FC (85) destacado como equipo más fuerte
- ✅ Sección de "Narrativa unificada" agregada
- ✅ Conexión explícita con Semana 12
- ✅ DICCIONARIO_DATOS.md actualizado con distribución completa de equipos

**Semana 12: Modelos Avanzados de Clasificación**
- ✅ Cambio completo de FC Barcelona → Tigres FC
- ✅ Dataset regenerado: `datos_tigres_fc.csv` (100 jugadores)
- ✅ Script generador actualizado: `generar_datos_liga.py`
- ✅ Notebook actualizado: 6 módulos con nueva narrativa
- ✅ DICCIONARIO_DATOS.md creado desde cero
- ✅ README actualizado con contexto de liga ficticia
- ✅ Conexión explícita con Semana 11 (85/100 habilidad)
- ✅ Archivo antiguo eliminado: `datos_barcelona.csv`

**Documentación General**
- ✅ README del Bloque 3 creado (este archivo)
- ✅ Narrativa unificada documentada
- ✅ Flujo pedagógico visualizado
- ✅ Estado de cada semana registrado

#### Cambios Pendientes ⏳

**Semana 13: Métricas Avanzadas de Evaluación**
- [ ] Revisar contenido actual
- [ ] Actualizar referencias de equipos/jugadores a Tigres FC
- [ ] Verificar datasets utilizados
- [ ] Conectar con análisis de Semana 12
- [ ] Actualizar README y crear DICCIONARIO_DATOS si es necesario

**Semana 14: Feature Engineering**
- [ ] Revisar contenido actual
- [ ] Actualizar referencias de equipos/jugadores a Tigres FC
- [ ] Verificar datasets utilizados
- [ ] Conectar con análisis de Semanas 12-13
- [ ] Actualizar README y documentación

**Semana 15: Proyecto Integrador Final**
- [ ] Revisar contenido actual
- [ ] Actualizar para usar liga ficticia completa (8 equipos)
- [ ] Permitir análisis comparativo entre equipos
- [ ] Incluir Tigres FC como caso de estudio destacado
- [ ] Actualizar rúbrica de evaluación
- [ ] Crear documentación completa del proyecto

**Semana 10: Análisis Estadístico Descriptivo**
- [ ] Revisar si necesita integración con la liga ficticia
- [ ] Determinar si debe introducir los equipos
- [ ] Actualizar si es necesario

---

## Beneficios de la Narrativa Unificada

### Para los Estudiantes
1. **Continuidad**: Mismos equipos y contexto a lo largo de 6 semanas
2. **Progresión lógica**: De análisis general (liga) a específico (jugadores)
3. **Motivación**: Historia coherente más interesante que datasets aislados
4. **Conexiones**: Cada semana se construye sobre la anterior
5. **Realismo**: Simula cómo se hace análisis de datos en el mundo real

### Para los Instructores
1. **Coherencia pedagógica**: Narrativa clara y fácil de seguir
2. **Reutilización**: Mismos equipos y conceptos en múltiples semanas
3. **Flexibilidad**: Posibilidad de agregar análisis adicionales
4. **Documentación**: Todo está claramente documentado y conectado
5. **Mantenimiento**: Más fácil actualizar contenido relacionado

### Para el Curso
1. **Profesionalismo**: Datasets sintéticos pero realistas y consistentes
2. **Reproducibilidad**: Datos generados con semillas fijas
3. **Escalabilidad**: Fácil agregar nuevas semanas con misma narrativa
4. **Claridad**: Objetivos de aprendizaje alineados con la historia

---

## Principios de Diseño

### Realismo Estadístico
- Distribuciones basadas en estadísticas reales de fútbol
- Habilidades de equipos diferenciadas (60-85)
- Distribuciones de goles, minutos, edades realistas

### Progresión Pedagógica
- Comenzar con conceptos simples (clasificación binaria)
- Avanzar a técnicas complejas (ensemble learning)
- Terminar con proyecto integrador

### Datos Sintéticos
- Generados mediante scripts reproducibles
- Semilla fija (42) para consistencia
- Documentados exhaustivamente

### Separación de Responsabilidades
- Scripts de generación separados de notebooks de análisis
- Archivos CSV versionados
- Diccionarios de datos completos

---

## Próximos Pasos

### Para Continuar el Trabajo

1. **Semana 13** (Siguiente prioridad):
   ```bash
   cd contenido/bloque-3/semana-13
   # Revisar archivos existentes
   # Actualizar con Tigres FC
   # Conectar con Semana 12
   ```

2. **Semana 14** (Segunda prioridad):
   ```bash
   cd contenido/bloque-3/semana-14
   # Revisar archivos existentes
   # Actualizar con Tigres FC
   # Agregar feature engineering específico
   ```

3. **Semana 15** (Tercera prioridad):
   ```bash
   cd contenido/bloque-3/semana-15
   # Revisar proyecto actual
   # Integrar liga completa
   # Crear rúbrica actualizada
   ```

4. **Semana 10** (Opcional):
   ```bash
   cd contenido/bloque-3/semana-10
   # Determinar si necesita cambios
   # Posiblemente introducir los equipos
   ```

### Verificación de Consistencia

Antes de considerar completado el bloque:
- [ ] Todas las referencias a equipos/jugadores son consistentes
- [ ] Todos los datasets tienen DICCIONARIO_DATOS.md
- [ ] Todos los READMEs mencionan la conexión con la liga ficticia
- [ ] Los 8 equipos tienen habilidades consistentes en todos los archivos
- [ ] La progresión macro → micro → integrador es clara

---

## Recursos Técnicos

### Scripts de Generación de Datos

**Semana 11**: `semana-11/generar_datos_liga.py`
- Genera 56 partidos de liga completa
- Incluye ventaja de casa y rachas
- Output: `datos_liga_futbol.csv`

**Semana 12**: `semana-12/generar_datos_liga.py`
- Genera 100 jugadores del Tigres FC
- Distribuciones realistas (goles, minutos, edad)
- Output: `datos_tigres_fc.csv`

### Notebooks Principales

**Semana 11**: `semana-11/modelado-predictivo-introduccion.ipynb`
- 3 sesiones de 50 minutos
- Introducción a ML con clasificación binaria
- Regresión Logística simple

**Semana 12**: `semana-12/modelos-avanzados-clasificacion.ipynb`
- 3 sesiones de 50 minutos
- Ensemble Learning con votación
- Regresión Logística + Random Forest

---

## Contacto y Contribuciones

**Proyecto**: PS5005 Programación Básica 1 - Ciencia de Datos Aplicada al Fútbol
**Bloque**: 3 - Modelado Predictivo y Machine Learning
**Institución**: Prepa Tec
**Propósito**: Educativo - Enseñanza de fundamentos de machine learning

Para contribuir o reportar problemas con la narrativa unificada, consultar con el equipo de desarrollo del curso.

---

## Licencia

Material educativo para uso académico en Prepa Tec. Se permite su uso y adaptación con fines educativos citando la fuente.

---

**Última actualización**: Octubre 2025
**Versión**: 2.0 (con narrativa unificada de la liga ficticia)
**Estado**: En progreso - Semanas 11-12 completadas, 13-15 pendientes
