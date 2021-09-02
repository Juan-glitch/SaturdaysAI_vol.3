import streamlit as st

# Visualizaciones
st.markdown("HELLO WORLD") # Titulo
st.markdown("__Con esto en negrita__") # Titulo pero en black
st.write("texto simple") # Texto simple 
st.write("__Texto simple en negrita__") # Texto simple en negrita 
st.markdown(":+1:") # Emoticonos?¿
st.markdown("<center>hello en html con propiedades</center>", True)
st.checkbox("Checkbox", help = "Información adicional")

# Checklist
if st.checkbox("Cbox interactivo", help = "Si me apretas, saco pecho"):
  """Texto random pero con emoticono :sneezing_face:"""
  """Otro texto pero con otra manera de poner emoticonos &#128520; """
  # Para más emoticonos: https://www.science.co.il/internet/html/Smileys.php
  
# Selector I
st.selectbox("Esto es un selectbox", ["Valor", "another-one", "Tercer-valor"]) # Encargado de efectuar un selectbox  
# st.multiselect("Y esto un multiselect", [1,2,3,4], default = [3,4])  # Efectua una selección mutiple

# Selector II
rad = st.radio("Esto es un botón radio", [1,2,3,4],
              format_func = lambda num: "Opcion " + str(num)) # Selecciona un valor y lo guarda para aplicarlo al modelo
st.write("El valor seleccionado ha sido " + str(rad))

# Slider
import datetime
st.slider("Entrega de proyecto - slider fechas", min_value = datetime.date(2021,9,1), max_value = datetime.date(2022,1,2), 
          value = [datetime.date(2021,9,15), datetime.date(2021,10,1)])
st.slider("Temperatura habitación - slider string", min_value = ["congelado", "hace frio", "templado","tengo calor", "ardiendo"], 
          value =["hace frio","templado"])
