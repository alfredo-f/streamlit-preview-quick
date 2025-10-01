import streamlit as st

st.set_page_config(layout="wide")

# --- Custom CSS for the "Preview" Billboard-Style Overlay with Animation ---
st.markdown("""
<style>
/*
Target all expander containers using the stable 'data-testid' attribute.
*/
div[data-testid="stExpander"] {
    position: relative; /* Needed for the overlay positioning */
    overflow: hidden;   /* This is the key: it clips anything outside its bounds */
}

/*
Create and style the "PREVIEW" ribbon.
The 'top' and 'right' values have been adjusted to hide the ribbon's end.
*/
div[data-testid="stExpander"]::before {
    content: 'PREVIEW';
    position: absolute;
    
    /* === ADJUSTED VALUES === */
    top: 12px;       /* Pushes the ribbon down slightly */
    right: -28px;      /* Pushes the ribbon further to the right */
    padding: 3px 40px; /* Increased padding to give it more length */
    /* ======================= */

    transform: rotate(45deg);
    background-color: #007bff;
    color: white;
    line-height: 20px;
    font-size: 11px;
    font-weight: bold;
    text-align: center;
    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
    z-index: 1;

    /* Soft shimmer effect from the previous step */
    background-image: linear-gradient(
        100deg, 
        transparent 20%, 
        rgba(255, 255, 255, 0.4) 50%, 
        transparent 80%
    );
    background-size: 200% 100%;
    animation: shimmer 3s infinite linear;
}

/*
Define the shimmer animation
*/
@keyframes shimmer {
    0% {
        background-position: 200% 0;
    }
    100% {
        background-position: -200% 0;
    }
}
</style>
""", unsafe_allow_html=True)


# --- Your Streamlit App ---

st.header("Feature Dashboard")

st.write("The expander below now has its 'PREVIEW' ribbon perfectly clipped.")

# Expander with the "Preview" overlay
with st.expander("AI-Powered Data Analysis", expanded=True):
    st.info("This functionality is in a preview state. Results may not be final.")
    st.slider("Confidence Threshold", 0.0, 1.0, 0.75)
    st.button("Analyze Data")

# Another expander, which will also get the overlay
with st.expander("Standard Reporting"):
    st.write("This is a stable and fully functional feature.")
    st.text_input("Enter your name")
