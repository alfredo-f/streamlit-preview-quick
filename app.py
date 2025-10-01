import streamlit as st

# --- Custom CSS for the "Preview" Badge ---
st.markdown("""
<style>
/* Target the Streamlit expander header */
.st-emotion-cache-1de5w8b:nth-of-type(1) .st-emotion-cache-p5c717 {
    position: relative;
    padding-right: 3rem; /* Add some padding to make space for the badge */
}

/* Style the "Preview" badge using a pseudo-element */
.st-emotion-cache-1de5w8b:nth-of-type(1) .st-emotion-cache-p5c717::after {
    content: 'Preview';
    position: absolute;
    right: 1rem;
    top: 50%;
    transform: translateY(-50%);
    background-color: #FF4B4B;
    color: white;
    padding: 0.2rem 0.5rem;
    border-radius: 0.25rem;
    font-size: 0.75rem;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# --- Your Streamlit App ---
st.header("App Features")

# Expander with the "Preview" badge
with st.expander("New Awesome Feature"):
    st.write("This functionality is in preview mode. Please provide feedback!")
    st.slider("Adjust a parameter", 0, 100, 50)

# A regular expander for comparison
with st.expander("Stable Feature"):
    st.write("This is a stable and fully functional feature.")
    st.text_input("Enter some text")
