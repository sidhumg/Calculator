create database school;

use school;

create table student(

SNo int,
Student_Name varchar(255),
Age int check (Age>=0 AND Age<=99),
Sex char(5),
Class char(2),
Fees int not null,
Class_rank int,
English_Mark int,
Python_Mark int,
Math_Mark int,
Class_teacher varchar(255));


create table teacher (
SNo int,
Name varchar(255),
Age int check (Age>=0 AND Age<=99),
Sex char(5),
Salary int,
Class_teacher_class char(255));

create table Principal (
SNo int,
Name varchar(255),
Age int check (Age>=0 AND Age<=99),
Sex char(6),
Salary int);

create table admin (
SNo int not null auto_increment primary key,
User_name varchar(10),
password varchar(10));

