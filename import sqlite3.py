import sqlite3

def criar_banco():
    conn = sqlite3.connect('vendas_coordenacao.db')
    cursor = conn.cursor()

    # Tabela de Vendedores
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vendedores (
            codigo TEXT PRIMARY KEY,
            nome TEXT NOT NULL
        )
    ''')

    # Tabela de Clientes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            codigo TEXT PRIMARY KEY,
            nome TEXT NOT NULL
        )
    ''')

    # Tabela de Registros de Visitas (Onde ficam as vendas)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS visitas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cod_vendedor TEXT,
            cod_cliente TEXT,
            comprou TEXT,
            produto TEXT,
            preco REAL,
            prazo TEXT,
            data_visita TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(cod_vendedor) REFERENCES vendedores(codigo),
            FOREIGN KEY(cod_cliente) REFERENCES clientes(codigo)
        )
    ''')

    # Inserindo dados de teste (Ignora se já existirem)
    vendedores = [('101', 'João Silva'), ('102', 'Maria Souza')]
    clientes = [('500', 'Loja ABC'), ('501', 'Mercado Central')]
    
    cursor.executemany('INSERT OR IGNORE INTO vendedores VALUES (?,?)', vendedores)
    cursor.executemany('INSERT OR IGNORE INTO clientes VALUES (?,?)', clientes)

    conn.commit()
    conn.close()

criar_banco()