-- ==================================
--          WELCOME
-- ==================================


create database smart_library;

use smart_library;


CREATE TABLE authors (
    author_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100)
);

INSERT INTO authors (author_id, name, email)VALUES
(1, 'R. D. Sharma', 'rd@books.com'),
(2, 'Stephen Hawking', NULL),
(3, 'Chetan Bhagat', 'chetan@india.com');

CREATE TABLE books (
    book_id INT PRIMARY KEY,
    title VARCHAR(150),
    author_id INT,
    category VARCHAR(50),
    isbn VARCHAR(20),
    published_date DATE,
    price DECIMAL(8,2),
    available BOOLEAN,
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);


INSERT INTO books (book_id, title, author_id, category, isbn, published_date, price, available)VALUES
(1, 'Mathematics Class 10', 1, 'Science', 'ISBN1', '2018-06-01', 450, TRUE),
(2, 'A Brief History of Time', 2, 'Science', 'ISBN2', '1995-01-01', 600, TRUE),
(3, 'Half Girlfriend', 3, 'Fiction', 'ISBN3', '2014-10-01', 300, TRUE);


CREATE TABLE members (
    member_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    phone_number VARCHAR(15),
    membership_date DATE
);

INSERT INTO members (member_id, name, email, phone_number, membership_date)VALUES
(1, 'Amit Patel', 'amit@gmail.com', '9876543210', '2021-05-10'),
(2, 'Neha Shah', NULL, '9123456780', '2023-01-15'),
(3, 'Rahul Mehta', 'rahul@gmail.com', '9988776655', '2019-08-20');


CREATE TABLE transactions (
    transaction_id INT PRIMARY KEY,
    member_id INT,
    book_id INT,
    borrow_date DATE,
    return_date DATE,
    fine_amount DECIMAL(6,2),
    FOREIGN KEY (member_id) REFERENCES members(member_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id)
);


INSERT INTO transactions (transaction_id, member_id, book_id, borrow_date, return_date, fine_amount)VALUES
(1, 1, 1, '2023-09-01', '2023-09-10', 0),
(2, 1, 2, '2023-11-01', NULL, 50),
(3, 2, 1, '2024-01-05', '2024-01-15', 0);



-- ==========================
--         quirys
-- ==========================


-- ===============================
-- 1. CRUD Operations
-- ===============================


INSERT INTO books VALUES
(4, 'Physics Fundamentals', 2, 'Science', 'ISBN4', '2021-07-01', 520, TRUE);

UPDATE books
SET available = FALSE
WHERE book_id = 2;

DELETE FROM members
WHERE member_id NOT IN (
    SELECT DISTINCT member_id
    FROM transactions
    WHERE borrow_date >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR)
);

SELECT * FROM books WHERE available = TRUE;


-- ===============================
-- 2. WHERE, HAVING, LIMIT
-- ===============================

SELECT * FROM books
WHERE YEAR(published_date) > 2015;

SELECT * FROM books
ORDER BY price DESC
LIMIT 5;

SELECT * FROM members
WHERE membership_date < '2022-01-01';


-- ===============================
-- 3. AND, OR, NOT
-- ===============================

SELECT * FROM books
WHERE category = 'Science' AND price < 500;

SELECT * FROM books
WHERE NOT available;

SELECT * FROM members
WHERE membership_date > '2020-01-01'
OR member_id IN (
    SELECT member_id
    FROM transactions
    GROUP BY member_id
    HAVING COUNT(*) > 3
);


-- ===============================
-- 4. ORDER BY & GROUP BY
-- ===============================

SELECT * FROM books ORDER BY title;

SELECT member_id, COUNT(*) AS books_borrowed
FROM transactions
GROUP BY member_id;

SELECT category, COUNT(*) AS total_books
FROM books
GROUP BY category;


-- ===============================
-- 5. Aggregate Functions
-- ===============================

SELECT AVG(price) AS average_price FROM books;

SELECT SUM(fine_amount) AS total_fine FROM transactions;

SELECT book_id
FROM transactions
GROUP BY book_id
ORDER BY COUNT(*) DESC;


-- ===============================
-- 6. Joins
-- ===============================

SELECT b.title, a.name
FROM books b
INNER JOIN authors a
ON b.author_id = a.author_id;

SELECT m.name, t.book_id
FROM members m
LEFT JOIN transactions t
ON m.member_id = t.member_id;

SELECT b.title
FROM transactions t
RIGHT JOIN books b
ON t.book_id = b.book_id
WHERE t.book_id IS NULL;

SELECT m.name
FROM members m
LEFT JOIN transactions t
ON m.member_id = t.member_id
WHERE t.member_id IS NULL;


-- ===============================
-- 7. Subqueries
-- ===============================

SELECT * FROM books
WHERE book_id IN (
    SELECT book_id
    FROM transactions
    WHERE member_id IN (
        SELECT member_id
        FROM members
        WHERE membership_date > '2022-01-01'
    )
);

SELECT * FROM members
WHERE member_id NOT IN (
    SELECT member_id FROM transactions
);


-- ===============================
-- 8. Date Functions
-- ===============================

SELECT YEAR(published_date) AS year, COUNT(*)
FROM books
GROUP BY year;

SELECT transaction_id,
DATEDIFF(return_date, borrow_date) AS days_difference
FROM transactions;

SELECT DATE_FORMAT(borrow_date, '%d-%m-%Y')
FROM transactions;


-- ===============================
-- 9. String Functions
-- ===============================

SELECT UPPER(title) FROM books;

SELECT TRIM(name) FROM authors;

SELECT IFNULL(email, 'Not Provided') FROM members;


-- ===============================
-- 10. Window Functions
-- ===============================

SELECT book_id,
COUNT(*) AS borrow_count,
RANK() OVER (ORDER BY COUNT(*) DESC) AS rank_no
FROM transactions
GROUP BY book_id;

SELECT member_id,
COUNT(*) OVER (PARTITION BY member_id) AS total_borrowed
FROM transactions;


-- ===============================
-- 11. CASE Expressions
-- ===============================

SELECT member_id,
CASE
    WHEN MAX(borrow_date) >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
    THEN 'Active'
    ELSE 'Inactive'
END AS membership_status
FROM transactions
GROUP BY member_id;

SELECT title,
CASE
    WHEN YEAR(published_date) > 2020 THEN 'New Arrival'
    WHEN YEAR(published_date) < 2000 THEN 'Classic'
    ELSE 'Regular'
END AS book_type
FROM books;


-- ==========================================
--                THANK YOU
-- ==========================================