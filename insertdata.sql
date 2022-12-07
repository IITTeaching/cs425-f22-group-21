-- This is just starter values for employees and branches

INSERT INTO Address VALUES
(1, '4959 W. North Ave.', 'Chicago', 'IL', '60639'),
(2, '4900 W. George St.', 'Chicago', 'IL', '60641'),
(3, '1300 N. Laramie Ave.', 'Chicago', 'IL', '60613'),
(4, '6969 W. Irving Park Rd.', 'Chicago', 'IL', '60615'),
(5, '4300 N. 31st St.', 'Chicago', 'IL', '60614'),
(6, '342 N. 38th St.', 'Chicago', 'IL', '60614'),
(7, '7800 W. Mountain Ave.', 'Chicago', 'IL', '60685'),
(8, '2389 N. Livington St.', 'Chicago', 'IL', '60675'),
(9, '246 W. 31st St.', 'Chicago', 'IL', '60616');

INSERT INTO Branch VALUES
(1, 1),
(2, 4);

INSERT INTO Employee VALUES
('ABC1234', 123456789, 'example123', 'Harsha', 'Pillai', 130000, 'Manager', 2, 1),
('A506790', 908908003, 'password', 'Erik', 'Pacheco', 45000, 'Bank Teller', 3, 1),
('L908769', 303789023, 'examplepass', 'Jungwoo', 'Hwang', 180000, 'Manager', 5, 4);

INSERT INTO Customer VALUES
(0, 'customer1', 'cpw1', 1, 'Taylor', 'Adam', 7),
(1, 'customer2', 'cpw2', 2, 'Annie', 'George', 8),
(2, 'customer3', 'cpw3', 2, 'Annie', 'George', 9);

INSERT INTO Account VALUES
(0, 001, 100),
(1, 002, 100000),
(2, 003, 5000);

INSERT INTO AccountType VALUES 
('Checkings', 0, FALSE, 0, 0, 0),
('Savings', 0, FALSE, 0, 0, 1),
('Checkings', 0, FALSE, 0, 0, 2);
