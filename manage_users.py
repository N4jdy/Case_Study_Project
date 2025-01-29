import streamlit as st
from users import User

def display():
    menu = ["Nutzer anlegen", "Nutzer anzeigen"]
    user_choice = st.radio("Optionen", menu)

    if user_choice == "Nutzer anlegen":
        st.subheader("Neuen Nutzer anlegen")
        users_list = User.find_all()
        
        with st.form("user_form"):
            new_username = st.text_input("Benutzername")
            new_email = st.text_input("E-Mail-Adresse")
            new_role = st.selectbox("Rolle", ["Administrator", "Nutzer"])
            new_password = st.text_input("Passwort", type="password")
            submitted = st.form_submit_button("Speichern")

            if submitted and new_username and new_email:
                new_id = len(users_list) + 1
                new_user = User(new_id, new_username, new_email, new_role, new_password)
                new_user.store_data()
                st.success(f"Nutzer {new_username} wurde erfolgreich angelegt!")
            elif submitted:
                st.error("Bitte alle Felder ausfüllen!")

    elif user_choice == "Nutzer anzeigen":
        st.subheader("Bestehende Nutzer anzeigen")
        users = User.find_all()
        if users:
            for user_info in users:
                st.write(f"**ID:** {user_info.id}")
                st.write(f"**Name:** {user_info.username}")
                st.write(f"**E-Mail:** {user_info.email}")
                st.write(f"**Rolle:** {user_info.role}")
                st.write("---")
        else:
            st.write("Keine Nutzer gefunden.")
