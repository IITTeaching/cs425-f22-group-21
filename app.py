import psycopg2

connection = {
 "dbname": "example",
 "user": "postgres",
 "password": "test",
 "port": 5432
}

#just wrote e in front of function that employees use and c that customers use
# Create a connection
try:
   conn = psycopg2.connect(**connection)
except:
  print(f"I am unable to connect to the database with connection parameters:\n{connection}")
  exit(1)
  
# Create a cursor
cur = conn.cursor()

# Withdrawl, Deposit, Transfer, and External transfer
# This can be accessed by managers, customers (for their own accounts), and tellers
def e_account_transaction(e_id, f):
    choice = 0
    while not(choice == 1 and choice == 2 and choice == 3 and choice == 4 and choice == 5):
        print("\nPlease, select an option from below:")
        print("1 - Withdrawl")
        print("2 - Deposit")
        print("3 - Transfer")
        print("4 - External transfer")
        print("5 - Go back")
        choice = int(input("\nPlease choose an option to continue: "))

        if choice == 1:
            e_Withdrawl(e_id, f)
        elif choice == 2:
            e_deposit(e_id, f)
        elif choice == 3:
            e_transfer(e_id, f)
        elif choice == 4:
            e_external_transfer(e_id, f)
        elif choice == 5:
            employee_controls(e_id, f)
        else:
            print("Please choose an option from above")

# Not sure what to do
def e_external_transfer():
    pass

# Employee withdrawl
def e_Withdrawl(e_id, f):
    choice = 0
    print("Which account to withdraw money?")
    try:
        input_num = int(input("Enter account number: "))
        cur.execute("SELECT * FROM Account WHERE account_num = '{}';".format(input_num))
        acc = cur.fetchone()
        input_amount = int(input("Enter amount of money to withdraw: "))
        print("Withdraw {amount} from account number {ac_num}?".format(amount = input_amount, ac_num = input_num))
        print("1 - yes")
        print("2 - no")        
        choice = int(input("Please choose an option to continue: "))

        if choice == 1 and acc[2] - input_amount >= 0:
            new_balance = acc[2] - input_amount
            cur.execute("UPDATE Account SET balance = {b} WHERE account_num = {a}".format(a = input_num,b = new_balance))
            print("{ac_num} has balance {amount}".format(amount = new_balance, ac_num = input_num))
            cur.execute("INSERT INTO Transaction VALUES ('By employee Withdraw {amount} from account number {ac_num}', {amount}, 'Withdrawl', {ac_id}, CURRENTCURRENT_TIMESTAMP);".format(amount = input_amount, ac_id = acc[0], ac_num = input_num))
            print("\nRedirecting to employee account transaction...")
            e_account_transaction(e_id, f)
        elif choice == 2:
            print("\nRedirecting to employee account transaction...")
            e_account_transaction(e_id, f)   
    except:
        print("c_id does not exists or does not have enough moeny")

# Employee deposit
def e_deposit(e_id, f):
    choice = 0
    print("Which account to deposit money?")
    try:
        input_num = int(input("Enter account number: "))
        cur.execute("SELECT * FROM Account WHERE account_num = '{}';".format(input_num))
        acc = cur.fetchone()
        input_amount = int(input("Enter amount of money to deposit: "))
        print("Deposit {amount} from account number {ac_num}?".format(amount = input_amount, ac_num = input_num))
        print("1 - yes")
        print("2 - no")        
        choice = int(input("Please choose an option to continue: "))

        if choice == 1:
            new_balance = acc[4] + input_amount
            cur.execute("UPDATE Account SET balance = {b} WHERE account_num = {a}".format(a = input_num,b = new_balance))
            print("{ac_num} has balance {amount}".format(amount = new_balance, ac_num = input_num))
            cur.execute("INSERT INTO Transaction VALUES ('By employee deposit {amount} from account number {ac_num}', {amount}, 'Deposit', {ac_id}, CURRENTCURRENT_TIMESTAMP);".format(amount = input_amount, ac_num = input_num, ac_id = acc[0]))
            print("\nRedirecting to employee account transaction...")
            e_account_transaction(e_id, f)
        elif choice == 2:
            print("\nRedirecting to employee account transaction...")
            e_account_transaction(e_id, f)   
    except:
        print("c_id does not exists or does not have enough moeny")

# Employee transfer
def e_transfer(e_id, f):
    choice = 0
    print("Which accounts to transfer money?")
    try:
        print("Enter account number: ")
        input_from = int(input("transfer from: "))
        input_to = int(input("transfer to: "))
        cur.execute("SELECT * FROM Account WHERE account_num = '{}';".format(input_from))
        acc_from = cur.fetchone()
        cur.execute("SELECT * FROM Account WHERE account_num = '{}';".format(input_to))
        acc_to = cur.fetchone()
        input_amount = int(input("Enter amount of money to transfer: "))
        print("transfer {amount} from account number {ac_num1} to account number {ac_num2}?".format(amount = input_amount, ac_num1 = input_from, ac_num2 = input_to))
        print("1 - yes")
        print("2 - no")        
        choice = int(input("Please choose an option to continue: "))

        if choice == 1 and acc_from[4] - input_amount >= 0:
            nbalance_from = acc_from[4] - input_amount
            nbalance_to = acc_to[4] + input_amount
            cur.execute("UPDATE Account SET balance = {b} WHERE account_num = {a}".format(a = nbalance_from,b = acc_from))
            cur.execute("UPDATE Account SET balance = {b} WHERE account_num = {a}".format(a = nbalance_to,b = acc_to))
            print("{ac_num1} has balance {amount1}\n{ac_num2} has balance {amount2}".format(amount1 = nbalance_from, amount2 = nbalance_to, ac_num1 = acc_from, ac_num2 = acc_to))
            cur.execute("INSERT INTO Transaction VALUES ('By employee transfer {amount} from account number {ac_num1} to account number {ac_num2}', {amount}, 'Transfer', {ac_id}, CURRENTCURRENT_TIMESTAMP);".format(amount = input_amount, ac_num1 = input_from, ac_num2 = input_to, ac_id = acc_from[0]))
            print("\nRedirecting to employee account transaction...")
            e_account_transaction(e_id, f)
        elif choice == 2:
            print("\nRedirecting to employee account transaction...")
            e_account_transaction(e_id, f)   
    except:
        print("c_id does not exists or does not have enough moeny") 

# Custumer transfer
def c_transfer (c_id):
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

        if choice == 1 and my_account[4] - amount >= 0:
            my_new_balance = my_account[4] - amount
            other_new_balance = other_account[4] + amount
            sql = "UPDATE account SET balance = {} WHERE account_id = '{}'".format(my_new_balance, my_account)
            cur.execute(sql)
            sql = "UPDATE account SET balance = {} WHERE account_id = '{}'".format(other_new_balance, other_account)
            cur.execute(sql)
            cur.execute("SELECT customer_username FROM Customer WHERE '{}'=customer_id".format(c_id))
            user_name = cur.fetchone()
            cur.execute("INSERT INTO Transaction VALUES ('By {user1} transfer {amount} from account number {ac_num1} to account number {ac_num2}', {amount}, 'Transfer', {ac_id}, CURRENTCURRENT_TIMESTAMP);".format(user1 = user_name, amount = amount, ac_num1 = my_account[1], ac_num2 = other_account[1], ac_id = c_id))
            print(f"\n Your current balance is :{my_new_balance[5]}")
            print("\nRedirecting to customer controls...")
            customer_controls(c_id)

        elif choice == 2:
            print("\nRedirecting to customer controls...")
            customer_controls(c_id)
        else:
            print("No authority or choose an option from above")

# Customer deposit
def c_deposit (c_id):
    amount = int(input("\nHow much would you like to deposit to your account?"))
    cur.execute("SELECT * FROM Account WHERE account_id = '{}'".format(c_id))
    account = cur.fetchone()
    print("\n depositing " + amount + " to your current balance of " + account[2])
    choice = 0
    while not (choice == 1 and choice == 2):
        print('\n Please, confirm the transaction:')
        print("1 - yes")
        print("2 - no")
        choice = int(input("\nPlease choose an option to continue: "))

        if choice == 1:
            new_balance = account[2] + amount
            sql = "UPDATE account SET balance = {} WHERE account_id = '{}'".format(new_balance, c_id)
            cur.execute(sql)
            cur.execute("SELECT customer_username FROM Customer WHERE '{}'=customer_id".format(c_id))
            user_name = cur.fetchone()
            cur.execute("INSERT INTO Transaction VALUES ('By {user} deposit {amount} from account number {ac_num}', {amount}, 'Deposit', {ac_id}, CURRENTCURRENT_TIMESTAMP);".format(user = user_name, amount = amount, ac_num = account[1], ac_id = c_id))
            print(f"\n Your current balance is :{account[2]}")
            print("\nRedirecting to customer controls...")
            customer_controls(c_id)

        elif choice == 2:
            print("\nRedirecting to customer controls...")
            customer_controls(c_id)
        else:
            print("No authority or choose an option from above")

# Customer withdrawl       
def c_withdrawal(c_id):
    amount = int(input("\nHow much would you like to withdraw from your account?"))
    cur.execute("SELECT * FROM Account WHERE account_id = '{}'".format(c_id))
    account = cur.fetchone()
    print("\n withdrawing " + amount + " to your current balance of " + account[2])
    choice = 0
    while not (choice == 1 and choice == 2):
        print('\n Please, confirm the transaction:')
        print("1 - yes")
        print("2 - no")
        choice = int(input("\nPlease choose an option to continue: "))

        if choice == 1 and account[2] - amount >= 0:
            new_balance = account[2] - amount
            sql = "UPDATE account SET balance = {} WHERE account_id = '{}'".format(new_balance, c_id)
            cur.execute(sql)
            cur.execute("SELECT customer_username FROM Customer WHERE '{}'=customer_id".format(c_id))
            user_name = cur.fetchone()
            cur.execute("INSERT INTO Transaction VALUES ('By {user} Withdraw {amount} from account number {ac_num}', {amount}, 'Withdrawl', {ac_id}, CURRENTCURRENT_TIMESTAMP);".format(user = user_name, amount = amount, ac_num = account[1], ac_id = c_id))
            print(f"\n Your current balance is :{account[2]}")
            print("\nRedirecting to customer controls...")
            customer_controls(c_id)

        elif choice == 2:
            print("\nRedirecting to customer controls...")
            customer_controls(c_id)
        else:
            print("No authority or choose an option from above")
          
# Add a new address
def add_address():
    try:
        street_name = input("Enter address: ")
        city = input("Enter city: ")
        state = input("Enter state: ")
        zip_code = input("Enter zip: ")

        cur.execute("SELECT address_id FROM Address ORDER BY address_id DESC;")
        all_ids = cur.fetchone()

        if len(all_ids) == 0:
            new_id = 1
        else:
            new_id = int(all_ids[0] + 1)

        cur.execute(f"INSERT INTO Address VALUES ({new_id}, '{street_name}', '{city}', '{state}', '{zip_code}');")
        conn.commit()

        return new_id

    except Exception as e:
        print(e)
          
# Choose a home branch
def choose_branch():
    cur.execute("SELECT branch_id, street_name, city, state, zip FROM Branch LEFT JOIN Address on branch_id = address_id;")
    all_branches = cur.fetchall()

    all_ids = []

    print() # spacing

    for rows in all_branches:
        all_ids.append(int(rows[0]))
        print(f"Branch ID: {rows[0]}, Address: {rows[1]} {rows[2]}, {rows[3]} {rows[4]}")
    
    h_branch_id = 0

    while h_branch_id not in all_ids:
        h_branch_id = int(input("Choose a home branch: "))

    return h_branch_id

# Create a new customer ID
def new_cid():
    cur.execute("SELECT customer_id FROM Customer ORDER BY customer_id DESC;")
    all_ids = cur.fetchone()

    if len(all_ids) == 0:
        return 1

    return all_ids[0] + 1
          
# Choose an account type for account creation
# IDK WHAT IM DOING
# HOPEFULLY THE LOGIC MAKES SENSE
def account_type(c_id):
    choice = 0
    account_num = ''.join(random.choice(string.digits) for _ in range(10))
    balance = c_deposit(c_id)

    while not(choice == 1 and choice == 2):
        print("\nChoose an account type:")
        print("1 - Checkings")
        print("2 - Savings")
        choice = int(input("Please choose an option: "))

        if choice == 1:
            try:
                cur.execute(f"SELECT account_id, account_type FROM AccountType WHERE account_id = {c_id};")
                found = cur.fetchall()

                # Checks if they have a checkings account already
                if (found[0] == c_id and found[1] == 'Checkings'):
                    print("You already have a checkings account.")
                    return False

                else:
                    cur.execute(f"INSERT INTO Account VALUES ({c_id}, {account_num}, {balance});")
                    cur.execute(f"INSERT INTO AccountType VALUES ('Checkings', {0}, 'FALSE', {0}, {0}, {c_id});")
                    conn.commit()
                    return True

            except Exception as e:
                print(e)
                return False

        elif choice == 2:
            try:
                cur.execute(f"SELECT account_id, account_type FROM AccountType WHERE account_id = {c_id};")
                found = cur.fetchall()

                # Checks if they have a savings account already
                if found[0] == c_id and found[1] == 'Savings':
                    print("You already have a savings account.")
                    return False
                
                else:
                    cur.execute(f"INSERT INTO Account VALUES ({c_id}, {account_num}, {balance});")
                    cur.execute(f"INSERT INTO AccountType VALUES ('Savings', {0}, 'FALSE', {0}, {0}, {c_id});")
                    conn.commit()
                    return True

            except Exception as e:
                print(e)
                return False
          
# Manager create customer account
def e_create_account(e_id, f):
    print("\nWelcome to Account Creation!\n")

    cust_id = new_cid()

    worked = account_type(cust_id)

    if worked:
        pass # leave as is
    else:
        e_account_management(f)

    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    lives_at_id = add_address()
    home_branch_id = choose_branch()
    user_name = input("Create a username (max characters is 10): ")
    password = input("Create a new password (max characters is 12): ")

    while len(user_name) > 11:
        user_name = input("Create a username (max characters is 10): ")

    while len(password) > 13:
        password = input("Create a new password (max characters is 12): ")

    # Insert inputted values into Customer table
    cur.execute(f"INSERT INTO Customer VALUES ({cust_id}, '{user_name}', '{password}', {home_branch_id}, '{first_name}', '{last_name}', {lives_at_id});")
    conn.commit()

    print(f"\nSuccessfully created an account for {first_name} {last_name}!\n")
    print("\nBringing you back to Account Management page...")
    e_account_management(e_id, f) # Brings back to Manager Account
    
# Customer create customer account
def c_create_account(c_id):
    print("\nWelcome to Account Creation!\n")

    cust_id = new_cid()

    worked = account_type(cust_id)

    if worked:
        pass # leave as is
    else:
        c_account_management()

    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    lives_at_id = add_address()
    home_branch_id = choose_branch()
    user_name = input("Create a username (max characters is 10): ")
    password = input("Create a new password (max characters is 12): ")

    while len(user_name) > 11:
        user_name = input("Create a username (max characters is 10): ")

    while len(password) > 13:
        password = input("Create a new password (max characters is 12): ")

    # Insert inputted values into Customer table
    cur.execute(f"INSERT INTO Customer VALUES ({cust_id}, '{user_name}', '{password}', {home_branch_id}, '{first_name}', '{last_name}', {lives_at_id});")
    conn.commit()

    print(f"\nSuccessfully created an account for {first_name} {last_name}!\n")
    print("\nBringing you back to Account Management page...")
    c_account_management(c_id) # Brings back to customer account
          
# Manager customer Account Deletion
def e_delete_account(e_id, f):
    print("\nCustomer Account Deletion Page\n")

    acc_num = int(input("\nPlease enter your account number to continue: "))

    sql = f"SELECT a.account_id, a.account_num, t.account_type FROM customer c LEFT JOIN account a ON c.customer_id = a.account_id LEFT JOIN accounttype t ON a.account_id = t.account_id WHERE a.account_num = {acc_num};"

    cur.execute(sql)
    accounts = cur.fetchall()

    acc_ids1 = []

    for rows in accounts:
        acc_ids1.append(int(rows[0]))
        print(f"{rows[0]} - Account #{rows[1]} & Account Type: {rows[2]}")

    choice = 0
    while choice not in acc_ids1:
        choice = int(input("Please choose which account you want to delete: "))

    # Executes the deletion
    try:
        cur.execute(f"DELETE FROM Account WHERE account_id = {choice};")
        cur.execute(f"DELETE FROM AccountType WHERE account_id = {choice};")
        conn.commit()

        print("Successfully deleteed account.")
        print("Redirecting back to Account Management Page....")
        e_account_management(e_id, f)

    except Exception as e:
        print(e, "Error occured while delete account.")
        print("Redirecting back to Account Management Page....")
        e_account_management(e_id, f)
          
# Customer customer Account Deletion
def c_delete_account(c_id):
    print("\nCustomer Account Deletion Page\n")

    acc_num = int(input("\nPlease enter your account number to continue: "))

    sql = f"SELECT a.account_id, a.account_num, t.account_type FROM customer c LEFT JOIN account a ON c.customer_id = a.account_id LEFT JOIN accounttype t ON a.account_id = t.account_id WHERE a.account_num = {acc_num};"

    cur.execute(sql)
    accounts = cur.fetchall()

    acc_ids2 = []

    for rows in accounts:
        acc_ids2.append(int(rows[0]))
        print(f"{rows[0]} - Account #{rows[1]} & Account Type: {rows[2]}")

    choice = 0
    while choice not in acc_ids2:
        choice = int(input("Please choose which account you want to delete: "))

    # Executes the deletion
    try:
        cur.execute(f"DELETE FROM Account WHERE account_id = {choice};")
        cur.execute(f"DELETE FROM AccountType WHERE account_id = {choice};")
        conn.commit()

        print("Successfully deleteed account.")
        print("Redirecting back to Account Management Page....")
        c_account_management()

    except Exception as e:
        print(e, "Error occured while delete account.")
        print("Redirecting back to Account Management Page....")
        c_account_management(c_id)
        
# Withdrawl, Deposit, Transfer, and External transfer - Employees
def e_account_transaction(e_id, f):
    choice = 0
    while not(choice == 1 and choice == 2 and choice == 3 and choice == 4 and choice == 5):
        print("\nPlease, select an option from below:")
        print("1 - Withdrawl")
        print("2 - Deposit")
        print("3 - Transfer")
        print("4 - External transfer")
        print("5 - Go back")
        choice = int(input("\nPlease choose an option to continue: "))

        if choice == 1:
            e_Withdrawl(e_id, f)
        elif choice == 2:
            e_deposit(e_id, f)
        elif choice == 3:
            e_transfer(e_id, f)
        elif choice == 4:
            e_external_transfer(e_id, f)
        elif choice == 5:
            employee_controls(e_id, f)
        else:
            print("Please choose an option from above")
  
# Withdrawl, Deposit, Transfer, and External transfer - Customer
def c_account_transaction(c_id):
    choice = 0
    while not (choice == 1 and choice == 2 and choice == 3 and choice == 4):
        print("\nPlease, select an option from below:")
        print("1 - Withdrawal")
        print("2 - Deposit")
        print("3 - Transfer")
        print("4 - Exit")
        choice = int(input("\nPlease choose an option to continue: "))

        if choice == 1:
            c_withdrawal(c_id)
        elif choice == 2:
            c_deposit(c_id)
        elif choice == 3:
            c_transfer(c_id)
        elif userInput == 4:
            print("\nRedirecting to customer controls...")
            customer_controls(c_id)
        else:
            print("No authority or choose an option from above")
          
# Customer account managemet
def c_account_management(c_id):
    print("\nCustomer Account Management Page\n")

    choice = 0
    while not(choice == 1 and choice == 2 and choice == 3 and choice == 4 and choice == 5):
        print("What would you like to do?")
        print("1 - Create an account")
        print("2 - Delete an account")
        print("3 - Show statement for an account")
        print("4 - Show pending transactions for an account")
        print("5 - Go back")
        choice = int(input("\nPlease choose an option to continue: "))

        if choice == 1:
            c_create_account(c_id)
        elif choice == 2:
            c_delete_account(c_id)
        elif choice == 3:
            c_show_statement(c_id)
        elif choice == 4:
            c_show_pending_trans(c_id)
        elif choice == 5:
            customer_controls(c_id)
        else:
            print("Invalid choice.")

# Not sure what to do on pending transaction
def c_show_pending_trans(c_id):
    pass

# Customer show statement
def c_show_statement(c_id):
    input_mon = input("Enter specific month to see statement: ")
    cur.execute("SELECT * FROM Transactions WHERE account_id = {} and month(trans_time) = {}".format(c_id, input_mon))
    statement = cur.fetchall()
    print(statement)
    c_account_management(c_id)

# Employee show statement
def e_show_statement(e_id, f):
    input_id = input("Enter account id to see statement: ")
    input_mon = input("Enter specific month to see statement: ")
    cur.execute("SELECT * FROM Transactions WHERE account_id = {} and month(trans_time) = {}".format(input_id, input_mon))
    statement = cur.fetchall()
    print(statement)
    e_account_management(e_id, f)

# Customer controls
def customer_controls(c_id):
    print("\nWelcome to Customer Controls!\n")

    choice = 0
    while not(choice == 1 and choice == 2 and choice == 3):
        print("\nSelect an option:")
        print("1 - Account Transactions")
        print("2 - Account Management")
        print("3 - Log out")
        choice = int(input("\nPlease choose an option to continue: "))
    
        if choice == 1:
            c_account_transaction(c_id)
        elif choice == 2:
            c_account_management(c_id)
        elif choice == 3:
            print("\nLogging you out...")
            exit(1)
        else:
            print("Invalid choice.")
          
# Manage accounts
# Managers only have access to this information
# There should also be an account management page for customers seperate from this one
# Account Management page for customers include: create, delete, show statement, and pending transactions
def e_account_management(e_id, f):
    print("\nManager Account Management Page\n")

    choice = 0
    while not(choice == 1 and choice == 2 and choice == 3 and choice == 4 and choice == 5 and choice == 6):
        print("What would you like to do?")
        print("1 - Create an account")
        print("2 - Delete an account")
        print("3 - Show statement for an account")
        print("4 - Show pending transactions for an account")
        print("5 - Add interest, overdraft fees, or account fees for an account")
        print("6 - Log out")
        choice = int(input("\nPlease choose an option to continue: "))

        if choice == 1:
            e_create_account(e_id, f)
        elif choice == 2:
            e_delete_account(e_id, f)
        elif choice == 3:
            e_show_statement(e_id, f)
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        elif choice == 6:
            print("\nLogging you out...")
            exit(1)
        else:
            print("\nPlease chooce an option from above")

# Manager analytics          
def e_analytics(employee_id, f):
    cur.execute("SELECT * FROM Employee WHERE emp_ID = '{}';".format(employee_id))
    employee = cur.fetchone()
    cur.execute("SELECT count(*) FROM (SELECT * FROM Employee WHERE works_at = {}) l".format(employee[8]))
    tot_emp = cur.fetchone()
    cur.execute("SELECT count(*) FROM (SELECT * FROM Employee WHERE works_at = {} and emp_role = 'Manager') l GROUP BY emp_role".format(employee[8]))
    num_manager = cur.fetchone()
    cur.execute("SELECT count(*) FROM (SELECT * FROM Employee WHERE works_at = {} and emp_role = 'Teller') l GROUP BY emp_role".format(employee[8]))
    num_teller = cur.fetchone()
    cur.execute("SELECT count(*) FROM (SELECT * FROM Employee WHERE works_at = {} and emp_role = 'Loan Specialist') l GROUP BY emp_role".format(employee[8]))
    num_loansp = cur.fetchone()
    cur.execute("SELECT avg(salary) FROM (SELECT * FROM Employee WHERE works_at = {} and emp_role = 'Manager') l GROUP BY emp_role".format(employee[8]))
    avg_salary_manager = cur.fetchone()
    cur.execute("SELECT avg(salary) FROM (SELECT * FROM Employee WHERE works_at = {} and emp_role = 'Teller') l GROUP BY emp_role".format(employee[8]))
    avg_salary_teller = cur.fetchone()
    cur.execute("SELECT avg(salary) FROM (SELECT * FROM Employee WHERE works_at = {} and emp_role = 'Loan Specialist') l GROUP BY emp_role".format(employee[8]))
    avg_salary_loansp = cur.fetchone()
    cur.execute("SELECT count(*) FROM Customer WHERE home_branch = {}".format(employee[8]))
    num_customer = cur.fetchone()
    cur.execute("SELECT avg(balance) FROM (SELECT * FROM Account WHERE account_id IN (SELECT customer_id FROM Customer WHERE home_branch = {}) ) l".format(employee[8]))
    avg_balance = cur.fetchone()
    cur.execute("SELECT sum(balance) FROM (SELECT * FROM Account WHERE account_id IN (SELECT customer_id FROM Customer WHERE home_branch = {})) l".format(employee[8]))
    tot_balance = cur.fetchone()
    print("\n", tot_balance, "\n")
    if num_teller == None:
        num_teller = [0]
        avg_salary_teller = [0]
    if num_loansp == None:
        num_loansp = [0]
        avg_salary_loansp = [0]
    if num_customer == None:
        num_customer = [0]
        avg_balance = [0]
        tot_balance = [0]
    print(f"Analytic of branch {employee[8]}: \n\
            -Number of employees: {tot_emp[0]}\n manager: {num_manager[0]}\n teller: {num_teller[0]}\n loan specialist: {num_loansp[0]}\n\
            -Salary:\n manager: {avg_salary_manager[0]}\n teller: {avg_salary_teller[0]}\n loan specialist: {avg_salary_loansp[0]}\n\
            -Customer:\n number of customer: {num_customer[0]}\n averager balance: {avg_balance[0]}\n total balance {tot_balance[0]}")
    
# Employee controls
def employee_controls(e_id, f):
    print("\nWelcome to Employee Controls!\n")

    choice = 0
    while not(choice == 1 and choice == 2 and choice == 3 and choice == 4):
        print("\nSelect an option:")
        print("1 - Account Transactions")
        print("2 - Account Management")
        print("3 - Analytics")
        print("4 - Log out")
        choice = int(input("\nPlease choose an option to continue: "))

        if choice == 1 and (f[6] == 'Manager' or f[6] == 'Bank Teller'):
            e_account_transaction(e_id, f)
        elif choice == 2 and f[6] == 'Manager':
            e_account_management(e_id, f)
        elif choice == 3 and f[6] == 'Manager':
            e_analytics(e_id, f)
        elif choice == 4:
            print("\nLogging you out...")
            exit(1)
        else:
            print("No authority or invalid choice.")

# Customer sign in
def c_signIn():
    while True:
        print("\nCustomer Sign in\n")

        user_name = input("Enter your username: ")
        password = input("Enter you password: ")

        cur.execute(f"SELECT * FROM Customer WHERE customer_username = '{user_name}' AND customer_password = '{password}';")
        found = cur.fetchone()

        if found:
            print(f"\nHello {found[4]} {found[5]}!\nID: {found[0]}")
            customer_controls(found[0])
        else:
            print("ID and/or Password is invalid. Try again.")
          
# Employee sign in
def e_signIn():
    while True:
        print("\nEmployee Sign in\n")

        em_id = input("Enter your employee ID: ")
        em_pass = input("Enter your password: ")

        cur.execute(f"SELECT * FROM Employee WHERE emp_ID = '{em_id}' AND password = '{em_pass}'")
        found = cur.fetchone()

        if found:
            print(f"\nHello {found[3]} {found[4]}!\nPosition: {found[6]}\nID: {found[0]}")
            employee_controls(em_id, found)
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
        c_signIn()
    elif userInput == 2:
        c_create_account()  # need to change the page they are brought back to-- currently goes to account management
    elif userInput == 3:
        e_signIn()
    elif userInput == 4:
        print("\nExiting...")
        exit(1)
    else:
        print("\nPlease choose an option from above.")
      
# Close the cursor
cur.close()

# Close the connection
conn.close()
