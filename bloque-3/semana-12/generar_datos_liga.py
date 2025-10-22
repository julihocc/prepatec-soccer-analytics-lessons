"""
Script de Generación de Datos Sintéticos - FC Barcelona
========================================================

Este script genera un dataset sintético de jugadores del FC Barcelona
con estadísticas realistas de una temporada de fútbol.

Autor: Equipo de Ciencia de Datos - Prepa Tec
Versión: 1.0
Fecha: 2025

Uso:
----
    python generar_datos_liga.py

Salida:
-------
    datos_barcelona.csv - Dataset con 15 jugadores y sus estadísticas
"""

import pandas as pd
import numpy as np


def generar_datos_jugadores_barcelona(num_jugadores=15, semilla_aleatoria=42):
    """
    Genera un dataset sintético de jugadores del Barcelona con estadísticas realistas.

    Parámetros:
    -----------
    num_jugadores : int
        Número de jugadores a generar (default: 15)
    semilla_aleatoria : int
        Semilla para reproducibilidad de resultados (default: 42)

    Retorna:
    --------
    pd.DataFrame
        DataFrame con columnas: Jugador, Goles_Temporada, Minutos_Jugados,
        Edad, Es_Titular

    Lógica de Generación:
    ---------------------
    1. Goles: Distribución exponencial (mayoría marca poco, pocos marcan mucho)
       - Rango: 0-15 goles
       - Realista para diferentes posiciones (defensas vs delanteros)

    2. Minutos: Distribución uniforme entre 400 y 2200
       - 400 minutos = suplente poco usado (~4 partidos completos)
       - 2200 minutos = titular indiscutible (~24 partidos completos)

    3. Edad: Distribución normal centrada en 25 años
       - Rango: 18-35 años
       - Refleja composición típica de plantilla profesional

    4. Es_Titular: Calculado mediante score ponderado
       - Score = 60% * minutos_normalizados + 40% * goles_normalizados
       - Umbral ajustado para tener ~60% de titulares
       - Refleja que minutos jugados es mejor predictor que goles
    """

    # Establecemos semilla para reproducibilidad
    np.random.seed(semilla_aleatoria)

    # Generamos nombres de jugadores usando prefijos realistas
    prefijos = ["Jugador", "Delantero", "Mediocampista", "Defensa", "Portero"]
    nombres_jugadores = [
        f"{np.random.choice(prefijos)}_{i+1}"
        for i in range(num_jugadores)
    ]

    # Generamos goles con distribución exponencial
    # La mayoría tendrá 0-3 goles, algunos 4-8, muy pocos más de 10
    goles_temporada = np.random.exponential(scale=2, size=num_jugadores)
    goles_temporada = np.clip(goles_temporada, 0, 15).astype(int)

    # Generamos minutos jugados con distribución uniforme
    # Simula desde suplentes ocasionales hasta titulares absolutos
    minutos_jugados = np.random.uniform(400, 2200, size=num_jugadores).astype(int)

    # Generamos edades con distribución normal centrada en 25 años
    edades = np.random.normal(loc=25, scale=5, size=num_jugadores)
    edades = np.clip(edades, 18, 35).astype(int)

    # Determinamos quién es titular basándonos en goles y minutos
    # Normalizamos las variables para combinarlas en un "score de titular"
    goles_norm = goles_temporada / goles_temporada.max() if goles_temporada.max() > 0 else goles_temporada
    minutos_norm = minutos_jugados / minutos_jugados.max()

    # Score combinado: 60% peso a minutos (más importante), 40% a goles
    score_titular = 0.6 * minutos_norm + 0.4 * goles_norm

    # Los jugadores con score > umbral son titulares
    # Ajustamos umbral para tener ~60% titulares (proporción realista)
    umbral = np.percentile(score_titular, 40)  # 60% están por encima
    es_titular = (score_titular > umbral).astype(int)

    # Creamos el DataFrame
    datos = pd.DataFrame({
        "Jugador": nombres_jugadores,
        "Goles_Temporada": goles_temporada,
        "Minutos_Jugados": minutos_jugados,
        "Edad": edades,
        "Es_Titular": es_titular
    })

    # Ordenamos por minutos jugados (descendente) para que parezca más realista
    datos = datos.sort_values("Minutos_Jugados", ascending=False).reset_index(drop=True)

    return datos


def main():
    """
    Función principal que genera y guarda el dataset.
    """
    print("="*70)
    print("Generador de Datos Sintéticos - FC Barcelona")
    print("="*70)
    print()

    # Generamos el dataset
    print("Generando dataset de 15 jugadores...")
    datos_barcelona = generar_datos_jugadores_barcelona(num_jugadores=15)

    # Mostramos resumen del dataset generado
    print("\nResumen del dataset generado:")
    print(f"  - Total de jugadores: {len(datos_barcelona)}")
    print(f"  - Titulares: {datos_barcelona['Es_Titular'].sum()}")
    print(f"  - Suplentes: {len(datos_barcelona) - datos_barcelona['Es_Titular'].sum()}")
    print(f"  - Goles (promedio): {datos_barcelona['Goles_Temporada'].mean():.1f}")
    print(f"  - Minutos (promedio): {datos_barcelona['Minutos_Jugados'].mean():.0f}")
    print(f"  - Edad (promedio): {datos_barcelona['Edad'].mean():.1f} años")

    # Guardamos el dataset como CSV
    nombre_archivo = "datos_barcelona.csv"
    datos_barcelona.to_csv(nombre_archivo, index=False, encoding='utf-8')
    print(f"\nDataset guardado exitosamente en: {nombre_archivo}")

    # Mostramos preview de los primeros 5 jugadores
    print("\nPreview de los primeros 5 jugadores:")
    print(datos_barcelona.head().to_string(index=False))

    print("\n" + "="*70)
    print("Proceso completado exitosamente")
    print("="*70)


if __name__ == "__main__":
    main()
