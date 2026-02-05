# Importa bcrypt para generar hash de contraseña
import bcrypt
# Importa funciones de conexión e inicialización de BD
from modelo import get_connection, init_db

# Inicializa/crea la base de datos con tablas users y components
init_db()
# Obtiene conexión a metalgear.db
conn = get_connection()
# Crea cursor para ejecutar consultas SQL
cur = conn.cursor()
# Contraseña plana: FOXHOUND
password = "FOXHOUND"
# Genera hash bcrypt con salt aleatorio (encode a bytes UTF-8)
hash_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
# Inserta usuario snake con hash (INSERT OR IGNORE evita duplicados)
cur.execute("INSERT OR IGNORE INTO users (username, password_hash) VALUES (?, ?)", 
            ("snake", hash_pw))
# Confirma la transacción en BD
conn.commit()
# Cierra conexión a BD
conn.close()
# Mensaje de confirmación
print("Usuario creado")
