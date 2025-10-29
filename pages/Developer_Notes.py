import streamlit as st

st.title("👨‍💻 Developer Notes & Project Overview")

st.markdown("""
### 🏋️ Project Title:
**Smart Calorie Calculator with Nutrition Analysis**

---

### 💡 Objective:
To build an **interactive Streamlit app** that helps users:
- Calculate daily calorie needs (BMR & TDEE)
- Search and analyze food nutrients
- Predict calorie values using a **Machine Learning model**
- Visualize macronutrient breakdown

---

### 🧠 Tools & Technologies Used:
- **Python** (Pandas, NumPy, Scikit-learn)
- **Streamlit** for app interface  
- **Matplotlib / Plotly** for data visualization  
- **CSV Dataset** (Food nutrition data)

---

### 📂 Project Structure:
-app.py → Main Calorie Calculator
-pages/Dataset_Info.py → Dataset statistics and preview
-pages/Model_Info.py → ML model explanation and prediction
-pages/Developer_Notes.py → Developer background and purpose
-food_data.csv → Nutrition dataset
            

---

### 👨‍🎓 Developer:
**Name:** Usman Khan  
**Course:** B.Sc Data Science  
**Project Type:** ISA PROJECT
**Year:** 2025  

---

### 🗒️ Future Improvements:
- Add meal planner using user goals  
- Connect to live nutrition APIs  
- Save user progress & history  
- Add authentication (login/logout)  

---

### ❤️ Acknowledgment:
This project was created for the **Internal Semester Assessment (ISA)** as a demonstration of integrating
**Data Cleaning, Machine Learning, and Web App Development** using **Streamlit**.

---

**Thank you for visiting the project! 🙌**
""")

# Footer
st.markdown("---")
st.caption("Created by Usman Khan")