CREATE SCHEMA `ecommerce2`;

CREATE TABLE `ecommerce2`.`learningjourneycourse` (
  `learning_journey_id` int,
  `course_id` int
);

CREATE TABLE `ecommerce2`.`learningjourney` (
  `id` int PRIMARY KEY,
  `staff_id` int UNIQUE NOT NULL,
  `job_role_id` int,
  `created_at` varchar(255) COMMENT 'When order created'
);

CREATE TABLE `ecommerce2`.`course` (
  `id` int PRIMARY KEY,
  `course_name` varchar(255),
  `course_description` varchar(255),
  `course_status` varchar(255),
  `course_type` varchar(255),
  `course_category` varchar(255)
  -- `created_at` datetime DEFAULT (now())
);


ALTER TABLE `ecommerce2`.`learningjourneycourse` ADD FOREIGN KEY (`learning_journey_id`) REFERENCES `ecommerce2`.`learningjourney` (`id`);

ALTER TABLE `ecommerce2`.`learningjourneycourse` ADD FOREIGN KEY (`course_id`) REFERENCES `ecommerce2`.`course` (`id`);


