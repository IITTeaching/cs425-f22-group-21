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
  
while not(userInput = 1) and not(userInput = 2) and not(userInput = 3) and not(userInput = 4):
  # Creating the interface for banking app upon starting
  print("Welcome to the Banking Application\n")
  print("1 - Customer Sign in")
  print("2 - Customer Sign up")
  print("3 - Employee Sign in")
  print("4 - Exit")
  userInput = int(input("Please choose an option to continue: "))

  if userInput = 1:
    pass
  elif userInput = 2:
    pass
  elif userInput = 3:
    pass
  elif userInput = 4:
    print("\nExiting...")
    exit()
  else:
    print("Please choose an option from above.")

# Close the cursor
cur.close()

# Close the connection
conn.close()
