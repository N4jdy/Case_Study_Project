import streamlit as st

def display():
    st.success("Erfolgreich eingeloggt!")
    st.write("Angemeldet als:")
    container = st.container(border=True)
    container.write(st.session_state.get('role'))
    container.write(f"Name: {st.session_state.get('name')}")
    container.write(f"Email: {st.session_state.get('email')}")
    #container.write(f"Passwort: {st.session_state.get('passwort')}")
