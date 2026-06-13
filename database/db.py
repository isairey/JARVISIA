import sqlite3

def conectar():
    conn = sqlite3.connect("database/memory.db")
    return conn

def crear_tablas():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS memoria(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pregunta TEXT,
        respuesta TEXT,
        fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS recordatorios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tarea TEXT,
        fecha TEXT
    )
    """)

    conn.commit()
    conn.close()