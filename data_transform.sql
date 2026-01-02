create database data;

use data;

create table customers(
customerId int primary key,
name varchar (50),
LastName varchar (50),
email varchar (50),
RegistrationDate date
);

INSERT INTO customers (customerId, name, LastName, email, RegistrationDate)
VALUES
(1, 'John', 'Deo', 'john.deo@email.com', '2022-03-15'),
(2, 'Jane', 'Smith', 'jane.smith@email.com', '2021-11-02');

