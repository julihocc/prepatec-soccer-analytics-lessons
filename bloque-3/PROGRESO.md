# Progreso del Bloque 3: Modelado Predictivo

**Última actualización**: Noviembre 2025
**Objetivo**: Crear 6 sesiones de 1 hora con notebooks autocontenidos
**Enfoque**: SIMPLE - Todo inline, sin módulos externos

---

## Estado General

```
Progreso: ████████████░░░░░░░░ 67% (4/6 sesiones)
```

| Sesión | Notebook | Estado | Prioridad |
|--------|----------|--------|-----------|
| 1. EDA | `01-eda.ipynb` | ✅ Completo | - |
| 2. Regresión Logística | `02-regresion-logistica.ipynb` | ✅ Completo | - |
| 3. Árboles Decisión | `03-arboles-decision.ipynb` | ✅ Completo | - |
| 4. Random Forest | `04-random-forest.ipynb` | ✅ Completo | - |
| 5. XGBoost | `05-xgboost.ipynb` | ⏳ Pendiente | Media |
| 6. Comparación | `06-comparacion-modelos.ipynb` | ⏳ Pendiente | Baja |

---

## Detalle por Sesión

### ✅ Sesión 1: EDA
**Archivo**: `notebook/01-eda.ipynb`
**Estado**: ✅ Completado

**Completado**:

- [x] Notebook creado y renombrado a `01-eda.ipynb`
- [x] Dataset disponible: `data/datos_liga_futbol.csv`
- [x] Diccionario de datos: `data/DICCIONARIO_DATOS.md`
- [x] Simplificado de 15 a 7 secciones esenciales:
  1. Configuración y Carga de Datos
  2. Inspección Inicial y Calidad de Datos
  3. Análisis de Resultados (Variable Objetivo)
  4. Análisis de Goles
  5. Características Clave: Habilidades y Rachas
  6. Matriz de Correlación
  7. Resumen y Conclusiones
- [x] Optimizado para sesión de 60 minutos

---

### ✅ Sesión 2: Regresión Logística
**Archivo**: `notebook/02-regresion-logistica.ipynb`
**Estado**: ✅ Completado

**Completado**:

- [x] Notebook autocontenido creado con 11 secciones
- [x] Feature engineering inline: Diferencia_Habilidad, Diferencia_Racha, Ratio_Habilidad
- [x] Train/test split (80/20, stratified, random_state=42)
- [x] Modelo de Regresión Logística entrenado
- [x] Evaluación completa: accuracy, confusion matrix, classification report
- [x] Análisis de coeficientes (feature importance)
- [x] Ejemplos de predicciones con probabilidades
- [x] Métricas guardadas para comparación futura

---

### ✅ Sesión 3: Árboles de Decisión
**Archivo**: `notebook/03-arboles-decision.ipynb`
**Estado**: ✅ Completado

**Completado**:

- [x] Notebook autocontenido con 11 secciones
- [x] Explicación clara de árboles de decisión con analogías
- [x] Visualización completa del árbol (full + simplified 3-level)
- [x] Decision path explanation para ejemplos individuales
- [x] Comparación detallada con Regresión Logística
- [x] Feature importance analysis
- [x] Análisis de overfitting
- [x] Ejemplos de predicciones con explicación de rutas

---

### ✅ Sesión 4: Random Forest
**Archivo**: `notebook/04-random-forest.ipynb`
**Estado**: ✅ Completado

**Completado**:

- [x] Notebook autocontenido con 11 secciones
- [x] Concepto de Ensemble Learning explicado con analogías
- [x] Entrenamiento de Random Forest (100 árboles)
- [x] Comparación triple: Logística vs Árbol vs Random Forest
- [x] Feature importance más robusta
- [x] Análisis de confianza en predicciones
- [x] Experimento: efecto del número de árboles (1-200)
- [x] Visualizaciones comparativas detalladas

---

### ⏳ Sesión 5: XGBoost
**Archivo**: `notebook/05-xgboost.ipynb`
**Estado**: No iniciada

**Tareas**:
- [ ] Crear notebook autocontenido
- [ ] XGBClassifier
- [ ] Tuning básico
- [ ] Comparar con 3 modelos anteriores

---

### ⏳ Sesión 6: Comparación Final
**Archivo**: `notebook/06-comparacion-modelos.ipynb`
**Estado**: No iniciada

**Tareas**:
- [ ] Crear notebook de comparación
- [ ] Dashboard con 4 modelos
- [ ] Análisis de casos difíciles
- [ ] Recomendación final

---

## Estructura de Archivos

```
bloque-3/
├── README.md ✅
├── PROGRESO.md ✅
│
├── data/ ✅
│   ├── datos_liga_futbol.csv ✅
│   ├── generar_datos_liga.py ✅
│   └── DICCIONARIO_DATOS.md ✅
│
└── notebook/ 🟡 (1/6 notebooks)
    ├── eda.ipynb ✅ (renombrar a 01-eda.ipynb)
    ├── 02-regresion-logistica.ipynb ⏳
    ├── 03-arboles-decision.ipynb ⏳
    ├── 04-random-forest.ipynb ⏳
    ├── 05-xgboost.ipynb ⏳
    └── 06-comparacion-modelos.ipynb ⏳
```

**Nota**: NO hay carpeta `src/` - todo es autocontenido en notebooks

---

## Próximos Pasos

### 🎯 Inmediato (Semana 1)

1. **Simplificar EDA** (~2 horas)
   - Reducir de 15 a 6-8 secciones
   - Renombrar `eda.ipynb` → `01-eda.ipynb`

2. **Crear Regresión Logística** (~3 horas)
   - Notebook autocontenido
   - Feature engineering inline
   - Archivo: `02-regresion-logistica.ipynb`

### 🎯 Corto Plazo (Semana 2)

3. **Crear Árboles de Decisión** (~2 horas)
4. **Crear Random Forest** (~2 horas)
5. **Crear XGBoost** (~2 horas)

### 🎯 Final (Semana 3)

6. **Crear Comparación** (~2 horas)
7. **Testing y ajustes** (~1 hora)

**Tiempo total estimado**: ~14 horas

---

## Registro de Cambios

### 2025-11-07 (Actualización 5)

- ✅ **SESIONES 3 & 4 COMPLETADAS**: Decision Trees y Random Forest
- ✅ Session 3: Visualización de árboles, decision paths, comparaciones
- ✅ Session 4: Ensemble learning, experimento con número de árboles
- ✅ Comparación triple de modelos con visualizaciones
- ✅ Feature importance robusta y análisis de confianza
- ✅ Progreso: 67% (4/6 sesiones)

### 2025-11-07 (Actualización 4)

- ✅ **SESIÓN 2 COMPLETADA**: Regresión Logística notebook finalizado
- ✅ Feature engineering inline con 3 nuevas variables
- ✅ Modelo baseline entrenado y evaluado
- ✅ 11 secciones con teoría, práctica y ejemplos
- ✅ Métricas guardadas para comparación
- ✅ Progreso: 33% (2/6 sesiones)

### 2025-11-07 (Actualización 3)

- ✅ **SESIÓN 1 COMPLETADA**: EDA notebook finalizado
- ✅ Simplificado de 15 a 7 secciones esenciales
- ✅ Renombrado a `01-eda.ipynb`
- ✅ Optimizado para sesión de 60 minutos en clase
- ✅ Siguiente paso: Crear notebook de Regresión Logística

### 2025-11-07 (Actualización 2)

- ✅ **SIMPLIFICADO**: Estructura sin módulos externos
- ✅ Eliminada carpeta `src/` del plan
- ✅ Reducido de 7 a 6 sesiones
- ✅ Feature engineering ahora inline en cada notebook
- ✅ README y PROGRESO actualizados

### 2025-11-07 (Inicial)

- ✅ Creado README.md con plan completo
- ✅ Creado PROGRESO.md para tracking
- ✅ EDA notebook existe (como `eda.ipynb`)
- ✅ Dataset centralizado en `data/`

---

## Métricas

**Notebooks**: 4/6 completados (67%)
**Estimado para completar**: ~4 horas (~3-4 días)

---

## Decisiones de Diseño

- ✅ **Notebooks autocontenidos**: Sin módulos externos, todo inline
- ✅ **Simplicidad**: Copiar/pegar código entre notebooks es OK (más didáctico)
- ✅ **Duración**: 60 minutos por sesión
- ✅ **Progresión**: De simple (logística) a complejo (XGBoost)
- ✅ **Consistencia**: Mismo train/test split (random_state=42) en todos

---

**Actualizar este archivo después de cada sesión**
