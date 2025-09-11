import streamlit as st

# Título de la aplicación
st.title("🔄 Conversor de Unidades de Velocidad")

# Entrada del valor de velocidad
valor = st.number_input("Ingresa el valor de la velocidad:", min_value=0.0, format="%.2f")

# Selección de tipo de conversión
opcion = st.radio(
    "Selecciona la conversión:",
    ("Kilómetros por hora (km/h) ➝ Metros por segundo (m/s)",
     "Metros por segundo (m/s) ➝ Kilómetros por hora (km/h)")
)

# Botón para ejecutar la conversión
if st.button("Convertir"):
    if opcion == "Kilómetros por hora (km/h) ➝ Metros por segundo (m/s)":
        resultado = valor / 3.6
        st.success(f"{valor:.2f} km/h = {resultado:.2f} m/s")
    else:
        resultado = valor * 3.6
        st.success(f"{valor:.2f} m/s = {resultado:.2f} km/h")


