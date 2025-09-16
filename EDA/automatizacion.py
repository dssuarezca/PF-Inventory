# ==========================================
# ETL incremental con BigQuery (con alerta solo si hay nuevos registros)
# ==========================================
import os
import pandas as pd
from google.cloud import bigquery
import requests
from datetime import datetime

# Configuración
PROJECT_ID = "inventarioproject-471611"
DATASET = "inventarioproject_henry"
TABLE_STAGING = f"{PROJECT_ID}.{DATASET}.compras_2017_staging"
TABLE_FINAL = f"{PROJECT_ID}.{DATASET}.compras_2017_clean"

# Cliente BigQuery
client = bigquery.Client(project=PROJECT_ID)

# 1. Leer CSV local (carpeta compartida en Drive sincronizado)
csv_path = r"G:\Mi unidad\proyecto_inventario\raw\compras_test.csv"
df = pd.read_csv(csv_path)

#---------------------------------------------------------------------------------------------------
# 2. Limpieza básica
df.columns = df.columns.str.lower().str.replace(" ", "_")

for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.lower().str.replace(" ", "_")

for col in df.columns:
    if "date" in col:
        df[col] = pd.to_datetime(df[col], errors="coerce")

#---------------------------------------------------------------------------------------------------
# 3. Subir a tabla staging
job_config = bigquery.LoadJobConfig(
    write_disposition="WRITE_TRUNCATE",
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
FROM `{TABLE_STAGING}` AS s
WHERE NOT EXISTS (
    SELECT 1
    FROM `{TABLE_FINAL}` AS c
    WHERE c.inventoryid = s.inventoryid
)
"""

query_job = client.query(sql)
query_job.result()

# Número de filas insertadas
inserted_rows = query_job.num_dml_affected_rows
print(f"🔎 Filas nuevas insertadas: {inserted_rows}")

#---------------------------------------------------------------------------------------------------
# 5. Notificación a Slack solo si hay filas nuevas
def notificar_slack(mensaje):
    url = "https://hooks.slack.com/services/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"
    payload = {"text": mensaje}
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("✅ Mensaje enviado a Slack")
    else:
        print(f"❌ Error al enviar mensaje: {response.status_code}, {response.text}")

if inserted_rows and inserted_rows > 0:
    notificar_slack(f"✅ Proceso completado: {inserted_rows} registros nuevos cargados en BigQuery.")
    notificacion_enviada = True
else:
    print("ℹ️ No se encontraron datos nuevos. No se envió notificación.")

#---------------------------------------------------------------------------------------------------
