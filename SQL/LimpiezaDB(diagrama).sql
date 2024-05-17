SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF EXISTS `Persona`;
DROP TABLE IF EXISTS `Rol`;
DROP TABLE IF EXISTS `Cuadrilla`;
DROP TABLE IF EXISTS `cat_colonias`;
DROP TABLE IF EXISTS `HistorialTrabajos`;
DROP TABLE IF EXISTS `MiembrosCuadrilla`;

SET FOREIGN_KEY_CHECKS = 1;


CREATE TABLE `Persona` (
    `personaId` CHAR(9) NOT NULL,
    `rolId` INT(1) NOT NULL,
    `nombre` VARCHAR(50) NOT NULL,
    `apellidoPaterno` VARCHAR(50) NOT NULL,
    `apellidoMaterno` VARCHAR(50) NOT NULL,
    `nombreUsuario` VARCHAR(50) NOT NULL,
    `contraseña` VARCHAR(50) NOT NULL,
    `email` VARCHAR(50) NOT NULL,
    `telefono` BIGINT NOT NULL,
    PRIMARY KEY (`personaId`)
);

CREATE TABLE `Rol` (
    `rolId` INT NOT NULL AUTO_INCREMENT,
    `rol` VARCHAR(50) NOT NULL,
    PRIMARY KEY (`rolId`)
);

CREATE TABLE `Cuadrilla` (
    `cuadrillaId` INT NOT NULL,
    `jefeCuadrillaId` INT NOT NULL,
    `nombre` VARCHAR(50) NOT NULL,
    `estado` VARCHAR(50) NOT NULL,
    PRIMARY KEY (`cuadrillaId`)
);

CREATE TABLE `cat_colonias` (
    `cve_incr_cp` INT NOT NULL AUTO_INCREMENT,
    `cve_codpost` CHAR(5),
    `nombre_colonia` VARCHAR(100),
    `tipo_asentamiento` VARCHAR(100),
    `municipio` VARCHAR(100),
    `estado` VARCHAR(100),
    `ciudad` VARCHAR(100),
    `lat` VARCHAR(40),
    `lon` VARCHAR(40),
    PRIMARY KEY (`cve_incr_cp`)
);

CREATE TABLE `HistorialTrabajos` (
    `historialTrabajosId` INT NOT NULL AUTO_INCREMENT,
    `cveColonia` INT NOT NULL,
    `cuadrillaId` INT NOT NULL,
    `descripcion` TEXT,
    `comentarios` TEXT,
    `rutaImagen` TEXT,
    `fechaAgendada` DATE,
    `estatus` VARCHAR(50) NOT NULL,
    PRIMARY KEY (`historialTrabajosId`)
);

CREATE TABLE `MiembrosCuadrilla` (
    `personaId` CHAR(9) NOT NULL,
    `cuadrillaId` INT NOT NULL,
    PRIMARY KEY (`personaId`, `cuadrillaId`)
);

