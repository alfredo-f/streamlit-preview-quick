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
*/
div[data-testid="stExpander"]::before {
    content: 'PREVIEW';
    position: absolute;
    top: 12px;
    right: -28px;
    padding: 3px 40px; /* Consistent padding to control ribbon size */
    
    /* === KEY CHANGE: Move ONLY the text === */
    text-align: center; /* Keep the text centered as its base position */
    text-indent: -15px; /* Pulls the text 15px to the left from center */
    /* ==================================== */

    transform: rotate(45deg);
    background-color: #007bff;
    color: white;
    line-height: 20px;
    font-size: 11px;
    font-weight: bold;
    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
    z-index: 1;

    /* Soft shimmer effect */
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

st.write("The text in the ribbon is now shifted left without moving the ribbon itself.")

# Expander with the "Preview" overlay
with st.expander("AI-Powered Data Analysis", expanded=True):
    st.info("This functionality is in a preview state. Results may not be final.")
    st.slider("Confidence Threshold", 0.0, 1.0, 0.75)
    st.button("Analyze Data")

# Another expander, which will also get the overlay
with st.expander("Standard Reporting"):
    st.write("This is a stable and fully functional feature.")
    st.text_input("Enter your name")
