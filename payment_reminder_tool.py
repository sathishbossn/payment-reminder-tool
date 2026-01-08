import streamlit as st
from datetime import date

# ---------------- PASSWORD CONFIG ----------------
APP_PASSWORD = "pay123"   # 🔑 change this anytime

st.set_page_config(page_title="Payment Reminder Generator", layout="centered")

st.markdown("## 🔐 Secure Access")
st.markdown("Enter your access password to continue")

password = st.text_input("Password", type="password")

if password != APP_PASSWORD:
    st.stop()

# ---------------- APP STARTS HERE ----------------
st.markdown("---")
st.title("💬 Payment Reminder Message Generator")
st.write("Generate polite, professional, or firm payment reminders in seconds.")

client = st.text_input("Client Name")
invoice = st.text_input("Invoice Number")
amount = st.text_input("Invoice Amount (USD)")
due_date = st.date_input("Invoice Due Date", value=date.today())

tone = st.selectbox(
    "Select Message Tone",
    ["Friendly", "Professional", "Firm"]
)

if st.button("Generate Messages"):
    if not client or not invoice or not amount:
        st.warning("Please fill all required fields.")
    else:
        st.subheader("📨 Generated Messages")

        if tone == "Friendly":
            messages = [
                f"Hi {client}, hope you're doing well. Just a gentle reminder regarding Invoice {invoice} for ${amount}, due on {due_date}.",
                f"Hello {client}, I’m checking in to see if you had a chance to review Invoice {invoice}. Please let me know if you need anything.",
                f"Hi {client}, just following up on Invoice {invoice}. Looking forward to your update."
            ]

        elif tone == "Professional":
            messages = [
                f"Dear {client}, this is a reminder that Invoice {invoice} for ${amount} was due on {due_date}.",
                f"Hello {client}, kindly let me know the status of Invoice {invoice} at your convenience.",
                f"Dear {client}, please advise if there are any issues preventing payment of Invoice {invoice}."
            ]

        else:  # Firm
            messages = [
                f"Dear {client}, Invoice {invoice} for ${amount} remains unpaid despite being due on {due_date}.",
                f"This is a follow-up regarding the overdue Invoice {invoice}. Please confirm payment status.",
                f"Kindly treat this as a final reminder for Invoice {invoice}."
            ]

        for msg in messages:
            st.code(msg)
