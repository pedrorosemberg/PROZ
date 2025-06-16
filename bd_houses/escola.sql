CREATE database escola;
USE escola;
CREATE TABLE alunos (
	codigo INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    endereco VARCHAR(100),
    sala VARCHAR(50),
    professor VARCHAR(100),
    disciplina VARCHAR(100),
    data DATE,
    nota DECIMAL(4,2)
);