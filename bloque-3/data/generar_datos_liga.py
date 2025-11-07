"""
Generador de Datos Sintéticos de Liga de Fútbol
=================================================

Este script genera datos realistas de una liga de fútbol ficticia
para usar en el curso de modelado predictivo.

Características de los datos generados:
- Liga de 8 equipos con diferentes niveles de habilidad
- Efectos realistas: ventaja de jugar en casa, racha de victorias
- Múltiples temporadas con consistencia estadística
- Datos de partidos individuales y estadísticas agregadas

Uso:
    from generar_datos_liga import generar_liga_futbol

    # Generar datos de una temporada (56 partidos)
    datos = generar_liga_futbol(semilla=42)

    # Generar múltiples temporadas
    datos = generar_liga_futbol(temporadas=3, semilla=42)
"""

import pandas as pd
import numpy as np
from typing import List, Dict, Optional


class GeneradorLigaFutbol:
    """Generador de datos sintéticos de liga de fútbol con características realistas."""

    def __init__(self, semilla: Optional[int] = None):
        """
        Inicializa el generador.

        Args:
            semilla: Semilla para reproducibilidad de los datos aleatorios
        """
        if semilla is not None:
            np.random.seed(semilla)

        # Equipos de la liga ficticia con niveles de habilidad realistas
        self.equipos = {
            "Tigres FC": 85,           # Equipo muy fuerte
            "Águilas United": 82,      # Equipo fuerte
            "Leones SC": 78,           # Equipo medio-fuerte
            "Halcones City": 75,       # Equipo medio
            "Lobos Atlético": 72,      # Equipo medio
            "Pumas CF": 68,            # Equipo medio-débil
            "Zorros FC": 65,           # Equipo débil
            "Cóndores United": 60      # Equipo muy débil
        }

        # Factores que afectan los resultados
        self.ventaja_local = 0.15      # 15% más de probabilidad de ganar en casa
        self.efecto_racha = 0.10       # 10% bonus por cada victoria consecutiva (máx 3)
        self.variabilidad = 0.20       # 20% de variabilidad aleatoria

    def _calcular_probabilidad_victoria(
        self,
        equipo_local: str,
        equipo_visitante: str,
        racha_local: int = 0,
        racha_visitante: int = 0
    ) -> float:
        """
        Calcula la probabilidad de que el equipo local gane el partido.

        Args:
            equipo_local: Nombre del equipo que juega en casa
            equipo_visitante: Nombre del equipo visitante
            racha_local: Número de victorias consecutivas del equipo local
            racha_visitante: Número de victorias consecutivas del equipo visitante

        Returns:
            Probabilidad de victoria del equipo local (0.0 a 1.0)
        """
        # Habilidades base
        habilidad_local = self.equipos[equipo_local]
        habilidad_visitante = self.equipos[equipo_visitante]

        # Aplicar ventaja de jugar en casa
        habilidad_local_ajustada = habilidad_local * (1 + self.ventaja_local)

        # Aplicar efecto de racha (máximo 3 victorias)
        bonus_racha_local = min(racha_local, 3) * self.efecto_racha
        bonus_racha_visitante = min(racha_visitante, 3) * self.efecto_racha

        habilidad_local_ajustada *= (1 + bonus_racha_local)
        habilidad_visitante *= (1 + bonus_racha_visitante)

        # Calcular probabilidad basada en diferencia de habilidades
        diferencia = habilidad_local_ajustada - habilidad_visitante
        probabilidad_base = 0.5 + (diferencia / 200)  # Normalizar entre 0 y 1

        # Agregar variabilidad aleatoria
        variabilidad = np.random.normal(0, self.variabilidad)
        probabilidad_final = np.clip(probabilidad_base + variabilidad, 0.05, 0.95)

        return probabilidad_final

    def _simular_goles(
        self,
        habilidad_ofensiva: float,
        habilidad_defensiva: float
    ) -> int:
        """
        Simula el número de goles que marca un equipo.

        Args:
            habilidad_ofensiva: Nivel de ataque del equipo (0-100)
            habilidad_defensiva: Nivel de defensa del rival (0-100)

        Returns:
            Número de goles marcados
        """
        # Tasa de goles esperados basada en habilidades
        tasa_goles = (habilidad_ofensiva / habilidad_defensiva) * 1.5
        tasa_goles = np.clip(tasa_goles, 0.5, 4.0)  # Limitar a rangos realistas

        # Usar distribución de Poisson (común para goles en fútbol)
        goles = np.random.poisson(tasa_goles)
        return int(goles)

    def _simular_partido(
        self,
        equipo_local: str,
        equipo_visitante: str,
        jornada: int,
        temporada: int = 1,
        rachas: Optional[Dict[str, int]] = None
    ) -> Dict:
        """
        Simula un partido completo entre dos equipos.

        Args:
            equipo_local: Equipo que juega en casa
            equipo_visitante: Equipo visitante
            jornada: Número de jornada
            temporada: Número de temporada
            rachas: Diccionario con rachas actuales de victorias

        Returns:
            Diccionario con toda la información del partido
        """
        if rachas is None:
            rachas = {equipo: 0 for equipo in self.equipos.keys()}

        # Calcular probabilidad de victoria
        prob_victoria_local = self._calcular_probabilidad_victoria(
            equipo_local,
            equipo_visitante,
            rachas.get(equipo_local, 0),
            rachas.get(equipo_visitante, 0)
        )

        # Simular goles
        goles_local = self._simular_goles(
            self.equipos[equipo_local],
            self.equipos[equipo_visitante]
        )
        goles_visitante = self._simular_goles(
            self.equipos[equipo_visitante],
            self.equipos[equipo_local]
        )

        # Convertir probabilidad de victoria local a tres resultados
        # Probabilidad empate típica en fútbol: ~25-30%
        prob_empate = 0.25
        prob_victoria_visitante = 1.0 - prob_victoria_local

        # Ajustar probabilidades para que sumen 1.0
        factor_ajuste = 1.0 - prob_empate
        prob_victoria_local_ajustada = prob_victoria_local * factor_ajuste
        prob_victoria_visitante_ajustada = prob_victoria_visitante * factor_ajuste

        # Determinar resultado basado en las tres probabilidades
        rand = np.random.random()
        if rand < prob_victoria_local_ajustada:
            # Victoria local
            if goles_local <= goles_visitante:
                goles_local = goles_visitante + np.random.randint(1, 3)
        elif rand < prob_victoria_local_ajustada + prob_empate:
            # Empate - asegurar que los goles sean iguales
            goles_compartidos = max(goles_local, goles_visitante)
            # A veces reducir para hacer empates más realistas (0-0, 1-1, 2-2)
            if goles_compartidos > 3 and np.random.random() < 0.5:
                goles_compartidos = np.random.randint(0, 3)
            goles_local = goles_compartidos
            goles_visitante = goles_compartidos
        else:
            # Victoria visitante
            if goles_visitante <= goles_local:
                goles_visitante = goles_local + np.random.randint(1, 3)

        # Determinar resultado
        if goles_local > goles_visitante:
            resultado = "Victoria Local"
            ganador = equipo_local
        elif goles_visitante > goles_local:
            resultado = "Victoria Visitante"
            ganador = equipo_visitante
        else:
            resultado = "Empate"
            ganador = "Empate"

        # Crear registro del partido
        return {
            "Temporada": temporada,
            "Jornada": jornada,
            "Equipo_Local": equipo_local,
            "Equipo_Visitante": equipo_visitante,
            "Goles_Local": goles_local,
            "Goles_Visitante": goles_visitante,
            "Resultado": resultado,
            "Ganador": ganador,
            "Juega_En_Casa": True,  # Siempre True para el equipo local
            "Probabilidad_Victoria_Local": round(prob_victoria_local, 3),
            "Habilidad_Local": self.equipos[equipo_local],
            "Habilidad_Visitante": self.equipos[equipo_visitante],
            "Racha_Local": rachas.get(equipo_local, 0),
            "Racha_Visitante": rachas.get(equipo_visitante, 0)
        }

    def _generar_calendario(self) -> List[tuple]:
        """
        Genera el calendario de partidos de una temporada (todos contra todos).

        Returns:
            Lista de tuplas (equipo_local, equipo_visitante) para cada jornada
        """
        equipos_lista = list(self.equipos.keys())
        partidos = []

        # Todos contra todos (ida y vuelta)
        for i, equipo_local in enumerate(equipos_lista):
            for j, equipo_visitante in enumerate(equipos_lista):
                if i != j:
                    partidos.append((equipo_local, equipo_visitante))

        # Mezclar para hacer el calendario más realista
        np.random.shuffle(partidos)

        return partidos

    def generar_temporada(self, temporada: int = 1) -> pd.DataFrame:
        """
        Genera una temporada completa de la liga.

        Args:
            temporada: Número de la temporada

        Returns:
            DataFrame con todos los partidos de la temporada
        """
        calendario = self._generar_calendario()
        partidos_temporada = []

        # Seguimiento de rachas de victorias
        rachas = {equipo: 0 for equipo in self.equipos.keys()}

        # Simular cada jornada
        num_partidos_por_jornada = len(self.equipos) // 2
        jornada_actual = 1

        for idx, (equipo_local, equipo_visitante) in enumerate(calendario):
            # Calcular número de jornada
            if idx > 0 and idx % num_partidos_por_jornada == 0:
                jornada_actual += 1

            # Simular partido
            partido = self._simular_partido(
                equipo_local,
                equipo_visitante,
                jornada_actual,
                temporada,
                rachas
            )

            partidos_temporada.append(partido)

            # Actualizar rachas
            if partido["Resultado"] == "Victoria Local":
                rachas[equipo_local] += 1
                rachas[equipo_visitante] = 0
            elif partido["Resultado"] == "Victoria Visitante":
                rachas[equipo_visitante] += 1
                rachas[equipo_local] = 0
            else:
                # Empate interrumpe rachas
                rachas[equipo_local] = 0
                rachas[equipo_visitante] = 0

        return pd.DataFrame(partidos_temporada)

    def generar_multiples_temporadas(self, num_temporadas: int = 3) -> pd.DataFrame:
        """
        Genera múltiples temporadas de la liga.

        Args:
            num_temporadas: Número de temporadas a generar

        Returns:
            DataFrame con todos los partidos de todas las temporadas
        """
        todas_temporadas = []

        for temporada in range(1, num_temporadas + 1):
            df_temporada = self.generar_temporada(temporada)
            todas_temporadas.append(df_temporada)

        return pd.concat(todas_temporadas, ignore_index=True)


def generar_liga_futbol(
    temporadas: int = 5,
    semilla: Optional[int] = 42
) -> pd.DataFrame:
    """
    Función principal para generar datos de liga de fútbol.

    Args:
        temporadas: Número de temporadas a generar (default: 1)
        semilla: Semilla para reproducibilidad (default: 42)

    Returns:
        DataFrame con todos los partidos generados

    Ejemplo:
        >>> datos = generar_liga_futbol(temporadas=2, semilla=42)
        >>> print(f"Partidos generados: {len(datos)}")
        >>> print(datos.head())
    """
    generador = GeneradorLigaFutbol(semilla=semilla)

    if temporadas == 1:
        return generador.generar_temporada(temporada=1)
    else:
        return generador.generar_multiples_temporadas(num_temporadas=temporadas)


def generar_estadisticas_equipos(datos_partidos: pd.DataFrame) -> pd.DataFrame:
    """
    Genera estadísticas agregadas por equipo a partir de los datos de partidos.

    Args:
        datos_partidos: DataFrame con los partidos de la liga

    Returns:
        DataFrame con estadísticas por equipo
    """
    estadisticas = []

    for equipo in datos_partidos["Equipo_Local"].unique():
        # Partidos como local
        partidos_local = datos_partidos[datos_partidos["Equipo_Local"] == equipo]
        victorias_local = len(partidos_local[partidos_local["Resultado"] == "Victoria Local"])
        goles_favor_local = partidos_local["Goles_Local"].sum()
        goles_contra_local = partidos_local["Goles_Visitante"].sum()

        # Partidos como visitante
        partidos_visitante = datos_partidos[datos_partidos["Equipo_Visitante"] == equipo]
        victorias_visitante = len(partidos_visitante[partidos_visitante["Resultado"] == "Victoria Visitante"])
        goles_favor_visitante = partidos_visitante["Goles_Visitante"].sum()
        goles_contra_visitante = partidos_visitante["Goles_Local"].sum()

        # Totales
        partidos_jugados = len(partidos_local) + len(partidos_visitante)
        victorias_totales = victorias_local + victorias_visitante
        empates = partidos_jugados - victorias_totales - (partidos_jugados - victorias_totales)
        goles_favor = goles_favor_local + goles_favor_visitante
        goles_contra = goles_contra_local + goles_contra_visitante
        puntos = (victorias_totales * 3) + empates

        estadisticas.append({
            "Equipo": equipo,
            "Partidos_Jugados": partidos_jugados,
            "Victorias": victorias_totales,
            "Victorias_Casa": victorias_local,
            "Victorias_Visitante": victorias_visitante,
            "Empates": empates,
            "Derrotas": partidos_jugados - victorias_totales - empates,
            "Goles_Favor": goles_favor,
            "Goles_Contra": goles_contra,
            "Diferencia_Goles": goles_favor - goles_contra,
            "Puntos": puntos,
            "Porcentaje_Victorias": round((victorias_totales / partidos_jugados) * 100, 1) if partidos_jugados > 0 else 0,
            "Promedio_Goles_Por_Partido": round(goles_favor / partidos_jugados, 2) if partidos_jugados > 0 else 0
        })

    df_estadisticas = pd.DataFrame(estadisticas)
    return df_estadisticas.sort_values("Puntos", ascending=False).reset_index(drop=True)


# Ejemplo de uso cuando se ejecuta el script directamente
if __name__ == "__main__":
    import os

    print("Generando datos de liga de fútbol...")
    print("=" * 50)

    # Generar cinco temporadas
    datos = generar_liga_futbol(temporadas=5, semilla=42)
    print(f"\nPartidos generados: {len(datos)}")
    print(f"Jornadas: {datos['Jornada'].max()}")

    print("\nPrimeros 5 partidos:")
    print(datos[["Jornada", "Equipo_Local", "Equipo_Visitante", "Goles_Local", "Goles_Visitante", "Resultado"]].head())

    # Generar estadísticas
    print("\n" + "=" * 50)
    print("Tabla de posiciones:")
    print("=" * 50)
    estadisticas = generar_estadisticas_equipos(datos)
    print(estadisticas[["Equipo", "Partidos_Jugados", "Victorias", "Empates", "Derrotas", "Goles_Favor", "Goles_Contra", "Puntos"]])

    # Análisis de ventaja local
    print("\n" + "=" * 50)
    print("Análisis de ventaja de jugar en casa:")
    print("=" * 50)
    victorias_local = len(datos[datos["Resultado"] == "Victoria Local"])
    victorias_visitante = len(datos[datos["Resultado"] == "Victoria Visitante"])
    empates = len(datos[datos["Resultado"] == "Empate"])
    total = len(datos)

    print(f"Victorias locales: {victorias_local} ({(victorias_local/total)*100:.1f}%)")
    print(f"Victorias visitantes: {victorias_visitante} ({(victorias_visitante/total)*100:.1f}%)")
    print(f"Empates: {empates} ({(empates/total)*100:.1f}%)")

    # Guardar CSV
    print("\n" + "=" * 50)
    print("Guardando datos en archivo CSV...")
    print("=" * 50)

    # Obtener directorio del script
    directorio_script = os.path.dirname(os.path.abspath(__file__))
    archivo_csv = os.path.join(directorio_script, "datos_liga_futbol.csv")

    # Guardar datos
    datos.to_csv(archivo_csv, index=False, encoding='utf-8')
    print(f"\nArchivo guardado exitosamente: {archivo_csv}")
    print(f"Tamaño del archivo: {os.path.getsize(archivo_csv) / 1024:.2f} KB")
    print(f"Filas: {len(datos)}")
    print(f"Columnas: {len(datos.columns)}")

    print("\n¡Listo! Ahora puedes usar este archivo CSV en tu análisis.")
