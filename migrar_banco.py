import sqlite3

conn = sqlite3.connect('cadastros.db')
c = conn.cursor()

# Criar nova tabela com a coluna 'empresa' no lugar de 'endereco'
c.execute('''
    CREATE TABLE IF NOT EXISTS inscritos_novo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        rg TEXT UNIQUE,
        cpf TEXT UNIQUE,
        celular TEXT,
        email TEXT,
        empresa TEXT,
        bairro TEXT
    )
''')

# Copiar os dados da tabela antiga para a nova
c.execute('''
    INSERT INTO inscritos_novo (id, nome, rg, cpf, celular, email, empresa, bairro)
    SELECT id, nome, rg, cpf, celular, email, endereco, bairro FROM inscritos
''')

# Apagar a tabela antiga e renomear a nova
c.execute('DROP TABLE inscritos')
c.execute('ALTER TABLE inscritos_novo RENAME TO inscritos')

conn.commit()
conn.close()

print("Banco de dados atualizado com sucesso!")