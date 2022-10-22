CREATE SCHEMA `ecommerce`;

CREATE TABLE `ecommerce`.`merchants` (
  `id` int,
  `country_code` int,
  `merchant_name` varchar(255),
  `created at` varchar(255),
  `admin_id` int,
  PRIMARY KEY (`id`, `country_code`)
);

CREATE TABLE `ecommerce`.`order_items` (
  `order_id` int,
  `product_id` int,
  `quantity` int DEFAULT 1
);

CREATE TABLE `ecommerce`.`orders` (
  `id` int PRIMARY KEY,
  `user_id` int UNIQUE NOT NULL,
  `status` varchar(255),
  `created_at` varchar(255) COMMENT 'When order created'
);

CREATE TABLE `ecommerce`.`learningjourneycourse` (
  `learning_journey_id` int,
  `course_id` int
);

CREATE TABLE `ecommerce`.`learningjourney` (
  `id` int PRIMARY KEY,
  `staff_id` int UNIQUE NOT NULL,
  `job_role_id` int,
  `created_at` varchar(255) COMMENT 'When order created'
);

CREATE TABLE `ecommerce`.`course` (
  `id` int PRIMARY KEY,
  `course_name` varchar(255),
  `course_description` varchar(255),
  `course_status` varchar(255),
  `course_type` varchar(255),
  `course_category` varchar(255),
  `created_at` datetime DEFAULT (now())
);

CREATE TABLE `ecommerce`.`products` (
  `id` int PRIMARY KEY,
  `name` varchar(255),
  `merchant_id` int NOT NULL,
  `price` int,
  `status` ENUM ('out_of_stock', 'in_stock', 'running_low'),
  `created_at` datetime DEFAULT (now())
);

CREATE TABLE `ecommerce`.`product_tags` (
  `id` int PRIMARY KEY,
  `name` varchar(255)
);

CREATE TABLE `ecommerce`.`merchant_periods` (
  `id` int PRIMARY KEY,
  `merchant_id` int,
  `country_code` int,
  `start_date` datetime,
  `end_date` datetime
);

CREATE TABLE `users` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `full_name` varchar(255),
  `created_at` timestamp,
  `country_code` int
);

CREATE TABLE `countries` (
  `code` int PRIMARY KEY,
  `name` varchar(255),
  `continent_name` varchar(255)
);

CREATE INDEX `product_status` ON `ecommerce`.`products` (`merchant_id`, `status`);

CREATE UNIQUE INDEX ``ecommerce`.products_index_1` ON `ecommerce`.`products` (`id`);

ALTER TABLE `ecommerce`.`merchants` ADD FOREIGN KEY (`admin_id`) REFERENCES `users` (`id`);

ALTER TABLE `ecommerce`.`merchants` ADD FOREIGN KEY (`country_code`) REFERENCES `countries` (`code`);

ALTER TABLE `ecommerce`.`order_items` ADD FOREIGN KEY (`order_id`) REFERENCES `ecommerce`.`orders` (`id`);

ALTER TABLE `ecommerce`.`order_items` ADD FOREIGN KEY (`product_id`) REFERENCES `ecommerce`.`products` (`id`);

ALTER TABLE `ecommerce`.`learningjourneycourse` ADD FOREIGN KEY (`learning_journey_id`) REFERENCES `ecommerce`.`learningjourney` (`id`);

ALTER TABLE `ecommerce`.`learningjourneycourse` ADD FOREIGN KEY (`course_id`) REFERENCES `ecommerce`.`course` (`id`);

ALTER TABLE `ecommerce`.`products` ADD FOREIGN KEY (`merchant_id`) REFERENCES `ecommerce`.`merchants` (`id`);

CREATE TABLE `ecommerce`.`product_tags_products` (
  `product_tags_id` int,
  `products_id` int,
  PRIMARY KEY (`product_tags_id`, `products_id`)
);

ALTER TABLE `ecommerce`.`product_tags_products` ADD FOREIGN KEY (`product_tags_id`) REFERENCES `ecommerce`.`product_tags` (`id`);

ALTER TABLE `ecommerce`.`product_tags_products` ADD FOREIGN KEY (`products_id`) REFERENCES `ecommerce`.`products` (`id`);


ALTER TABLE `ecommerce`.`merchant_periods` ADD FOREIGN KEY (`merchant_id`, `country_code`) REFERENCES `ecommerce`.`merchants` (`id`, `country_code`);

ALTER TABLE `users` ADD FOREIGN KEY (`country_code`) REFERENCES `countries` (`code`);
