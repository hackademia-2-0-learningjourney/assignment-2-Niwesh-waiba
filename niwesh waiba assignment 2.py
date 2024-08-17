import json

# File to store user data
file_name = 'userData.json'

# Function to add a new user to the JSON file
def addUser(userName, password, phoneNumber):
    # Load existing data
    try:
        with open(file_name, 'r') as f:
            users_data = json.load(f)
    except FileNotFoundError:
        users_data = {}

    # Add new user data
    users_data[userName] = {
        'password': password,
        'phoneNumber': phoneNumber
    }

    # Save updated data back to the file
    with open(file_name, 'w') as f:
        json.dump(users_data, f)

# Function to check user credentials during sign in
def signIn(userName, password):
    try:
        with open(file_name, 'r') as f:
            users_data = json.load(f)
    except FileNotFoundError:
        return False, None

    if userName in users_data and users_data[userName]['password'] == password:
        return True, users_data[userName]['phoneNumber']
    else:
        return False, None

while True:
    choice = input('Enter \n1 for sign up \n2 for sign in \n3 to quit\n')
    
    if choice == '1':
        userName = input('Enter Username: ')
        password = input('Enter Password: ')
        phoneNumber = input('Enter Phone Number: ')
        addUser(userName, password, phoneNumber)
        print('User signed up successfully!\n')
        
    elif choice == '2':
        userName = input('Enter Username: ')
        password = input('Enter Password: ')
        is_valid, phoneNumber = signIn(userName, password)
        
        if is_valid:
            print(f'Welcome to the device! Your phone number is {phoneNumber}\n')
        else:
            print('Invalid credentials. Program terminated.')
            break
        
    elif choice == '3':
        print('Exiting the program.')
        break
        
    else:
        print('Invalid choice. Please try again.\n')
