-- ========================================================================
-- 						 WELCOME TO DATA TRANSFORM 
-- ========================================================================

create database data ;

use data;

CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    Name VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    RegistrationDate DATE
);

INSERT INTO Customers VALUES
(1, 'John', 'Doe', ' john.doe@email.com ', '2022-03-15'),
(2, 'Jane', 'Smith', 'jane.smith@email.com', '2021-11-02'),
(3, 'Alex', 'Brown', 'alex.brown@email.com', '2023-01-10');


CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE,
    TotalAmount DECIMAL(10,2),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

INSERT INTO Orders VALUES
(101, 1, '2023-07-01', 150.50),
(102, 2, '2023-07-03', 200.75),
(103, 1, '2023-08-15', 1200.00);


CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    Name VARCHAR(50),
    LastName VARCHAR(50),
    Department VARCHAR(50),
    HireDate DATE,
    Salary DECIMAL(10,2)
);

INSERT INTO Employees VALUES
(1, 'Mark', 'Johnson', 'Sales', '2020-01-15', 50000),
(2, 'Susan', 'Lee', 'HR', '2021-03-20', 55000),
(3, 'David', 'Miller', 'IT', '2019-06-10', 65000);

-- 1

SELECT * 
FROM Customers c
INNER JOIN Orders o
ON c.CustomerID = o.CustomerID;


-- 2

SELECT c.CustomerID, c.Name, c.LastName, o.OrderID, o.TotalAmount
FROM Customers c
LEFT JOIN Orders o
ON c.CustomerID = o.CustomerID;


-- 3

SELECT o.orderid, c.Name, c.LastName, c.customerId, c.RegistrationDate
FROM Customers c
RIGHT JOIN Orders o
ON c.CustomerID = o.CustomerID;



-- 4

SELECT *
FROM Customers c
join Orders o
ON c.CustomerID = o.CustomerID;



-- 5

select customerId from orders
where totalamount > (select avg(totalamount) from orders );



-- 6

SELECT *
FROM Employees
WHERE Salary >
(SELECT AVG(Salary) FROM Employees);


-- 7


SELECT OrderID,
       EXTRACT(YEAR FROM OrderDate) AS OrderYear,
       EXTRACT(MONTH FROM OrderDate) AS OrderMonth
FROM Orders;


-- 8

SELECT OrderID,
       DATEDIFF(CURDATE(), OrderDate) AS DaysDifference
FROM Orders;


-- 9

SELECT OrderID,
       DATE_FORMAT(OrderDate, '%d-%m-%Y') AS FormattedDate
FROM Orders;


-- 10

SELECT CustomerID,
       CONCAT(Name, ' ', LastName) AS FullName
FROM Customers;


-- 11

SELECT REPLACE(Name, 'John', 'Jonathan') AS UpdatedName
FROM Customers;


-- 12

SELECT 
	   UPPER(Name) AS Name_Upper,
       LOWER(LastName) AS LastName_Lower
FROM Customers;


-- 13

SELECT TRIM(Email) AS CleanEmail
FROM Customers;


-- 14

SELECT OrderID, OrderDate, TotalAmount,
       SUM(TotalAmount) OVER (ORDER BY OrderDate) AS RunningTotal
FROM Orders;


-- 15

SELECT OrderID, OrderDate, TotalAmount,
       SUM(TotalAmount) OVER (ORDER BY OrderDate) AS RunningTotal
FROM Orders;


-- 16

SELECT OrderID, TotalAmount,
       CASE
           WHEN TotalAmount > 1000 THEN '10% Discount'
           WHEN TotalAmount > 500 THEN '5% Discount'
           ELSE 'No Discount'
       END AS Discount
FROM Orders;


-- 17

SELECT EmployeeID, firstName, Salary,
       CASE
           WHEN Salary >= 60000 THEN 'High'
           WHEN Salary BETWEEN 40000 AND 59999 THEN 'Medium'
           ELSE 'Low'
       END AS SalaryCategory
FROM Employees;

-- ========================================================================
-- 								Thank you 
-- ========================================================================