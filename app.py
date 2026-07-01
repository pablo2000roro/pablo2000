import streamlit as st
import pandas as pd
from api_client import obtener_clima_api

st.set_page_config(page_title="API-CLIMA", page_icon=":cloud:", layout="wide")

st.title("API CLIMA - STREAMLIT Pablo Rodriguez")
st.write("Aplicación para consultar datos del clima desde una API")

menu = st.sidebar.selectbox(
    "Seleccione una opción",
    [
        "Inicio",
        "Consultar Clima"
    ]
)

# -------------------- INICIO --------------------
if menu == "Inicio":
    st.header("Bienvenido a la APP de Clima ")
    st.info("Seleccione 'Consultar Clima' para ver los datos")

# -------------------- CLIMA --------------------
elif menu == "Consultar Clima":
    st.header("Consultar clima 🌡️")
    st.code("https://api.open-meteo.com")

    if st.button("Obtener datos del clima"):
        clima = obtener_clima_api()

        if clima:
            df = pd.DataFrame({
                "Hora": clima["hourly"]["time"],
                "Temperatura (°C)": clima["hourly"]["temperature_2m"]
            })

            st.success("Datos del clima obtenidos correctamente")

            # Mostrar tabla
            st.subheader("Tabla de temperaturas")
            st.dataframe(df, use_container_width=True)

            # Métricas
            col1, col2, col3 = st.columns(3)
            col1.metric("Registros", len(df))
            col2.metric("Temp. Máxima", df["Temperatura (°C)"].max())
            col3.metric("Temp. Mínima", df["Temperatura (°C)"].min())

            # Gráfico
            st.subheader("Gráfico de temperatura")
            st.line_chart(df.set_index("Hora"))

        else:
            st.error("No se pudieron obtener datos del clima")