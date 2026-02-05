# Módulo para SQLite
import sqlite3  
# Para hash/verificación de contraseñas
import bcrypt   

# Nombre del archivo de la base de datos
DB_NAME = "metalgear.db"  

# Devuelve conexión activa a metalgear.db
def get_connection():
    return sqlite3.connect(DB_NAME)

# Crea tablas users/components con constraints y usuario semilla
def init_db():
    conn = get_connection()
    cur = conn.cursor()
    # Tabla users con hash bcrypt
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash BLOB NOT NULL
        )
    """)
    # Tabla components con CHECK integrity 0-100
    cur.execute("""
        CREATE TABLE IF NOT EXISTS components(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            integrity INTEGER NOT NULL CHECK(integrity BETWEEN 0 AND 100)
        )
    """)
    conn.commit()
    conn.close()

# Verifica login snake/FOXHOUND con bcrypt.checkpw()
def check_login(username, password_plain):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
    row = cur.fetchone()
    conn.close()
    if not row:
        return False
    stored = row[0]
    return bcrypt.checkpw(password_plain.encode('utf-8'), stored)

# Retorna lista (id, name, desc, integrity) para Treeview
def get_all_components():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, description, integrity FROM components")
    rows = cur.fetchall()
    conn.close()
    return rows

# Crea nuevo componente 
def create_component(name, description, integrity):
    if not (0 <= integrity <= 100):
        raise ValueError("La integridad debe estar entre 0 y 100")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO components(name, description, integrity) VALUES (?,?,?)",
        (name, description, integrity)
    )
    conn.commit()
    conn.close()

# Actualiza componente 
def update_component(comp_id, name, description, integrity):
    if not (0 <= integrity <= 100):
        raise ValueError("La integridad debe estar entre 0 y 100")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE components SET name=?, description=?, integrity=? WHERE id=?",
        (name, description, integrity, comp_id)
    )
    conn.commit()
    conn.close()

# Elimina componente por ID
def delete_component(comp_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM components WHERE id = ?", (comp_id,))
    conn.commit()
    conn.close()
