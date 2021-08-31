import streamlit as st

st.markdown("HELLO WORLD") # Titulo
st.markdown("__Con esto en negrita__") # Titulo pero en black
st.write("texto simple") # Texto simple 
st.write("__Texto simple en negrita__") # Texto simple en negrita 
st.markdown(":+1:") # Emoticonos?¿
st.markdown("<center>hello en html con propiedades</center>", True)
st.checkbox("Checkbox", help = "Información adicional")

if st.checkbox("Cbox interactivo", help = "Si me apretas, saco pecho"):
  """Texto random pero con emoticono :sneezing_face:"""
  """Otro texto pero con otra manera de poner emoticonos :&#128520;:"""
  # Para más emoticonos: https://www.science.co.il/internet/html/Smileys.php
  
 
