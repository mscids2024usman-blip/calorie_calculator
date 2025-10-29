import streamlit as st

st.set_page_config(page_title="About Project", layout="centered")

st.title("📘 About the Project")
st.write("---")

st.markdown("""dtr
### 💡 Calorie Calculator App

This project is a **Data Science-based web application** that helps users calculate their **BMR (Basal Metabolic Rate)**, **TDEE (Total Daily Energy Expenditure)**, and explore **food nutrition data** interactively.

It also uses a **Machine Learning model (Linear Regression)** to predict total calories based on protein, carbs, and fat values.

---

### 🧩 Tech Stack
- **Python**
- **Streamlit**
- **Pandas**
- **Scikit-learn**
- **Matplotlib**

---

### 🧠 Learning Outcomes
This project demonstrates the practical implementation of:
- Data cleaning and preprocessing
- Machine learning (Linear Regression)
- Interactive data visualization
- Streamlit app deployment

---

### 👤 Author
**Usman Khan**  
_Data Science Student_  
📍 India  
📧 khanusman00004@gmail.com

---

### 🚀 Future Improvements
- Add user calorie tracking and progress charts  
- Integrate real-time fitness APIs  
- Save user profiles and data history
""")

st.markdown("---")
st.caption("Created by Usman Khan")