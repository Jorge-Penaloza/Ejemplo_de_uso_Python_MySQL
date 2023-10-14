-- MySQL Workbench Synchronization
-- Generated: 2021-10-03 17:08
-- Model: New Model
-- Version: 1.0
-- Project: Name of the project
-- Author: ricar

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

CREATE SCHEMA IF NOT EXISTS `colegio` DEFAULT CHARACTER SET utf8 ;

CREATE TABLE IF NOT EXISTS `colegio`.`personas` (
  `rut` CHAR(10) NOT NULL,
  `nombre` VARCHAR(255) NOT NULL,
  `apellido` VARCHAR(255) NOT NULL,
  `direccion` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`rut`),
  UNIQUE INDEX `rut_UNIQUE` (`rut` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

CREATE TABLE IF NOT EXISTS `colegio`.`estudiantes` (
  `rut` CHAR(10) NOT NULL,
  `anio` INT(11) NOT NULL,
  INDEX `rut_a` (`rut` ASC),
  PRIMARY KEY (`rut`, `anio`),
  CONSTRAINT `rut_p`
    FOREIGN KEY (`rut`)
    REFERENCES `colegio`.`personas` (`rut`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

CREATE TABLE IF NOT EXISTS `colegio`.`apoderados` (
  `rut` CHAR(10) NOT NULL,
  `rut_alumno` CHAR(10) NOT NULL,
  INDEX `rut_a_idx` (`rut_alumno` ASC),
  PRIMARY KEY (`rut`, `rut_alumno`),
  CONSTRAINT `rut_p1`
    FOREIGN KEY (`rut`)
    REFERENCES `colegio`.`personas` (`rut`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `rut_a1`
    FOREIGN KEY (`rut_alumno`)
    REFERENCES `colegio`.`estudiantes` (`rut`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

CREATE TABLE IF NOT EXISTS `colegio`.`asignatura` (
  `codigo` INT(11) NOT NULL,
  `descripcion` VARCHAR(255) NOT NULL,
  `planEstudios` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`codigo`),
  UNIQUE INDEX `codigo_UNIQUE` (`codigo` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

CREATE TABLE IF NOT EXISTS `colegio`.`actividad` (
  `codigo` INT(11) NOT NULL,
  `descripcion` VARCHAR(255) NOT NULL,
  `planEstudios` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`codigo`),
  UNIQUE INDEX `codigo_UNIQUE` (`codigo` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

CREATE TABLE IF NOT EXISTS `colegio`.`inscripcionesAsignaturas` (
  `codigo` INT(11) NOT NULL,
  `rut_alumno` CHAR(10) NOT NULL,
  INDEX `rut_a_idx` (`rut_alumno` ASC),
  INDEX `rut_a` (`rut_alumno` ASC),
  INDEX `codigo_a` (`codigo` ASC),
  PRIMARY KEY (`codigo`, `rut_alumno`),
  CONSTRAINT `codigo_a2`
    FOREIGN KEY (`codigo`)
    REFERENCES `colegio`.`asignatura` (`codigo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `rut_a2`
    FOREIGN KEY (`rut_alumno`)
    REFERENCES `colegio`.`estudiantes` (`rut`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

CREATE TABLE IF NOT EXISTS `colegio`.`inscripcionesActividades` (
  `codigo` INT(11) NOT NULL,
  `rut_alumno` CHAR(10) NOT NULL,
  INDEX `rut_a_idx` (`rut_alumno` ASC),
  INDEX `rut_a` (`rut_alumno` ASC),
  INDEX `codigo_a` (`codigo` ASC),
  PRIMARY KEY (`codigo`, `rut_alumno`),
  CONSTRAINT `codigo_a3`
    FOREIGN KEY (`codigo`)
    REFERENCES `colegio`.`actividad` (`codigo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `rut_a3`
    FOREIGN KEY (`rut_alumno`)
    REFERENCES `colegio`.`estudiantes` (`rut`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
