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

# Create a new customer ID
def c_id():
    cur.execute("SELECT customer_id FROM Customer ORDER BY customer_id DESC")
    id = cur.fetchall()

    if len(id) == 0:
        return 1

    return id[0] + 1

# Add an address
def add_address():
    try:
        add = str(input("Enter address: "))
        city = str(input("Enter city: "))
        state = str(input("Enter state: "))
        zip = str(input("Enter zip: "))

        cur.execute("SELECT address_id FROM Address ORDER BY address_id DESC;")
        add_id = cur.fetchall
        
        if len(add_id) == 0:
            new_add = 1
        else:
            new_add = add_id[0] + 1;

        cur.execute(f"INSERT INTO Address VALUES ({new_add}, '{add}', '{city}', '{state}', '{zip}');")
        conn.commit()

        return new_add

    except:
        print("Error occured while trying to add address.")
        yesno = input("Do you want to try again? (y/n): ")

        if yesno.lower() == 'y':
            add_address()
        else:
            pass

# Selecting a home branch
def choose_branch():
    cur.execute("SELECT branch_id, add, city, state, zip FROM Branch LEFT JOIN Address ON branch_id = address_id;")
    all_branches = cur.fetchall()

    h_ids=[]

    for rows in all_branches:
        h_ids.append(int(rows[0]))
        print(f"\nBranch ID: {rows[0]}, Address: {rows[1]} {rows[2]}, {rows[3]} {rows[4]}")
    
    h_branch = 0

    while h_branch not in h_ids:
        h_branch = int(input("Choose a home branch: "))

    return h_branch

# For bank account creation - Checkings OR Savings
def checks_savings(c_id, un, p):
    choice = 0
    account_num = ''.join(random.choice(string.digits) for _ in range(10))

    balance = input("Enter a starting balance for your account: ") # Don't know what to really put for the balance part of it

    while not(choice == 1 and choice == 2):
        print("\nChoose the account type")
        print("1 - Checkings")
        print("2 - Savings")
        choice = int(input("Please choose one: "))
    
    if choice == 1:
        try:
            cur.execute(f"INSERT INTO Account VALUES ({c_id}, {account_num}, '{un}', '{p}', {balance});")
            cur.execute(f"INSERT INTO AccountType VALUES ('Checkings', {0}, 'FALSE', {0}, {0}, {c_id});")
            conn.commit()
        except:
            print("Didn't work.")
    else:
        try:
            cur.execute(f"INSERT INTO Account VALUES ({c_id}, {account_num}, '{un}', '{p}', {balance});")
            cur.execute(f"INSERT INTO AccountType VALUES ('Savings', {0}, 'FALSE', {0}, {0}, {c_id});")
            conn.commit()
        except:
            print("Didn't work.")

# Create a customer account
def create_account():
    try:
        print("\nWelcome to Account Creation\n")
        
        fname = str(input("Enter first name: "))
        lname = str(input("Enter last name: "))
        address = add_address()
        h_branch = choose_branch()
        cust_id = c_id()
        userName = input("Please enter a username (Max characters is 10): ")
        password = input("Please enter a passoword (Max characters is 12): ")

        cur.execute(f"INSERT INTO Customer VALUES ({cust_id}, {userName}, {password}, {h_branch}, '{fname}', '{lname}', '{address}');")
        conn.commit()


        checks_savings(cust_id, userName, password)

        print(f"\nSuccessfully created an account for {fname} {lname}!\n")
        
        print("\nBring you back to Account Management page...") # Needs to be brought back to account management page for employees only
        account_managment() 
        
    except:
        print("Didnt work.")

# Customers, Managers only
# Customers can only remove their own account
# Don't know how this would really work though
def delete_account():
    pass

# Withdrawl, Deposit, Transfer, and External transfer
# This can be accessed by managers, customers (for their own accounts), and tellers
def account_transaction():
    choice = 0
    while not(choice == 1 and choice == 2 and choice == 3 and choice == 4):
        print("\nPlease, select an option from below:")
        print("1 - Withdrawl")
        print("2 - Deposit")
        print("3 - Transfer")
        print("4 - External transfer")
        print("5 - Log out") # or maybe go back or main
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
            print("\nLogging you out...") 
            exit(1)
        else:
            print("Please choose an option from above")

# Manage accounts
# Managers only have access to this information
# There should also be an account management page for customers seperate from this one
  # Account Management page for customers include: create, delete, show statement, and pending transactions
def account_managment():
    choice = 0
    while not(choice == 1 and choice == 2 and choice == 3 and choice == 4 and choice == 5 and choice == 6):
        print("\nAccount Management\n")
        print("What would you like to do?")
        print("1 - Create an account")
        print("2 - Delete an account")
        print("3 - Show statement for an account")
        print("4 - Show pending transactions for an account")
        print("5 - Add interest, overdraft fees, or account fees for an account")
        print("6 - Log out")
        choice = int(input("\nPlease choose an option to continue: "))

        if choice == 1:
            create_account()
        elif choice == 2:
            delete_account()
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        elif choice == 6:
            print("\nLogging you out...")
            exit(1)
        else:
            print("\nPlease chooce an option from above")


def analytics():
    pass

#def loan():
#   pass
 
# Controls for employees
# So far only have done it for manager
def employeeControls(em_id, f):
    print(f"\nHello {f[3]} {f[4]}! Position: {f[6]}\nID: {em_id}")

    choice = 0
    #if f[6] == 'Manager':
    while not(choice == 1 and choice == 2 and choice == 3 and choice == 4):
        print("\nPlease, select an option from below:")
        print("1 - Account Transactions")
        print("2 - Account Management")
        print("3 - Analytics")
        print("4 - Log out") #loan maybe
        choice = int(input("\nPlease choose an option to continue: "))

        if choice == 1 and (f[6] == 'Manager' or 'Teller'):
            pass #account_transaction()
        elif choice == 2 and f[6] == 'Manager':
            account_managment()
        elif choice == 3 and f[6] == 'Manager':
            pass #analytics()
        elif choice == 4:
            print("\nLogging you out...") # Once they log out should they be brought back to the main screen instead of exiting?
            exit(1)
        else:
            print("No authority or choose an option from above")

# Employee Sign in
# Searches for ID and Password match
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

def transfer (c_id, f):
    other_accountid = int(input("\nPlease insert account number to transfer money to: "))
    cur.execute("SELECT * FROM Account WHERE account_id = '{}'".format(c_id))
    my_account = cur.fetchone()
    cur.execute("SELECT * FROM Account WHERE account_id = '{}'".format(other_accountid))
    other_account = cur.fetchone()

    amount = int(input("\nHow much would you like to transfer to another account?"))

    choice = 0
    while not (choice == 1 and choice == 2):
        print('\n Please, confirm the transaction:')
        print("1 - yes")
        print("2 - no")
        choice = int(input("\nPlease choose an option to continue: "))

        if choice == 1:
            my_new_balance = my_account[4] - amount
            other_new_balance = other_account[4] + amount
            sql = "UPDATE account SET balance = {} WHERE account_id = '{}'".format(my_new_balance, my_account)
            cur.execute(sql)
            sql = "UPDATE account SET balance = {} WHERE account_id = '{}'".format(other_new_balance, other_account)
            cur.execute(sql)

            print(f"\n Your current balance is :{my_new_balance[5]}")
            print("\nRedirecting to customer controls...")
            customerControls(c_id, f)

        elif choice == 2:
            print("\nRedirecting to customer controls...")
            customerControls(c_id, f)
        else:
            print("No authority or choose an option from above")

def deposit (c_id, f):
    amount = int(input("\nHow much would you like to deposit to your account?"))
    cur.execute("SELECT * FROM Account WHERE account_id = '{}'".format(c_id))
    account = cur.fetchone()
    print("\n depositing " + amount + " to your current balance of " + account[4])
    choice = 0
    while not (choice == 1 and choice == 2):
        print('\n Please, confirm the transaction:')
        print("1 - yes")
        print("2 - no")
        choice = int(input("\nPlease choose an option to continue: "))

        if choice == 1:
            new_balance = account[4] + amount
            sql = "UPDATE account SET balance = {} WHERE account_id = '{}'".format(new_balance, c_id)
            cur.execute(sql)
            print(f"\n Your current balance is :{account[5]}")
            print("\nRedirecting to customer controls...")
            customerControls(c_id, f)

        elif choice == 2:
            print("\nRedirecting to customer controls...")
            customerControls(c_id, f)
        else:
            print("No authority or choose an option from above")
def withdrawal(c_id, f):
    amount = int(input("\nHow much would you like to withdraw from your account?"))
    cur.execute("SELECT * FROM Account WHERE account_id = '{}'".format(c_id))
    account = cur.fetchone()
    print("\n withdrawing " + amount + " to your current balance of " + account[4])
    choice = 0
    while not (choice == 1 and choice == 2):
        print('\n Please, confirm the transaction:')
        print("1 - yes")
        print("2 - no")
        choice = int(input("\nPlease choose an option to continue: "))

        if choice == 1:
            new_balance = account[4] - amount
            sql = "UPDATE account SET balance = {} WHERE account_id = '{}'".format(new_balance, c_id)
            cur.execute(sql)
            print(f"\n Your current balance is :{account[5]}")
            print("\nRedirecting to customer controls...")
            customerControls(c_id, f)

        elif choice == 2:
            print("\nRedirecting to customer controls...")
            customerControls(c_id, f)
        else:
            print("No authority or choose an option from above")

def c_account_transaction(c_id, f):
    choice = 0
    while not (choice == 1 and choice == 2 and choice == 3 and choice == 4):
        print("\nPlease, select an option from below:")
        print("1 - Withdrawal")
        print("2 - Deposit")
        print("3 - Transfer")
        print("4 - Exit")
        choice = int(input("\nPlease choose an option to continue: "))

        if choice == 1:
            withdrawal(c_id, f)
        elif choice == 2:
            deposit(c_id, f)
        elif choice == 3:
            transfer(c_id, f)
        elif userInput == 4:
            print("\nRedirecting to customer controls...")
            customerControls(c_id, f)
        else:
            print("No authority or choose an option from above")

# Customer Sign in
# Searches for ID and Password match
def customerControls(c_id, f):
    print(f"\nHello {f[4]} {f[5]}! \nID: {c_id}")

    choice = 0
    while not (choice == 1 and choice == 2 and choice == 3 and choice == 4):
        print("\nPlease, select an option from below:")
        print("1 - Account Transactions")
        print("2 - Account Management")
        print("3 - Log out")
        choice = int(input("\nPlease choose an option to continue: "))

        if choice == 1:
            c_account_transaction(c_id, f)
        elif choice == 2:
            #c_account_managment()
            pass
        elif choice == 3:
            print(
                "\nLogging you out...")
            exit(1)
        else:
            print("No authority or choose an option from above")

def customerSignIn():
    while True:
        print("\nCustomer Sign in\n")
        c_username = input("Please enter your username: ")
        c_password = input("Enter your password: ")

        # Execute SQL Code & Fetch
        cur.execute("SELECT * FROM Customer WHERE customer_username = '{}' AND customer_password = '{}'".format(c_username, c_password))
        found = cur.fetchone()

        if (found):
            customerControls(found[0], found)
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
        customerSignIn()
    elif userInput == 2:
        create_account()  # need to change the page they are brought back to-- currently goes to account management
    elif userInput == 3:
        employeeSignIn()
    elif userInput == 4:
        print("\nExiting...")
        exit(1)
    else:
        print("\nPlease choose an option from above.")
      
# Close the cursor
cur.close()

# Close the connection
conn.close()
