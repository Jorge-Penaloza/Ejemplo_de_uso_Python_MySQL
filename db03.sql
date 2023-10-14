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