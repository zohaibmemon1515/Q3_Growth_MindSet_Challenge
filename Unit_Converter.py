import streamlit as st
import requests


LENGTH_FACTORS = {
    "Meters": 1,
    "Kilometers": 0.001,
    "Centimeters": 100,
    "Millimeters": 1000,
    "Miles": 0.000621371,
    "Yards": 1.09361,
    "Feet": 3.28084,
    "Inches": 39.3701
}

WEIGHT_FACTORS = {
    "Kilograms": 1,
    "Grams": 1000,
    "Milligrams": 1e6,
    "Pounds": 2.20462,
    "Ounces": 35.274
}


def length_converter(value, from_unit, to_unit):
    return value * (LENGTH_FACTORS[from_unit] / LENGTH_FACTORS[to_unit])

def weight_converter(value, from_unit, to_unit):
    return value * (WEIGHT_FACTORS[from_unit] / WEIGHT_FACTORS[to_unit])

def temperature_converter(amount, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (amount * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (amount - 32) * 5/9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return amount + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return amount - 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (amount - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (amount - 273.15) * 9/5 + 32
    return amount

def currency_converter(amount, from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if to_currency in data["rates"]:
            return amount * data["rates"][to_currency]
        else:
            return "Invalid currency code"
    else:
        return "API Error: Unable to fetch rates"


st.set_page_config(page_title="Universal Converter", page_icon="🔄", layout="centered")

st.title("🔄 Universal Unit Converter")
st.write("Easily convert **Length, Weight, Temperature, and Currency** in real-time!")


conversion_type = st.selectbox("📌 Select Conversion Type", ["Length", "Weight", "Temperature", "Currency"])

st.divider() 


if conversion_type == "Length":
    st.subheader("📏 Length Converter")
    amount = st.number_input("Enter Value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From Unit", list(LENGTH_FACTORS.keys()))
    to_unit = st.selectbox("To Unit", list(LENGTH_FACTORS.keys()))
    
    if st.button("Convert"):
        result = length_converter(amount, from_unit, to_unit)
        st.success(f"✅ {amount} {from_unit} = {result:.4f} {to_unit}")


elif conversion_type == "Weight":
    st.subheader("⚖️ Weight Converter")
    amount = st.number_input("Enter Value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From Unit", list(WEIGHT_FACTORS.keys()))
    to_unit = st.selectbox("To Unit", list(WEIGHT_FACTORS.keys()))
    
    if st.button("Convert"):
        result = weight_converter(amount, from_unit, to_unit)
        st.success(f"✅ {amount} {from_unit} = {result:.4f} {to_unit}")


elif conversion_type == "Temperature":
    st.subheader("🌡️ Temperature Converter")
    amount = st.number_input("Enter Value:", format="%.2f")
    from_unit = st.selectbox("From Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    
    if st.button("Convert"):
        result = temperature_converter(amount, from_unit, to_unit)
        st.success(f"✅ {amount}° {from_unit} = {result:.2f}° {to_unit}")


elif conversion_type == "Currency":
    st.subheader("💰 Currency Converter")
    amount = st.number_input("Enter Amount:", min_value=1.0, format="%.2f")
    from_currency = st.text_input("From Currency (e.g., USD, EUR, GBP)", value="USD").upper()
    to_currency = st.text_input("To Currency (e.g., USD, EUR, GBP)", value="PKR").upper()
    
    if st.button("Convert"):
        try:
            result = currency_converter(amount, from_currency, to_currency)
            if isinstance(result, str):
                st.error(result)
            else:
                st.success(f"✅ {amount} {from_currency} = {result:.2f} {to_currency}")
        except Exception as e:
            st.error("⚠️ Invalid currency code or conversion error. Try again.")


st.divider()
st.caption("🚀 Created by **MD Zohaib Memon** | Universal Unit Converter | Powered by Python & Streamlit")
