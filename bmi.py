import streamlit as st
st.set_page_config(page_title="BMI Calculator", page_icon="📱", layout="centered")
st.title("📱 BMI Calculator")
st.write("Let's Calculate Your **Body Mass Index [BMI]** And Understand What It Means")

st.header("Enter Your Details 🧨")

weight = st.number_input("Enter Your Weight (in kg)", min_value=10, max_value=300, value=65)
height = st.number_input("Enter Your Height (in cm)", min_value=90, max_value=200, value=170)

st.write(f"💉 Your Weight: {weight} kg")
st.write(f"📏 Your Height: {height} cm")

if st.button("Calculate BMI"):
    h_m = height / 100  # Convert height from cm to meters
    bmi = weight / (h_m)**2
    st.success(f"Your BMI is: **{bmi:.2f}**")

# Print BMI Categories
if bmi < 18.5:
    category = "Underweight 🤣"
    color = "#ccb3ff"
elif 18.5 <= bmi < 25:
    category = "Normal Weight 😎"
    color = "#53c653"
elif 25 <= bmi < 30:
    category = "Overweight 😐"
    color = "#ff9933"
else:
    category = "Obese 😟"
    color = "#666666"

st.markdown(f"<div style='background-color: {color};padding: 15px; border-radius: 10px;'><h3 style='color: white;'>{category}</h3></div>", unsafe_allow_html=True)