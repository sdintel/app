import streamlit as st
from datetime import datetime

st.title("SDI First App")

# Title of the app
st.title("Julian Day Calculator")

# Instructions for the user
st.write("Enter a year, month, and day to calculate the Julian Day.")

# Input fields for year, month, and day
year = st.number_input("Year", min_value=1, max_value=9999, value=2025)
month = st.number_input("Month", min_value=1, max_value=12, value=3)
day = st.number_input("Day", min_value=1, max_value=31, value=26)

# Function to calculate Julian Day
def calculate_julian_day(year, month, day):
    date = datetime(year, month, day)
    julian_day = date.timetuple().tm_yday
    return julian_day

# Calculate and display the Julian day
julian_day = calculate_julian_day(year, month, day)
st.write(f"The Julian day for {month}/{day}/{year} is: {julian_day}")

st.title("Square Calculator")
st.write("This app allows you to select a value using the slider, and it will show the square of that value.")

# Slider widget for user input
x = st.slider("Select a value", 0, 100)

# Display the result
st.write(f"The value you selected is: {x}")
st.write(f"{x} squared is: {x*x}")
