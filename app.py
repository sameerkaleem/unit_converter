import streamlit as st

# Functionality
def distance_converter(from_unit, to_unit, value):
    units = {
        "Meters": 1,
        "Kilometers": 1000,
        "Feet": 0.3048,
        "Miles": 1609.34,
    }
    result = value * units[from_unit] / units[to_unit]
    return result

def temperature_converter(from_unit, to_unit, value):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        result = (value * 9 / 5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        result = (value - 32) * 5 / 9
    else:
        result = value
    return result

def weight_converter(from_unit, to_unit, value):
    units = {
        "Kilograms": 1,
        "Grams": 0.001,
        "Pounds": 0.453592,
        "Ounces": 0.0283495,
    }
    result = value * units[from_unit] / units[to_unit]  
    return result

def pressure_converter(from_unit, to_unit, value):
    units = {
        "Pascal": 1,
        "Hectopascal": 100,
        "Kilopascal": 1000,
        "Bar": 100000,
        "PSI": 6894.76,
        "Atmosphere": 101325,  # Added atmospheres
        "Torr": 133.322,  # Added Torr
    }
    result = value * units[from_unit] / units[to_unit]
    return result 


# UI

st.title("Unit Converter")

# Select Category
category = st.selectbox("Select Category", ["Distance", "Temperature", "Weight", "Pressure"])

if category == "Distance":
    st.subheader("Distance Converter")
    from_unit = st.selectbox("From", ["Meters", "Kilometers", "Feet", "Miles"])
    to_unit = st.selectbox("To", ["Meters", "Kilometers", "Feet", "Miles"])
    value = st.number_input("Enter value", min_value=0.0)
    if st.button("Convert"):
        if value > 0:
            result = distance_converter(from_unit, to_unit, value)
            st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
        else:
            st.warning("Please enter a valid positive number.")

elif category == "Temperature":
    st.subheader("Temperature Converter")
    from_unit = st.selectbox("From", ["Celsius", "Fahrenheit"])
    to_unit = st.selectbox("To", ["Celsius", "Fahrenheit"])
    value = st.number_input("Enter value")
    if st.button("Convert"):
        if value:
            result = temperature_converter(from_unit, to_unit, value)
            st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
        else:
            st.warning("Please enter a valid temperature.")

elif category == "Weight":
    st.subheader("Weight Converter")
    from_unit = st.selectbox("From", ["Kilograms", "Grams", "Pounds", "Ounces"])
    to_unit = st.selectbox("To", ["Kilograms", "Grams", "Pounds", "Ounces"])
    value = st.number_input("Enter value", min_value=0.0)
    if st.button("Convert"):
        if value > 0:
            result = weight_converter(from_unit, to_unit, value)
            st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
        else:
            st.warning("Please enter a valid positive number.")

elif category == "Pressure":
    st.subheader("Pressure Converter")
    from_unit = st.selectbox("From", ["Pascal", "Hectopascal", "Kilopascal", "Bar", "PSI", "Atmosphere", "Torr"])
    to_unit = st.selectbox("To", ["Pascal", "Hectopascal", "Kilopascal", "Bar", "PSI", "Atmosphere", "Torr"])
    value = st.number_input("Enter value", min_value=0.0)
    if st.button("Convert"):
        if value > 0:
            result = pressure_converter(from_unit, to_unit, value)
            st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
        else:
            st.warning("Please enter a valid positive number.")
