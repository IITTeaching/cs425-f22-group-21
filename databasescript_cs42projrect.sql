/*
 Need to add cascade delete calls, check relationships (check employee type eg)
 */
CREATE TABLE employee (
  ssn NUMERIC(9),
  firstName varchar,
  lastName varchar,
  salary numeric,
  --branch varchar, --is this stored in an address form
  street varchar,
  house_num int,
  city varchar,
  state varchar,
  zip char(5),
  empRole varchar,
  primary key(ssn),
  foreign key (street, house_num, city, state, zip) references Branch
  );

CREATE TABLE Branch (
    street varchar,
    house_num int,
    city varchar,
    state varchar,
    zip char(5), --int has no size restriction so i made this a char type
    primary key (street, house_num, city, state, zip)
);

CREATE TABLE Customer (
    firstName varchar,
    lastName varchar,
    street varchar,
    house_num int,
    city varchar,
    state varchar,
    zip char(5),
    branch_street varchar, --home branch
    branch_house_num int,
    branch_city varchar,
    branch_state varchar,
    branch_zip char(5),
    id int,
    accountNum int, --accountNum to find account owners
    primary key (id),
    foreign key (branch_street, branch_house_num,branch_city, branch_state, branch_zip) references branch,
    foreign key (accountNum) references account
);

CREATE TABLE account(
    accountNum int,
    accountType varchar,
    balance int,
    primary key (accountNum)
);

CREATE TABLE transactions(
    description varchar,
    amount int,
    trans_type varchar,
    accountNum int,
    foreign key (accountNum) references account
);

CREATE TABLE loan(
    loan_amount int,
    startDate date,
    endDate date,
    interestSchedule int, --is this the percentage?
    accountNum int,
    primary key (loan_amount, startDate, endDate, interestSchedule),
    foreign key (accountNum) references account
)