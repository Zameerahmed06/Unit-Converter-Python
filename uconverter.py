import streamlit as st

# Streamlit Title
st.title("Unit Converter")

#Dropdowns For Unit Selection
unit_types ={
    "length":{
        "Meter to Kilometer":0.0001,
        "Meter to Centimeter":100,
        "Kilometer to Meter":1000,
        },
    "weight":{
        "Gram to Kilogram":0.001,
        "Kilogram to Gram":1000,
        },
    "Temperature":"special",
}
selected_type = st.selectbox("Select Unit", list(unit_types.keys()))

#Special Conversion Options
if selected_type == "Temperature":
    conversion = st.selectbox("Select Conversion", ["Celsius to Fahrenheit", "Fahrenheit to Celsius"])
else:
    conversion = st.selectbox("Select Conversion", list(unit_types[selected_type].keys()))
    

# Input value
input_value = st.number_input("Enter value:", min_value=0.0, step=0.1)

def convert(value, conversion):
    if conversion == "Celsius to Fahrenheit":
        return value * 9/5 + 32
    elif conversion == "Fahrenheit to Celsius":
        return (value - 32) * 5/9
    else:
        return value * unit_types[selected_type][conversion]
    
if st.button("Convert"):
    result = convert(input_value, conversion)
    st.success(f"Result: {result}")
