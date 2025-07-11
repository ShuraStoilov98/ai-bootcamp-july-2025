import streamlit as st  # Import Streamlit library

st.title("Welcome to the Streamlit Tutorial")  # Set the title of the app
st.write ("Hello, Streamlit!")  # Display a simple message

st.text_input("Enter your name:", key="name")  # Input field for user name
st.button("Submit", on_click=lambda: st.write(f"Hello, {st.session_state.name}!"))  # Button to greet the user


# streamlit run streamlit_tutorial.py  # Command to run the Streamlit app
# Save this code in a file named streamlit_tutorial.py and run it using the command