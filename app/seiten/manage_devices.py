import streamlit as st
import json
import os

def display():
    devices_db_file = os.path.join(os.path.dirname(__file__), 'database.json')
    with open(devices_db_file, 'r', encoding='utf-8') as file:
        devices_db = json.load(file)

  

    categories = {}
    for device_id, device_info in devices_db['devices'].items():
        category = device_info['category']
        if category not in categories:
            categories[category] = []
        categories[category].append(device_info)


   
    tabs = st.tabs(list(categories.keys()))

    for tab, (category, devices) in zip(tabs, categories.items()):
        with tab:
            st.subheader(category)
            for device_info in devices:
                device_name = device_info['device_name']
                managed_by_user_id = device_info['managed_by_user_id']
                description = device_info['description']
                image_url = device_info['image_url']
                
                col1, col2 = st.columns([1, 3])
                with col1:
                    st.image(image_url, caption=device_name, use_container_width=True)
                with col2:
                    st.write(f"**{device_name}**")
                    st.write(description)
                    st.write(managed_by_user_id)
                if st.button(f"Gerät bearbeiten ({device_name})"):
                    st.success(f"Gerät {device_name} bearbeitet.")

