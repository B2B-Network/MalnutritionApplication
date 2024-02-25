
import pandas as pd
import csv

def sign_up_insert(name, email, password, phone_number):
    try:
        # Create a DataFrame with the user data
        user_data = pd.DataFrame({
            'name': [name],
            'email': [email],
            'password': [password],
            'phone_number': [phone_number]
        })

        # Write the DataFrame to a CSV file
        with open('signup_user.csv', mode='a', newline='') as file:
            user_data.to_csv(file, header=not file.tell(), index=False)

        print('User saved to CSV file')
    except Exception as e:
        print(f'Error: {e}')

def insert_login_details(email, password):
    try:
        # Create a DataFrame with the user data
        user_data = pd.DataFrame({
            'email': [email],
            'password': [password]
        })

        # Write the DataFrame to a CSV file
        with open('login_data.csv', mode='a', newline='') as file:
            user_data.to_csv(file, header=not file.tell(), index=False)

        print('User saved to CSV file')
    except Exception as e:
        print(f'Error: {e}')

def prediction(age,bmi,muac,cc,hc,mw,fd):
    try:
        # Create a DataFrame with the user data
        user_data = pd.DataFrame({
            'age': [age],
            'bmi': [bmi],
            'muac': [muac],
            'cc': [cc],
            'hc': [hc],
            'mw': [mw],
            'fd': [fd],
        })

        # Write the DataFrame to a CSV file
        with open('user_details.csv', mode='a', newline='') as file:
            user_data.to_csv(file, header=not file.tell(), index=False)

        print('User saved to CSV file')
    except Exception as e:
        print(f'Error: {e}')
