import streamlit as st
import os

st.set_page_config(page_title="Importivos León", layout="wide")


col1, col2 = st.columns([1, 5]) 

with col1:
    st.image("logo.png", width=150)  

with col2:
    st.title("Nuestro Catálogo Deportivo")


st.markdown("<p style='font-size:16px; color: gray;'>Calle 52 # 16-31 Barrio San Miguel</p>", unsafe_allow_html=True)


carpeta = "catalogo"

# Soportar .jfif además de otras extensiones
extensiones_validas = (".png", ".jpg", ".jpeg", ".webp", ".jfif")
imagenes = [f for f in os.listdir(carpeta) if f.lower().endswith(extensiones_validas)]

imagenes.sort()

# Mostrar las imágenes en tabla (imagen + título + precio)
for archivo in imagenes:
    try:
        # Separar título y precio usando el nombre del archivo
        nombre_archivo = os.path.splitext(archivo)[0]  # quita extensión
        titulo, precio = nombre_archivo.split(" - ")
        precio_formateado = "{:,.0f}".format(int(precio))  # Convierte el precio en un número y lo formatea

        # Crear las columnas para imagen, título y precio
        col1, col2, col3 = st.columns([2, 3, 1])

        with col1:
            st.image(os.path.join(carpeta, archivo), use_container_width=True)

        with col2:
            st.markdown(f"### {titulo}")

        with col3:
            st.markdown(f"<h4 style='color: green;'>${precio_formateado}</h4>", unsafe_allow_html=True)

        st.markdown("---") 
    except ValueError:
        st.warning(f"El archivo '{archivo}' no tiene el formato esperado: 'nombre - precio.jfif'")