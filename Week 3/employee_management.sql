-- InternNova SQL Assignment: Tasks 1 to 5
-- Database: employee_management

-- Step 1: CREATE DATABASE 
-- Step 2: CREATE employee_management Table.

CREATE DATABASE employee_management;

-- TASK 1: Create tables and insert sample records

CREATE TABLE Employees (
    Employee_ID INT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    Department VARCHAR(30),
    Age INT,
    Salary NUMERIC(10,2)
);

INSERT INTO Employees (Employee_ID, Name, Department, Age, Salary)
VALUES
    (101, 'Rahul', 'IT', 22, 25000),
    (102, 'Aman', 'HR', 24, 28000),
    (103, 'Priya', 'Sales', 23, 30000),
    (104, 'Rohit', 'IT', 25, 27000),
    (105, 'Neha', 'Finance', 26, 32000),
    (106, 'Ankit', 'HR', 23, 26000),
    (107, 'Pooja', 'Sales', 24, 35000),
    (108, 'Karan', 'IT', 27, 40000),
    (109, 'Sneha', 'Finance', 22, 29000),
    (110, 'Vikas', 'Sales', 26, 31000);

SELECT * FROM Employees;

SELECT Name, Department, Salary
FROM Employees;

SELECT
    Employee_ID AS ID,
    Name AS Employee_Name,
    Salary AS Monthly_Salary
FROM Employees;


-- TASK 2: WHERE, ORDER BY AND AGGREGATE FUNCTIONS

SELECT *
FROM Employees
WHERE Salary > 30000;

SELECT *
FROM Employees
WHERE Age >= 24;

SELECT *
FROM Employees
WHERE Department = 'IT';

SELECT *
FROM Employees
ORDER BY Salary DESC;

SELECT COUNT(*) AS Total_Employees
FROM Employees;

SELECT SUM(Salary) AS Total_Salary
FROM Employees;

SELECT AVG(Salary) AS Average_Salary
FROM Employees;

SELECT MIN(Salary) AS Lowest_Salary
FROM Employees;

SELECT MAX(Salary) AS Highest_Salary
FROM Employees;


-- TASK 3: GROUP BY AND HAVING

SELECT
    Department,
    COUNT(*) AS Employee_Count,
    AVG(Salary) AS Average_Salary
FROM Employees
GROUP BY Department;

SELECT
    Department,
    COUNT(*) AS Employee_Count,
    AVG(Salary) AS Average_Salary
FROM Employees
GROUP BY Department
HAVING AVG(Salary) > 28000;


-- TASK 4: SQL JOINS

CREATE TABLE Departments (
    Department_ID INT PRIMARY KEY,
    Department_Name VARCHAR(30) UNIQUE NOT NULL,
    Manager VARCHAR(50)
);

INSERT INTO Departments (Department_ID, Department_Name, Manager)
VALUES
    (1, 'IT', 'Mr. Sharma'),
    (2, 'HR', 'Ms. Verma'),
    (3, 'Sales', 'Mr. Kumar'),
    (4, 'Finance', 'Ms. Singh'),
    (5, 'Marketing', 'Mr. Patel');

-- INNER JOIN: only matching department records
SELECT
    e.Employee_ID,
    e.Name,
    e.Department,
    d.Manager
FROM Employees e
INNER JOIN Departments d
    ON e.Department = d.Department_Name;

-- LEFT JOIN: all employees, with matching department details
SELECT
    e.Employee_ID,
    e.Name,
    e.Department,
    d.Manager
FROM Employees e
LEFT JOIN Departments d
    ON e.Department = d.Department_Name;

-- RIGHT JOIN: all departments, including departments without employees
SELECT
    e.Employee_ID,
    e.Name,
    d.Department_Name,
    d.Manager
FROM Employees e
RIGHT JOIN Departments d
    ON e.Department = d.Department_Name;


-- TASK 5: SQL SUBQUERIES

-- Find employees earning more than the average salary
SELECT
    Employee_ID,
    Name,
    Department,
    Salary
FROM Employees
WHERE Salary > (
    SELECT AVG(Salary)
    FROM Employees
);

-- Find employees earning the highest salary in the company
SELECT
    Employee_ID,
    Name,
    Department,
    Salary
FROM Employees
WHERE Salary = (
    SELECT MAX(Salary)
    FROM Employees
);

-- Find employees working in departments whose average salary is above 28000
SELECT
    Employee_ID,
    Name,
    Department,
    Salary
FROM Employees
WHERE Department IN (
    SELECT Department
    FROM Employees
    GROUP BY Department
    HAVING AVG(Salary) > 28000
);
