import streamlit as st

# --- Custom CSS for the "Preview" Billboard-Style Overlay ---
st.markdown("""
<style>
/* Target the container of the first expander */
.st-emotion-cache-1de5w8b:nth-of-type(1) {
    position: relative; /* This is crucial for positioning the overlay */
    overflow: hidden; /* This will hide the part of the ribbon that goes outside the container */
}

/* Style the "Preview" ribbon */
.st-emotion-cache-1de5w8b:nth-of-type(1)::before {
    content: 'PREVIEW';
    position: absolute;
    top: 20px;
    left: -45px;
    transform: rotate(-45deg);
    background-color: #FF4B4B; /* A noticeable color */
    color: white;
    padding: 5px 40px;
    font-size: 0.75rem;
    font-weight: bold;
    text-align: center;
    box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
    z-index: 1; /* Ensure it's on top of the expander content */
}
</style>
""", unsafe_allow_html=True)


# --- Your Streamlit App ---

st.header("Feature Dashboard")

# Expander with the "Preview" overlay
with st.expander("AI-Powered Data Analysis", expanded=True):
    st.info("This functionality is in a preview state. Results may not be final.")
    st.slider("Confidence Threshold", 0.0, 1.0, 0.75)
    st.button("Analyze Data")

# A regular expander for comparison
with st.expander("Standard Reporting"):
    st.write("This is a stable and fully functional feature.")
    st.text_input("Enter your name")
