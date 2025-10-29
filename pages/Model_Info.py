import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

st.title("🤖 Model Information & Training")

st.write("""
### 🎯 Purpose:
This page explains how the ML model predicts **calories** from the given **macronutrients** (Protein, Carbs, Fat).
We use a simple **Linear Regression** model from Scikit-learn.
""")

uploaded_file = st.file_uploader("Upload your cleaned dataset (CSV)", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Check columns
    required_cols = ["protein", "carbs", "fat", "calories"]
    if all(col in df.columns for col in required_cols):
        X = df[["protein", "carbs", "fat"]]
        y = df["calories"]

        model = LinearRegression()
        model.fit(X, y)

        st.success("✅ Model successfully trained!")

        st.subheader("📈 Model Coefficients")
        st.write(pd.DataFrame({
            "Nutrient": ["Protein", "Carbs", "Fat"],
            "Coefficient": model.coef_
        }))

        st.write("**Intercept:**", model.intercept_)

        st.subheader("🧮 Test Prediction Example")
        protein = st.number_input("Protein (g)", 0, 100, 20)
        carbs = st.number_input("Carbs (g)", 0, 100, 30)
        fat = st.number_input("Fat (g)", 0, 100, 10)

        if st.button("Predict Calories"):
            input_data = np.array([[protein, carbs, fat]])
            pred = model.predict(input_data)[0]
            st.success(f"Estimated Calories: **{pred:.2f} kcal**")

        st.info("💡 Tip: Adjust macros above to test different food combinations.")

    else:
        st.error(f"Dataset must contain these columns: {required_cols}")

else:
    st.info("👆 Upload your dataset to train and test the model.")


st.markdown("---")
st.caption("Created by Usman Khan")