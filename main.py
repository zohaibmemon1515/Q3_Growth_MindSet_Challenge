import streamlit as st
import hashlib
from cryptography.fernet import Fernet

def hass_Pass(Passkey):
    return hashlib.sha256(Passkey.encode()).hexdigest()

def inject_css():
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');
            html, body, [class*="css"] {
                font-family: 'Inter', sans-serif;
                background-color: #f3f6fa;
                color: #222;
            }
            .block-container {
                padding: 3rem 4rem;
                max-width: 900px;
            }
            .stButton>button {
                border-radius: 8px;
                padding: 0.6rem 1.2rem;
                background: linear-gradient(135deg, #667eea, #764ba2);
                color: white;
                font-weight: 600;
                border: none;
                transition: all 0.3s ease-in-out;
                margin-top: 1rem;
                box-shadow: 0 4px 14px rgba(0,0,0,0.1);
            }
            .stButton>button:hover {
                transform: scale(1.04);
                background: linear-gradient(135deg, #5a67d8, #6b46c1);
            }
            .stTextInput>div>div>input,
            .stTextArea textarea {
                border-radius: 10px !important;
                padding: 0.75rem !important;
                border: 1px solid #d3d3d3;
                background-color: #fff;
            }
            .stRadio > div {
                flex-direction: row !important;
                gap: 2rem;
            }
            .markdown-text-container {
                font-size: 1rem;
                color: #444;
            }
            h1, h2, h3, h4 {
                color: #333;
                font-weight: 700;
            }
            .card {
                background-color: white;
                padding: 2rem;
                border-radius: 15px;
                box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.05);
                margin-bottom: 2rem;
            }
            .sidebar .sidebar-content {
                background-color: #fff;
            }
        </style>
    """, unsafe_allow_html=True)

def signup_page():
    st.markdown("### 🧾 Create an Account")
    username = st.text_input("👤 Username")
    password = st.text_input("🔑 Password", type="password")
    if st.button("🚀 Sign Up"):
        if username in st.session_state.users:
            st.error("⚠️ Username already exists.")
        elif username and password:
            st.session_state.users[username] = {"password": hass_Pass(password)}
            st.success("✅ Account created! You can now log in.")
            st.session_state.signup_complete = True
        else:
            st.error("❗Please fill all fields.")

def login_page():
    st.markdown("### 🔐 User Login")
    st.markdown("Enter your login details to access your secure vault.")
    username = st.text_input("👤 Username")
    password = st.text_input("🔑 Password", type="password")
    if st.button("🔓 Login"):
        if username in st.session_state.users and st.session_state.users[username]["password"] == hass_Pass(password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.Attempts[username] = 0
            st.session_state.login_Required[username] = False
            st.success("✅ Login successful!")
            st.rerun()
        else:
            st.error("❌ Invalid credentials")

def insert_data():
    st.markdown("### 📝 Store Encrypted Data")
    st.markdown("Securely store your sensitive data using encryption.")
    data = st.text_area("💬 Enter your text")
    passkey = st.text_input("🔐 Passkey", type="password")
    if st.button("Encrypt Data Securely"):
        if data and passkey:
            hassed_Passkey = hass_Pass(passkey)
            Encrypt_data = st.session_state.cipher_suite.encrypt(data.encode()).decode()
            st.session_state.stored_data[st.session_state.username] = {
                "encrypted_text": Encrypt_data,
                "passkey": hassed_Passkey
            }
            st.session_state.Attempts[st.session_state.username] = 0
            st.success("✅ Data encrypted and stored!")
        else:
            st.error("❗Please fill all fields.")

def retrieve_data():
    st.markdown("### 🔓 Retrieve Your Data")
    st.markdown("Access your encrypted data by entering your passkey.")
    user = st.session_state.username
    if st.session_state.login_Required.get(user):
        st.warning("🔒 Too many failed attempts. Please log in again.")
        if st.button("🔁 Re-Login"):
            st.session_state.logged_in = False
            st.rerun()
        return
    passkey = st.text_input("🔐 Passkey", type="password")
    if st.button("🔍 Decrypt"):
        if user in st.session_state.stored_data:
            hashed_input = hass_Pass(passkey)
            actual = st.session_state.stored_data[user]
            if hashed_input == actual["passkey"]:
                decrypted = st.session_state.cipher_suite.decrypt(actual["encrypted_text"].encode()).decode()
                st.success("✅ Decryption successful!")
                st.markdown("#### 📄 Your Decrypted Data:")
                st.code(decrypted, language='text')
                st.session_state.Attempts[user] = 0
            else:
                st.session_state.Attempts[user] = st.session_state.Attempts.get(user, 0) + 1
                st.error(f"❌ Incorrect passkey. Attempts: {st.session_state.Attempts[user]} / 3")
                if st.session_state.Attempts[user] >= 3:
                    st.session_state.login_Required[user] = True
        else:
            st.warning("⚠️ No stored data found.")

def main():
    st.set_page_config(page_title="Secure Vault 🛡️", page_icon="🛡️")
    inject_css()
    for key, default in {
        "logged_in": False,
        "signup_complete": False,
        "username": "",
        "fernet_key": Fernet.generate_key(),
        "cipher_suite": None,
        "users": {},
        "stored_data": {},
        "Attempts": {},
        "login_Required": {}
    }.items():
        if key not in st.session_state:
            st.session_state[key] = default
    st.session_state.cipher_suite = Fernet(st.session_state.fernet_key)
    if not st.session_state.logged_in:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        tab = st.radio("🔄 Choose an option", ["Login", "Sign Up"])
        if tab == "Sign Up":
            signup_page()
        else:
            login_page()
        st.markdown("</div>", unsafe_allow_html=True)
        return
    st.sidebar.title(f"👋 Welcome, {st.session_state.username}")
    st.sidebar.markdown("---")
    menu = st.sidebar.radio("📂 Navigation", ["🏠 Home", "📝 Insert Data", "🔍 Retrieve Data", "🚪 Logout"])
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    if menu == "🏠 Home":
        st.title("🛡️ Secure Data Encryption System")
        st.markdown("""
            Welcome to your personal encrypted data vault.
            - 🔐 Powered by **Fernet encryption**
            - 💾 Store and retrieve securely
            - ⛔ 3 wrong passkey attempts = forced re-login
        """)
    elif menu == "📝 Insert Data":
        insert_data()
    elif menu == "🔍 Retrieve Data":
        retrieve_data()
    elif menu == "🚪 Logout":
        st.session_state.logged_in = False
        st.success("👋 You've been logged out.")
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
