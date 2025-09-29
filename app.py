import streamlit as st
from bank import Bank

st.set_page_config(page_title="Banking System", layout="centered")
st.title("🏦 Simple Bank Management System")

menu = ["Create Account", "Deposit Money", "Withdraw Money", "Show Details", "Update Details", "Delete Account"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Create Account":
    st.header("Create a New Account")
    name = st.text_input("Enter Name")
    age = st.number_input("Enter Age", min_value=0, step=1)
    email = st.text_input("Enter Email")
    pin = st.text_input("Enter 4-digit PIN", type="password")

    if st.button("Create Account"):
        if not name or not email or not pin:
            st.warning("⚠ Please fill all fields.")
        else:
            account, msg = Bank.create_account(name, age, email, pin)
            st.success(msg)
            if account:
                st.json(account)

elif choice == "Deposit Money":
    st.header("Deposit Money")
    acc = st.text_input("Enter Account No")
    pin = st.text_input("Enter PIN", type="password")
    amount = st.number_input("Enter Amount", min_value=1, step=1)
    if st.button("Deposit"):
        st.info(Bank.deposit(acc, int(pin), amount))

elif choice == "Withdraw Money":
    st.header("Withdraw Money")
    acc = st.text_input("Enter Account No")
    pin = st.text_input("Enter PIN", type="password")
    amount = st.number_input("Enter Amount", min_value=1, step=1)
    if st.button("Withdraw"):
        st.info(Bank.withdraw(acc, int(pin), amount))

elif choice == "Show Details":
    st.header("Account Details")
    acc = st.text_input("Enter Account No")
    pin = st.text_input("Enter PIN", type="password")
    if st.button("Get Details"):
        details = Bank.details(acc, int(pin))
        if details:
            st.json(details)
        else:
            st.error("❌ Account not found.")

elif choice == "Update Details":
    st.header("Update Account Details")
    acc = st.text_input("Enter Account No")
    pin = st.text_input("Enter PIN", type="password")
    new_name = st.text_input("Enter New Name (optional)")
    new_email = st.text_input("Enter New Email (optional)")
    new_pin = st.text_input("Enter New 4-digit PIN (optional)", type="password")

    if st.button("Update"):
        st.success(Bank.update_details(acc, int(pin), new_name, new_email, new_pin))

elif choice == "Delete Account":
    st.header("Delete Account")
    acc = st.text_input("Enter Account No")
    pin = st.text_input("Enter PIN", type="password")
    if st.button("Delete"):
        st.error(Bank.delete(acc, int(pin)))
