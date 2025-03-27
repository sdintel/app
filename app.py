import streamlit as st
# SDI is cool!
st.title("Square Calculator")
st.write("This app allows you to select a value using the slider, and it will show the square of that value.")

# Slider widget for user input
x = st.slider("Select a value", 0, 100)

# Display the result
st.write(f"The value you selected is: {x}")
st.write(f"{x} squared is: {x*x}")
