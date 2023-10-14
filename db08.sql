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
