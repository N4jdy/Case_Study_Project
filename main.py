import streamlit as st
st.write("## Wartungskosten")

# Callbacks for the number inputs
def update_price_from_euro():
    st.session_state.price_dollar = st.session_state.price_euro * 1.1

def update_price_from_dollar():
    st.session_state.price_euro = st.session_state.price_dollar * 0.9

# Number inputs for the maintenance costs
st.number_input(label="Wartungskosten in Euro", 
                            key = "price_euro",
                            on_change=update_price_from_euro)

st.number_input(label="Wartungskosten in Dollar", 
                            key = "price_dollar",
                            on_change=update_price_from_dollar)