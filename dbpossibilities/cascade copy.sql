SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


-- Database: `ljms`
--
CREATE DATABASE IF NOT EXISTS `ljms3` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `ljms3`;

CREATE TABLE customer (  
  ID INT NOT NULL AUTO_INCREMENT,  
  Name varchar(50) NOT NULL,  
  City varchar(50) NOT NULL,  
  PRIMARY KEY (ID)  
);  

CREATE TABLE contact (  
  ID INT,  
  Customer_Id INT,  
  Customer_Info varchar(50) NOT NULL,  
  Type varchar(50) NOT NULL,  
  INDEX par_ind (Customer_Id),  
  CONSTRAINT fk_customer FOREIGN KEY (Customer_Id)  
  REFERENCES customer(ID)  
  ON DELETE CASCADE  
  ON UPDATE CASCADE  
);  

INSERT INTO customer(Name, City) VALUES  
('Joseph', 'California'),  
('Mary', 'NewYork'),  
('John', 'Alaska');  


INSERT INTO contact (Customer_Id, Customer_Info, Type) VALUES  
(1, 'Joseph@javatpoint.com', 'email'),  
(1, '121-121-121', 'work' ),  
(1, '123-123-123', 'home'),  
(2, 'Mary@javatpoint.com', 'email'),  
(2, 'Mary@javatpoint.com', 'email'),  
(2, '212-212-212', 'work'),  
(3, 'John@javatpoint.com', 'email'),  
(3, '313-313-313', 'home');  