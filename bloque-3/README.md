# Bloque 3: Modelado Predictivo y Machine Learning

## Descripción General

El Bloque 3 introduce a los estudiantes de preparatoria al mundo del modelado predictivo y machine learning mediante el contexto del fútbol. A lo largo de 6 semanas (Semanas 10-15), los estudiantes aprenden desde conceptos básicos de estadística descriptiva hasta la construcción de modelos predictivos complejos, utilizando una **narrativa unificada** basada en una liga de fútbol ficticia.

**Público objetivo**: Estudiantes de preparatoria (15-18 años) sin experiencia previa en machine learning
**Duración**: 6 semanas (50 minutos por sesión)
**Enfoque pedagógico**: Metodología Socrática con analogías del fútbol
**Herramientas**: Python, pandas, numpy, matplotlib, seaborn, scikit-learn

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

## Progresión Pedagógica por Semanas

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
