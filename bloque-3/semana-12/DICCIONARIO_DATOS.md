# Diccionario de Datos - datos_tigres_fc.csv

## Descripción General

Este archivo contiene datos históricos de jugadores del Tigres FC, el equipo más fuerte de la liga ficticia presentada en la Semana 11 (85 puntos de habilidad). Los datos incluyen estadísticas individuales de rendimiento de 100 jugadores a lo largo de 3 temporadas, utilizados para entrenar modelos de clasificación que predicen si un jugador debería ser titular o suplente.

**Fuente**: Generado sintéticamente mediante `generar_datos_liga.py`
**Formato**: CSV (Comma Separated Values)
**Codificación**: UTF-8
**Total de registros**: 100 jugadores
**Periodo**: Temporadas 2021-22, 2022-23, 2023-24
**Contexto**: Dataset del equipo más fuerte de la liga ficticia (Semana 11)

---

## Estructura de Datos

### Variables de Identificación

| Campo | Tipo | Formato | Descripción |
|-------|------|---------|-------------|
| `Jugador` | str | Posicion_Temporada_ID | Identificador único del jugador con formato: "Posicion_Temporada_NumeroAleatorio" |

**Ejemplos de identificadores:**
- `Defensa_Central_2023-24_39`
- `Delantero_Centro_2022-23_32`
- `Mediocampista_Ofensivo_2021-22_100`

**Posiciones incluidas** (10 tipos):
1. Portero
2. Defensa Central
3. Lateral Derecho
4. Lateral Izquierdo
5. Mediocampista Defensivo
6. Mediocampista Centro
7. Mediocampista Ofensivo
8. Extremo Derecho
9. Extremo Izquierdo
10. Delantero Centro

**Temporadas incluidas**: 2021-22, 2022-23, 2023-24

---

### Variables Estadísticas (Features)

| Campo | Tipo | Rango | Media | Mediana | Descripción |
|-------|------|-------|-------|---------|-------------|
| `Goles_Temporada` | int | 0-11 | ~2.0 | 1 | Número de goles marcados por el jugador durante la temporada |
| `Minutos_Jugados` | int | 400-2200 | ~1162 | ~1140 | Minutos totales jugados por el jugador durante la temporada |
| `Edad` | int | 18-35 | ~25.0 | 25 | Edad del jugador en años |

**Distribución de Goles** (Exponencial):
- 0-3 goles: ~75% de los jugadores (típico de defensas y mediocampistas)
- 4-7 goles: ~20% de los jugadores (mediocampistas ofensivos y extremos)
- 8-11 goles: ~5% de los jugadores (delanteros destacados)

**Distribución de Minutos** (Uniforme):
- 400-1000 minutos: Suplentes (~40% del dataset)
- 1000-1600 minutos: Jugadores rotación (~30% del dataset)
- 1600-2200 minutos: Titulares habituales (~30% del dataset)

**Distribución de Edad** (Normal):
- Media: 25 años (edad típica de jugador profesional)
- Desviación estándar: ~5 años
- Rango realista: 18-35 años

---

### Variable Objetivo (Target)

| Campo | Tipo | Valores | Distribución | Descripción |
|-------|------|---------|--------------|-------------|
| `Es_Titular` | int | 0, 1 | 60% titulares (1)<br>40% suplentes (0) | Variable binaria que indica si el jugador es considerado titular |

**Valores:**
- `1`: Titular (jugador que normalmente inicia los partidos)
- `0`: Suplente (jugador de rotación o banca)

**Distribución típica:**
- Titulares: ~60 jugadores (60%)
- Suplentes: ~40 jugadores (40%)

**Criterio de clasificación:**
La variable `Es_Titular` se calcula mediante un score ponderado:
```
Score = 0.60 × (Minutos_Normalizados) + 0.40 × (Goles_Normalizados)
Es_Titular = 1 si Score >= 0.6, 0 en caso contrario
```

Este criterio refleja que:
- Los minutos jugados son el factor más importante (60%)
- Los goles son un factor secundario importante (40%)
- Jugadores con >1400 minutos casi siempre son titulares
- Jugadores con <800 minutos casi nunca son titulares

---

## Notas Metodológicas

### Realismo Estadístico

Los datos sintéticos están diseñados para reflejar patrones reales del fútbol profesional:

**1. Distribución de Goles (Exponencial)**
- La mayoría de jugadores marcan pocos goles (0-3)
- Solo unos pocos delanteros marcan muchos goles (8+)
- Refleja la realidad: defensas y porteros raramente marcan

**2. Distribución de Minutos (Uniforme)**
- Variedad desde suplentes (400 min) hasta titulares absolutos (2200 min)
- Permite al modelo aprender el espectro completo de participación
- Simula rotaciones realistas de plantilla

**3. Distribución de Edad (Normal)**
- Centrada en 25 años (edad pico de rendimiento)
- Incluye jóvenes promesas (18-22) y veteranos (30-35)
- Refleja composición típica de plantillas profesionales

**4. Relación Minutos-Titularidad**
- Correlación fuerte pero no perfecta (r ≈ 0.85)
- Permite casos especiales (ej: jugador joven con pocos minutos pero alto potencial)
- Introduce variabilidad realista en las decisiones técnicas

---

## Conexión con la Liga Ficticia (Semana 11)

Este dataset representa un análisis **micro** (jugadores individuales) del equipo analizado en **macro** (nivel de liga) en la Semana 11:

**Contexto de la liga:**
- **Tigres FC**: 85/100 puntos de habilidad
- **Posición**: Equipo más fuerte de la liga de 8 equipos
- **Competidores**: Águilas United (82), Leones SC (78), Halcones City (75), etc.

**Progresión narrativa:**
1. **Semana 11**: Análisis de 56 partidos de la liga → Identificación del Tigres FC como el más fuerte
2. **Semana 12**: Análisis de 100 jugadores del Tigres FC → Predicción de titulares mediante ensemble learning

Esta conexión permite a los estudiantes entender cómo el análisis de datos opera a diferentes niveles (liga completa vs equipo individual).

---

## Casos de Uso

Este dataset está diseñado para:

### 1. Clasificación Binaria
- **Objetivo**: Predecir si un jugador es titular (1) o suplente (0)
- **Algoritmos sugeridos**: Regresión Logística, Random Forest, SVM
- **Métricas**: Accuracy, Precision, Recall, F1-Score

### 2. Ensemble Learning (Módulo Principal)
- **Técnica**: Votación por mayoría de múltiples modelos
- **Ventaja**: Combinar predicciones de diferentes algoritmos
- **Aplicación**: Sistema robusto de selección de titulares

### 3. Análisis Exploratorio de Datos
- Correlación entre goles y minutos jugados
- Distribución de edades por posición
- Patrones de titularidad por temporada
- Análisis de rendimiento por posición

### 4. Ingeniería de Características (Semana 14)
- Transformación de posiciones (encoding)
- Creación de variables derivadas (goles_por_minuto)
- Normalización y estandarización
- Feature importance analysis

---

## Variables Derivadas (Usadas en Análisis Avanzados)

Estas variables no están en el CSV original pero pueden calcularse para análisis posteriores:

| Variable Derivada | Fórmula | Uso |
|-------------------|---------|-----|
| `Goles_Por_90min` | `(Goles_Temporada / Minutos_Jugados) × 90` | Normalizar rendimiento goleador |
| `Minutos_Normalizados` | `Minutos_Jugados / 2200` | Escalar minutos a rango [0,1] |
| `Categoria_Edad` | `"Joven" (18-23), "Prime" (24-29), "Veterano" (30+)` | Análisis por grupo etario |
| `Es_Goleador` | `Goles_Temporada >= 5` | Identificar jugadores ofensivos destacados |
| `Participacion_Alta` | `Minutos_Jugados >= 1500` | Jugadores con alta carga de minutos |

---

## Train/Test Split Recomendado

Para evaluación robusta de modelos:

**División estándar (usada en el notebook):**
- **Train set**: 70% (~70 jugadores)
- **Test set**: 30% (~30 jugadores)
- **Random state**: 42 (reproducibilidad)

**Ventajas de 100 registros:**
- Test set de 30 casos es estadísticamente significativo
- Cada error en test = ~3.3% de impacto (vs 20% con 5 casos)
- Permite entrenar modelos más generalizables
- Suficiente para validar ensemble learning

**Consideración importante:**
Aunque 100 registros es pequeño para producción, es apropiado para:
- Fines educativos e introducción a ML
- Demostración de conceptos de ensemble learning
- Comparación de algoritmos básicos
- Entrenamiento de modelos lineales simples

---

## Limitaciones y Consideraciones

### Limitaciones Técnicas

1. **Datos Sintéticos**: No representan jugadores reales del Tigres FC
2. **Tamaño Moderado**: 100 registros es suficiente para educación, insuficiente para producción
3. **Variables Limitadas**: Solo 3 features (goles, minutos, edad)
4. **Sin Variables Contextuales**: Falta información de lesiones, forma física, táctica del equipo
5. **Simplificación**: El criterio de titularidad real es mucho más complejo

### Limitaciones del Modelo

**Variables NO consideradas** (importantes en la realidad):
- Rendimiento táctico y posicional
- Química con compañeros de equipo
- Estado físico y lesiones
- Análisis de video y métricas avanzadas
- Consideraciones estratégicas del entrenador

### Consideraciones Éticas

1. **Automatización de Decisiones Humanas**:
   - Un modelo NO debe reemplazar completamente el juicio del entrenador
   - Los jugadores son personas, no solo estadísticas
   - Factores humanos (liderazgo, mentalidad) son cruciales

2. **Sesgo en los Datos**:
   - El modelo aprende de datos históricos (puede perpetuar sesgos)
   - Jugadores jóvenes pueden estar subrepresentados
   - No captura potencial futuro o desarrollo

3. **Uso Responsable**:
   - Usar como herramienta de apoyo, no decisión final
   - Combinar con análisis cualitativo
   - Mantener transparencia con jugadores

---

## Ejemplo de Registro

```csv
Jugador,Goles_Temporada,Minutos_Jugados,Edad,Es_Titular
Delantero_Centro_2022-23_32,2,1995,24,1
```

**Interpretación:**
- **Jugador**: Delantero Centro de la temporada 2022-23 (ID: 32)
- **Goles**: 2 goles en la temporada (rendimiento moderado para delantero)
- **Minutos**: 1995 minutos jugados (alta participación, casi 22 partidos completos)
- **Edad**: 24 años (edad pico de rendimiento)
- **Clasificación**: Titular (1) - justificado por alta participación en minutos

**Por qué es titular:**
```
Score = 0.60 × (1995/2200) + 0.40 × (2/11)
Score = 0.60 × 0.907 + 0.40 × 0.182
Score = 0.544 + 0.073 = 0.617 ≥ 0.6 → Titular
```

---

## Comparación con Dataset de Liga (Semana 11)

| Aspecto | Semana 11 (Liga) | Semana 12 (Jugadores) |
|---------|------------------|------------------------|
| **Nivel de análisis** | Macro (equipos) | Micro (individuos) |
| **Unidad de observación** | Partidos (56) | Jugadores (100) |
| **Variables clave** | Resultado, Habilidad equipo, Racha | Goles, Minutos, Edad |
| **Objetivo** | Predecir ganador de partido | Predecir titular vs suplente |
| **Técnica ML** | Regresión Logística simple | Ensemble Learning (votación) |
| **Contexto** | Liga completa de 8 equipos | Tigres FC (equipo más fuerte) |

**Conexión narrativa:**
El análisis de Semana 11 identifica al Tigres FC como el equipo más exitoso (85/100). La Semana 12 profundiza en este equipo, analizando qué hace a sus jugadores titulares, complementando el análisis macro con insights micro.

---

## Información de Contacto y Licencia

**Proyecto**: PS5005 Programación Básica 1 - Ciencia de Datos Aplicada al Fútbol
**Bloque**: 3 - Modelado Predictivo
**Semana**: 12 - Modelos Avanzados de Clasificación
**Institución**: Prepa Tec
**Propósito**: Educativo - Enseñanza de ensemble learning y clasificación binaria
**Licencia**: Uso educativo

Para regenerar o modificar los datos, consultar el script `generar_datos_liga.py` en el mismo directorio.

---

**Última actualización**: Octubre 2025
**Versión**: 1.0
**Autor**: Equipo de Ciencia de Datos - Prepa Tec
