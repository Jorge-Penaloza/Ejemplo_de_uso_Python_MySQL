CREATE TABLE IF NOT EXISTS `colegio`.`asignatura` (
  `codigo` INT(11) NOT NULL,
  `descripcion` VARCHAR(255) NOT NULL,
  `planEstudios` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`codigo`),
  UNIQUE INDEX `codigo_UNIQUE` (`codigo` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;