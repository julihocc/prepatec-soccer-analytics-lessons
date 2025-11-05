"""
Script para generar datos sintéticos de evaluación de jugadores del Tigres FC.

Este script genera un dataset de 15 jugadores del Tigres FC con sus predicciones
de titularidad y la realidad del partido, diseñado específicamente para enseñar
métricas avanzadas de evaluación de modelos de clasificación.

Autor: Equipo PS5005
Fecha: Octubre 2025
Contexto: Semana 13 - Métricas Avanzadas de Evaluación
"""

import pandas as pd
import numpy as np

# Configuramos la semilla para reproducibilidad
np.random.seed(42)


def generar_datos_evaluacion_tigres():
    """
    Genera datos sintéticos de evaluación para el Tigres FC.

    El dataset está diseñado para producir métricas específicas:
    - 9 Verdaderos Positivos (TP)
    - 4 Verdaderos Negativos (TN)
    - 1 Falso Positivo (FP)
    - 1 Falso Negativo (FN)

    Esto resulta en:
    - Accuracy: 86.7% (13/15)
    - Precision: 90.0% (9/10)
    - Recall: 90.0% (9/10)

    Returns:
        pd.DataFrame: Dataset con 15 jugadores y sus características
    """

    # Lista de jugadores del Tigres FC (nombres ficticios)
    jugadores = [
        "Rodriguez G",      # TP
        "Martinez L",       # TP
        "Hernandez C",      # TP
        "Garcia M",         # TP
        "Lopez R",          # FN - Predijo suplente, fue titular
        "Sanchez J",        # TP
        "Gonzalez A",       # TP
        "Perez D",          # TP
        "Torres F",         # TP
        "Ramirez E",        # TP
        "Flores H",         # FP - Predijo titular, fue suplente
        "Morales P",        # TN
        "Castro S",         # TN
        "Ortiz V",          # TN
        "Mendoza I",        # TN
    ]

    # Predicciones del modelo (1 = Titular, 0 = Suplente)
    # El modelo predijo 10 titulares y 5 suplentes
    predicciones_modelo = [
        1, 1, 1, 1, 0,  # Rodriguez, Martinez, Hernandez, Garcia, Lopez (Lopez=FN)
        1, 1, 1, 1, 1,  # Sanchez, Gonzalez, Perez, Torres, Ramirez
        1, 0, 0, 0, 0   # Flores (FP), Morales, Castro, Ortiz, Mendoza
    ]

    # Realidad del partido (1 = Titular, 0 = Suplente)
    # En realidad fueron 10 titulares y 5 suplentes
    realidad_partido = [
        1, 1, 1, 1, 1,  # Rodriguez, Martinez, Hernandez, Garcia, Lopez (Lopez=FN)
        1, 1, 1, 1, 1,  # Sanchez, Gonzalez, Perez, Torres, Ramirez
        0, 0, 0, 0, 0   # Flores (FP), Morales, Castro, Ortiz, Mendoza
    ]

    # Generamos características adicionales para contexto realista
    # Estas características son coherentes con el estado de titular/suplente

    goles_por_partido = []
    minutos_jugados = []
    edad = []

    for i, (pred, real) in enumerate(zip(predicciones_modelo, realidad_partido)):
        # Si es titular real, estadísticas más altas
        if real == 1:
            goles_base = np.random.uniform(0.3, 0.8)
            minutos_base = np.random.uniform(70, 90)
            edad_base = np.random.randint(24, 30)
        else:
            goles_base = np.random.uniform(0.0, 0.3)
            minutos_base = np.random.uniform(20, 50)
            edad_base = np.random.randint(20, 35)

        goles_por_partido.append(round(goles_base, 2))
        minutos_jugados.append(int(minutos_base))
        edad.append(edad_base)

    # Creamos el DataFrame
    datos = pd.DataFrame({
        'jugador': jugadores,
        'goles_por_partido': goles_por_partido,
        'minutos_promedio': minutos_jugados,
        'edad': edad,
        'prediccion_modelo': predicciones_modelo,
        'titular_real': realidad_partido,
        'prediccion_texto': ['Titular' if x == 1 else 'Suplente' for x in predicciones_modelo],
        'realidad_texto': ['Titular' if x == 1 else 'Suplente' for x in realidad_partido]
    })

    # Agregamos una columna de tipo de resultado para análisis
    def clasificar_resultado(pred, real):
        if pred == 1 and real == 1:
            return 'TP'  # Verdadero Positivo
        elif pred == 0 and real == 0:
            return 'TN'  # Verdadero Negativo
        elif pred == 1 and real == 0:
            return 'FP'  # Falso Positivo
        elif pred == 0 and real == 1:
            return 'FN'  # Falso Negativo

    datos['tipo_resultado'] = datos.apply(
        lambda row: clasificar_resultado(row['prediccion_modelo'], row['titular_real']),
        axis=1
    )

    return datos


def guardar_datos(datos, nombre_archivo='datos_evaluacion_tigres_fc.csv'):
    """
    Guarda el DataFrame en un archivo CSV.

    Args:
        datos (pd.DataFrame): Dataset a guardar
        nombre_archivo (str): Nombre del archivo CSV
    """
    datos.to_csv(nombre_archivo, index=False, encoding='utf-8')
    print(f"Datos guardados exitosamente en: {nombre_archivo}")
    print(f"Total de registros: {len(datos)}")


def mostrar_estadisticas(datos):
    """
    Muestra estadísticas descriptivas del dataset generado.

    Args:
        datos (pd.DataFrame): Dataset a analizar
    """
    print("\n" + "="*70)
    print("ESTADÍSTICAS DEL DATASET GENERADO")
    print("="*70)

    # Conteo de predicciones
    print("\nPredicciones del modelo:")
    print(f"  Titulares predichos: {datos['prediccion_modelo'].sum()}")
    print(f"  Suplentes predichos: {len(datos) - datos['prediccion_modelo'].sum()}")

    # Conteo de realidad
    print("\nRealidad del partido:")
    print(f"  Titulares reales: {datos['titular_real'].sum()}")
    print(f"  Suplentes reales: {len(datos) - datos['titular_real'].sum()}")

    # Conteo de resultados
    print("\nTipos de resultados:")
    conteo_resultados = datos['tipo_resultado'].value_counts()
    for tipo in ['TP', 'TN', 'FP', 'FN']:
        if tipo in conteo_resultados:
            print(f"  {tipo}: {conteo_resultados[tipo]}")
        else:
            print(f"  {tipo}: 0")

    # Cálculo de métricas
    tp = len(datos[datos['tipo_resultado'] == 'TP'])
    tn = len(datos[datos['tipo_resultado'] == 'TN'])
    fp = len(datos[datos['tipo_resultado'] == 'FP'])
    fn = len(datos[datos['tipo_resultado'] == 'FN'])

    accuracy = (tp + tn) / len(datos) * 100
    precision = tp / (tp + fp) * 100 if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) * 100 if (tp + fn) > 0 else 0

    print("\nMétricas esperadas:")
    print(f"  Accuracy: {accuracy:.1f}%")
    print(f"  Precision: {precision:.1f}%")
    print(f"  Recall: {recall:.1f}%")

    # Estadísticas de características
    print("\nEstadísticas de características:")
    print(f"  Goles por partido (promedio): {datos['goles_por_partido'].mean():.2f}")
    print(f"  Minutos promedio: {datos['minutos_promedio'].mean():.1f}")
    print(f"  Edad promedio: {datos['edad'].mean():.1f}")

    print("\n" + "="*70)


def main():
    """Función principal que ejecuta la generación de datos."""
    print("Generando datos sintéticos de evaluación para el Tigres FC...")
    print("Contexto: Semana 13 - Métricas Avanzadas de Evaluación")
    print()

    # Generar datos
    datos = generar_datos_evaluacion_tigres()

    # Mostrar estadísticas
    mostrar_estadisticas(datos)

    # Guardar datos
    guardar_datos(datos)

    # Mostrar primeras filas
    print("\nPrimeras 5 filas del dataset:")
    print(datos.head())

    print("\nDatos generados exitosamente!")


if __name__ == "__main__":
    main()
