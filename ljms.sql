SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


-- Database: `ljms`
--
CREATE DATABASE IF NOT EXISTS `ljms` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `ljms`;

-- --------------------------------------------------------

-- Table strcuture for table 'Role'
CREATE TABLE `Role` (
    `role_id` int PRIMARY KEY AUTO_INCREMENT,
    `role_name` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- Table strcuture for table 'Staff'
CREATE TABLE `Staff` (
    `staff_id` int PRIMARY KEY,
    `staff_Fname` varchar(50) NOT NULL,
    `staff_Lname` varchar(50) NOT NULL,
    `department` varchar(50) NOT NULL,
    `email` varchar(50) NOT NULL,
    `role` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- Table strcuture for table 'JobRole'
CREATE TABLE `JobRole` (
    `job_role_id` int PRIMARY KEY AUTO_INCREMENT,
    `job_role_name` varchar(100) NOT NULL,
    `job_role_description` varchar(500) NOT NULL,
    `job_role_deleted` boolean DEFAULT false
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- Table strcuture for table 'Skill'
CREATE TABLE `Skill` (
    `skill_id` int PRIMARY KEY AUTO_INCREMENT,
    `skill_name` varchar(100) NOT NULL,
    `skill_description` varchar(500) NOT NULL,
    `skill_deleted` boolean DEFAULT false
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- Table strcuture for table 'Course'
CREATE TABLE `Course` (
    `course_id` varchar(20) PRIMARY KEY,
    `course_name` varchar(50) NOT NULL,
    `course_description` varchar(255) DEFAULT NULL,
    `course_status` varchar(15) DEFAULT NULL,
    `course_type` varchar(10) DEFAULT NULL,
    `course_category` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- Table strcuture for table 'Registeration'
CREATE TABLE `Registeration` (
    `reg_id` int PRIMARY KEY,
    `course_id` varchar(20) NOT NULL,
    `staff_id` int NOT NULL,
    `reg_status` varchar(20) DEFAULT NULL,
    `completion_status` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- Table strcuture for table 'LearningJourney'
CREATE TABLE `LearningJourney` (
    `learning_journey_id` int PRIMARY KEY AUTO_INCREMENT,
    `staff_id` int NOT NULL,
    `job_role_id` int NOT NULL 
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- Table strcuture for table 'LearningJourneySkill'
CREATE TABLE `LearningJourneySkill` (
    `learning_journey_id` int NOT NULL,
    `skill_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Table strcuture for table 'JobRoleSkill'
CREATE TABLE `JobRoleSkill` (
    `job_role_id` int NOT NULL,
    `skill_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- Table strcuture for table 'LearningJourneyCourse'
CREATE TABLE `LearningJourneyCourse` (
    `learning_journey_id` int NOT NULL,
    `course_id` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



-- insert data for table `Skill`

INSERT INTO `Skill` (`skill_id`, `skill_name`, `skill_description`) VALUES
(3, 'JavaScript', 'JavaScript is a lightweight interpreted programming language.' ),
(4, 'Market Research', 'Market Research is the process of determining the viability of a new service or product through research conducted directly with potential customers.' ),
(5, 'Machine Learning', 'Machine learning (ML) is a type of artificial intelligence (AI) that allows software applications to become more accurate at predicting outcomes without being explicitly programmed to do so.'),
(7, 'Software Testing', 'Software testing is the process of assessing the functionality of a software program.');

-- insert data for table `JobRole`

INSERT INTO `JobRole` (`job_role_id`, `job_role_name`, `job_role_description`) VALUES
(1, 'Data Analyst', "A data analyst reviews data to identify key insights into a business's customers and ways the data can be used to solve problems."),
(2, 'Software Engineer', 'A software engineer analyzes and modifies existing software as well as designing, constructing and testing end-user applications that meet user needs'),
(3, 'Product Manager', 'A Product Manager is a professional who combines both product planning and marketing to manage the entire life cycle of one project.');


-- insert data for table `Courses`

INSERT INTO `Course` (`course_id`, `course_name`, `course_description`, `course_status`, `course_type`, `course_category`) VALUES
('COR001', 'Systems Thinking and Design', 'This foundation module aims to introduce students to the fundamental concepts and underlying principles of systems thinking.', 'Active', 'Internal', 'Core' ),
('COR002', 'Lean Six Sigma Green Belt Certification', 'Apply Lean Six Sigma methodology and statistical tools such as Minitab to be used in process analytics', 'Active', 'Internal', 'Core'),
('COR004', 'Service Excellence', 'The programme provides the learner with the key foundations of what builds customer confidence in the service industry', 'Pending', 'Internal', 'Core'),
('FIN003', 'Business Continuity Planning', 'Business continuity planning is essential in any business to minimise loss when faced with potential threats and disruptions.', 'Retired', 'External', 'Finance'),
('tch004', 'Introduction to Open Platform Communications', 'This course provides the participants with a good in-depth understanding of the SS IEC 62541 standard', 'Pending', 'Internal', 'Technical');

-- insert data for table `Registeration`

INSERT INTO `Registeration` (`reg_id`, `course_id`, `staff_id`, `reg_status`, `completion_status`) VALUES
(249, 'FIN003', 140004, 'Registered', 'OnGoing'),
(8, 'COR002', 140036, 'Waitlist', NULL),
(5, 'COR002', 140003, 'Rejected', NULL),
(245, 'COR001', 130001, 'Registered', 'Completed');

-- insert data for table `Role`

INSERT INTO `Role` (`role_id`, `role_name`) VALUES
(1, 'Admin'),
(2, 'User'),
(3, 'Manager'),
(4, 'Trainer');

-- insert data for table `Staff`

INSERT INTO `Staff` (`staff_id`, `staff_Fname`, `staff_Lname`, `department`, `email`, `role`) VALUES
(140004, 'Mary', 'Teo', 'Sales', 'Mary.Teo@allinone.com.sg', 2),
(140036, 'Charlotte', 'Wong', 'Sales', 'Charlotte.Wong@allinone.com.sg', 2),
(140003, 'Janice', 'Chan', 'Sales', 'Janice.Chan@allinone.com.sg', 2),
(130001, 'John', 'Sim', 'Chariman', 'jack.sim@allinone.com.sg', 1),
(140001, 'Derek', 'Tan', 'Sales', 'Derek.Tan@allinone.com.sg', 3),
(150075, 'Liam', 'Tan', 'Ops', 'Liam.Tan@allinone.com.sg', 4);

-- insert data for table `LearningJourney`

INSERT INTO `LearningJourney` (`learning_journey_id`, `staff_id`, `job_role_id`) VALUES
(1, 140004, 1),
(2, 140001, 2),
(3, 140036, 3);


-- Add foreign key to table 'Staff'
ALTER TABLE `Staff`
ADD FOREIGN KEY (`role`) REFERENCES `Role`(`role_id`);

-- Add foreign key to table 'LearningJourney'
ALTER TABLE `LearningJourney`
ADD FOREIGN KEY (`staff_id`) REFERENCES `Staff`(`staff_id`);
ALTER TABLE `LearningJourney`
ADD FOREIGN KEY (`job_role_id`) REFERENCES `JobRole`(`job_role_id`);

-- Add foreign key to table 'LearningJourneySkill'
ALTER TABLE `LearningJourneySkill`
ADD FOREIGN KEY (`learning_journey_id`) REFERENCES `LearningJourney`(`learning_journey_id`);
ALTER TABLE `LearningJourneySkill`
ADD FOREIGN KEY (`skill_id`) REFERENCES `Skill`(`skill_id`);

-- Add foreign key to table 'JobRoleSkill'
ALTER TABLE `JobRoleSkill`
ADD FOREIGN KEY (`job_role_id`) REFERENCES `JobRole`(`job_role_id`);
ALTER TABLE `JobRoleSkill`
ADD FOREIGN KEY (`skill_id`) REFERENCES `Skill`(`skill_id`);

-- Add foreign key to table 'LearningJourneyCourse'
ALTER TABLE `LearningJourneyCourse`
ADD FOREIGN KEY (`learning_journey_id`) REFERENCES `LearningJourney`(`learning_journey_id`);
ALTER TABLE `LearningJourneyCourse`
ADD FOREIGN KEY (`course_id`) REFERENCES `Course`(`course_id`);

-- Add foreign key to table 'Registeration'
ALTER TABLE `Registeration`
ADD FOREIGN KEY (`course_id`) REFERENCES `Course`(`course_id`);
ALTER TABLE `Registeration`
ADD FOREIGN KEY (`staff_id`) REFERENCES `Staff`(`staff_id`);




-- ASSUME: LearningJourney, Skill, JobRole is added by name, the ID will be randomly assigned with incremental

