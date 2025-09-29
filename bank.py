import json
import random
import string
from pathlib import Path


class Bank:
    database = 'data.json'
    data = []

    # Load existing data
    try:
        if Path(database).exists():
            with open(database, "r") as fs:
                data = json.load(fs)
        else:
            data = []
    except Exception as err:
        print(f"An exception occurred: {err}")
        data = []

    @classmethod
    def __update(cls):
        """Update JSON file with latest data"""
        with open(cls.database, 'w') as fs:
            json.dump(cls.data, fs, indent=4)

    @classmethod
    def __accountgenerate(cls):
        """Generate a random account number"""
        alpha = random.choices(string.ascii_uppercase, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*", k=1)
        acc_id = alpha + num + spchar
        random.shuffle(acc_id)
        return "".join(acc_id)

    @classmethod
    def create_account(cls, name, age, email, pin):
        if age < 18 or len(str(pin)) != 4:
            return None, "❌ Sorry, you cannot create an account."

        info = {
            "name": name,
            "age": age,
            "email": email,
            "pin": int(pin),
            "accountNo": cls.__accountgenerate(),
            "balance": 0
        }

        cls.data.append(info)
        cls.__update()
        return info, "✅ Account created successfully!"

    @classmethod
    def authenticate(cls, accountNo, pin):
        return [i for i in cls.data if i['accountNo'] == accountNo and i['pin'] == pin]

    @classmethod
    def deposit(cls, accountNo, pin, amount):
        userdata = cls.authenticate(accountNo, pin)
        if not userdata:
            return "❌ Account not found."
        if amount <= 0 or amount > 10000:
            return "❌ Deposit must be between 1 and 10000."
        userdata[0]['balance'] += amount
        cls.__update()
        return f"✅ Deposited {amount}. New Balance: {userdata[0]['balance']}"

    @classmethod
    def withdraw(cls, accountNo, pin, amount):
        userdata = cls.authenticate(accountNo, pin)
        if not userdata:
            return "❌ Account not found."
        if amount <= 0 or amount > userdata[0]['balance']:
            return "❌ Invalid withdrawal amount."
        userdata[0]['balance'] -= amount
        cls.__update()
        return f"✅ Withdrawn {amount}. New Balance: {userdata[0]['balance']}"

    @classmethod
    def details(cls, accountNo, pin):
        userdata = cls.authenticate(accountNo, pin)
        if not userdata:
            return None
        return userdata[0]

    @classmethod
    def update_details(cls, accountNo, pin, new_name=None, new_email=None, new_pin=None):
        userdata = cls.authenticate(accountNo, pin)
        if not userdata:
            return "❌ Account not found."

        if new_name:
            userdata[0]['name'] = new_name
        if new_email:
            userdata[0]['email'] = new_email
        if new_pin and len(str(new_pin)) == 4:
            userdata[0]['pin'] = int(new_pin)

        cls.__update()
        return "✅ Details updated successfully!"

    @classmethod
    def delete(cls, accountNo, pin):
        userdata = cls.authenticate(accountNo, pin)
        if not userdata:
            return "❌ Account not found."
        cls.data.remove(userdata[0])
        cls.__update()
        return "✅ Account deleted successfully."
