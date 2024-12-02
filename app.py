import streamlit as st

# Set the title of the app
st.title("Welcome to My Streamlit App!")

# Add a header
st.header("About This App")

# Add some text
st.write("""
    This is a simple Streamlit application created to demonstrate how Streamlit works.
    You can add text, images, charts, and more to build interactive web applications.
""")

# Add an input box
name = st.text_input("Enter your name:")

# Display a personalized message
if name:
    st.write(f"Hello, {name}! Welcome to the Streamlit app.")

# Add a button
if st.button("Click Me!"):
    st.write("You clicked the button!")

# Add a number slider
age = st.slider("Select your age:", 1, 100, 25)
st.write(f"Your age is: {age}")

# Add a select box
favorite_color = st.selectbox("What's your favorite color?", ["Red", "Blue", "Green", "Yellow"])
st.write(f"Your favorite color is: {favorite_color}")
