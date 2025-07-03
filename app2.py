import streamlit as st
import time
from PIL import Image
import os

# --- Configuración general ---
st.set_page_config(page_title="Tortas Peruanas", page_icon="🍰", layout="wide")

# --- Estilos personalizados ---
st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"] > .main {
    background-color: #1a1a1a !important;
    color: #ffffff !important;
    font-family: 'Segoe UI', sans-serif;
}

h1, h2, h3, h4 {
    color: #ffffff;
    font-weight: 600;
    text-align: center;
}

hr {
    border: 0;
    height: 1px;
    background: #444;
    margin: 2rem 0;
}

img {
    border-radius: 1rem;
    margin-bottom: 1rem;
    object-fit: cover;
}

a.whatsapp-button {
    position: fixed;
    bottom: 25px;
    right: 25px;
    background-color: #25D366;
    color: white;
    border-radius: 50%;
    padding: 0.8rem 1rem;
    text-decoration: none;
    font-size: 2rem;
    z-index: 1000;
    box-shadow: 0 0 15px rgba(0,0,0,0.4);
    transition: transform 0.3s ease;
}

a.whatsapp-button:hover {
    transform: scale(1.1);
}

[data-testid="stSidebar"] {
    transition: transform 0.3s ease;
    transform: translateX(-100%);
    position: fixed;
    top: 0;
    left: 0;
    height: 100%;
    background-color: #1a1a1a !important;
    z-index: 1001;
    padding: 1rem;
    color: white;
    overflow-y: auto;
    width: 250px;
}

.sidebar-visible [data-testid="stSidebar"] {
    transform: translateX(0);
}
</style>
""", unsafe_allow_html=True)

# --- Botón para mostrar/ocultar menú ---
if 'sidebar_visible' not in st.session_state:
    st.session_state.sidebar_visible = False

if st.button("☰ Menú", key="toggle_sidebar"):
    st.session_state.sidebar_visible = not st.session_state.sidebar_visible

sidebar_class = "sidebar-visible" if st.session_state.sidebar_visible else ""
st.markdown(f"<div class='{sidebar_class}'>", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    if st.session_state.sidebar_visible:
        st.markdown("### Menú de navegación")
        st.markdown("- [🏠 Inicio](#inicio)")
        st.markdown("- [📸 Catálogo](#catalogo)")
        st.markdown("- [📍 Ubicación](#ubicacion)")
        st.markdown("- [✉️ Contacto](#contacto)")

# --- Contenido principal ---
st.markdown("<h1 id='inicio'>Tortas Peruanas a Pedido</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; font-weight: normal;'>Delicias artesanales con tradición y sabor</h4>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

carrusel_imgs = [
    "Imag/Empanadas Peruanas de Carne - Acomer_pe.jpg",
    "Imag/Picarones Pasados Receta de ChileRecetas.jpg",
    "Imag/Empanadas Peruanas de Carne - Acomer_pe.jpg"
]

img_placeholder = st.empty()
for i in range(2):
    for img_path in carrusel_imgs:
        img_placeholder.image(img_path, use_container_width=True)
        time.sleep(3)

# --- Galería tipo mosaico ---
st.markdown("<h2 id='catalogo'>Nuestro Catálogo</h2>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("""
<div style='text-align: center;'>
    Aquí puedes mostrar distintas categorías de tortas, empanadas, postres típicos, etc. con sus precios y descripciones.
</div>
""", unsafe_allow_html=True)

# --- Galería de imágenes ---
galeria_imgs = [
    "Imag/Empanadas Peruanas de Carne - Acomer_pe.jpg",
    "Imag/Picarones Pasados Receta de ChileRecetas.jpg",
    "Imag/Tortas Peruanas Barcelona.jpg",
    "Imag/Tortas Peruanas Barcelona.jpg",
    "Imag/Picarones Pasados Receta de ChileRecetas.jpg",
    "Imag/Empanadas Peruanas de Carne - Acomer_pe.jpg"
]

cols = st.columns(3)
for idx, url in enumerate(galeria_imgs):
    with cols[idx % 3]:
        st.image(url, use_container_width=True)

st.markdown("<hr>", unsafe_allow_html=True)

# --- Ubicación ---
st.markdown("<h2 id='ubicacion'>Dónde Estamos</h2>", unsafe_allow_html=True)
st.map()

# --- Contacto ---
st.markdown("<h2 id='contacto'>Contacto</h2>", unsafe_allow_html=True)
st.markdown("Puedes hablar con nosotros directamente por WhatsApp. ¡Haz clic en el botón verde abajo!", unsafe_allow_html=True)

# --- Botón de WhatsApp ---
telefono = "630318586"
st.markdown(f"""
<a href="https://wa.me/{telefono}" class="whatsapp-button" target="_blank">💬</a>
""", unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
<hr>
<div style='text-align: center; font-size: 0.85em;'>
    © 2025 Tortas Peruanas Artesanales | Todos los derechos reservados
</div>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------- XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ----------------------------------------
# ---------------------------------------- XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ----------------------------------------
# ---------------------------------------- XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ----------------------------------------
# ---------------------------------------- XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ----------------------------------------
# ---------------------------------------- XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ----------------------------------------
# ---------------------------------------- XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ----------------------------------------

import streamlit as st
import time

# --- Configuración general ---
st.set_page_config(page_title="Tortas Peruanas", page_icon="🍰", layout="wide")

# --- Estilos personalizados ---
st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"] > .main {
    background-color: #1a1a1a !important;
    color: #ffffff !important;
    font-family: 'Segoe UI', sans-serif;
}
h1, h2, h3, h4 {
    color: #ffffff;
    font-weight: 600;
    text-align: center;
}
hr {
    border: 0;
    height: 1px;
    background: #444;
    margin: 2rem 0;
}
img {
    border-radius: 1rem;
    margin-bottom: 1rem;
    object-fit: cover;
}
a.whatsapp-button {
    position: fixed;
    bottom: 25px;
    right: 25px;
    background-color: #25D366;
    color: white;
    border-radius: 50%;
    padding: 0.8rem 1rem;
    text-decoration: none;
    font-size: 2rem;
    z-index: 1000;
    box-shadow: 0 0 15px rgba(0,0,0,0.4);
    transition: transform 0.3s ease;
}
a.whatsapp-button:hover {
    transform: scale(1.1);
}

/* Estilo botón menú */
div[data-testid="stButton"] button {
    background-color: #ff4b4b;
    color: white;
    padding: 0.6rem 1rem;
    border-radius: 8px;
    border: none;
    margin-bottom: 1rem;
    font-weight: bold;
    cursor: pointer;
}
div[data-testid="stButton"] button:hover {
    background-color: #ff1f1f;
}

/* Sidebar personalizado */
.custom-sidebar {
    position: fixed;
    top: 0;
    left: 0;
    width: 250px;
    height: 100%;
    background-color: #111;
    color: white;
    padding: 2rem 1rem;
    z-index: 1001;
    transform: translateX(-100%);
    transition: transform 0.3s ease;
}
.custom-sidebar.visible {
    transform: translateX(0);
}
</style>
""", unsafe_allow_html=True)

# --- Botón para mostrar/ocultar menú ---
if "sidebar_visible" not in st.session_state:
    st.session_state.sidebar_visible = False

if st.button("☰ Menú"):
    st.session_state.sidebar_visible = not st.session_state.sidebar_visible

# --- Sidebar HTML manual ---
if st.session_state.sidebar_visible:
    st.markdown("""
    <div class="custom-sidebar visible">
        <h4>Menú de navegación</h4>
        <ul style="list-style: none; padding-left: 0;">
            <li>🏠 <a href="#inicio" style="color:white;">Inicio</a></li>
            <li>📸 <a href="#catalogo" style="color:white;">Catálogo</a></li>
            <li>📍 <a href="#ubicacion" style="color:white;">Ubicación</a></li>
            <li>✉️ <a href="#contacto" style="color:white;">Contacto</a></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# --- Contenido principal ---
st.markdown("<h1 id='inicio'>Tortas Peruanas a Pedido</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; font-weight: normal;'>Delicias artesanales con tradición y sabor</h4>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)




# --- Estilo CSS para el fondo negro (versión mejorada) ---
st.markdown("""
<style>
/* Selector para el contenedor principal de la aplicación */
.stApp {
    background-color: #000000; /* Fondo negro */
    color: #FFFFFF; /* Letras blancas por defecto */
}

/* También aseguramos que el cuerpo y html sean negros */
html, body {
    background-color: #000000 !important;
    color: #FFFFFF !important;
}

/* El contenedor principal de la vista de la app */
[data-testid="stAppViewContainer"] {
    background-color: #000000 !important;
    color: #FFFFFF !important;
}

/* Aseguramos que el main content también tenga el fondo negro */
.main .block-container {
    background-color: #000000 !important;
    color: #FFFFFF !important;
}

/* Aseguramos que la barra lateral (si existe o se activa) también tenga fondo negro */
[data-testid="stSidebar"] {
    background-color: #1A1A1A !important;
    color: #FFFFFF !important;
}

/* El elemento que contiene el 'main' (que es donde está la página) */
[data-testid="stAppViewContainer"] > .main {
    background-color: #1A1A1A !important;
    color: #FFFFFF !important;
}

/* Si tu layout es 'wide', a veces hay un padding que expone el fondo blanco.
   Esto lo arregla si es el caso. */
.css-1dp5vir.e8zbici1 { /* Este selector puede variar con versiones de Streamlit */
    background-color: #000000 !important;
    color: #FFFFFF !important;
}
.css-fg4lnv.e8zbici1 { /* Otro selector común para el contenedor del contenido */
    background-color: #000000 !important;
    color: #FFFFFF !important;
}
/* Agregamos una regla para el contenido principal si el problema es que un div interno mantiene el fondo blanco */
.reportview-container .main .block-container {
    background-color: #000000 !important;
    color: #FFFFFF !important;
}


/* Tus estilos existentes para los encabezados */
h1 {
    text-align: center;
    margin-top: -40px;
    color:#FD676C; /* Este color lo mantienes específico para tu h1 */
}
</style>
""", unsafe_allow_html=True)


# --------------------- MENU ---------------------

# Menú
page = option_menu(
     menu_title=None,
     options=["Inicio", "Pasteles y Tortas", "Nuestros Pies","Cheescakes","Empanadas", "Contacto"],
     icons=["info-circle", "pin", "house", "calendar-check", "coin", "bar-chart","camera","arrow-up-right", "check-circle"],
    default_index=0,
    orientation="horizontal",
      styles={
        "nav-link": {"font-size": "14px", "text-align": "center", "margin": "0px", "padding": "0px", "--hover-color": "#eee"},
        "icon": {"margin": "auto", "display": "block"}}
)


    st.markdown("<h5 style='text-align: center; margin-top: 0px; '></h5>" ,unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; margin-top: 0px; '></h5>" ,unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; margin-top: 0px; '></h5>" ,unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; margin-top: 0px; '></h5>" ,unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; margin-top: 0px; '></h5>" ,unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; margin-top: 0px; '></h5>" ,unsafe_allow_html=True)