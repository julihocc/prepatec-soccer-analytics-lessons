# Progreso del Bloque 3: Modelado Predictivo

**Última actualización**: Noviembre 2025
**Objetivo**: Crear 6 sesiones de 1 hora con notebooks autocontenidos
**Enfoque**: SIMPLE - Todo inline, sin módulos externos

---

## Estado General

```
Progreso: ███░░░░░░░░░░░░░░░░░ 17% (1/6 sesiones)
```

| Sesión | Notebook | Estado | Prioridad |
|--------|----------|--------|-----------|
| 1. EDA | `01-eda.ipynb` | ✅ Existe (simplificar) | Alta |
| 2. Regresión Logística | `02-regresion-logistica.ipynb` | ⏳ Pendiente | Alta |
| 3. Árboles Decisión | `03-arboles-decision.ipynb` | ⏳ Pendiente | Media |
| 4. Random Forest | `04-random-forest.ipynb` | ⏳ Pendiente | Media |
| 5. XGBoost | `05-xgboost.ipynb` | ⏳ Pendiente | Media |
| 6. Comparación | `06-comparacion-modelos.ipynb` | ⏳ Pendiente | Baja |

---

## Detalle por Sesión

### ✅ Sesión 1: EDA
**Archivo**: `notebook/eda.ipynb` (renombrar a `01-eda.ipynb`)
**Estado**: Existe pero debe simplificarse

**Completado**:
- [x] Notebook creado
- [x] Dataset disponible: `data/datos_liga_futbol.csv`
- [x] Diccionario de datos: `data/DICCIONARIO_DATOS.md`

**Pendiente**:
- [ ] Simplificar de 15 a 6-8 secciones
- [ ] Mantener solo lo esencial:
  - Carga e inspección
  - Calidad de datos
  - Análisis de resultados
  - Análisis de goles
  - Ventaja local
  - Correlaciones
  - Resumen ejecutivo
- [ ] Probar en clase (60 minutos)

---

### ⏳ Sesión 2: Regresión Logística
**Archivo**: `notebook/02-regresion-logistica.ipynb`
**Estado**: No iniciada
**Prioridad**: Alta (siguiente tarea)

**Tareas**:
- [ ] Crear notebook autocontenido
- [ ] Feature engineering inline (15 min)
- [ ] Regresión logística (15 min)
- [ ] Evaluación y métricas (20 min)
- [ ] Guardar métricas para comparación (10 min)

**Contenido clave**:
- Crear features: Diferencia_Habilidad, Diferencia_Racha, Ratio_Habilidad
- Train/test split (80/20, random_state=42)
- LogisticRegression de sklearn
- Matriz de confusión, accuracy

---

### ⏳ Sesión 3: Árboles de Decisión
**Archivo**: `notebook/03-arboles-decision.ipynb`
**Estado**: No iniciada

**Tareas**:
- [ ] Crear notebook autocontenido
- [ ] Mismo preprocesamiento que Sesión 2
- [ ] DecisionTreeClassifier
- [ ] Visualización del árbol
- [ ] Comparar con regresión logística

---

### ⏳ Sesión 4: Random Forest
**Archivo**: `notebook/04-random-forest.ipynb`
**Estado**: No iniciada

**Tareas**:
- [ ] Crear notebook autocontenido
- [ ] RandomForestClassifier
- [ ] Feature importance
- [ ] Comparar con 2 modelos anteriores

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

**Notebooks**: 1/6 completados (17%)
**Estimado para completar**: 14 horas (~2 semanas)

---

## Decisiones de Diseño

- ✅ **Notebooks autocontenidos**: Sin módulos externos, todo inline
- ✅ **Simplicidad**: Copiar/pegar código entre notebooks es OK (más didáctico)
- ✅ **Duración**: 60 minutos por sesión
- ✅ **Progresión**: De simple (logística) a complejo (XGBoost)
- ✅ **Consistencia**: Mismo train/test split (random_state=42) en todos

---

**Actualizar este archivo después de cada sesión**
