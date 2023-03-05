import pandas as pd
import numpy as np
import streamlit as st
import re

# Tamaño del cuadro de texto
TEXT_BOX_HEIGHT = 5
TEXT_BOX_WIDTH = 7

# Definir la interfaz
st.title(":rainbow::rainbow: La peor App de la historia :rainbow::rainbow:")
st.write("Ingrese texto en uno o ambos de los siguientes cuadros de texto, luego haga clic en el botón 'Convertir Texto'.")

# Cuadro de texto para texto delimitado por comas
st.subheader("Texto delimitado por comas")
text_input_coma = st.text_input("Ingrese texto delimitado por comas", height=TEXT_BOX_HEIGHT)

# Cuadro de texto para texto en columnas
st.subheader("Texto en columnas")
text_input_column = st.text_area("Ingrese texto en columnas, delimitado por enter", height=TEXT_BOX_HEIGHT, width=TEXT_BOX_WIDTH)

# Funciones de conversión
def convertidor_coma_a_column(text):
    if ',' in text:
        return "\n".join(text.split(", ")).strip()
    else:
        raise ValueError(":ghost: Pusiste cualquier cosa Botardo :ghost:")

def convertidor_column_a_coma(text):
    lines = text.splitlines()
    if any(',' in line for line in lines):
        raise ValueError(":ghost: Pusiste cualquier cosa Botardo :ghost:")
    return ", ".join(lines)

# Botón para convertir texto
if st.button(":hot_pepper: Convertir Texto :hot_pepper:"):
    if text_input_coma:
        result = convertidor_coma_a_column(text_input_coma)
        st.success("Texto convertido:")
        st.code(result, language='python')
    elif text_input_column:
        try:
            result = convertidor_column_a_coma(text_input_column)
            st.success("Texto convertido:")
            st.code(result, language='python')
        except ValueError as e:
            st.error(str(e))
    else:
        st.warning("No se ingresó ningún texto.")
