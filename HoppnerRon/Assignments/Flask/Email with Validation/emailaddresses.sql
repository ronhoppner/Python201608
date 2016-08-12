-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema emailaddresses
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema emailaddresses
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `emailaddresses` DEFAULT CHARACTER SET utf8 ;
USE `emailaddresses` ;

-- -----------------------------------------------------
-- Table `emailaddresses`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `emailaddresses`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `emailaddresses`.`email`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `emailaddresses`.`email` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `address` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
