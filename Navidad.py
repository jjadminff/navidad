import streamlit as st
import datetime
import time

# Configuración de la página (muy importante para celular)
st.set_page_config(
    page_title="Cuenta regresiva 🎄",
    page_icon="🎅",
    layout="centered"
)

# Fecha actual y Navidad
today = datetime.date.today()
xmas = datetime.date(today.year, 12, 25)

# Si ya pasó Navidad, usar el próximo año
if today > xmas:
    xmas = datetime.date(today.year + 1, 12, 25)

days_left = (xmas - today).days

# Título grande
st.markdown(
    "<h1 style='text-align: center; color: red;'>🎄 ¡Hola Tommy! 🎄</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h2 style='text-align: center;'>Faltan...</h2>",
    unsafe_allow_html=True
)

# Número grande (impacto visual)
st.markdown(
    f"""
    <div style="text-align:center; font-size:80px; font-weight:bold; color:green;">
        {days_left}
    </div>
    <div style="text-align:center; font-size:30px;">
        días para Navidad 🎅🎁
    </div>
    """,
    unsafe_allow_html=True
)

# Barra de progreso
total_days = 365
progress = int((total_days - days_left) / total_days * 100)
st.progress(progress)

# Animación simple
if days_left <= 10:
    st.balloons()  # confeti 🎈

# Pequeña animación tipo "nieve"
with st.empty():
    for _ in range(3):
        st.markdown("❄️ ❄️ ❄️ ❄️ ❄️")
        time.sleep(0.5)

# Mensaje final
st.markdown(
    "<p style='text-align:center; font-size:20px;'>🎁 Santa ya viene en camino...</p>",
    unsafe_allow_html=True
)
