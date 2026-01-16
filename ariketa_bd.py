import sqlite3

#Conectar la base de datos
#Crear la base de datos 
conexion = sqlite3.connect('athletic.db')
cursor = conexion.cursor()

# Crear tabla jugadores
cursor.execute('''
   CREATE TABLE IF NOT EXISTS jugadores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        posicion TEXT NOT NULL,
        dorsal INTEGER UNIQUE CHECK(dorsal BETWEEN 1 AND 99),
        goles INTEGER DEFAULT 0 CHECK(goles >= 0),
        fecha_alta DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')

# Insertar un registro de ejemplo
cursor.execute('''
    INSERT INTO jugadores (nombre, posicion, dorsal, goles) 
    VALUES ('Iñaki Williams', 'Delantero', 22, 15)
''')

# Confirmar cambios y guardar
conexion.commit()

# Verificar la inserción (opcional)
cursor.execute("SELECT * FROM jugadores")
registros = cursor.fetchall()
print("Tabla 'jugadores' del Athletic creada e inserción realizada correctamente.")
print("Registros en la tabla:")
for reg in registros:
    print(reg)

# Cerrar conexión
conexion.close()