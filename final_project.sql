-- =================================================
--                    WELCOME
-- =================================================

create database final;

use final;

CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    BirthDate DATE,
    EnrollmentDate DATE
);

CREATE TABLE Courses (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(100),
    DepartmentID INT,
    Credits INT
);

CREATE TABLE Instructors (
    InstructorID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    DepartmentID INT,
    Salary DECIMAL(10,2)
);

CREATE TABLE Enrollments (
    EnrollmentID INT PRIMARY KEY,
    StudentID INT,
    CourseID INT,
    EnrollmentDate DATE,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);

CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(100)
);



-- INSERTING THE DATA :

-- 1

INSERT INTO Students VALUES
(1, 'John', 'Doe', 'john.doe@email.com', '2000-01-15', '2022-08-01'),
(2, 'Jane', 'Smith', 'jane.smith@email.com', '1999-05-25', '2021-08-01');


-- 2

INSERT INTO Courses VALUES
(101, 'Introduction to SQL', 1, 3),
(102, 'Data Structures', 2, 4);


-- 3

INSERT INTO Instructors VALUES
(1, 'Alice', 'Johnson', 'alice.johnson@univ.com', 1, 80000),
(2, 'Bob', 'Lee', 'bob.lee@univ.com', 2, 75000);


-- 4

INSERT INTO Enrollments VALUES
(1, 1, 101, '2022-08-01'),
(2, 2, 102, '2021-08-01');


-- 5

INSERT INTO Departments VALUES
(1, 'Computer Science'),
(2, 'Mathematics');


-- -------------------------------------------
--             QUERIES :
-- -------------------------------------------

-- 1

-- CRUD :-

INSERT INTO Students VALUES (3, 'Mark', 'Taylor', 'mark@email.com', '2001-04-10', '2023-08-01');

SELECT * FROM Students;

UPDATE Students SET Email = 'john.updated@email.com' WHERE StudentID = 1;

DELETE FROM Students WHERE StudentID = 3;


-- 2

SELECT * FROM Students
WHERE EnrollmentDate > '2022-12-31';


-- 3

SELECT * FROM Courses
WHERE DepartmentID = (
    SELECT DepartmentID FROM Departments
    WHERE DepartmentName = 'Mathematics'
)
LIMIT 5;


-- 4

SELECT CourseID, COUNT(StudentID) AS TotalStudents
FROM Enrollments
GROUP BY CourseID
HAVING COUNT(StudentID) ;


-- 5

SELECT StudentID
FROM Enrollments
WHERE CourseID IN (101, 102)
GROUP BY StudentID
HAVING COUNT(DISTINCT CourseID) ;


-- 6

SELECT DISTINCT StudentID
FROM Enrollments
WHERE CourseID IN (101, 102);


-- 7

SELECT AVG(Credits) AS AverageCredits
FROM Courses;


-- 8

SELECT MAX(Salary) AS MaxSalary
FROM Instructors
WHERE DepartmentID = (
    SELECT DepartmentID FROM Departments
    WHERE DepartmentName = 'Computer Science'
);


-- 9

SELECT d.DepartmentName, COUNT(e.StudentID) AS StudentCount
FROM Departments d
JOIN Courses c ON d.DepartmentID = c.DepartmentID
JOIN Enrollments e ON c.CourseID = e.CourseID
GROUP BY d.DepartmentName;


-- 10

SELECT s.FirstName, s.LastName, c.CourseName
FROM Students s
INNER JOIN Enrollments e ON s.StudentID = e.StudentID
INNER JOIN Courses c ON e.CourseID = c.CourseID;


-- 11

SELECT s.FirstName, s.LastName, c.CourseName
FROM Students s
LEFT JOIN Enrollments e ON s.StudentID = e.StudentID
LEFT JOIN Courses c ON e.CourseID = c.CourseID;


-- 12

SELECT DISTINCT StudentID
FROM Enrollments
WHERE CourseID IN (
    SELECT CourseID
    FROM Enrollments
    GROUP BY CourseID
    HAVING COUNT(StudentID)
);


-- 13

SELECT StudentID, YEAR(EnrollmentDate) AS EnrollmentYear
FROM Students;


-- 14

SELECT CONCAT(FirstName, ' ', LastName) AS InstructorName
FROM Instructors;


-- 15

SELECT CourseID,
COUNT(StudentID) OVER (ORDER BY CourseID) AS RunningTotal
FROM Enrollments;


-- 16

SELECT StudentID,
CASE
    WHEN EnrollmentDate <= DATE_SUB(CURDATE(), INTERVAL 4 YEAR)
    THEN 'Senior'
    ELSE 'Junior'
END AS Status
FROM Students;

-- ==========================================================
--                       THANK YOU 
-- ==========================================================