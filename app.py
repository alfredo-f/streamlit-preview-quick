import streamlit as st

st.set_page_config(layout="wide")

st.markdown("""
<style>
/*
Target the container of the first expander element on the page.
We are using the 'data-testid' attribute for a more reliable selection.
*/
div[data-testid="stExpander"]:nth-of-type(1) {
    position: relative; /* Set position context for the overlay */
    overflow: hidden;   /* Hide the parts of the ribbon outside the border */
}

/*
Create the "PREVIEW" ribbon using the ::before pseudo-element.
*/
div[data-testid="stExpander"]:nth-of-type(1)::before {
    content: 'PREVIEW';
    position: absolute;
    top: 20px;
    right: -45px; /* Position it on the right */
    transform: rotate(45deg); /* Rotate it */
    background-color: #007bff; /* A different color for visibility */
    color: white;
    padding: 5px 40px;
    font-size: 0.75rem;
    font-weight: bold;
    text-align: center;
    box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
    z-index: 1; /* Ensure it's on top of other content */
}
</style>
""", unsafe_allow_html=True)


# --- Your Streamlit App ---

st.header("Feature Dashboard")

# The first expander will get the "PREVIEW" ribbon
with st.expander("AI-Powered Data Analysis"):
    st.info("This functionality is in a preview state. Results may not be final.")
    st.slider("Confidence Threshold", 0.0, 1.0, 0.75)
    st.button("Analyze Data")

# A regular expander for comparison
with st.expander("Standard Reporting"):
    st.write("This is a stable and fully functional feature.")
    st.text_input("Enter your name")
