CREATE TABLE usuario(
	nome VARCHAR(40) NOT NULL,
    id_usuario INT NOT NULL,
    PRIMARY KEY (id_usuario)
);

CREATE TABLE alimentos(
	comida varchar(25) NOT NULL,
    gramas int(4) NOT NULL,
    id_comida int NOT NULL,
    PRIMARY KEY (id_comida)
);

CREATE TABLE data(
	dia_mes_ano date NOT NULL,
    horario (time)
    