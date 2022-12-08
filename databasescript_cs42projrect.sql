DROP TABLE IF EXISTS Transactions CASCADE;
DROP TABLE IF EXISTS AccountType CASCADE;
DROP TABLE IF EXISTS Account CASCADE;
DROP TABLE IF EXISTS Customer CASCADE;
DROP TABLE IF EXISTS Employee CASCADE;
DROP TABLE IF EXISTS Branch CASCADE;
DROP TABLE IF EXISTS Address CASCADE;
DROP TABLE IF EXISTS Loan CASCADE;


CREATE TABLE Address (
  address_id int PRIMARY KEY,
  street_name text NOT NULL,
  city text NOT NULL,
  state text NOT NULL,
  zip char(5) NOT NULL
);

CREATE TABLE Branch (
  branch_id serial PRIMARY KEY,
  branch_at int REFERENCES Address(address_id)
);
 
CREATE TABLE Employee (
  emp_ID varchar(15) PRIMARY KEY,
  ssn numeric(9) UNIQUE,
  password varchar(15) UNIQUE NOT NULL,
  first_name text NOT NULL,
  last_name text NOT NULL,
  salary numeric NOT NULL,
  emp_role text NOT NULL,
  lives_at int REFERENCES Address(address_id),
  works_at int,
  CONSTRAINT emp_role_check CHECK (emp_role IN ('Manager', 'Bank Teller', 'Loan Specialist'))
 );

CREATE TABLE Customer (
  customer_id serial PRIMARY KEY,
  customer_username varchar(10) NOT NULL,
  customer_password varchar(12) UNIQUE NOT NULL,
  home_branch int REFERENCES Branch(branch_id),
  first_name text NOT NULL,
  last_name text NOT NULL,
  lives_at int REFERENCES Address(address_id)
);

CREATE TABLE Account (
   account_id int REFERENCES Customer(customer_id) ON DELETE CASCADE,
   account_num int PRIMARY KEY,
   balance int NOT NULL
);

CREATE TABLE AccountType (
   account_type text NOT NULL,
   interest_rate int DEFAULT 0,
   allow_neg boolean DEFAULT FALSE,
   overdraft_fee int DEFAULT 0,
   monthly_fee int DEFAULT 0,
   account_id int REFERENCES Customer(customer_id) ON DELETE CASCADE PRIMARY KEY,
   CONSTRAINT account_type_check CHECK (account_type IN ('Checkings', 'Savings'))
);

CREATE TABLE Transactions (
   description text,
   amount int NOT NULL,
   trans_type text NOT NULL,
   account_id int REFERENCES Customer (customer_id),
   transaction_date timestamp NOT NULL, -- ADDED
   pending boolean DEFAULT TRUE,
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
