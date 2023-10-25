import streamlit as st
import pandas as pd

# Establecer el ancho del sidebar
st.set_page_config(layout="wide")

# Cargar datos
data = pd.read_csv("Datasets/Applicant.csv")

# Encabezado de la aplicación
st.title("Visualización de Datos")


# Sidebar para la selección de roles
st.sidebar.title("Filtrar Roles")
selected_roles = st.sidebar.multiselect("Selecciona Roles", data["role"].unique())

# Sidebar para la selección de cantidad de años
st.sidebar.title("Filtrar por Cantidad de Años")
selected_years_option = st.sidebar.selectbox("Selecciona Cantidad de Años", ["Todos","0 a 2 años", "2 a 5 años", "> 5 años"])

if selected_years_option == "Todos":
    filtered_data = data[data["TotalMeces"] > 0] # No aplicar ningún filtro por años
else:
    # Mapear la opción seleccionada a un rango de años
    if selected_years_option == "0 a 2 años":
        selected_years = (0, 2)
        # Filtrar por TotalMeces en el rango de 0 a 48
        filtered_data = data[(data["TotalMeces"] >= selected_years[0]) & (data["TotalMeces"] <= 24)]
    elif selected_years_option == "2 a 5 años":
        selected_years = (2, 5)
        # Filtrar por TotalMeces en el rango de 2 a 60
        filtered_data = data[ (data["TotalMeces"] >= 24)& (data["TotalMeces"] <= 59)]
    else:
        selected_years = (5, float('inf'))
        # Filtrar por TotalMeces mayor a 60S
        filtered_data = data[data["TotalMeces"] > 59]

# Verificar si se han seleccionado roles
if not selected_roles:
    # Mostrar los datos completos con las columnas seleccionadas
    st.dataframe(filtered_data[['userId', 'role', 'TotalMeces', 'señority']], width=10000, height=750)
else:
    # Filtrar los datos según los roles seleccionados
    filtered_data = filtered_data[filtered_data["role"].isin(selected_roles)]
    
    # Mostrar los datos filtrados con columnas seleccionadas y más anchas
    st.dataframe(filtered_data[['userId', 'role', 'TotalMeces', 'señority']], width=10000, height=750)
