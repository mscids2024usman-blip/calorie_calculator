import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="Calorie Calculator App", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv("food_data.csv")
    df.columns = [c.strip().lower() for c in df.columns]
    df.dropna(subset=["calories"], inplace=True)
    return df

df = load_data()


def calculate_bmr(weight, height, age, gender):
    if gender == "Male":
        return 10 * weight + 6.25 * height - 5 * age + 5
    else:
        return 10 * weight + 6.25 * height - 5 * age - 161

def calculate_tdee(bmr, activity_level):
    activity_multipliers = {
        "Sedentary (little/no exercise)": 1.2,
        "Lightly active (1-3 days/week)": 1.375,
        "Moderately active (3-5 days/week)": 1.55,
        "Very active (6-7 days/week)": 1.725,
        "Super active (athlete)": 1.9,
    }
    return bmr * activity_multipliers[activity_level]


st.title("💪 Calorie Calculator App")
st.write("Track calories, calculate BMR/TDEE, and explore food nutrition.")


col1, col2 = st.columns(2)
with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    weight = st.number_input("Weight (kg)", min_value=30.0, max_value=200.0, value=70.0)
    height = st.number_input("Height (cm)", min_value=100.0, max_value=250.0, value=175.0)
with col2:
    age = st.number_input("Age", min_value=10, max_value=100, value=20)
    activity = st.selectbox("Activity Level", [
        "Sedentary (little/no exercise)",
        "Lightly active (1-3 days/week)",
        "Moderately active (3-5 days/week)",
        "Very active (6-7 days/week)",
        "Super active (athlete)"
    ])


if st.button("Calculate Calories"):
    bmr = calculate_bmr(weight, height, age, gender)
    tdee = calculate_tdee(bmr, activity)
    st.success(f"**Your BMR:** {bmr:.2f} kcal/day")
    st.info(f"**Your TDEE (maintenance calories):** {tdee:.2f} kcal/day")


st.subheader("🍎 Search Food Items")
query = st.text_input("Enter food name (e.g., rice, egg, chicken):").lower()

if query:
    results = df[df["food"].str.contains(query, case=False, na=False)]
    if not results.empty:
        st.dataframe(results[["food", "calories", "protein", "carbs", "fat"]].head(10))
    else:
        st.warning("No matching food found.")


st.subheader("🤖 Predict Calories from Macros (Protein, Carbs, Fat)")
X = df[["protein", "carbs", "fat"]]
y = df["calories"]

model = LinearRegression()
model.fit(X, y)

p = st.number_input("Protein (g)", 0.0, 200.0, 20.0)
c = st.number_input("Carbs (g)", 0.0, 300.0, 50.0)
f = st.number_input("Fat (g)", 0.0, 100.0, 10.0)

if st.button("Predict Calories"):
    pred = model.predict([[p, c, f]])[0]
    st.success(f"Estimated Calories: {pred:.2f} kcal")

    # Pie Chart
    labels = ["Protein", "Carbs", "Fat"]
    values = [p*4, c*4, f*9] 
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
    ax.set_title("Macro Calorie Breakdown")
    st.pyplot(fig)
