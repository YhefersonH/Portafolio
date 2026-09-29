import os
import streamlit as st

st.set_page_config(page_title="Aplicaciones de IA", layout="wide")
st.title("Aplicaciones de Inteligencia Artificial.")

with st.sidebar:
    st.subheader("Aplicaciones con Inteligencia Artificial.")
    parrafo = (
        "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
        "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
        "resulta en una mayor eficiencia y precisión en diversos campos."
    )
    st.write(parrafo)

url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")

# ---------------------------------------------------------------
# LISTA DE PROYECTOS (11 espacios)
# - imagen: archivo que debe estar en la MISMA carpeta que Intro.py
# - url:    pega aquí el enlace de cada streamlit
# ---------------------------------------------------------------
PROYECTOS = [
    {
        "titulo": "🎯 Descenso de Gradiente",
        "imagen": "descenso_gradiente.png",
        "descripcion": "Explora cómo la tasa de aprendizaje y el punto inicial afectan la convergencia del descenso de gradiente, con la trayectoria en 3D y la curva de error.",
        "url": "",
    },
    {
        "titulo": "📈 Regresión: conceptos clave",
        "imagen": "regresion_conceptos.png",
        "descripcion": "Recorre el modelo, la función de costo, el gradiente y las métricas de evaluación con datos reales de vivienda en California.",
        "url": "",
    },
    {
        "titulo": "🌡️ Series de Tiempo con sensor IoT",
        "imagen": "series_tiempo_iot.png",
        "descripcion": "Simula un sensor de temperatura y analiza tendencia, estacionalidad, ruido, ACF/PACF, ventanas deslizantes y modelos clásicos.",
        "url": "",
    },
    {
        "titulo": "☁️ Predictor de calidad del aire",
        "imagen": "calidad_aire_cornare.png",
        "descripcion": "Carga modelos entrenados (.pkl) y genera predicciones de PM2.5 y PM10 hacia adelante para CORNARE.",
        "url": "",
    },
    {
        "titulo": "🌡️ Predictor de Sensación Térmica",
        "imagen": "sensacion_termica.png",
        "descripcion": "Usa datos de temperatura y humedad de un sensor IoT (DHT22 con ESP32 vía InfluxDB) para entrenar una regresión lineal.",
        "url": "",
    },
    {
        "titulo": "🍎 ¿Qué fruta es más parecida?",
        "imagen": "fruta_parecida.png",
        "descripcion": "Ingresa peso, diámetro y dulzor de una fruta y mira su distancia a manzana, banano, naranja y pera.",
        "url": "",
    },
    {
        "titulo": "🚨 Detector de Anomalías",
        "imagen": "detector_anomalias.png",
        "descripcion": "Compara una alarma por regla lógica, la notación Big-O y un benchmark entre evaluación ingenua y vectorizada con NumPy.",
        "url": "",
    },
    {
        "titulo": "🌧️ ¿Lloverá mañana?",
        "imagen": "lluvia_logistica.png",
        "descripcion": "Regresión logística interactiva: elige variables y umbral, simula un nuevo día y observa la probabilidad de lluvia en la curva sigmoide.",
        "url": "",
    },
    {
        "titulo": "🌱 KNN con suelos de AGROSAVIA",
        "imagen": "knn_suelos.png",
        "descripcion": "Clasifica la fertilidad del suelo (baja, media, alta) con KNN y explora escalado, elección de k, métricas y fuga de datos.",
        "url": "",
    },
    {
        "titulo": "🗂️ Datos: preparación y estructura",
        "imagen": "datos_preparacion.png",
        "descripcion": "Experimenta con un dataset sintético de sensores IoT: tipos de datos, valores faltantes, outliers, normalización y división train/val/test.",
        "url": "",
    },
    {
        "titulo": "🌊 Monitoreo del Nivel del Río",
        "imagen": "nivel_rio.png",
        "descripcion": "Consulta por rango de fechas el nivel del río en la Estación 18, Quebrada Doradal (Puerto Triunfo).",
        "url": "",
    },
]

COLUMNAS = 3


def mostrar_proyecto(p):
    """Dibuja una tarjeta de proyecto dentro de la columna actual."""
    st.subheader(p["titulo"])

    if p["imagen"] and os.path.exists(p["imagen"]):
        st.image(p["imagen"], width=280)
    else:
        st.caption("🖼️ Imagen pendiente: " + (p["imagen"] or "sin nombre"))

    st.write(p["descripcion"])

    if p["url"]:
        st.write(f"[Abrir aplicación]({p['url']})")
    else:
        st.write("🔜 Enlace próximamente")


# Se recorre la lista de 3 en 3 para que cada fila quede alineada
for i in range(0, len(PROYECTOS), COLUMNAS):
    fila = st.columns(COLUMNAS)
    for col, proyecto in zip(fila, PROYECTOS[i:i + COLUMNAS]):
        with col:
            mostrar_proyecto(proyecto)
    st.divider()
