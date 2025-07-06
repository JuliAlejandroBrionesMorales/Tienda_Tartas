# --------------------- LIBRERIAS ---------------------

import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image, ExifTags  # Para corregir la orientación de las imágenes
from io import BytesIO  # Para manejar imágenes en memoria
import urllib.parse  # Para manejar URLs
import base64

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
                background-image: url(data:image/png;base64,{encoded_string.decode()});
                background-size: cover;
                background-attachment: fixed;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )
add_bg_from_local(r"Imag/2_Fondo_supiro_limeño.jpg")  


# --------------------- PERSONALIZACIÓN DE PÁGINA y BOTÓN FLOTANTE ---------------------

st.markdown("""
<style>
[data-testid="stSidebar"] {
    background-color: #000000 !important;
}
[data-testid="stSidebar"] * {
    color: white;
    text-shadow: 2px 2px 6px rgba(0,0,0,0.7);
}
body, h1, h2, h3, h4, h5, h6, div, p, ul, li {
    color: white;
    text-shadow: 2px 2px 6px rgba(0,0,0,0.7);
}
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

/* Botón flotante WhatsApp */
.floating-whatsapp {
    position: fixed;
    bottom: 25px;
    right: 25px;
    background-color: #25d366;
    border-radius: 50%;
    width: 60px;
    height: 60px;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 9999;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.3);
    transition: background-color 0.3s ease;
}
.floating-whatsapp:hover {
    background-color: #1ebe5d;
}
.floating-whatsapp img {
    width: 32px;
    height: 32px;
}
</style>
<a href="https://wa.me/34695605067" class="floating-whatsapp" target="_blank">
    <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" alt="WhatsApp"/>
</a>
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

# Función para mostrar los tamaños de las tartas con texto en formato h5
def mostrar_tamaños():
    st.markdown("<h5 style='margin-top: -15px;'>En 'Sabor a Perú', elaboramos todas nuestras exquisitas tortas y pasteles en tres tamaños:</h5>", unsafe_allow_html=True)
    st.markdown("<h5>1️⃣ Pequeña: rinde hasta 10 porciones.</h5>", unsafe_allow_html=True)
    st.markdown("<h5>2️⃣ Mediana: hasta 15 porciones.</h5>", unsafe_allow_html=True)
    st.markdown("<h5>3️⃣ Grande: para 20 porciones.</h5>", unsafe_allow_html=True)


# Personalización de las cartas de productos (con espacio mejorado)
st.markdown("""
<style>
.product-card {
    background-color: #1c1c1c;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 4px 15px rgba(255, 255, 255, 0.1);
    margin-bottom: 30px;
    text-align: center;
    color: white;
    text-shadow: none;
}
.product-card * {
    text-shadow: none !important;
}

/* Imagen */
.product-image {
    border-radius: 12px;
    margin-bottom: 15px;
    width: 100%;
    height: auto;
}

/* Título: blanco y más grande */
.product-name {
    font-weight: bold;
    font-size: 22px;
    margin-bottom: 10px;
    color: white;
}

/* Descripción: blanco y más grande */
.product-desc {
    font-size: 17px;
    color: white;
    margin-bottom: 20px;  /* más espacio para el botón */
}

/* Precios: blanco */
.product-price {
    font-size: 15px;
    color: white;
    font-weight: bold;
    margin-bottom: 10px;
}

/* Botón */
.buy-button {
    background-color: #1ebe5d;
    color: white;
    padding: 10px 18px;
    border: none;
    border-radius: 8px;
    font-size: 15px;
    margin-top: 10px;  /* menor separación superior */
    cursor: pointer;
    transition: background-color 0.2s ease;
}
.buy-button:hover {
    background-color: #11a94e;
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
                    numero_whatsapp = "34695605067"

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

# Función para mostrar tarjetas de dulces de página "Dulces Tradicionales"
def mostrar_tarjetas_dulces(dulces):
    cols = st.columns(2)  # Puedes usar 2 o 3 columnas según prefieras
    for i, dulce in enumerate(dulces):
        with cols[i % 2]:  # Para repartir en columnas
            imagen = corregir_orientacion(dulce["image"])
            img64 = imagen_a_base64(imagen)

            mensaje = f"Hola, estoy interesado en el dulce tradicional: {dulce['name']}. ¿Me podrías dar más información sobre precios y disponibilidad?"
            mensaje_codificado = urllib.parse.quote(mensaje)
            link_whatsapp = f"https://wa.me/34695605067?text={mensaje_codificado}"

            st.markdown(f"""
                <div class="product-card">
                    <img src="data:image/jpeg;base64,{img64}" class="product-image"/>
                    <div class="product-name">{dulce['name']}</div>
                    <div class="product-desc">{dulce['desc']}</div>
                    <a href="{link_whatsapp}" target="_blank" class="buy-button">Consultar por WhatsApp</a>
                </div>
            """, unsafe_allow_html=True)


# --------------------- SIDEBAR ---------------------

st.sidebar.image("Imag/1_logo sabor a peru.png", use_container_width=True)
st.sidebar.title("Menu de Navegación")
st.sidebar.write('-------')

# Secciones como páginas independientes
pagina = st.sidebar.radio("Ir a:", ["Inicio","Pasteles y Tortas", "Cheescakes", "Nuestros Pies", "Empanadas", "Tartas de la Semana", "Dulces Tradicionales"])


# --------------------- PÁGINAS ---------------------

if pagina == "Inicio":
    st.markdown("<h5 style='margin-top: 10px;'>En <strong>'Sabor a Perú'</strong> elaboramos con cariño una gran variedad de tartas y postres tradicionales de la repostería peruana, listos para ser encargados desde la comodidad de tu hogar.</h5>", unsafe_allow_html=True)

    # Primer bloque de imágenes
    with st.container():
        col1, col2 = st.columns(2)
        for col, imgs in zip([col1, col2], [
            ["Imag/3_torta helada.jpg", "Imag/4_torta de chocolate.jpg", "Imag/5_tarta tres leches.png"],
            ["Imag/6_tarta volteada de piña.jpg", "Imag/7_keke de naranja.jpg", "Imag/8_Tarta de manzana.jpg"]
        ]):
            for img in imgs:
                st.markdown(
                    f"""
                    <div style="background-color: #111; padding: 10px; border-radius: 12px; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.5);">
                        <img src="data:image/jpeg;base64,{imagen_a_base64(corregir_orientacion(img))}" style="width: 100%; border-radius: 10px;"/>
                    </div>
                    """, unsafe_allow_html=True
                )

    st.markdown("<h5 style='margin-top: 10px;'>Descubre nuestros clásicos más populares como la tarta húmeda de chocolate, el pastel de tres leches, la torta helada o el pie de limón, entre muchos otros. También realizamos tartas personalizadas para cumpleaños, bodas, bautizos o baby showers.</h5>", unsafe_allow_html=True)

    # Segundo bloque de imágenes personalizadas
    with st.container():
        col1, col2 = st.columns(2)
        for col, imgs in zip([col1, col2], [
            ["Imag/25_tarta cumple chocolate.jpg", "Imag/26_tarta_cumple_lacazitos.jpg", "Imag/24_tarta cumple cars.jpg"],
            ["Imag/24_tarta cumple cara mario bross.jpg", "Imag/23_tarta cumple patrulla canina.jpg", "Imag/22_tarta cumple dinosaurio.jpg"]
        ]):
            for img in imgs:
                st.markdown(
                    f"""
                    <div style="background-color: #111; padding: 10px; border-radius: 12px; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.5);">
                        <img src="data:image/jpeg;base64,{imagen_a_base64(corregir_orientacion(img))}" style="width: 100%; border-radius: 10px;"/>
                    </div>
                    """, unsafe_allow_html=True
                )

    st.markdown("<h5 style='margin-top: 10px;'>⚡ Haz tu pedido online y disfruta del auténtico sabor peruano donde quieras.</h5>", unsafe_allow_html=True)

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
        },
        {
            "name": "Tarta Volteada de Piña",
            "desc": "Tarta invertida con piña caramelizada y bizcocho suave.",
            "image": "Imag/6_tarta volteada de piña.jpg",
            "precios": {"pequeña": 32, "mediana": 42, "grande": 58}
        },
        {
            "name": "Tarta de Manzana",
            "desc": "Deliciosa tarta con manzanas frescas y canela.",
            "image": "Imag/8_Tarta de manzana.jpg",
            "precios": {"pequeña": 32, "mediana": 42, "grande": 58}
        },
        {
            "name": "Crema Volteada", 
            "desc": "Delicioso postre tradicional peruano, elaborado con huevos, leche condensada y leche evaporada, con una suave textura y un irresistible baño de caramelo. ",
            "image": "Imag/17_Crema Volteada.jpg",  
            "precios": {"pequeña": 32, "mediana": 42, "grande": 58}
        }   

    ]
    mostrar_tarjetas(pasteles, columnas=3)

elif pagina == "Cheescakes":
    st.title("Cheescakes")
    mostrar_tamaños()
    cheescakes = [
        {
            "name": "CheeseCake de Fresa",
            "desc": "Una base crujiente de galleta coronada con una suave crema de queso y fresas frescas.",
            "image": "Imag/21_CheeseCake de fresa.jpg",
            "precios": {"pequeña": 32, "mediana": 42, "grande": 58}
        },
        {
            "name": "CheeseCake de Maracuyá",
            "desc": "Refrescante, tropical y exótica. Con una cobertura vibrante de maracuyá que contrasta perfectamente con la suavidad del cheesecake tradicional.",
            "image": "Imag/23_CheeseCake de Maracuya.jpg",
            "precios": {"pequeña": 32, "mediana": 42, "grande": 58}
        },
        {
            "name": "CheeseCake de Chocolate",
            "desc": "Un sueño para los amantes del chocolate: base de galleta de cacao, relleno cremoso de queso y cobertura de chocolate negro. Puro placer.",
            "image": "Imag/22_CheeseCake de Chocolate.jpg",
            "precios": {"pequeña": 32, "mediana": 42, "grande": 58}
        },
        {
            "name": "CheeseCake de Arándonos",
            "desc": "Sabor intenso y equilibrio perfecto entre lo dulce y lo ácido. Decorado con una deliciosa compota de arándanos naturales.",
            "image": "Imag/20_cheesecake de arandanos.jpg",
            "precios": {"pequeña": 32, "mediana": 42, "grande": 58}
        }
    ]
    mostrar_tarjetas(cheescakes, columnas=3)
    
elif pagina == "Nuestros Pies":
    st.title("Nuestros Pies")
    mostrar_tamaños()
    pies = [
        {
            "name": "Pie de Limón",
            "desc": "Base crujiente de galleta con un relleno cremoso y ácido de limón, cubierto con merengue flameado.",
            "image": "Imag/9_Pie de Limon.jpg",
            "precios": {"pequeña": 32, "mediana": 42, "grande": 58}
        },
        {
            "name": "Pie de Manzana",
            "desc": "Relleno de manzanas dulces y canela sobre una base dorada y hojaldrada.",
            "image": "Imag/10_Pie manzana.jpg",
            "precios": {"pequeña": 32, "mediana": 42, "grande": 58}
        },
        {
            "name": "Pie de Maracuya",
            "desc": "Delicioso toque tropical. Base crujiente y relleno suave de maracuyá que ofrece el equilibrio justo entre dulzor y acidez.",
            "image": "Imag/10_Pie de maracuya.jpg",
            "precios": {"pequeña": 32, "mediana": 42, "grande": 58}
        }
    ]
    mostrar_tarjetas(pies, columnas=3)
   
elif pagina == "Empanadas":
    st.title("Empanadas")
    st.markdown("<h5 style='margin-top: -15px;'>En 'Sabor a Perú', ofrecemos nuestras deliciosas empanadas en tres tamaños de pedido:</h5>", unsafe_allow_html=True)
    st.markdown("<h5>1️⃣ Pequeña: incluye 12 unidades.</h5>", unsafe_allow_html=True)
    st.markdown("<h5>2️⃣ Mediana: incluye 24 unidades.</h5>", unsafe_allow_html=True)
    st.markdown("<h5>3️⃣ Grande: incluye 36 unidades.</h5>", unsafe_allow_html=True)

    empanadas = [
        {
            "name": "Emapanada de Carne",
            "desc": "Clásica y sabrosa: carne de res sazonada al estilo peruano, cocinada con cebolla, huevo y aceitunas, dentro de una masa dorada al horno. Perfecta como tentempié o comida completa.",
            "image": "Imag/19_Empanada peruana.jpg",
            "precios": {"pequeña": 25, "mediana": 45, "grande": 60}
        },
        {
            "name": "Empanasada de Pollo",
            "desc": "Rellena de jugoso pollo desmenuzado, cebolla dorada y un toque de especias peruanas, envuelta en una masa suave y ligeramente crujiente.",
            "image": "Imag/27_Empanada de Pollo.jpg",
            "precios": {"pequeña": 25, "mediana": 45, "grande": 60}
        }
    ]
    mostrar_tarjetas(empanadas, columnas=2)

elif pagina == "Tartas de la Semana":
    st.title("Tartas de la Semana")
    
    st.markdown("""
    <h5 style='margin-top: -10px;'>🧁 Cada semana en <em>'Sabor a Perú'</em> preparamos 3 tartas diferentes para que puedas disfrutarlas <strong>por porciones</strong>.</h5>
    <h5 style='margin-top: 10px;'>Estas tartas pueden variar cada fin de semana y se venden por trozos (tajadas) a <strong>3 €</strong> cada uno.</h5>

    <h5 style='margin-top: 10px;'><ul style='margin-left: 20px; list-style: none; padding-left: 0;'>
        <li>🍫 <strong>Torta de Chocolate</strong></li>
        <li>🍋 <strong>Pie de Limón</strong></li>
        <li>🍰 <strong>Torta Helada</strong></li>
        <li>🥛 <strong>Tarta Tres Leches</strong></li>
        <li>🍎 <strong>Tarta de Manzana</strong></li>
    </ul></h5>

    <h5 style='margin-top: 20px;'>📦 <strong>¡Entrega gratuita a domicilio a partir de 5 trozos!</strong> (puedes combinar sabores)<br>
    🚚 Servicio disponible solo en la zona de <strong>Madrid Sur</strong><br>
    🗓️ Entregas los <strong>sábados por la mañana</strong>, directamente en tu domicilio.</h5>
    """, unsafe_allow_html=True)

    # Tarjetas para cada tarta
    tartas_semana = [
        {
            "nombre": "Torta de Chocolate",
            "desc": "Bizcocho húmedo con relleno de manjar y cobertura de chocolate.",
            "imagen": "Imag/4_torta de chocolate.jpg"
        },
        {
            "nombre": "Pie de Limón",
            "desc": "Base crocante con relleno cremoso de limón y merengue.",
            "imagen": "Imag/9_Pie de Limon.jpg"
        },
        {
            "nombre": "Torta Helada",
            "desc": "Postre tradicional con gelatina y crema batida.",
            "imagen": "Imag/3_torta helada.jpg"
        },
        {
            "nombre": "Tarta Tres Leches",
            "desc": "Bizcocho esponjoso bañado en leche condensada, evaporada y nata.",
            "imagen": "Imag/5_tarta tres leches.png"
        },
        {
            "nombre": "CheeseCake de Maracuya",
            "desc": "Refrescante, tropical y exótica. Con una cobertura vibrante de maracuyá que contrasta perfectamente con la suavidad del cheesecake tradicional.",
            "imagen": "Imag/23_CheeseCake de Maracuya.jpg"
        },
    ]

    st.markdown("<br>", unsafe_allow_html=True)
    cols = st.columns(2)
    for i, tarta in enumerate(tartas_semana):
        with cols[i % 2]:
            with st.container():
                st.markdown(f"""
                    <div class="product-card">
                        <img src="data:image/jpeg;base64,{imagen_a_base64(corregir_orientacion(tarta['imagen']))}" class="product-image"/>
                        <div class="product-name">{tarta['nombre']}</div>
                        <div class="product-desc">{tarta['desc']}</div>
                        <div class="product-price">Precio por trozo: 3 €</div>
                        <a href="https://wa.me/34695605067?text=Hola,%20quiero%20encargar%20la%20{urllib.parse.quote(tarta['nombre'])}" target="_blank" class="buy-button">Encargar por WhatsApp</a>
                    </div>
                """, unsafe_allow_html=True)


elif pagina == "Dulces Tradicionales": 
    st.title("Dulces Tradicionales")
    st.markdown("<h5 style='margin-top: 10px;'>Estos dulces están disponibles bajo encargo personalizado. El precio puede variar según la cantidad y requisitos específicos del cliente.</h5>", unsafe_allow_html=True)
    dulces_tradicionales = [
    {
        "name": "Alfajores Peruanos",
        "desc": "Galletas suaves rellenas de manjar blanco y espolvoreadas con azúcar glas.",
        "image": "Imag/16_Alfajores peruanos.jpg"
    },
    {
        "name": "Picarones",
        "desc": "Rosquillas tradicionales hechas con zapallo y camote, fritas y bañadas en miel de chancaca. Pueden prepararse con masa de harina o de yuca.",
        "image": "Imag/14_Picarones.jpg"
    },
    {
        "name": "Leche Asada",
        "desc": "Postre cremoso horneado con textura similar al flan.",
        "image": "Imag/18_Leche Asada.jpg"
    },
    {
        "name": "Suspiro Limeño",
        "desc": "Postre tradicional con base de manjar blanco y merengue al oporto.",
        "image": "Imag/13_Suspiro a la Limeña.jpg"
    },
    ]
    mostrar_tarjetas_dulces(dulces_tradicionales)

