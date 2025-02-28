# database.py - Gerenciamento do banco de dados

import sqlite3

def conectar_bd():
    conn = sqlite3.connect('cadastros.db')
    return conn

def listar_inscritos():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM inscritos")
    dados = cursor.fetchall()
    conn.close()
    return dados 