import streamlit as st
from utils.device_data import get_device_data

def display():
    rooms = get_device_data()

    tabs = st.tabs(list(rooms.keys()))
    for tab, (room, devices) in zip(tabs, rooms.items()):
        with tab:
            st.subheader(room)
            for device, description, image in devices:
                col1, col2 = st.columns([1, 3])
                with col1:
                    st.image(image, caption=device, use_container_width=True)
                with col2:
                    st.write(f"**{device}**")
                    st.write(description)
                st.button(f"Gerät bearbeiten ({device})")
