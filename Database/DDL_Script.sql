-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema NewsCollection
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema NewsCollection
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `NewsCollection` DEFAULT CHARACTER SET utf8 ;
SHOW WARNINGS;
USE `NewsCollection` ;

-- -----------------------------------------------------
-- Table `NewsCollection`.`Article`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `NewsCollection`.`Article` (
  `Title` VARCHAR(100) NOT NULL,
  `Publish_Time` VARCHAR(45) NULL,
  `Genre` VARCHAR(10) NULL,
  `Content` LONGTEXT NULL,
  PRIMARY KEY (`Title`))
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `NewsCollection`.`Author`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `NewsCollection`.`Author` (
  `Name` VARCHAR(20) NOT NULL,
  `Bio` VARCHAR(100) NULL,
  `Contact` VARCHAR(20) NULL,
  PRIMARY KEY (`Name`))
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `NewsCollection`.`Comment`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `NewsCollection`.`Comment` (
  `Reader` INT UNSIGNED NOT NULL,
  `Time` DATETIME(100) NULL,
  `Content` VARCHAR(100) NULL,
  `Title` VARCHAR(100) NULL,
  INDEX `fk_comment_article_idx` (`Title` ASC) VISIBLE,
  CONSTRAINT `fk_comment_article`
    FOREIGN KEY (`Title`)
    REFERENCES `NewsCollection`.`Article` (`Title`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `NewsCollection`.`Article_has_Author`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `NewsCollection`.`Article_has_Author` (
  `Author_Name` VARCHAR(20) NOT NULL,
  `Article_Title` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`Author_Name`, `Article_Title`),
  INDEX `fk_Article_has_Author_Author1_idx` (`Author_Name` ASC) VISIBLE,
  INDEX `fk_Article_has_Author_Article_idx` (`Article_Title` ASC) VISIBLE,
  CONSTRAINT `fk_Article_has_Author_Author1`
    FOREIGN KEY (`Author_Name`)
    REFERENCES `NewsCollection`.`Author` (`Name`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Article_has_Author_Article`
    FOREIGN KEY (`Article_Title`)
    REFERENCES `NewsCollection`.`Article` (`Title`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW WARNINGS;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
