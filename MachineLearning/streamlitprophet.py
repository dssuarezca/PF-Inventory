import streamlit as st
from prophet import Prophet
import pandas as pd

#leemos el dataset de ventas finales para predecir ventas futuras

@st.cache_data
def load_data():
    return pd.read_excel("F:\\Documentos\\PF Inventory\\data clean\\ventas_2017_clean.xlsx", engine="openpyxl")

df_ventas_finales = load_data()

#creamos un titulo para el streamlift
st.title("📊 Predicción de Ventas")

# Usuario selecciona filtros
producto = st.selectbox("Selecciona producto", df_ventas_finales["descripcion"].unique())
ciudad = st.selectbox("Selecciona ciudad", df_ventas_finales["ciudad"].unique())
tienda = st.selectbox("Selecciona tienda", df_ventas_finales["tienda"].unique())


# Filtrar los datos
df_filtro = df_ventas_finales[(df_ventas_finales["descripcion"] == producto) &
            (df_ventas_finales["ciudad"] == ciudad) &
            (df_ventas_finales["tienda"] == tienda)][["fecha_venta","cantidad_vendida"]]

df_filtro = df_filtro.rename(columns={"fecha_venta":"ds","cantidad_vendida":"y"})

# Creamos un boton para predecir las ventas
if st.button("🔮 Predecir Ventas"):
    # mostramos un mensaje por si se filtran datos incorrectos
    if df_filtro.shape[0] < 2:
        st.warning("⚠️ No hay suficientes ventas históricas para este producto/tienda/ciudad.")
    else:
        # Entrenar Prophet para esa combinación
        m = Prophet()
        m.fit(df_filtro)
        input_data = pd.DataFrame({
            "descripcion": [producto],
            "ciudad": [ciudad],
            "tienda": [tienda],
        })

        # Predecir próximos 90 días
        future = m.make_future_dataframe(periods=90, freq="D")
        forecast = m.predict(future)

        # Total de ventas esperadas
        total = forecast.tail(90)["yhat"].sum()
        st.success(f"🔮 Se esperan {total:.0f} ventas en los próximos 3 meses para {producto} - {ciudad} - {tienda}")
