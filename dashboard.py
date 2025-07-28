import pandas as pd
import streamlit as st
import plotly.express as px
from sqlalchemy import create_engine

st.title("📡 Dashboard IoT - Temperatura")

engine = create_engine('postgresql://postgres:senha@localhost:5432/iot_db')
df = pd.read_sql("SELECT * FROM temperature_readings", engine)

# Gráficos
tab1, tab2, tab3 = st.tabs([" Por Local", " Por Data", " Por Sala"])

with tab1:
    by_location = df.groupby("location")["temp"].mean().reset_index()
    st.plotly_chart(px.bar(by_location, x="location", y="temp", title="Temperatura Média - Local"))

with tab2:
    df["data"] = df["noted_date"].dt.date
    temp_day = df.groupby("data")["temp"].agg(["max", "min"]).reset_index()
    st.plotly_chart(px.line(temp_day, x="data", y=["max", "min"], title="Temperaturas Máximas e Mínimas por Dia"))

with tab3:
    room_avg = df.groupby("room_id")["temp"].mean().reset_index()
    st.plotly_chart(px.bar(room_avg, x="room_id", y="temp", title="Temperatura Média por Sala"))
