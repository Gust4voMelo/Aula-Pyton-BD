import sqlite3

conn = sqlite3.connect('banco.db')

codigo_sql = """
-- Tabela Autor
CREATE TABLE Autor (
	id_autor INT PRIMARY KEY AUTOINCREMENT NOT NULL,
    nome VARCHAR(70) NOT NULL,
    data_nascimento DATE NOT NULL,
    nacionalidade VARCHAR(50) NOT NULL
);

ALTER TABLE Autor MODIFY COLUMN nome VARCHAR(70) NOT NULL;

-- Tabela Livro
CREATE TABLE Livro (
	id_livro INT PRIMARY KEY AUTOINCREMENT NOT NULL,
    titulo VARCHAR (200) NOT NULL,
    ano_publicacao DATE NOT NULL,
    editora VARCHAR(100) NOT NULL,
    id_autor INT NOT NULL,
    FOREIGN KEY (id_autor) REFERENCES Autor (id_autor)
);

-- Populando Autor
INSERT INTO Autor (nome, data_nascimento, nacionalidade) 
VALUES
	('George Orwell', '1903-06-25', 'Inglês'),
    ('Aldous Huxley', '1894-06-26', 'Inglês'),
    ('Neal Shusterman', '1962-11-12', 'Americano');

-- Populando Livro 
INSERT INTO Livro (titulo, ano_publicacao, editora, id_autor)
VALUES
	('1984', '1949-01-01', 'Companhia das Letras', 1),
	('A Revolução dos Bichos', '1945-01-01', 'Companhia das Letras', 1),
    ('Adimiravel Mundo Novo', '1932-01-01', 'Antígona', 2),
    ('O Ceifador', '2016-01-01', 'Seguinte', 3),
    ('A Nuvem', '2018-01-01', 'Seguinte', 3),
    ('O Timbre', '2020-01-01', 'Seguinte', 3);
    """

conn.execute(codigo_sql)
conn.commit()
conn.close()