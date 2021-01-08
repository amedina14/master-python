CREATE DATABASE IF NOT EXISTS master_python;
use master_python;

CREATE TABLE IF NOT EXISTS users(
id          int(25) auto_increment not null,
nome        varchar(30) not null,
cognome     varchar(30) not null,
email       varchar(60) not null,
password    varchar(255) not null,
data        date not null,
CONSTRAINT pk_users PRIMARY KEY(id),
CONSTRAINT uq_email UNIQUE(email)
)ENGINE=InnoDb;

CREATE TABLE IF NOT EXISTS notes(
id          int(25) auto_increment not null,
user_id     int(25) not null,
titulo      varchar(30) not null,
contenuto   MEDIUMTEXT,
data        date not null,
CONSTRAINT pk_users PRIMARY KEY(id),
CONSTRAINT fk_nota_user FOREIGN KEY(user_id) REFERENCES users(id)
)ENGINE=InnoDb;