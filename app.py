import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Smart Calorie Calculator",
    page_icon="🍎",
    layout="wide",
)

st.sidebar.title("⚙️ Settings")
theme = st.sidebar.radio("Theme", ["🌙 Dark Mode", "☀️ Light Mode"])

if theme == "🌙 Dark Mode":
    st.markdown("""
        <style>
            .stApp { background-color: #0E1117; color: #FAFAFA; }
            h1, h2, h3, h4 { color: #FF4B4B; }
            .stButton>button {
                background-color: #FF4B4B; color: white;
                border-radius: 10px; height: 3em; width: 100%;
                border: none;
            }
            .stButton>button:hover {
                background-color: #FF6F61; color: white;
            }
            .stTextInput>div>div>input,
            .stNumberInput input,
            .stSelectbox div[data-baseweb="select"] > div {
                background-color: #1C1E24; color: white; border-radius: 8px;
            }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
            .stApp { background-color: #FFFFFF; color: #000000; }
            h1, h2, h3, h4 { color: #2E8B57; }
            .stButton>button {
                background-color: #2E8B57; color: white;
                border-radius: 10px; height: 3em; width: 100%;
                border: none;
            }
            .stButton>button:hover {
                background-color: #3CB371; color: white;
            }
            .stTextInput>div>div>input,
            .stNumberInput input,
            .stSelectbox div[data-baseweb="select"] > div {
                background-color: #F0F0F0; color: black; border-radius: 8px;
            }
        </style>
    """, unsafe_allow_html=True)

st.title("🏋️ Smart Calorie & Nutrition Analyzer")
st.caption("Developed by Usman Khan | ISA Project 2025")
st.markdown("---")

@st.cache_data
def load_data():
    try:
        df = pd.read_csv("food_data.csv")
        df.columns = df.columns.str.lower()
        df.fillna(0, inplace=True)
        return df
    except Exception:
        return pd.DataFrame()

df = load_data()

st.header("📏 Personal Calorie Calculator")

col1, col2, col3 = st.columns(3)
with col1:
    weight = st.number_input("Weight (kg)", 30, 200, 70)
with col2:
    height = st.number_input("Height (cm)", 100, 220, 175)
with col3:
    age = st.number_input("Age (years)", 10, 80, 20)

gender = st.selectbox("Gender", ["Male", "Female"])
activity = st.selectbox("Activity Level", [
    "Sedentary (little/no exercise)",
    "Light (1–3 days/week)",
    "Moderate (3–5 days/week)",
    "Active (6–7 days/week)",
    "Very Active (hard exercise & physical job)"
])

def calculate_bmr(weight, height, age, gender):
    if gender == "Male":
        return 10 * weight + 6.25 * height - 5 * age + 5
    return 10 * weight + 6.25 * height - 5 * age - 161

def get_activity_factor(activity):
    factors = {
        "Sedentary (little/no exercise)": 1.2,
        "Light (1–3 days/week)": 1.375,
        "Moderate (3–5 days/week)": 1.55,
        "Active (6–7 days/week)": 1.725,
        "Very Active (hard exercise & physical job)": 1.9
    }
    return factors[activity]

if st.button("🔢 Calculate My Calories"):
    bmr = calculate_bmr(weight, height, age, gender)
    tdee = bmr * get_activity_factor(activity)
    st.success(f"BMR: {bmr:.2f} kcal/day")
    st.success(f"TDEE (Total Daily Energy Expenditure): {tdee:.2f} kcal/day")

st.markdown("---")
st.header("🍱 Food Nutrition Lookup")

if not df.empty:
    food_query = st.text_input("Search for a food item:")
    if food_query:
        results = df[df["food"].str.contains(food_query, case=False, na=False)]
        if not results.empty:
            st.dataframe(results)
        else:
            st.warning("No matching food found.")
else:
    st.warning("Dataset not loaded. Please make sure 'food_data.csv' exists in the folder.")

st.markdown("---")
st.header("🤖 Predict Calories from Macronutrients")

if not df.empty and all(col in df.columns for col in ["protein", "carbs", "fat", "calories"]):
    X = df[["protein", "carbs", "fat"]]
    y = df["calories"]
    model = LinearRegression()
    model.fit(X, y)

    c1, c2, c3 = st.columns(3)
    with c1:
        p = st.number_input("Protein (g)", 0, 200, 25)
    with c2:
        c = st.number_input("Carbs (g)", 0, 200, 40)
    with c3:
        f = st.number_input("Fat (g)", 0, 100, 10)

    if st.button("Predict Calories 🔥"):
        pred = model.predict(np.array([[p, c, f]]))[0]
        st.success(f"Estimated Calories: {pred:.2f} kcal")

        fig, ax = plt.subplots()
        ax.pie([p, c, f], labels=["Protein", "Carbs", "Fat"], autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        st.pyplot(fig)

        st.subheader("📊 Macro Comparison")
        fig2, ax2 = plt.subplots()
        sns.barplot(x=["Protein", "Carbs", "Fat"], y=[p, c, f], ax=ax2)
        ax2.set_ylabel("Grams")
        st.pyplot(fig2)

st.markdown("---")
st.caption("© 2025 Usman Khan | IMSC Data Science | ISA Project")
