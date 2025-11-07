# Diccionario de Datos - datos_liga_futbol.csv

## Descripción General

Este archivo contiene datos históricos de partidos de una liga de fútbol simulada con 8 equipos. Los datos incluyen información sobre resultados, estadísticas de equipos, y métricas predictivas utilizadas para entrenar modelos de machine learning.

**Fuente**: Generado sintéticamente mediante `generar_datos_liga.py`
**Formato**: CSV (Comma Separated Values)
**Codificación**: UTF-8
**Total de registros**: 56 partidos
**Periodo**: Temporada 1, Jornadas 1-14

---

## Estructura de Datos

### Variables de Identificación

| Campo | Tipo | Rango | Descripción |
|-------|------|-------|-------------|
| `Temporada` | int | 1 | Número de temporada de la liga |
| `Jornada` | int | 1-14 | Número de jornada (fecha) en que se jugó el partido |

### Variables de Equipos

| Campo | Tipo | Valores Únicos | Descripción |
|-------|------|----------------|-------------|
| `Equipo_Local` | str | 8 equipos | Nombre del equipo que juega en casa |
| `Equipo_Visitante` | str | 8 equipos | Nombre del equipo que juega de visitante |

**Equipos de la liga:**
1. Águilas United
2. Cóndores United
3. Halcones City
4. Leones SC
5. Lobos Atlético
6. Pumas CF
7. Tigres FC
8. Zorros FC

### Variables de Resultado

| Campo | Tipo | Valores Posibles | Descripción |
|-------|------|------------------|-------------|
| `Goles_Local` | int | 0-7 | Cantidad de goles marcados por el equipo local |
| `Goles_Visitante` | int | 0-6 | Cantidad de goles marcados por el equipo visitante |
| `Resultado` | str | Victoria Local<br>Victoria Visitante<br>Empate | Resultado final del partido desde la perspectiva del equipo local |
| `Ganador` | str | Nombre del equipo<br>"Empate" | Equipo que ganó el partido, o "Empate" si hubo empate |

**Distribución de resultados (típica):**
- Victorias Locales: ~21-24 partidos (38-42%)
- Empates: ~14 partidos (25%)
- Victorias Visitantes: ~18-21 partidos (33-37%)

### Variables Contextuales

| Campo | Tipo | Valores | Descripción |
|-------|------|---------|-------------|
| `Juega_En_Casa` | bool | True/False | Indica si el registro representa al equipo local (siempre True en este dataset) |

### Variables Predictivas

| Campo | Tipo | Rango | Media | Desv. Est. | Descripción |
|-------|------|-------|-------|------------|-------------|
| `Probabilidad_Victoria_Local` | float | 0.13 - 0.95 | ~0.55 | ~0.20 | Probabilidad calculada de victoria del equipo local basada en modelo interno |
| `Habilidad_Local` | int | 60-85 | ~73 | ~8.9 | Nivel de habilidad del equipo local (escala 0-100) |
| `Habilidad_Visitante` | int | 60-85 | ~73 | ~8.9 | Nivel de habilidad del equipo visitante (escala 0-100) |
| `Racha_Local` | int | 0-5 | ~0.79 | ~1.28 | Número de victorias consecutivas del equipo local antes de este partido |
| `Racha_Visitante` | int | 0-6 | ~0.79 | ~1.28 | Número de victorias consecutivas del equipo visitante antes de este partido |

---

## Notas Metodológicas

### Habilidad de Equipos

Los valores de habilidad representan la fuerza relativa de cada equipo en una escala de 0 a 100:

**Distribución de habilidades:**
1. **Tigres FC: 85** - Equipo más fuerte (analizado en detalle en Semana 12)
2. Águilas United: 82 - Equipo fuerte
3. Leones SC: 78 - Equipo medio-fuerte
4. Halcones City: 75 - Equipo medio
5. Lobos Atlético: 72 - Equipo medio
6. Pumas CF: 68 - Equipo medio-débil
7. Zorros FC: 65 - Equipo débil
8. Cóndores United: 60 - Equipo más débil

**Rango**: 60-85 puntos (diferencia máxima: 25 puntos)

La diferencia de habilidad entre equipos (`Habilidad_Local - Habilidad_Visitante`) varía de -25 a +25 puntos.

**Conexión con Semana 12:** El Tigres FC, como el equipo más fuerte de la liga, es analizado a nivel de jugadores individuales en la Semana 12, donde se estudian datos de 100 jugadores históricos del equipo.

### Rachas de Victoria

- Una racha se cuenta como el número de victorias consecutivas antes del partido actual
- Valor 0 indica que el equipo no tiene racha activa
- Las rachas influyen en el rendimiento del equipo y son un factor predictivo
- En este dataset, ~17.9% de los partidos involucran equipos con racha de 2+ victorias

### Probabilidad de Victoria

La `Probabilidad_Victoria_Local` es generada por el algoritmo de simulación y representa:
- Una estimación basada en habilidad, ventaja de casa, y rachas
- No es una predicción de modelo de ML, sino una probabilidad teórica del generador
- Útil para validar modelos predictivos comparando con probabilidades reales

---

## Variables Derivadas (Usadas en Modelado)

Estas variables no están en el CSV original pero se calculan en el notebook para machine learning:

| Variable Derivada | Fórmula | Descripción |
|-------------------|---------|-------------|
| `Juega_Casa_Numerico` | Siempre 1 | Versión numérica de que el equipo juega en casa |
| `Diferencia_Habilidad` | `Habilidad_Local - Habilidad_Visitante` | Diferencia de habilidad entre equipos |
| `Tiene_Racha` | `Racha_Local >= 2` | Variable binaria: 1 si tiene racha significativa, 0 si no |
| `Gana_Local` | `Resultado == 'Victoria Local'` | Variable objetivo: 1 si ganó el local, 0 si no |

---

## Casos de Uso

Este dataset está diseñado para:

1. **Introducción a Machine Learning**
   - Clasificación multi-clase (victoria local, empate, victoria visitante)
   - Clasificación binaria (ganador vs no-ganador)
   - Regresión logística multinomial
   - Evaluación de modelos con métricas básicas

2. **Análisis Exploratorio de Datos**
   - Ventaja de jugar en casa
   - Correlación entre habilidad y resultados
   - Impacto de rachas en rendimiento
   - Análisis de distribución de empates

3. **Visualización de Datos Deportivos**
   - Distribución de goles
   - Comparación de equipos
   - Patrones temporales por jornada
   - Frecuencia de empates por marcador (0-0, 1-1, 2-2, etc.)

4. **Ingeniería de Características**
   - Transformación de variables categóricas
   - Creación de variables numéricas
   - Normalización de datos

---

## Limitaciones y Consideraciones

1. **Datos Simulados**: Los datos son generados sintéticamente y no representan una liga real
2. **Problema Multi-clase**: El dataset incluye tres resultados posibles (victoria local, empate, victoria visitante), lo que lo hace apropiado para clasificación multi-clase
3. **Distribución Realista**: Los empates representan aproximadamente 25% de los partidos, similar a ligas de fútbol reales
4. **Tamaño del Dataset**: 56 partidos es un dataset pequeño para ML, apropiado solo para fines educativos
5. **Variables Contextuales**: Faltan variables reales como clima, lesiones, o cambios de entrenador

---

## Ejemplo de Registro

```csv
Temporada,Jornada,Equipo_Local,Equipo_Visitante,Goles_Local,Goles_Visitante,Resultado,Ganador,Juega_En_Casa,Probabilidad_Victoria_Local,Habilidad_Local,Habilidad_Visitante,Racha_Local,Racha_Visitante
1,1,Tigres FC,Águilas United,3,2,Victoria Local,Tigres FC,True,0.576,85,82,0,0
```

**Interpretación:**
- En la Jornada 1, Tigres FC (local) venció a Águilas United (visitante) 3-2
- Tigres FC tenía 85 de habilidad vs 82 de Águilas United
- Ningún equipo tenía racha activa (ambos en 0)
- La probabilidad calculada de victoria local era 57.6%
- El resultado coincidió con la predicción (victoria local)

---

## Información de Contacto y Licencia

**Proyecto**: PS5005 Programación Básica 1 - Ciencia de Datos Aplicada al Fútbol
**Institución**: Prepa Tec
**Propósito**: Educativo - Enseñanza de fundamentos de machine learning
**Licencia**: Uso educativo

Para regenerar o modificar los datos, consultar el script `generar_datos_liga.py`.
