-- Adminer 5.3.0 MySQL 9.3.0 dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

DROP TABLE IF EXISTS `questions`;
CREATE TABLE `questions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `question` text NOT NULL,
  `reponse` text NOT NULL,
  `satisfaction` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- 2025-08-20 09:24:25 UTC
