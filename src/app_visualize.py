import streamlit as st
import pandas as pd
import db
from objects import Employee

st.title("Employee Vecta Corp Menu")

# Conexión a la base de datos sqlite
db.connect()

# Crear una lista de opciones
opciones = ["View", "Add", "Delete"]

# Crear el menú desplegable
selection = st.selectbox("Selecciona una opción:", opciones)

if selection == "View":
    st.write("VECTA CORP HELP DESK EMPLOYEES")
    employees = db.get_employees()

    columns = ["employeeid", "name", "username",
               "password", "email", "roleid"]
    df = pd.DataFrame(columns=columns)

    for employee in employees:
        new_data = {
            'employeeid':[employee.employeeid],
            'name':[employee.name],
            'username':[employee.username],
            'password':[employee.password],
            'email':[employee.email],
            'roleid':[db.get_role_from_roleid(employee.roleid)]
        }
        new_df = pd.DataFrame(new_data)
        df = pd.concat([df, new_df])

    st.table(df)

if selection== "Add":

    with st.form(key='Add new employee:'):

        col1, col2 = st.columns(2)

        with col1:
            name = st.text_input(label="Name")
            email = st.text_input(label="Email")
            role = st.text_input(label="Role")

        with col2:
            username = st.text_input(label="UserName")
            password = st.text_input(label="Password")

        st.form_submit_button(label="Submit", type='primary')

        employee = Employee(name=name,
                            email=email,
                            roleid=db.get_roleid_from_role(str(role)),
                             username=username,
                             password=password)
        
        db.add_employee(employee)
        st.write("Uploading user data to database.")