import streamlit as st
import pandas as pd
import db
from objects import Employee

# Functions
def add_employee(name, email, role, username, password):
    employee = Employee(name=name,
                            email=email,
                            roleid=db.get_roleid_from_role(str(role)),
                             username=username,
                             password=password)
    db.add_employee(employee)

def update_employee(employeeid, name, email, role, username, password):
    employee = Employee(employeeid = employeeid,
                            name=name,
                            email=email,
                            roleid=roleid,
                            username=username,
                            password=password)
    db.update_employee(employee)

    st.write("Uploading user data to database.")
    
    return None


st.title("Employee Vecta Corp Menu")

# Conexión a la base de datos sqlite
db.connect()

# Crear una lista de opciones
opciones = ["View", "Add", "Delete", "Update"]

# Crear el menú desplegable
selection = st.selectbox("Selecciona una opción:", opciones)

if selection == "View":
    st.write("VECTA CORP HELP DESK EMPLOYEES")
    employees = db.get_employees()

    columns = ["employeeid", "name", "username",
               "password", "email", "role"]
    df = pd.DataFrame(columns=columns)

    for employee in employees:
        new_data = {
            'employeeid':[employee.employeeid],
            'name':[employee.name],
            'username':[employee.username],
            'password':[employee.password],
            'email':[employee.email],
            'role':[db.get_role_from_roleid(employee.roleid)]
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

        submitted = st.form_submit_button(label="Submit", type='primary')

        if submitted:
            add_employee(name, email,role, username, password)

if selection=="Delete":

    with st.form("Delete Employee Form"):

        employeeid = st.text_input(label="Put the employee id:")

        delete_button = st.form_submit_button(label="Show description", type="primary")    

        if delete_button:
            employee = db.get_employee(employeeid)

            st.write(f"Employee Name: {employee.name}")
            st.write(f"Username: {employee.username}")
            st.write(f"Role: {db.get_role_from_roleid(employee.roleid)}")

            st.subheader("Are you sure?")
        
        ok_button = st.form_submit_button(label="Delete", type="primary")

        if ok_button:
            db.delete_employee(employeeid)
            st.write(f"Employee has been removed.")

if selection=="Update":

    with st.form("Submit Form"):

        employeeid = st.text_input(label="Put the employee id:")

        show_button = st.form_submit_button(label="Show description", type="primary") 

        name = ""
        email = ""
        roleid = 0
        username = ""
        password = ""

        if show_button:
            employee = db.get_employee(employeeid)

            col1, col2 = st.columns(2)

            with col1:
                name = st.text_input(label="Name", value=employee.name)
                email = st.text_input(label="Email", value=employee.email)
                roleid = st.text_input(label="RoleID", value=employee.roleid)

            with col2:
                username = st.text_input(label="UserName", value=employee.username)
                password = st.text_input(label="Password", value=employee.password)

        update = st.form_submit_button(label="Update", type='primary')

        if update:
            st.write(f"Updating info ...")
            update_employee(employeeid, name, email, roleid, username, password)
        

           

        
    
    #@st.dialog("Are you sure")
    #def Box_Delete(employeeid):
    #    pass

    #if Box_Delete not in st.session_state:

        
        
        
