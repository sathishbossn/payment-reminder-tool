import streamlit as st
from datetime import date
import time
import streamlit.components.v1 as components

# ================= CONFIG =================
APP_PASSWORD = "pay123"        # 🔑 change anytime
SESSION_TIMEOUT = 1800         # 30 minutes

st.set_page_config(
    page_title="Payment Reminder Generator",
    layout="centered"
)

# ================= SESSION INIT =================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "last_active" not in st.session_state:
    st.session_state.last_active = time.time()

# ================= LOGIN FUNCTION =================
def login():
    if st.session_state.password == APP_PASSWORD:
        st.session_state.logged_in = True
        st.session_state.last_active = time.time()
    else:
        st.error("❌ Incorrect password")

# ================= LOGIN SCREEN =================
if not st.session_state.logged_in:
    st.markdown(
        """
        <div style="text-align:center; padding:40px;">
            <h1>🔐 Secure Access</h1>
            <p style="color:gray;">Enter your access password</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.text_input(
        "Password",
        type="password",
        key="password",
        on_change=login
    )

    st.stop()

# ================= SESSION TIMEOUT =================
current_time = time.time()

if current_time - st.session_state.last_active > SESSION_TIMEOUT:
    st.session_state.logged_in = False
    st.experimental_rerun()

st.session_state.last_active = current_time

# ================= LOGOUT BUTTON =================
col1, col2 = st.columns([1, 6])
with col1:
    if st.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.experimental_rerun()

# ================= APP UI =================
st.markdown("## 💬 Payment Reminder Message Generator")
st.caption("Polite • Professional • Firm — ready-to-send messages")

st.markdown("---")

# ================= INPUTS =================
left, right = st.columns(2)

with left:
    client = st.text_input("Client Name")
    invoice = st.text_input("Invoice Number")
    amount = st.text_input("Invoice Amount")

with right:
    currency = st.selectbox(
        "Currency",
        ["USD ($)", "EUR (€)", "GBP (£)", "INR (₹)"]
    )
    due_date = st.date_input("Invoice Due Date", value=date.today())
    tone = st.selectbox(
        "Message Tone",
        ["Friendly", "Professional", "Firm"]
    )

currency_symbol = {
    "USD ($)": "$",
    "EUR (€)": "€",
    "GBP (£)": "£",
    "INR (₹)": "₹"
}[currency]

# ================= COPY BUTTON =================
def copy_button(text):
    components.html(
        f"""
        <button onclick="navigator.clipboard.writeText(`{text}`)"
        style="
        background:#2563eb;
        color:white;
        padding:8px 16px;
        border:none;
        border-radius:8px;
        cursor:pointer;
        margin-bottom:20px;">
        📋 Copy message
        </button>
        """,
        height=45
    )

# ================= GENERATE =================
st.markdown("### 📩 Generated Messages")

if st.button("🚀 Generate Messages", use_container_width=True):
    if not client or not invoice or not amount:
        st.warning("Please fill all required fields.")
    else:
        if tone == "Friendly":
            messages = [
                f"Hi {client}, hope you're doing well. Just a gentle reminder regarding Invoice {invoice} for {currency_symbol}{amount}, due on {due_date}.",
                f"Hello {client}, I’m checking in to see if you had a chance to review Invoice {invoice}. Please let me know if you need anything.",
                f"Hi {client}, just following up on Invoice {invoice}. Looking forward to your update."
            ]
        elif tone == "Professional":
            messages = [
                f"Dear {client}, this is a reminder that Invoice {invoice} for {currency_symbol}{amount} was due on {due_date}.",
                f"Hello {client}, kindly let me know the status of Invoice {invoice} at your convenience.",
                f"Dear {client}, please advise if there are any issues preventing payment of Invoice {invoice}."
            ]
        else:
            messages = [
                f"Dear {client}, Invoice {invoice} for {currency_symbol}{amount} remains unpaid despite being due on {due_date}.",
                f"This is a follow-up regarding the overdue Invoice {invoice}. Please confirm payment status.",
                f"Kindly treat this as a final reminder for Invoice {invoice}."
            ]

        for i, msg in enumerate(messages, start=1):
            st.text_area(f"Message {i}", msg, height=90)
            copy_button(msg)

st.markdown("---")
st.caption("🔒 Secure • 🌍 Global • ⚡ Instant")
