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