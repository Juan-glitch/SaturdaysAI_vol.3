import streamlit as st

st.markdown("HELLO WORLD") # Titulo
st.markdown("__Con esto en negrita__") # Titulo pero en black
st.write("texto simple") # Texto simple 
st.write("__Texto simple en negrita__") # Texto simple en negrita 
st.markdown(":+1:") # Emoticonos?¿
st.markdown("<center>hello en html con propiedades</center>", True)
streamlit.checkbox("Checkbox", help = "Información adicional")
