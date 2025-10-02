import streamlit as st

st.title("Hiding the Multiselect Tooltip")

# Inject custom CSS to hide the tooltip element
st.markdown("""
<style>
    /* This targets the tooltip element itself. */
    [data-baseweb="tooltip"] {
        display: none !important;
    }
</style>
""", unsafe_allow_html=True)

options = [
    "AGLIANA VIA ENEA COLZI 13/15/17AKSDHGUJSHFGSHFJKHFJKASHFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",
    "ABBASANTA VIA S. AGOSTINO",
    "ACQUI TERME ROMITA 80",
    "ALBA CORSO ASTI 24",
    "ALBENGA PIAVE 27"
]

st.multiselect(
    "Choose options",
    options,
    placeholder="Choose options"
)
