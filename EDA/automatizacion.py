# ==========================================
# ETL incremental con BigQuery
# ==========================================
import os
import pandas as pd
from google.cloud import bigquery

# Configuración
PROJECT_ID = "inventarioproject-471611"
DATASET = "inventarioproject_henry"
TABLE_STAGING = f"{PROJECT_ID}.{DATASET}.compras_2017_staging"
TABLE_FINAL = f"{PROJECT_ID}.{DATASET}.compras_2017_clean"


# Cliente BigQuery
client = bigquery.Client(project=PROJECT_ID)


# 1. Leer CSV local (carpeta compartida en OneDrive/Drive sincronizado)
csv_path = r"G:\Mi unidad\proyecto_inventario\raw\compras_test.csv"
df = pd.read_csv(csv_path)


#---------------------------------------------------------------------------------------------------

# 2. Limpieza básica

# --- 1. Pasar nombres de columnas a minúsculas y reemplazar espacios por "_"
df.columns = df.columns.str.lower().str.replace(" ", "_")


# --- 2. Pasar todo el contenido de las columnas tipo string a minúsculas y reemplazar espacios por "_"
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.lower().str.replace(" ", "_")


# --- 3. Convertir todas las columnas que contengan "date" en su nombre a tipo datetime
for col in df.columns:
    if "date" in col:
        df[col] = pd.to_datetime(df[col], errors="coerce")  # "coerce" pone NaT si hay error


#---------------------------------------------------------------------------------------------------

# 3. Subir a tabla staging
job_config = bigquery.LoadJobConfig(
    write_disposition="WRITE_TRUNCATE",  # pisa staging cada vez
    autodetect=True
)

job = client.load_table_from_dataframe(df, TABLE_STAGING, job_config=job_config)
job.result()
print("✅ Datos cargados en tabla staging")

#---------------------------------------------------------------------------------------------------

# 4. SQL incremental para pasar solo los nuevos registros a la tabla final
sql = f"""
INSERT INTO `{TABLE_FINAL}`
SELECT *
FROM `{TABLE_STAGING}` s
WHERE NOT EXISTS (
    SELECT 1
    FROM `{TABLE_FINAL}` c
    WHERE c.inventoryid = s.inventoryid
)
"""

query_job = client.query(sql)
query_job.result()
print("✅ Carga incremental completada en tabla final")
