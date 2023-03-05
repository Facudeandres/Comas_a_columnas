import pandas as pd
import numpy as np
import streamlit as st
import re

st.header(":rainbow::rainbow: La peor App de la historia :rainbow::rainbow:")

convertidor_coma_a_column = "Ingrese texto delimitado por comas"
convertidor_column_a_coma = "Ingrese texto en columnas"

# Dividimos la pantalla en 3 columnas, la primera y la tercera para los inputs y la segunda para el botón
col1, col2, col3 = st.beta_columns([1, 3, 1])

# Creamos los inputs dentro de las columnas 1 y 3
with col1:
    text_input_coma = st.text_input(convertidor_coma_a_column, height=150)
with col3:
    text_input_column = st.text_area(convertidor_column_a_coma, height=150)

# Botón en el centro de la pantalla
with col2:
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
            raise ValueError(":ghost: Pusiste cualquier cosa Botardo :ghost:")
