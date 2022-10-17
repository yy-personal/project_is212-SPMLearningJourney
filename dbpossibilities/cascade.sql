SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


-- Database: `ljms`
--
CREATE DATABASE IF NOT EXISTS `ljms3` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `ljms3`;


CREATE TABLE `learningjourneycourse` (
  `learning_journey_id` int,
  `course_id` int
);

CREATE TABLE `learningjourney` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `staff_id` int UNIQUE NOT NULL,
  `job_role_id` int,
  PRIMARY KEY (`id`)  
  -- `created_at` varchar(255) COMMENT 'When order created'
);

CREATE TABLE `course` (
  `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `course_name` varchar(255),
  `course_description` varchar(255),
  `course_status` varchar(255),
  `course_type` varchar(255),
  `course_category` varchar(255)
  -- `created_at` datetime DEFAULT (now())
);

ALTER TABLE `learningjourneycourse` ADD FOREIGN KEY (`learning_journey_id`) REFERENCES `learningjourney` (`id`)
ON DELETE CASCADE;

ALTER TABLE `learningjourneycourse` ADD FOREIGN KEY (`course_id`) REFERENCES `course` (`id`)
ON DELETE CASCADE;


INSERT INTO `learningjourney`(`staff_id`, `job_role_id`) VALUES  
(1, 2),  
(2, 3),  
(3, 4);  

INSERT INTO `course`(`course_name`, `course_description`, `course_status`, `course_type`, `course_category`) VALUES  
("Database management", "databasing ....", "active", "DM", "DM101"),  
("Database management2", "databasing2 ....", "active2", "DM2", "DM1012"),  
("Database management3", "databasing3 ....", "active3", "DM3", "DM1013");


INSERT INTO `learningjourneycourse`(`learning_journey_id`, `course_id`) VALUES  
(1, 1),  
(2, 1),  
(3, 2);  

-- -- Table strcuture for table 'courses'
-- CREATE TABLE course (
--     id INT NOT NULL AUTO_INCREMENT,  
--     name varchar(100) DEFAULT NULL,
--     description varchar(500) DEFAULT NULL,
--     status varchar(50) DEFAULT NULL,
--     type varchar(50) DEFAULT NULL,
--     category varchar(50) NULL,
--     PRIMARY KEY (ID)  
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- -- Table strcuture for table 'learningjourney'
-- CREATE TABLE learningjourney (
--     id INT NOT NULL AUTO_INCREMENT,  
--     roleid INT DEFAULT NOT NULL,
--     PRIMARY KEY (ID)  
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- -- Table strcuture for table 'learningjourneycourse'
-- CREATE TABLE learningjourneycourse (
--     learningjourneyid int(10) NOT NULL,
--     courseid int(10) DEFAULT NOT NULL,
--     Type varchar(50) NOT NULL,  
--     INDEX par_ind (learningjourneyid), 
--     INDEX par_ind2 (courseid),   
--     CONSTRAINT fk_learningjourneyid FOREIGN KEY (learningjourneyid)  
--     REFERENCES learningjourney(id),
--     CONSTRAINT fk_courseid FOREIGN KEY (courseid)  
--     REFERENCES course(id)  
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8;


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