import streamlit as st
import re

def check_password_strength(password):
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    return score, feedback

st.set_page_config(page_title="Password Strength Checker", page_icon="🔒", layout="centered")

st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

        body {
            font-family: 'Poppins', sans-serif;
            background-color: #f4f4f4;
        }
        .main {
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.1);
            max-width: 450px;
            margin: auto;
            margin-top: 50px;
        }
        .stTextInput > div > div > input {
            padding: 12px;
            border-radius: 8px;
            border: 1px solid #ddd;
            font-size: 16px;
        }
        .stButton > button {
            background-color: #B88E2F;
            color: white;
            font-size: 16px;
            padding: 10px;
            border-radius: 8px;
            border: none;
            transition: all 0.3s ease-in-out;
        }
        .stButton > button:hover {
            background-color: #926F23;
            transform: scale(1.05);
        }
    </style>
    """,
    unsafe_allow_html=True
)



st.title("🔒 Password Strength Checker")
st.write("Enter a password to check its strength.")

password = st.text_input("Enter Your Password", type="password")

if st.button("Check Strength"):
    if password:
        score, feedback = check_password_strength(password)
        
        if score == 4:
            st.success("✅ Strong Password!")
        elif score == 3:
            st.warning("⚠️ Moderate Password!")
        else:
            st.error("❌ Weak Password!")
        
        if feedback:
            st.write("### Suggestions:")
            for tip in feedback:
                st.write(f"- {tip}")
    else:
        st.error("Please enter a password to check.")

st.markdown("</div>", unsafe_allow_html=True)
