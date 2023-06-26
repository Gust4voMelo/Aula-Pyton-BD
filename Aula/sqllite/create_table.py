import sqlite3

conn= sqlite3.connect('banco.db')
cursor = conn.cursor()

crete_table_query = """
create table clients (
    id interger not null primary key autoincrement,
    nome text not null,
    idade interger,
    cpf varchar(11) not null
);
"""