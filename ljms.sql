SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


-- Database: `ljms`
--
CREATE DATABASE IF NOT EXISTS `ljms` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `ljms`;

-- --------------------------------------------------------

-- Table strcuture for table 'role'
--
CREATE TABLE `role` (
    `id` int(10) NOT NULL,
    `name` varchar(100) DEFAULT NULL,
    `description` varchar(100) DEFAULT NULL,
    `skill_id` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Table strcuture for table 'skill'
CREATE TABLE `skill` (
    `id` int(10) NOT NULL,
    `name` varchar(100) DEFAULT NULL,
    `description` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- insert data for table `skill`

INSERT INTO `skill` (`id`, `name`, `description`) VALUES
(1, 'Python', 'Python is a computer programming language often used to build websites and software, automate tasks, and conduct data analysis.'),
(2, 'Strategic Thinking', 'Strategic thinking is an organizational and pragmatic type of critical thinking.'),
(3, 'JavaScript', 'JavaScript is a lightweight interpreted programming language.'),
(4, 'Market Research', 'Market Research is the process of determining the viability of a new service or product through research conducted directly with potential customers.'),
(5, 'Machine Learning', 'Machine learning (ML) is a type of artificial intelligence (AI) that allows software applications to become more accurate at predicting outcomes without being explicitly programmed to do so.'),
(6, 'Object-Oriented Design', 'Object-oriented design (OOD) is the process of planning a system of interacting objects for the purpose of solving a software problem.'),
(7, 'Software Testing', 'Software testing is the process of assessing the functionality of a software program.');

-- insert data for table `role`

INSERT INTO `role` (`id`, `name`, `description` , `skill_id`) VALUES
(1, 'Data Analyst', "A data analyst reviews data to identify key insights into a business's customers and ways the data can be used to solve problems." , 1),
(2, 'Software Engineer', 'A software engineer analyzes and modifies existing software as well as designing, constructing and testing end-user applications that meet user needs', 2),
(3, 'Product Manager', 'A Product Manager is a professional who combines both product planning and marketing to manage the entire life cycle of one project.' , 4);

-- Indexes for table `role`

ALTER TABLE `role`
    ADD PRIMARY KEY (`id`),
    ADD KEY `skill_id` (`skill_id`);

-- Indexes for table `skill`

ALTER TABLE `skill`
    ADD PRIMARY KEY (`id`);


-- ASSUME: skill,role is added by name, the ID will be randomly assigned with incremental

-- AUTO_INCREMENT for table `role`

ALTER TABLE `role`
    MODIFY `id` int(10) NOT NULL AUTO_INCREMENT;


--
-- AUTO_INCREMENT for table `consultation`

ALTER TABLE `skill`
    MODIFY `id` int(10) NOT NULL AUTO_INCREMENT;

-- Constraints for table `role`

ALTER TABLE `role`
    ADD CONSTRAINT `role_ibfk_1` FOREIGN KEY (`skill_id`) REFERENCES `skill` (`id`);