import streamlit as st
import pandas as pd

# Page title
st.title("📊 Dataset Information")

# File uploader for dataset
uploaded_file = st.file_uploader("Upload your dataset (CSV)", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("🔍 Dataset Preview")
    st.dataframe(df.head())

    st.subheader("🧠 Basic Info")
    st.write("**Shape:**", df.shape)
    st.write("**Columns:**", list(df.columns))

    st.subheader("🧼 Missing Values")
    st.write(df.isnull().sum())

    st.subheader("📈 Statistical Summary")
    st.write(df.describe())

    st.subheader("🪶 Column Data Types")
    st.write(df.dtypes)

    st.success("✅ Dataset successfully loaded and analyzed!")

else:
    st.info("👆 Please upload your dataset to view details.")

# Footer
st.markdown("---")
st.caption("Created by Usman Khan")