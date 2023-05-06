insert into author (Name, Bio, Contact)
values
(
    "Nguyen",
    "nigga boizz ",
    "fuckyou@gmail.mommy"
)
    
insert into article (Title,Publish_Time, Genre, Content, Author_Name)
values
(
	"Con cu",
    "12 23 45 ",
    "Politics",
    "Hello tung con cu ",
    "Nguyen"
)
insert into article (Title,Publish_Time, Genre, Content, Author_Name)
values
(
	"Cai lon",
    "12 23 45 ",
    "Politics",
    "Hello tung con cac ",
    "Nguyen"
)
select * from article ;
select *from author;
DELETE FROM  author;
drop database NewsCollection;
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
-- -----------------------------------------------------
-- Schema newscollection
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema newscollection
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `newscollection` DEFAULT CHARACTER SET utf8mb3 ;
SHOW WARNINGS;
USE `NewsCollection` ;

-- -----------------------------------------------------
-- Table `NewsCollection`.`Author`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `NewsCollection`.`Author` (
  `Name` VARCHAR(100) NOT NULL,
  `Bio` VARCHAR(900) NULL,
  `Contact` VARCHAR(200) NULL,
  PRIMARY KEY (`Name`))
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `NewsCollection`.`Article`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `NewsCollection`.`Article` (
  `Title` VARCHAR(300) NOT NULL,
  `Publish_Time` VARCHAR(45) NULL,
  `Genre` VARCHAR(20) NULL,
  `Content` LONGTEXT NULL,
  `Author_Name` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`Title`, `Author_Name`),
  INDEX `fk_Article_Author1_idx` (`Author_Name` ASC) VISIBLE,
  CONSTRAINT `fk_Article_Author1`
    FOREIGN KEY (`Author_Name`)
    REFERENCES `NewsCollection`.`Author` (`Name`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `NewsCollection`.`Comment`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `NewsCollection`.`Comment` (
  `Reader` INT UNSIGNED NOT NULL,
  `Time` DATETIME(200) NULL,
  `Content` VARCHAR(500) NULL,
  `Title` VARCHAR(300) NULL,
  INDEX `fk_comment_article_idx` (`Title` ASC) VISIBLE,
  CONSTRAINT `fk_comment_article`
    FOREIGN KEY (`Title`)
    REFERENCES `NewsCollection`.`Article` (`Title`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW WARNINGS;
USE `newscollection` ;

-- -----------------------------------------------------
-- Table `newscollection`.`article`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `newscollection`.`article` (
  `Title` VARCHAR(300) NOT NULL,
  `Publish_Time` VARCHAR(100) NULL DEFAULT NULL,
  `Genre` VARCHAR(20) NULL DEFAULT NULL,
  `Content` LONGTEXT NULL DEFAULT NULL,
  PRIMARY KEY (`Title`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `newscollection`.`author`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `newscollection`.`author` (
  `Name` VARCHAR(100) NOT NULL,
  `Bio` VARCHAR(900) NULL DEFAULT NULL,
  `Contact` VARCHAR(200) NULL DEFAULT NULL,
  PRIMARY KEY (`Name`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `newscollection`.`article_has_author`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `newscollection`.`article_has_author` (
  `Author_Name` VARCHAR(100) NOT NULL,
  `Article_Title` VARCHAR(300) NOT NULL,
  PRIMARY KEY (`Author_Name`, `Article_Title`),
  INDEX `fk_Article_has_Author_Author1_idx` (`Author_Name` ASC) VISIBLE,
  INDEX `fk_Article_has_Author_Article_idx` (`Article_Title` ASC) VISIBLE,
  CONSTRAINT `fk_Article_has_Author_Article`
    FOREIGN KEY (`Article_Title`)
    REFERENCES `newscollection`.`article` (`Title`),
  CONSTRAINT `fk_Article_has_Author_Author1`
    FOREIGN KEY (`Author_Name`)
    REFERENCES `newscollection`.`author` (`Name`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;

SHOW WARNINGS;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
