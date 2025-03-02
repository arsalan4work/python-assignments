# Importing Streamlit library
import streamlit as st

# Distance Convert Funciton
def distance_convert(from_unit, to_unit, value):
   units={
      "Meters":1,
      "Kilometers":1000,
      "Feet":0.3048,
      "Miles":1609.34,
   }
   result = value * units[from_unit] / units[to_unit]
   return  result

# Temperature Convert Funciton
def temperature_convert(from_unit, to_unit, value):
   if from_unit == "Celsius" and to_unit == "Fahrenheit":
      return (value * 9/5) + 32
   elif from_unit == "Fahrenheit" and to_unit == "Celsius":
      return(value - 32) * 5/9
   return value

# Weight Convert Funciton
def weight_convert(from_unit, to_unit, value):
   units={
      "Kilograms":1,
      "Grams":0.001,
      "Pounds":2.20462,
      "Ounces":35.274,
   }
   result = value * units[from_unit] / units[to_unit]
   return  result

# Area Convert Function
def area_convert(from_unit, to_unit, value):
    units = {
        "Square Meters": 1,
        "Square Kilometers": 1_000_000,
        "Square Feet": 0.092903,
        "Square Miles": 2_589_988.11,  
        "Acres": 4046.86,
        "Hectares": 10_000
    }
    result = value * units[from_unit] / units[to_unit]
    return result

# Main Title of Web App
st.title("🌍 Welcome to Unit Converter")
category = st.selectbox("Select Category: 🔽", ["Distance", "Temperature", "Weight", "Area"])

if category == "Distance":
   from_unit = st.selectbox("From", ["Meters", "Kilometers", "Feet", "Miles"])
   to_unit = st.selectbox("To", ["Meters", "Kilometers", "Feet", "Miles"])
   value = st.number_input("Enter value", min_value=0.0, format="%.2f")
   if st.button("🔄 Convert"):
      result = distance_convert(from_unit, to_unit, value)
      st.success(f"✅ {value} {from_unit} is equal to {result:.2f} {to_unit}")

elif category == "Temperature":
   from_unit = st.selectbox("From", ["Celsius", "Fahrenheit"])
   to_unit = st.selectbox("To", ["Celsius", "Fahrenheit"])
   value = st.number_input("Enter value", min_value=0.0, format="%.2f")
   if st.button("🔄 Convert"):
      result = temperature_convert(from_unit, to_unit, value)
      st.success(f"✅ {value} {from_unit} is equal to {result:.2f} {to_unit}")

elif category == "Weight":
   from_unit = st.selectbox("From", ["Kilograms", "Grams", "Pounds", "Ounces"])
   to_unit = st.selectbox("To", ["Kilograms", "Grams", "Pounds", "Ounces"])
   value = st.number_input("Enter value", min_value=0.0, format="%.2f")
   if st.button("🔄 Convert"):
      result = weight_convert(from_unit, to_unit, value)
      st.success(f"✅ {value} {from_unit} is equal to {result:.2f} {to_unit}")

elif category == "Area":
   from_unit = st.selectbox("From", ["Square Meters", "Square Kilometers", "Square Feet", "Acres", "Hectares"])
   to_unit = st.selectbox("To", ["Square Meters", "Square Kilometers", "Square Feet", "Acres", "Hectares"])
   value = st.number_input("Enter value", min_value=0.0, format="%.2f")
   if st.button("🔄 Convert"):
      result = area_convert(from_unit, to_unit, value)
      st.success(f"✅ {value} {from_unit} is equal to {result:.2f} {to_unit}")

st.write("---------------------------------------------------------------------------------")
st.write("Build with ❤ by Arsalan")