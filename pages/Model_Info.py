import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

st.title("🤖 Model Information & Training")

st.write("""
### 🎯 Purpose:
This page explains how the ML model predicts **calories** from macronutrients (Protein, Carbs, Fat).
A simple **Linear Regression** model from Scikit-learn is used.
""")

uploaded_file = st.file_uploader("Upload cleaned dataset (CSV)", type=["csv"], key="model_uploader")

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        st.error(f"Error reading file: {e}")
        st.stop()

    df.columns = [c.strip().lower() for c in df.columns]

    rename_map = {
        "carbohydrates": "carbs",
        "carbohydrate": "carbs",
        "carb": "carbs",
        "protein_g": "protein",
        "fat_g": "fat",
        "calories_kcal": "calories"
    }
    df = df.rename(columns=rename_map)

    required_cols = ["protein", "carbs", "fat", "calories"]
    if all(col in df.columns for col in required_cols):
        X = df[["protein", "carbs", "fat"]].apply(pd.to_numeric, errors="coerce").fillna(0)
        y = pd.to_numeric(df["calories"], errors="coerce").fillna(0)

        model = LinearRegression()
        model.fit(X, y)
        preds = model.predict(X)
        score = r2_score(y, preds)

        st.success("✅ Model trained successfully")

        st.subheader("📈 Model Coefficients")
        coef_df = pd.DataFrame({
            "Nutrient": ["Protein", "Carbs", "Fat"],
            "Coefficient": model.coef_.round(4)
        })
        st.table(coef_df)

        st.write("**Intercept:**", round(model.intercept_, 4))
        st.write(f"**Model R² score:** {score:.3f}")

        st.subheader("🧮 Test Prediction")
        protein = st.number_input("Protein (g)", min_value=0.0, max_value=1000.0, value=20.0, key="mi_protein")
        carbs = st.number_input("Carbs (g)", min_value=0.0, max_value=1000.0, value=30.0, key="mi_carbs")
        fat = st.number_input("Fat (g)", min_value=0.0, max_value=1000.0, value=10.0, key="mi_fat")

        if st.button("Predict Calories", key="mi_predict"):
            input_data = np.array([[protein, carbs, fat]])
            pred = model.predict(input_data)[0]
            st.success(f"Estimated Calories: **{pred:.2f} kcal**")
            st.info("Note: Model is linear and based on the provided dataset; accuracy depends on dataset quality.")
    else:
        st.error(f"Dataset must contain these columns (case-insensitive): {required_cols}")
else:
    st.info("👆 Upload your dataset (CSV with columns: protein, carbs, fat, calories) to train and test the model.")

st.markdown("---")
st.caption("Created by Usman Khan")
