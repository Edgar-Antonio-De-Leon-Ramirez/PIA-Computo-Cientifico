import os
import pandas as pd
import pyarrow.parquet as pq

# Configuración de rutas relativas consistentes
SRC_DIR = os.path.dirname(os.path.abspath(__file__)) if '__file__' in locals() else os.getcwd()
BASE_DIR = os.path.dirname(SRC_DIR)
PATH_PARQUET = os.path.join(BASE_DIR, "data", "processed", "fact_steam_games.parquet")

print("=== PIPELINE DE AUDITORÍA: VALIDACIÓN DE MEDIDAS (PANDAS VS DAX) ===")

if os.path.exists(PATH_PARQUET):
    # Leer el archivo Parquet generado por la tubería origen
    dataset = pq.read_table(PATH_PARQUET)
    df = dataset.to_pandas()
    
    print(f"✅ Archivo Parquet detectado correctamente. Auditando {len(df)} filas.\n")
    
    # --- VALIDACIÓN MEDIDA 1: Total de Jugadores Concurrentes ---
    pandas_m1 = df["Jugadores_Simultaneos_CCU"].sum()
    print(f"| MEDIDA 1 | Total_CCU_Global")
    print(f"  -> Resultado en Pandas: {pandas_m1:,}")
    print(f"  -> Equivalente DAX: Total_CCU_Global = SUM(fact_steam_games[Jugadores_Simultaneos_CCU])\n")
    
    # --- VALIDACIÓN MEDIDA 2: Promedio de Índice de Estabilidad ---
    pandas_m2 = df["Indice_Estabilidad_Retencion"].mean()
    print(f"| MEDIDA 2 | Promedio_Estabilidad_Retencion")
    print(f"  -> Resultado en Pandas: {round(pandas_m2, 2)}")
    print(f"  -> Equivalente DAX: Promedio_Estabilidad = AVERAGE(fact_steam_games[Indice_Estabilidad_Retencion])\n")
    
    # --- VALIDACIÓN MEDIDA 3: Ratio de Retención en Lanzamientos Recientes ---
    df_recientes = df[df["Generacion_Ciclo_Vida"] == "Lanzamiento Reciente"]
    pandas_m3 = df_recientes["Indice_Estabilidad_Retencion"].mean()
    print(f"| MEDIDA 3 | Promedio_Estabilidad_Juegos_Recientes")
    print(f"  -> Resultado en Pandas: {round(pandas_m3, 2)}")
    print(f"  -> Equivalente DAX: Promedio_Estabilidad_Recientes = CALCULATE(AVERAGE(fact_steam_games[Indice_Estabilidad_Retencion]), fact_steam_games[Generacion_Ciclo_Vida] == \"Lanzamiento Reciente\")\n")
    
    # --- EXTRACCIÓN DE METADATOS DE AUDITORÍA (Requisito de la entrega) ---
    print("=== METADATOS DE CONFIGURACIÓN DEL PARQUET ===")
    metadatos = dataset.schema.metadata
    for llave, valor in metadatos.items():
        print(f"  📍 {llave.decode('utf-8')}: {valor.decode('utf-8')}")
        
else:
    print(f"❌ Error: No se encontró el archivo Parquet en la ruta {PATH_PARQUET}. Ejecuta primero descargar_juegos_steam.py")