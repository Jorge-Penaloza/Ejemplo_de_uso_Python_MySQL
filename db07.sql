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
