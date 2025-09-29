# Python Bank Management Project

A simple **Bank Management System** built with Python, featuring a command-line interface and a user-friendly frontend powered by Streamlit. This project allows users to:
- Create bank accounts
- Deposit money
- Withdraw money
- View account details
- Update account information
- Delete accounts

All data is stored locally in a JSON file for simplicity and easy management.

---

## Features

- **Account Creation:** Users can register a new bank account with basic details.
- **Deposit Money:** Deposit funds into an existing account, with simple validation.
- **Withdraw Money:** Withdraw funds, ensuring sufficient balance.
- **Account Details:** Securely access and display your account information.
- **Update Details:** Modify your name, email, or PIN (age/account number/balance are immutable).
- **Delete Account:** Remove your account safely after confirmation.
- **Front End with Streamlit:** A graphical interface for all major functionalities (see below).

---

## How It Works

The core logic is implemented in the `Bank` class. Functions are provided for each operation, with input and output managed through the console or Streamlit app. Data is persisted in a local `data.json` file.

### Main Functionalities

- **Create account:** Validates age and PIN before creation.
- **Deposit/Withdraw:** Validates account info and transaction amount.
- **Show/Update/Delete:** Securely access and modify account.

---

## Getting Started

### Prerequisites

- Python 3.7+
- [Streamlit](https://streamlit.io/) (`pip install streamlit`)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Bhawneet1/Python_Bank_Management_Project.git
   cd Python_Bank_Management_Project
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **(Optional) Sample Data:**
   - The system will create a `data.json` file automatically on first run if it doesn't exist.

---

## Running the Application

### 1. Command-Line Interface

To use the text-based version, run:

```bash
python bank_system.py
```
*(Replace `bank_system.py` with your script filename.)*

You will be prompted to select an action and provide necessary details.

---

### 2. Streamlit Front End

A user-friendly GUI is included, built with Streamlit.

**To launch the Streamlit app:**

```bash
streamlit run streamlit_app.py
```

You will be able to:
- Sign up for a new account
- Log in with account number and PIN
- View, update, deposit, withdraw, or delete your account
- All via an interactive web interface

---

## Project Structure

```
.
├── bank_system.py         # Main Python logic (CLI)
├── streamlit_app.py       # Streamlit frontend
├── data.json              # Data storage (auto-generated)
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## Screenshots

*You can add screenshots of your Streamlit UI here for better visualization.*

---

## Contributing

Contributions are welcome! Please open issues or submit pull requests.

---

## License

This project is licensed under the MIT License.

---

## Author

- [Bhawneet1](https://github.com/Bhawneet1)

---

### Notes

- This is a basic educational project. For real-world banking or sensitive data, implement stronger authentication and security measures.
- Make sure you do not share sensitive account info with anyone.
