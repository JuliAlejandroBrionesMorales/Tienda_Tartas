# --------------------- LIBRERIAS ---------------------

import streamlit as st
from streamlit_option_menu import option_menu
import base64
import os # Pendiente confirmar si es útil
import json # Pendiente confirmar si es útil


# --------------------- CONFIGURACIÓN SITIO WEB ---------------------

st.set_page_config(page_title="Tortas Peruanas", 
                   page_icon="🍰", 
                   layout="wide")


# --------------------- COLUMNAS ---------------------

# Centro de la página
col1, col2, col3 = st.columns([3, 1, 3])

with col2:
    st.image("Imag/1_logo sabor a peru.png", width=75)

st.markdown("<h1 style='text-align: center; margin-top: -40px; color:#FFFFFF;'>Delicias artesanales con tradición y sabor</h1>" ,unsafe_allow_html=True)


# --------------------- IMAGEN DE FONDO ---------------------

def add_bg_from_local(image_file):
        with open(image_file, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        st.markdown(
        f"""
        <style>
            .stApp {{
            background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
        )
add_bg_from_local(r"Imag/2_fondo negro.jpg")  


# --------------------- PERSONALIZACIÓN DE PÁGINA ---------------------

import streamlit as st

st.markdown("""
<style>
/* Fondo negro para el sidebar */
[data-testid="stSidebar"] {
    background-color: #000000 !important;
}

/* Texto en blanco dentro del sidebar */
[data-testid="stSidebar"] * {
    color: white !important;
}

/* Texto blanco en el cuerpo de la app */
body, h1, h2, h3, h4, h5, h6, div {
    color: white !important;
}

/* Responsive columns */
@media (max-width: 768px) {
    .responsive-col {
        display: block !important;
        width: 100% !important;
    }
}
@media (min-width: 769px) {
    .responsive-container {
        display: flex !important;
        gap: 1rem;
    }
    .responsive-col {
        width: 50% !important;
    }
}
</style>
""", unsafe_allow_html=True)

# Resto de tu código Streamlit



# --------------------- SIDEBAR ---------------------
st.sidebar.image("Imag/1_logo sabor a peru.png", use_container_width=True)
st.sidebar.title("Menu de Navegación")
st.sidebar.write('-------')

# Secciones como páginas independientes
pagina = st.sidebar.radio("Ir a:", ["Inicio","Pasteles y Tortas", "Cheescakes", "Nuestros Pies", "Empanadas", "Contacto"])

# --------------------- PÁGINAS ---------------------

if pagina == "Inicio":
    st.markdown("<h6 style= 'margin-top: -15px; '>En 'Sabor a Perú' elaboramos con cariño una gran variedad de tartas y postres tradicionales de la respostería peruana, listos para ser encargados desde la comodidad de tu hogar.</h6>" ,unsafe_allow_html=True)
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.image("Imag/3_torta helada.jpg", use_container_width=True)
            st.image("Imag/4_torta de chocolate.jpg", use_container_width=True)
            st.image("Imag/5_tarta tres leches.png", use_container_width=True)
        with col2:
            st.image("Imag/6_tarta volteada de piña.jpg", use_container_width=True)
            st.image("Imag/7_keke de naranja.jpg", use_container_width=True)
            st.image("Imag/8_Tarta de manzana.jpg", use_container_width=True)
    st.markdown("Descubre nuestro clásico más populares como la tarta húmeda de chocolate, el pastel de tres leches, la torta helada o el pie de limón, entre muchos otros. También realizamos tartas personalizadas para cumpleaños, bodas, bautizos o baby showers.")
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.image("Imag/25_tarta cumple chocolate.jpg", use_container_width=True)
            st.image("Imag/26_tarta_cumple_lacazitos.jpg", use_container_width=True)
            st.image("Imag/24_tarta cumple cars.jpg", use_container_width=True)
        with col2:
            st.image("Imag/24_tarta cumple cara mario bross.jpg", use_container_width=True)
            st.image("Imag/23_tarta cumple patrulla canina.jpg", use_container_width=True)
            st.image("Imag/22_tarta cumple dinosaurio.jpg", use_container_width=True)
    st.markdown("⚡ Haz tu pedido online y disfruta del auténtico sabor peruano donde quieras.")


elif pagina == "Pasteles y Tortas":
    st.title("Pasteles y Tortas")
    st.markdown("<h6 style= 'margin-top: -15px; '>En 'Sabor a Perú', elaboramos todas nuestras exquisitas tortas y pasteles en tres tamaños, pensado para adaptarse a sus necesidades:</h6>" ,unsafe_allow_html=True)
    st.markdown("<h6 style= 'margin-top: -5px; '>1️⃣ Pequeña: para reuniones íntimas, rinde hasta 10 porciones.</h6>" ,unsafe_allow_html=True)
    st.markdown("<h6 style= 'margin-top: -5px; '>2️⃣ Mediano: perfecto para celebraciones de tamaño moderado, con capacidad para 15 porciones.</h6>" ,unsafe_allow_html=True)
    st.markdown("<h6 style= 'margin-top: -5px; '>3️⃣ Grande: diseñado para eventos más grandes, ofreciendo hasta 20 porciones.</h6>" ,unsafe_allow_html=True)
    with st.container(): 
        col1, col2 = st.columns(2)
        with col1:
            st.image("Imag/3_torta helada.jpg", use_container_width=True)
            st.markdown("<h6 style= 'margin-top: -5px; '>1️⃣ Pequeña: 35 € / 2️⃣ Mediano: 45 €  / 3️⃣ Grande: 60 € </h6>" ,unsafe_allow_html=True)
            st.image("", use_container_width=True)
            st.image("", use_container_width=True)
        with col2:
            st.image("", use_container_width=True)
            st.image("", use_container_width=True)
            st.image("", use_container_width=True)
    st.markdown("Descubre nuestro clásico más populares como la tarta húmeda de chocolate, el pastel de tres leches, la torta helada o el pie de limón, entre muchos otros. También realizamos tartas personalizadas para cumpleaños, bodas, bautizos o baby showers.")
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.image("Imag/25_tarta cumple chocolate.jpg", use_container_width=True)
            st.image("Imag/26_tarta_cumple_lacazitos.jpg", use_container_width=True)
            st.image("Imag/24_tarta cumple cars.jpg", use_container_width=True)
        with col2:
            st.image("Imag/24_tarta cumple cara mario bross.jpg", use_container_width=True)
            st.image("Imag/23_tarta cumple patrulla canina.jpg", use_container_width=True)
            st.image("Imag/22_tarta cumple dinosaurio.jpg", use_container_width=True)
    st.markdown("⚡ Haz tu pedido online y disfruta del auténtico sabor peruano donde quieras.")
    
elif pagina == "Cheescakes":
    st.title("Cheescakes")
    
elif pagina == "Nuestros Pies":
    st.title("Nuestros Pies")
   
elif pagina == "Empanadas":
    st.title("Empanadas")

elif pagina == "Contacto":
    st.title("Contacto")