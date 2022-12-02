import psycopg2

connection = {
 "dbname": "example",
 "user": "postgres",
 "password": "test",
 "port": 5432
}

# Create a connection
try:
   conn = psycopg2.connect(**connection)
except:
  print(f"I am unable to connect to the database with connection parameters:\n{connection}")
  exit(1)
  
# Create a cursor
cur = conn.cursor()

def employeeControls(em_id, f):
    print(f"\nHello {f[3]} {f[4]}! Position: {f[6]}")

    choice = 0
    while not(choice == 1 and choice == 2 and choice == 3 and choice == 4 and choice == 5):
        if f[6] == 'Manager':
            print("\nPlease, select an option from below:")
            print("1 - Create an account")
            print("2 - Delete an account")
            print("3 - Account Transactions")
            print("4 - Account Management")
            print("5 - Analytics")
            choice = int(input("\nPlease choose an option to continue: "))

            if choice == 1:
                pass
            elif choice == 2:
                pass
            elif choice == 3:
                pass
            elif choice == 4:
                pass
            elif choice == 5:
                pass
            else:
                print("\nPlease choose an option from above")

def employeeSignIn():
    while True:
        print("\nEmployee Sign in\n")
        employeeID = input("Please enter your employee ID: ")
        employeePassword = input("Enter your password: ")

        # Execute SQL Code & Fetch
        cur.execute("SELECT * FROM Employee WHERE emp_ID = '{}' AND password = '{}'".format(employeeID, employeePassword))
        found = cur.fetchone()

        if (found):
            employeeControls(employeeID, found)
        else:
            print("ID and/or Password is invalid. Try again.")

# Main
userInput = 0
while not(userInput == 1 and userInput == 2 and  userInput == 3 and userInput == 4):
    print("\nWelcome to the Banking Application\n")
    print("1 - Customer Sign in")
    print("2 - Customer Sign up")
    print("3 - Employee Sign in")
    print("4 - Exit")
    userInput = int(input("\nPlease choose an option to continue: "))

    if userInput == 1:
        pass
    elif userInput == 2:
        pass
    elif userInput == 3:
        employeeSignIn()
    elif userInput == 4:
        print("\nExiting...")
        exit()
    else:
        print("\nPlease choose an option from above.")

# Close the cursor
cur.close()

# Close the connection
conn.close()
