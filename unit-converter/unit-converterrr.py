# # Import streamlit library
import streamlit as st

# Distance Converter Function
def distance_converter(from_unit, to_unit, value):
    units = {
        "Meters": 1,
        "Kilometers": 1000,
        "Feet": 0.3048,
        "Miles": 1609.34,
    }
    result = value * units[from_unit] / units[to_unit]
    return result

# Temperature Converter Function
def temperature_converter(from_unit, to_unit, value):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    return value  # If same unit is selected

# Weight Converter Function 
def weight_converter(from_unit, to_unit, value):
    units = {
        "Kilograms": 1,
        "Grams": 0.001,
        "Pounds": 0.453592,
        "Ounces": 0.0283495,
    }
    result = value * units[from_unit] / units[to_unit]
    return result

# Pressure Converter Function
def pressure_converter(from_unit, to_unit, value):
    units = {
        "Pascals": 1,
        "Hectopascals": 100,
        "Kilopascals": 1000,
        "Bar": 100000,
    }
    result = value * units[from_unit] / units[to_unit]
    return result

# # Title of our app
st.title("🌍 Welcome to Unit Converter")
category = st.selectbox("Select Category", ["Distance", "Temperature", "Weight", "Pressure"])

if category == "Distance":
    from_unit = st.selectbox("From", ["Meters", "Kilometers", "Feet", "Miles"])
    to_unit = st.selectbox("To", ["Meters", "Kilometers", "Feet", "Miles"])
    value = st.number_input("Enter Value", min_value=0.0, format="%.2f")
    if st.button("Convert"):
        result = distance_converter(from_unit, to_unit, value)
        st.write(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")

elif category == "Temperature":
    from_unit = st.selectbox("From", ["Celsius", "Fahrenheit"])
    to_unit = st.selectbox("To", ["Celsius", "Fahrenheit"])
    value = st.number_input("Enter Value", format="%.2f")
    if st.button("Convert"):
        result = temperature_converter(from_unit, to_unit, value)
        st.write(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")

elif category == "Weight":
    from_unit = st.selectbox("From", ["Kilograms", "Grams", "Pounds", "Ounces"])
    to_unit = st.selectbox("To", ["Kilograms", "Grams", "Pounds", "Ounces"])
    value = st.number_input("Enter Value", min_value=0.0, format="%.2f")
    if st.button("Convert"):
        result = weight_converter(from_unit, to_unit, value)
        st.write(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")

elif category == "Pressure":
    from_unit = st.selectbox("From", ["Pascals", "Hectopascals", "Kilopascals", "Bar"])
    to_unit = st.selectbox("To", ["Pascals", "Hectopascals", "Kilopascals", "Bar"])
    value = st.number_input("Enter Value", min_value=0.0, format="%.2f")
    if st.button("Convert"):
        result = pressure_converter(from_unit, to_unit, value)
        st.write(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")

# # In Last Added Text to our app
st.text("Created with ❤ by Arsalan using streamlit")