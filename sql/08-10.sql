create database institute;
show databases;
create table Department(dept_id int , 
dept_name varchar (50),
dept_location varchar(50)
);
create table Staff(staff_id int , 
first_name varchar (50),
last_name varchar(50),
dob date,
dept_id int);

desc staff;
alter table Staff add location varchar(10); -- this query for add a single colmn in the table 
alter table Staff add  Joining_year int ;
alter table Staff  add (age int ,contact_no int(10));

/* changing the dataa type;*/
alter table Staff  modify first_name text;
desc Staff;
alter table Staff drop column contact_no;
alter table staff modify last_name varchar(100);
alter table staff add primary key(staff_id);
alter table Department add primary key(dept_id);
desc Staff;
desc Department;
-- syntax : Alter table tablename drop primary key; 
alter table department drop primary key;
-- adding foriegn key between two tables 
Alter table Staff add constraint FK_Staff_Department 
foreign key(dept_id) references Department(dept_id);
-- 
Alter table Staff drop  foreign key FK_Staff_Department;
 alter table Staff rename staff;
 rename table staff to staff1;

-- DML COMMANDS 
create database college;
select college;
create table Employees(EmpID int, FirstName varchar(10),
LastName varchar(10) , EmpAGE int , Empzond varchar(10));
desc Epmmloyees;
Insert into Employees 
values
(1,"Vansh","Joshi" ,20,"North");

-- Multiple rows Insertion Method 
Insert into Employees(EmpID ,FirstName , LastName ,EmpAGE , Empzond) values
(1,"shivam","Jaiswal" ,20,"North"),
(1,"Priyam","Jaiswal" ,20,"South");
--- DELETE STATEMENT
delete from Employees  where EmpId = 103 ;

-- NOT NULL CONSTRAINTS 
create database company_db;
use company_db;
create table Employee(EmpID int, FirstName varchar(10),
LastName varchar(10) , EmpAge int);

-- unique key 
create table employee1(empid int NOT NULL, FirstName varchar(30), LastName varchar (30), unique(empid));
insert into employee1 values (101, "Vansh", "Bijwani");
insert into employee1 values (102, "Shivam", "OG");
insert into employee1 values (NULL, "Shivam", "OG");

show create table employee1;
alter table employee1 add column salary int, add check (salary>1);

select *from employee1;
desc employee1;


-- alter table employee1 drop check employee1_chk;


-- check constraints


create table employee4((EmpID int, FirstName varchar(10),
LastName varchar(10) , EmpAGE int ,salary int, check(EmpAGE>20), primary key (EmpID));

alter table employee4 add constraint chk_EmpAGE_salary
check(EmpAGE>20 and salary>= 5000);





insert into employee3 values ();