# --------------------- LIBRERIAS ---------------------

import streamlit as st
from streamlit_option_menu import option_menu
import base64
import os # Pendiente confirmar si es útil
import json # Pendiente confirmar si es útil
from PIL import Image, ExifTags # Para corregir la orientación de las imágenes
from io import BytesIO # Para manejar imágenes en memoria
import math
import urllib.parse # Para manejar URLs


# --------------------- CONFIGURACIÓN SITIO WEB ---------------------

st.set_page_config(page_title="Tortas Peruanas", 
                   page_icon="🍰", 
                   layout="wide")

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
add_bg_from_local(r"Imag\2_Fondo_supiro_limeño.jpg")  


# --------------------- PERSONALIZACIÓN DE PÁGINA y CREACIÓN DE FUNCIONES ---------------------

# Personalización de fondo/sidebar y columnas reponsivas para adaptación a móviles y ordenadores
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

# Función para corregir imagen
def corregir_orientacion(image_path):
    image = Image.open(image_path)
    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                break
        exif = image._getexif()
        if exif is not None:
            orientation = exif.get(orientation)
            if orientation == 3:
                image = image.rotate(180, expand=True)
            elif orientation == 6:
                image = image.rotate(270, expand=True)
            elif orientation == 8:
                image = image.rotate(90, expand=True)
    except:
        pass
    return image

# Función imagen en base 64
def imagen_a_base64(imagen):
    buffer = BytesIO()
    imagen.save(buffer, format="JPEG")
    return base64.b64encode(buffer.getvalue()).decode("utf-8")

# Función para mostrar los tamaños de la tartas
def mostrar_tamaños():
    st.markdown("<h6 style='margin-top: -15px;'>En 'Sabor a Perú', elaboramos todas nuestras exquisitas tortas y pasteles en tres tamaños:</h6>", unsafe_allow_html=True)
    st.markdown("<h6>1️⃣ Pequeña: rinde hasta 10 porciones.</h6>", unsafe_allow_html=True)
    st.markdown("<h6>2️⃣ Mediana: hasta 15 porciones.</h6>", unsafe_allow_html=True)
    st.markdown("<h6>3️⃣ Grande: para 20 porciones.</h6>", unsafe_allow_html=True)

# Personalización de las cartas de productos
st.markdown("""
<style>
.product-card {
    background-color: #1c1c1c;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 4px 15px rgba(255, 255, 255, 0.1);
    margin-bottom: 30px;
    text-align: center;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.product-card:hover {
    transform: scale(1.02);
    box-shadow: 0 6px 20px rgba(255, 255, 255, 0.3);
}
.product-image {
    border-radius: 12px;
    margin-bottom: 15px;
    width: 100%;
    height: auto;
}
.product-name {
    font-weight: bold;
    font-size: 20px;
    margin-bottom: 10px;
    color: #ffd700;
}
.product-desc {
    font-size: 15px;
    color: #ddd;
    margin-bottom: 12px;
}
.product-price {
    font-size: 15px;
    color: #ff6f61;
    font-weight: bold;
}
.buy-button {
    background-color: #ff6f61;
    color: white;
    padding: 8px 16px;
    border: none;
    border-radius: 8px;
    font-size: 14px;
    margin-top: 12px;
    cursor: pointer;
    transition: background-color 0.2s ease;
}
.buy-button:hover {
    background-color: #e85a4f;
}
</style>
""", unsafe_allow_html=True)


# Función para mostrar la tarjeta de productos
def mostrar_tarjetas(productos, columnas=3):
    for i in range(0, len(productos), columnas):
        cols = st.columns(columnas)
        for j in range(columnas):
            idx = i + j
            if idx < len(productos):
                p = productos[idx]
                imagen = corregir_orientacion(p["image"])
                img64 = imagen_a_base64(imagen)
                with cols[j]:
                    # Número de WhatsApp al que deben contactar
                    numero_whatsapp = "34630318586"

                    mensaje = f"Hola, quiero encargar la tarta {p['name']}. ¿Podrías darme más información?"
                    mensaje_codificado = urllib.parse.quote(mensaje)
                    link_whatsapp = f"https://wa.me/{numero_whatsapp}?text={mensaje_codificado}"

                    st.markdown(f"""
                        <div class="product-card">
                            <img src="data:image/jpeg;base64,{img64}" class="product-image"/>
                            <div class="product-name">{p['name']}</div>
                            <div class="product-desc">{p['desc']}</div>
                            <div class="product-price">Pequeña: {p['precios']['pequeña']} €</div>
                            <div class="product-price">Mediana: {p['precios']['mediana']} €</div>
                            <div class="product-price">Grande: {p['precios']['grande']} €</div>
                            <a href="{link_whatsapp}" target="_blank" class="buy-button">Encargar por WhatsApp</a>
                        </div>
                    """, unsafe_allow_html=True)

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
    mostrar_tamaños()
    
    pasteles = [
        {
            "name": "Torta de Chocolate",
            "desc": "Bizcocho húmedo con relleno de manjar y cobertura de chocolate.",
            "image": "Imag/4_torta de chocolate.jpg",
            "precios": {"pequeña": 35, "mediana": 45, "grande": 60}
        },
        {
            "name": "Torta Helada",
            "desc": "Postre frío con capas de gelatina, crema y bizcocho.",
            "image": "Imag/3_torta helada.jpg",
            "precios": {"pequeña": 30, "mediana": 40, "grande": 55}
        },
        {
            "name": "Tres Leches",
            "desc": "Bizcocho esponjoso bañado en leche condensada, evaporada y nata.",
            "image": "Imag/5_tarta tres leches.png",
            "precios": {"pequeña": 32, "mediana": 42, "grande": 58}
        }
    ]
    
    mostrar_tarjetas(pasteles, columnas=3)

elif pagina == "Cheescakes":
    st.title("Cheescakes")
    
elif pagina == "Nuestros Pies":
    st.title("Nuestros Pies")
   
elif pagina == "Empanadas":
    st.title("Empanadas")

elif pagina == "Contacto":
    st.title("Contacto")