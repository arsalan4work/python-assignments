import streamlit as st
from cryptography.fernet import Fernet
import hashlib
import base64
import json
import time
import os

# -------------------- Config --------------------
DATA_FILE = "data.json"
LOCKOUT_TIME = 3  # seconds


# -------------------- Function to generate fernet key --------------------
def get_fernet_key(passkey):
    """Return Fernet-compatible key from passkey using SHA256"""
    return base64.urlsafe_b64encode(hashlib.sha256(passkey.encode()).digest())

# -------------------- Function to encrypt data using fernet and hashlib --------------------
def encrypt_data(plain_text, passkey):
    key = get_fernet_key(passkey)
    f = Fernet(key)
    encrypted_text = f.encrypt(plain_text.encode()).decode()
    hashed_passkey = hashlib.sha256(passkey.encode()).hexdigest()
    return encrypted_text, hashed_passkey

# -------------------- Function to decrypt data using fernet --------------------
def decrypt_data(encrypted_text, passkey):
    try:
        key = get_fernet_key(passkey)
        f = Fernet(key)
        return f.decrypt(encrypted_text.encode()).decode()
    except Exception:
        return None

# -------------------- Function to load data using file handling and json --------------------
def load_data():
    if not os.path.exists(DATA_FILE) or os.path.getsize(DATA_FILE) == 0:
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

# -------------------- Function to save data into data.json file --------------------
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


# -------------------- Session State Init --------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"
if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0
if "authorized" not in st.session_state:
    st.session_state.authorized = True
if "lockout_start" not in st.session_state:
    st.session_state.lockout_start = 0


# -------------------- CSS --------------------
st.markdown("""
    <style>
    .main { background-color: #f4f6fa; }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 20px;
    }
    </style>
""", unsafe_allow_html=True)


# -------------------- Pages --------------------
def home():
    st.title("🔐 Secure Data Encryption System")
    st.write("Use the sidebar to navigate.")


def store_data():
    st.title("📦 Store Encrypted Data")
    text = st.text_area("Enter the data to encrypt:")
    passkey = st.text_input("Enter a secret passkey:", type="password")

    if st.button("Encrypt and Save"):
        if text and passkey:
            encrypted_text, hashed_passkey = encrypt_data(text, passkey)
            data = load_data()
            data[encrypted_text] = {"encrypted_text": encrypted_text, "passkey": hashed_passkey}
            save_data(data)
            st.success("✅ Data encrypted and stored successfully!")
        else:
            st.error("⚠️ Please fill in both fields.")


def retrieve_data():
    st.title("🔍 Retrieve Encrypted Data")

    if not st.session_state.authorized:
        st.warning("🔒 You must reauthorize.")
        st.session_state.page = "Login"  # Redirect to login if not authorized
        st.rerun()  # Rerun to redirect to login page
        return

    if st.session_state.failed_attempts >= 3:
        time_elapsed = time.time() - st.session_state.lockout_start
        if time_elapsed < LOCKOUT_TIME:
            st.warning(f"⏳ Locked out. Try again in {int(LOCKOUT_TIME - time_elapsed)} seconds.")
            return
        else:
            st.session_state.failed_attempts = 0
            st.session_state.authorized = True

    passkey_input = st.text_input("Enter your secret passkey:", type="password")

    if st.button("Retrieve Data"):
        if not passkey_input:
            st.error("⚠️ Please enter your passkey.")
            return

        data = load_data()
        hashed_input = hashlib.sha256(passkey_input.encode()).hexdigest()

        found = False
        for record in data.values():
            if record["passkey"] == hashed_input:
                decrypted = decrypt_data(record["encrypted_text"], passkey_input)
                if decrypted:
                    st.success("✅ Decrypted Data:")
                    st.code(decrypted, language="text")
                    st.session_state.failed_attempts = 0
                    found = True
                    break

        if not found:
            st.session_state.failed_attempts += 1
            st.error(f"❌ Incorrect passkey! Attempt {st.session_state.failed_attempts}/3")
            if st.session_state.failed_attempts >= 3:
                st.warning("🔒 Too many attempts. Locked out.")
                st.session_state.lockout_start = time.time()
                st.session_state.authorized = False
                st.session_state.page = "Login"  # Redirect to login on lockout
                st.rerun()  # Rerun to redirect to login page


def login():
    st.title("🔐 Reauthorization Required")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "admin":
            st.session_state.failed_attempts = 0
            st.session_state.authorized = True
            st.session_state.page = "Home"
            st.success("✅ Login successful!")
        else:
            st.error("❌ Invalid credentials.")


# -------------------- Sidebar Navigation --------------------
st.sidebar.title("🔍 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Store Data", "Retrieve Data", "Login"])
st.session_state.page = page

# -------------------- Page Routing --------------------
if st.session_state.page == "Home":
    home()
elif st.session_state.page == "Store Data":
    store_data()
elif st.session_state.page == "Retrieve Data":
    retrieve_data()
elif st.session_state.page == "Login":
    login()
