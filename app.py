import streamlit as st

# It's good practice to set the page config at the beginning of your script.
st.set_page_config(layout="wide")

st.title("Disabling Tooltips on List Items with JavaScript")

st.write("Below is a list where each item has a 'title' attribute, which normally creates a tooltip on hover.")

# This is an example of a list that would have tooltips.
# We use st.markdown to render this HTML.
st.markdown("""
    <ul>
        <li title="This is a tooltip for item 1">List Item 1</li>
        <li title="This is a tooltip for item 2">List Item 2</li>
        <li title="This is a tooltip for item 3">List Item 3</li>
    </ul>
""", unsafe_allow_html=True)

st.write("Now, we will inject a JavaScript snippet to remove those 'title' attributes.")

# The JavaScript code to be injected.
# It selects all <li> elements and removes their 'title' attribute.
js_to_remove_tooltips = """
<script>
    const allListItems = document.querySelectorAll('li');
    allListItems.forEach(item => {
        item.removeAttribute('title');
    });
</script>
"""

# Use st.markdown to inject the JavaScript into the app.
# The unsafe_allow_html=True argument is crucial for this to work.
st.markdown(js_to_remove_tooltips, unsafe_allow_html=True)

st.success("The JavaScript has been injected. The tooltips on the list items above should now be disabled.")

st.info("Because Streamlit re-runs the script on each interaction, this JavaScript will be applied every time the page updates.")
