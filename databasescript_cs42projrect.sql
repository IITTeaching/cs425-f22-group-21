DROP TABLE IF EXISTS Employee cascade;
DROP TABLE IF EXISTS Branch cascade;
DROP TABLE IF EXISTS Customer cascade;
DROP TABLE IF EXISTS Transactions cascade;
DROP TABLE IF EXISTS Account cascade;
DROP TABLE IF EXISTS Loan cascade;

CREATE TABLE Address (
  address_id serial PRIMARY KEY,
  add text NOT NULL,
  city text NOT NULL,
  state text NOT NULL,
  zip char(5) NOT NULL
);
 
CREATE TABLE Employee (
  emp_ID varchar(15) UNIQUE,
  ssn numeric(9) UNIQUE,
  password varchar(15) UNIQUE NOT NULL,
  first_name varchar NOT NULL,
  last_name varchar NOT NULL,
  salary numeric NOT NULL,
  emp_role varchar NOT NULL,
  lives_at int REFERENCES Address(address_id),
  works_at int REFERENCES Branch(branch_id),
  PRIMARY KEY (emp_ID, ssn),
  CONSTRAINT emp_role_check CHECK (emp_role IN ('Manager', 'Bank Teller', 'Loan Specialist'))
 );

CREATE TABLE Branch (
  branch_id serial PRIMARY KEY,
  branch_at int REFERENCES Address(address_id)
);

CREATE TABLE Customer (
  customer_id serial PRIMARY KEY,
  home_branch int REFERENCES Branch(branch_id),
  firstName varchar NOT NULL,
  lastName varchar NOT NULL,
  username varchar(10) UNIQUE NOT NULL,
  password varchar(12) UNIQUE NOT NULL,
  lives_at int REFERENCES Address(address_id),
);

CREATE TABLE Account (
   account_id int REFERENCES Customer(customer_id) ON DELETE CASCADE,
   account_num int PRIMARY KEY,
   username varchar(15) UNIQUE NOT NULL,
   password varchar(15) NOT NULL,
   balance int NOT NULL
);

CREATE TABLE AccountType (
   account_type varchar PRIMARY KEY,
   interest_rate int DEFAULT NULL,
   allow_neg boolean DEFAULT FALSE,
   overdraft_fee int DEFAULT NULL,
   monthly_fee int DEFAULT NULL,
   account_num int REFERENCES Account ON DELETE CASCADE,
   CONSTRAINT account_type_check CHECK (account_type IN ('Checkings', 'Savings'))
);


CREATE TABLE Transactions (
   description text,
   amount int NOT NULL,
   trans_type varchar NOT NULL,
   account_num int REFERENCES Account,
   CONSTRAINT transaction_type_check CHECK (trans_type IN ('Deposit', 'Withdrawal', 'Transfer', 'External Transfer'))
);

CREATE TABLE Loan (
   loan_amount int,
   start_date date,
   end_date date,
   interest_schedule int,
   account_num int,
   PRIMARY KEY (loan_amount, start_date, end_date, interest_schedule),
   FOREIGN KEY (account_num) REFERENCES Account
);
