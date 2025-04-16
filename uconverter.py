import streamlit as st

# Page Config
st.set_page_config(page_title="Universal Unit Converter", layout="centered")

# Custom Styles
st.markdown("""
    <style>
        .stApp {
            background-color: #0d1117;
            color: #e6edf3;
            font-family: 'Segoe UI', sans-serif;
        }
        h1, h3 {
            color: #ffffff;
        }
        .stButton>button {
            background-color: #1f6feb;
            color: white;
            border-radius: 8px;
            padding: 0.5rem 1.5rem;
            font-weight: bold;
            transition: 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #1158c7;
        }
        .stSelectbox label, .stNumberInput label {
            font-weight: 600;
            color: #c9d1d9;
        }
        .stSuccess {
            background-color: #1c2b3a !important;
            border-left: 5px solid #2ea043;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🔁 Universal Unit Converter")
st.caption("By Zameer Ahmed — Make quick & accurate conversions across units.")

st.markdown("---")

# Unit types
unit_types = {
    "Length 📏": {
        "Meter to Kilometer": 0.001,
        "Meter to Centimeter": 100,
        "Kilometer to Meter": 1000,
    },
    "Weight ⚖️": {
        "Gram to Kilogram": 0.001,
        "Kilogram to Gram": 1000,
    },
    "Temperature 🌡️": "special"
}

# Dropdowns
selected_type = st.selectbox("🌐 Select Unit Type", list(unit_types.keys()))

if selected_type == "Temperature 🌡️":
    conversion = st.selectbox("Select Conversion Type", ["Celsius to Fahrenheit", "Fahrenheit to Celsius"])
else:
    conversion = st.selectbox("Select Conversion Type", list(unit_types[selected_type].keys()))

# Input Value
input_value = st.number_input("🔢 Enter value to convert:", min_value=0.0, step=0.1)

# Conversion Logic
def convert(value, conversion):
    if conversion == "Celsius to Fahrenheit":
        return round(value * 9/5 + 32, 2)
    elif conversion == "Fahrenheit to Celsius":
        return round((value - 32) * 5/9, 2)
    else:
        return round(value * unit_types[selected_type][conversion], 2)

# Convert Button
if st.button("✨ Convert"):
    result = convert(input_value, conversion)
    st.success(f"✅ Converted Result: **{result}**")

    if selected_type.startswith("Temperature"):
        unit = "°F" if "Fahrenheit" in conversion else "°C"
        st.markdown(f"**That's equivalent to:** `{result} {unit}`")
    else:
        st.markdown(f"**Clean and done! 🔁 Your result is:** `{result}`")

st.markdown("---")
st.caption("Need more unit categories? Drop a request to Zameer 🚀")
