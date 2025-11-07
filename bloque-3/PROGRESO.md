# Progreso del Bloque 3: Modelado Predictivo

**Última actualización**: Noviembre 2025
**Objetivo**: Crear 7 sesiones modulares de 1 hora para enseñar modelado predictivo

---

## Estado General

```
Progreso: ████░░░░░░░░░░░░░░░░ 15% (1/7 sesiones)
```

| Fase | Estado | Completado |
|------|--------|------------|
| **Fundamentos** | 🟡 En progreso | 1/4 |
| **Modelos Básicos** | ⚪ Pendiente | 0/2 |
| **Modelos Avanzados** | ⚪ Pendiente | 0/2 |
| **Integración** | ⚪ Pendiente | 0/1 |

---

## Fase 1: Fundamentos (En Progreso)

### ✅ Sesión 1: EDA
- [x] Notebook creado: `notebook/01-eda.ipynb` (anteriormente `main.ipynb`)
- [x] Dataset disponible: `data/datos_liga_futbol.csv`
- [x] Diccionario de datos: `data/DICCIONARIO_DATOS.md`
- [ ] **PENDIENTE**: Simplificar notebook a 6-8 secciones para 1 hora
- [ ] **PENDIENTE**: Probar en clase con estudiantes

**Notas**:
- Notebook actual tiene 15 secciones - demasiado extenso
- Reducir enfoque a lo esencial para predicción
- Mover análisis detallado a apéndice opcional

---

### ⏳ Sesión 2: Feature Engineering
**Estado**: No iniciada
**Prioridad**: Alta (siguiente tarea)

**Tareas**:
- [ ] Crear módulo `src/features.py` con funciones reutilizables
- [ ] Crear módulo `src/__init__.py`
- [ ] Crear notebook `notebook/02-feature-engineering.ipynb`
- [ ] Documentar funciones con docstrings
- [ ] Crear ejemplos de uso
- [ ] Probar funciones con dataset completo

**Entregables esperados**:
```python
# src/features.py debe incluir:
- crear_features_basicas(df)
- crear_features_avanzadas(df)
- preparar_datos_modelado(df)
```

---

### ⏳ Módulo de Evaluación
**Estado**: No iniciado
**Prioridad**: Alta (paralelo a Sesión 2)

**Tareas**:
- [ ] Crear módulo `src/evaluacion.py`
- [ ] Funciones para matriz de confusión
- [ ] Funciones para gráficos comparativos
- [ ] Funciones para reportes de métricas
- [ ] Documentar con ejemplos

---

### ⏳ Módulo de Utilidades
**Estado**: No iniciado
**Prioridad**: Media

**Tareas**:
- [ ] Crear módulo `src/utils.py`
- [ ] Funciones de carga de datos
- [ ] Funciones de guardado de modelos
- [ ] Funciones auxiliares comunes

---

## Fase 2: Modelos Básicos (Pendiente)

### ⏳ Sesión 3: Regresión Logística
**Estado**: No iniciada
**Archivo**: `notebook/03-regresion-logistica.ipynb`

**Tareas**:
- [ ] Crear estructura del notebook
- [ ] Sección teórica (10 min)
- [ ] Implementación del modelo (20 min)
- [ ] Evaluación y métricas (20 min)
- [ ] Interpretación (10 min)
- [ ] Guardar modelo entrenado
- [ ] Probar en clase

---

### ⏳ Sesión 4: Árboles de Decisión
**Estado**: No iniciada
**Archivo**: `notebook/04-arboles-decision.ipynb`

**Tareas**:
- [ ] Crear estructura del notebook
- [ ] Sección teórica (15 min)
- [ ] Implementación del modelo (15 min)
- [ ] Visualización del árbol (15 min)
- [ ] Comparación con regresión logística (15 min)
- [ ] Probar en clase

---

## Fase 3: Modelos Avanzados (Pendiente)

### ⏳ Sesión 5: Random Forest
**Estado**: No iniciada
**Archivo**: `notebook/05-random-forest.ipynb`

**Tareas**:
- [ ] Crear estructura del notebook
- [ ] Explicar ensemble learning
- [ ] Implementar Random Forest
- [ ] Feature importance
- [ ] Comparar con modelos anteriores
- [ ] Probar en clase

---

### ⏳ Sesión 6: XGBoost
**Estado**: No iniciada
**Archivo**: `notebook/06-xgboost.ipynb`

**Tareas**:
- [ ] Crear estructura del notebook
- [ ] Explicar gradient boosting
- [ ] Implementar XGBoost
- [ ] Tuning básico de hiperparámetros
- [ ] Comparar con modelos anteriores
- [ ] Probar en clase

---

## Fase 4: Integración (Pendiente)

### ⏳ Sesión 7: Comparación de Modelos
**Estado**: No iniciada
**Archivo**: `notebook/07-comparacion-modelos.ipynb`

**Tareas**:
- [ ] Crear estructura del notebook
- [ ] Cargar todos los modelos
- [ ] Dashboard comparativo
- [ ] Análisis de casos difíciles
- [ ] Recomendaciones finales
- [ ] Reporte ejecutivo
- [ ] Probar en clase

---

## Estructura de Archivos Actual

```
bloque-3/
├── README.md ✅
├── PROGRESO.md ✅ (este archivo)
│
├── data/ ✅
│   ├── datos_liga_futbol.csv ✅
│   ├── generar_datos_liga.py ✅
│   └── DICCIONARIO_DATOS.md ✅
│
├── src/ ⏳ (carpeta a crear)
│   ├── __init__.py ⏳
│   ├── features.py ⏳
│   ├── evaluacion.py ⏳
│   └── utils.py ⏳
│
└── notebook/ 🟡 (1/7 notebooks)
    ├── eda.ipynb ✅ (renombrado de 01-eda.ipynb)
    ├── 02-feature-engineering.ipynb ⏳
    ├── 03-regresion-logistica.ipynb ⏳
    ├── 04-arboles-decision.ipynb ⏳
    ├── 05-random-forest.ipynb ⏳
    ├── 06-xgboost.ipynb ⏳
    └── 07-comparacion-modelos.ipynb ⏳
```

---

## Próxima Sesión de Trabajo

### 🎯 Objetivo Inmediato: Completar Fase 1

**Tarea 1**: Simplificar EDA notebook
- Tiempo estimado: 2 horas
- Reducir de 15 a 6-8 secciones
- Mantener solo lo esencial para predicción

**Tarea 2**: Crear `src/features.py`
- Tiempo estimado: 3 horas
- Implementar funciones básicas y avanzadas
- Documentar con docstrings
- Probar con dataset

**Tarea 3**: Crear notebook de feature engineering
- Tiempo estimado: 3 horas
- Explicar conceptos
- Usar funciones de `src/features.py`
- Crear train/test split

**Total estimado Fase 1**: 8 horas

---

## Registro de Cambios

### 2025-11-07
- ✅ Creado README.md con plan completo de 7 sesiones
- ✅ Creado PROGRESO.md para tracking
- ✅ EDA notebook existe (como `eda.ipynb`)
- ✅ Dataset centralizado en `data/`
- ⏳ Pendiente: Simplificar EDA
- ⏳ Pendiente: Crear módulos en `src/`

---

## Métricas de Progreso

### Notebooks
- Completados: 1/7 (14%)
- En progreso: 0/7 (0%)
- Pendientes: 6/7 (86%)

### Módulos de Código
- Completados: 0/3 (0%)
- Pendientes: 3/3 (100%)

### Fase General
- Fase 1 (Fundamentos): 25% (1/4 items)
- Fase 2 (Básicos): 0% (0/2 items)
- Fase 3 (Avanzados): 0% (0/2 items)
- Fase 4 (Integración): 0% (0/1 items)

---

## Notas y Observaciones

### Decisiones de Diseño
- **Modularidad**: Cada notebook es independiente pero usa módulos compartidos
- **Duración**: 50-60 minutos efectivos por sesión
- **Progresión**: De simple (logística) a complejo (XGBoost)
- **Comparación**: Mismas métricas y datos para todos los modelos

### Desafíos Anticipados
1. **Empates difíciles de predecir**: Es normal, ocurre en fútbol real también
2. **Balance de teoría/práctica**: Mantener teoría en 10-15 minutos máximo
3. **Tiempo de ejecución**: XGBoost puede ser lento, considerar parámetros

### Ideas Futuras
- [ ] Agregar validación cruzada en comparación final
- [ ] Considerar SMOTE para balancear clases (Empate)
- [ ] Análisis de errores más profundo
- [ ] Predicciones por equipo específico

---

**Mantener este archivo actualizado después de cada sesión de trabajo**
