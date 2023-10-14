CREATE TABLE IF NOT EXISTS `colegio`.`personas` (
  `rut` CHAR(10) NOT NULL,
  `nombre` VARCHAR(255) NOT NULL,
  `apellido` VARCHAR(255) NOT NULL,
  `direccion` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`rut`),
  UNIQUE INDEX `rut_UNIQUE` (`rut` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;