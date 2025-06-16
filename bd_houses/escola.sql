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

show TABLES;

INSERT INTO alunos VALUES (
	NULL,
    'Maria Onofre',
    'Rua Crucilândia, 27',
    '3',
    'Fernando Sabiá',
    'Lógica de Programação',
    '2025-06-16',
    7.0
);

INSERT INTO alunos VALUES (
	NULL,
    'Pedro Almobolívar',
    'Rua Kanindê, 157',
    '3',
    'Fernando Sabiá',
    'Lógica de Programação',
    '2025-06-16',
    9.9
);

INSERT INTO alunos VALUES (
	NULL,
    'Suzana von Bismark',
    'Avenida das Oliveiras, 187',
    '3',
    'Fernando Sabiá',
    'Lógica de Programação',
    '2025-06-16',
    8.9
);

INSERT INTO alunos VALUES (
	NULL,
    'Cleiton de Faria',
    'Alameda das Flores Bonitas, 34',
    '3',
    'Fernando Sabiá',
    'Lógica de Programação',
    '2025-06-16',
    5.7
);

SELECT * FROM alunos;