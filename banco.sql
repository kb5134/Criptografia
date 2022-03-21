CREATE TABLE gulosa(
    chave int NOT NULL PRIMARY KEY,
    dicionarios varchar(250),
    data DATETIME DEFAULT now()
);