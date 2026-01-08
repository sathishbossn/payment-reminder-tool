import streamlit as st
from datetime import date
import streamlit.components.v1 as components

# ---------------- PASSWORD ----------------
APP_PASSWORD = "pay123"

st.set_page_config(page_title="Payment Reminder Generator", layout="centered")

st.markdown("## 🔐 Secure Access")
password = st.text_input("Password", type="password")

if password != APP_PASSWORD:
    st.stop()

# ---------------- APP ----------------
st.markdown("---")
st.title("💬 Payment Reminder Message Generator")
st.write("Generate polite, professional, or firm payment reminders in seconds.")

client = st.text_input("Client Name")
invoice = st.text_input("Invoice Number")

currency = st.selectbox(
    "Currency",
    ["USD ($)", "EUR (€)", "GBP (£)", "INR (₹)"]
)

amount = st.text_input("Invoice Amount")
due_date = st.date_input("Invoice Due Date", value=date.today())

tone = st.selectbox(
    "Select Message Tone",
    ["Friendly", "Professional", "Firm"]
)

currency_symbol = {
    "USD ($)": "$",
    "EUR (€)": "€",
    "GBP (£)": "£",
    "INR (₹)": "₹"
}[currency]

# ---------------- COPY FUNCTION ----------------
def copy_button(text):
    components.html(
        f"""
        <button onclick="navigator.clipboard.writeText(`{text}`)"
        style="
        background-color:#4CAF50;
        color:white;
        padding:6px 12px;
        border:none;
        border-radius:6px;
        cursor:pointer;">
        📋 Copy
        </button>
        """,
        height=40,
    )

# ---------------- GENERATE ----------------
if st.button("Generate Messages"):
    if not client or not invoice or not amount:
        st.warning("Please fill all required fields.")
    else:
        st.subheader("📨 Generated Messages")

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
