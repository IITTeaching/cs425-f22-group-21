DROP TABLE IF EXISTS Employee cascade;
DROP TABLE IF EXISTS Branch cascade;
DROP TABLE IF EXISTS Customer cascade;
DROP TABLE IF EXISTS Transactions cascade;
DROP TABLE IF EXISTS Account cascade;
DROP TABLE IF EXISTS Loan cascade;
 
CREATE TABLE Employee (
  emp_ID serial UNIQUE,
  ssn numeric(9) UNIQUE,
  first_name varchar NOT NULL,
  last_name varchar NOT NULL,
  salary numeric NOT NULL,
  street varchar NOT NULL,
  house_num int NOT NULL,
  city varchar NOT NULL,
  state varchar NOT NULL, 
  zip char(5) NOT NULL,
  emp_role varchar NOT NULL,
  works_at int REFERENCES Branch(branch_id),
  PRIMARY KEY (emp_ID, ssn),
  CONSTRAINT emp_role_check CHECK (emp_role IN ('Manager', 'Teller', 'Loan Specialist'))
 );

CREATE TABLE Branch (
    branch_id serial PRIMARY KEY,
    street varchar NOT NULL,
    house_num int NOT NULL,
    city varchar NOT NULL,
    state varchar NOT NULL,
    zip char(5),
    emp_ID int REFERENCES Employee ON DELETE CASCADE
);

CREATE TABLE Customer (
    customer_id serial,
    home_branch int REFERENCES Branch(branch_id),
    firstName varchar NOT NULL,
    lastName varchar NOT NULL,
    street varchar NOT NULL,
    house_num int NOT NULL,
    city varchar NOT NULL,
    state varchar NOT NULL,
    zip char(5) NOT NULL,
    account_num int,
    PRIMARY KEY (customer_id),
    FOREIGN KEY (account_num) REFERENCES Account
);

CREATE TABLE Account (
    account_id int REFERENCES Customer(customer_id) ON DELETE CASCADE,
    account_num int PRIMARY KEY,
    account_type varchar NOT NULL,
    balance int NOT NULL,
    CONSTRAINT account_type_check CHECK (account_type IN ('Checking', 'Savings'))
);

CREATE TABLE accountType ( --specify details of different account types
    account_type varchar NOT NULL,
    interest_rate int NOT NULL,
    allow_neg boolean NOT NULL DEFAULT FALSE,
    overdraft_fee int NOT NULL,
    monthly_fee int NOT NULL,
    account_num int REFERENCES Account, -- would we need to add this to specify whose account we are talking about.
    PRIMARY KEY (account_type)
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


