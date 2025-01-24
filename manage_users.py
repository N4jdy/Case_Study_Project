import streamlit as st

def display():
    menu = ["Nutzer anlegen", "Nutzer anzeigen"]
    user_choice = st.radio("Optionen", menu)

    if user_choice == "Nutzer anlegen":
        st.subheader("Neuen Nutzer anlegen")
        with st.form("user_form"):
            username = st.text_input("Benutzername")
            email = st.text_input("E-Mail-Adresse")
            role = st.selectbox("Rolle", ["Administrator", "Nutzer"])
            submitted = st.form_submit_button("Speichern")

            if submitted:
                st.success(f"Nutzer {username} wurde erfolgreich angelegt!")

    elif user_choice == "Nutzer anzeigen":
        st.subheader("Bestehende Nutzer anzeigen")
        st.write("[Platzhalter: Liste der Nutzer]")
