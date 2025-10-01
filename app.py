import streamlit as st

st.set_page_config(layout="wide")

# --- Custom CSS for the "Preview" Billboard-Style Overlay ---
st.markdown("""
<style>
/*
Target all expander containers using the stable 'data-testid' attribute.
*/
div[data-testid="stExpander"] {
    position: relative; /* Needed for the overlay positioning */
    overflow: hidden;   /* This clips the ribbon for the corner effect */
}

/*
Create and style the "PREVIEW" ribbon.
The 'top' and 'right' values have been adjusted for full visibility.
*/
div[data-testid="stExpander"]::before {
    content: 'PREVIEW';
    position: absolute;
    top: 7px;
    right: -18px;
    transform: rotate(45deg);
    background-color: #007bff;
    color: white;
    padding: 3px 35px;
    line-height: 20px;
    font-size: 11px;
    font-weight: bold;
    text-align: center;
    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
    z-index: 1;
}
</style>
""", unsafe_allow_html=True)


# --- Your Streamlit App ---

st.header("Feature Dashboard")

# Expander with the "Preview" overlay
with st.expander("AI-Powered Data Analysis"):
    st.info("This functionality is in a preview state. Results may not be final.")
    st.slider("Confidence Threshold", 0.0, 1.0, 0.75)
    st.button("Analyze Data")

# Another expander, which will also get the overlay
with st.expander("Standard Reporting"):
    st.write("This is a stable and fully functional feature.")
    st.text_input("Enter your name")
