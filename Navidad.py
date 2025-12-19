import streamlit as st
import datetime
from zoneinfo import ZoneInfo

# 🔄 Auto refresco cada segundo (oficial)
from streamlit_autorefresh import st_autorefresh
st_autorefresh(interval=1000, key="contador_navidad")

# Configuración para celular
st.set_page_config(
    page_title="Navidad de Tommy 🎄",
    page_icon="🎅",
    layout="centered"
)

# Hora de Costa Rica
cr_now = datetime.datetime.now(ZoneInfo("America/Costa_Rica"))
today = cr_now.date()

# Próxima Navidad
xmas = datetime.date(today.year, 12, 25)
if today > xmas:
    xmas = datetime.date(today.year + 1, 12, 25)

# Conteo estable (solo días)
days_left = (xmas - today).days

# 🎄 UI
st.markdown(
    "<h1 style='text-align:center; color:red;'>🎄 ¡Hola Tommy! 🎄</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h3 style='text-align:center;'>Faltan</h3>",
    unsafe_allow_html=True
)

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

# Animaciones
if days_left <= 10:
    st.snow()

if days_left == 0:
    st.balloons()
    st.markdown(
        "<h2 style='text-align:center;'>🎉 ¡HOY ES NAVIDAD! 🎁</h2>",
        unsafe_allow_html=True
    )

# Barra de progreso
progress = int((365 - days_left) / 365 * 100)
st.progress(progress)

# 🎵 Rodolfo el Reno (autoplay silencioso)
st.markdown("""
<iframe width="0" height="0"
src="https://www.youtube.com/embed/VjL031bE9FA?autoplay=1&mute=1&loop=1&playlist=VjL031bE9FA"
frameborder="0"
allow="autoplay">
</iframe>
""", unsafe_allow_html=True)

st.info("🔊 Toca ▶️ para escuchar a Rodolfo el Reno 🎶")

st.video("https://www.youtube.com/watch?v=VjL031bE9FA")
