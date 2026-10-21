import streamlit as st

# Configuración de la página web
st.set_page_config(page_title="Calculadora de IMC", page_icon="⚖️", layout="centered")

# Título y descripción
st.title("⚖️ Calculadora de Índice de Masa Corporal (IMC)")
st.write("Ingresa tus datos a continuación para conocer tu IMC y tu estado de salud.")

# Contenedor para los datos de entrada
st.subheader("Tus datos")
peso = st.number_input("Peso (en kg)", min_value=1.0, max_value=300.0, value=70.0, step=0.5)
estatura = st.number_input("Estatura (en metros, ej: 1.75)", min_value=0.5, max_value=2.5, value=1.70, step=0.01)

# Botón para calcular
if st.button("Calcular mi IMC", type="primary"):
    if estatura > 0:
        # Fórmula del IMC
        imc = peso / (estatura ** 2)
        
        # Mostrar el resultado
        st.divider()
        st.subheader(f"Tu resultado: **{imc:.2f}**")
        
        # Clasificación médica
        if imc < 18.5:
            st.warning("Clasificación: **Bajo peso**. Te sugerimos consultar con un especialista en nutrición.")
        elif 18.5 <= imc < 25:
            st.success("Clasificación: **Peso normal (Saludable)**. ¡Excelente trabajo!")
        elif 25 <= imc < 30:
            st.warning("Clasificación: **Sobrepeso**. Intenta mantener hábitos activos y una dieta equilibrada.")
        elif 30 <= imc < 35:
            st.error("Clasificación: **Obesidad Grado I**. Considera buscar orientación profesional.")
        elif 35 <= imc < 40:
            st.error("Clasificación: **Obesidad Grado II**. Es recomendable acudir al médico.")
        else:
            st.error("Clasificación: **Obesidad Grado III (Mórbida)**. Busca atención médica prioritaria.")

# --- SECCIÓN DE CRÉDITOS ---
st.divider()
st.caption("💻 **Hecho por Julio Moroyoqui **")