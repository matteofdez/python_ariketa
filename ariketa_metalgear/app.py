# Se utiliza para el hash de contraseñas
import bcrypt  
# Importa la función que crea BD mas el usuario semilla
from modelo import init_db 
# Importa clase Controller principal
from controladores import Controller 

# Función principal de la aplicación
def main():
    # Inicializa la base de datos SQLite con tablas y usuario snake/FOXHOUND
    init_db()
    # Crea instancia del controlador
    c = Controller()
    # Inicia la aplicación
    c.run()

# Ejecuta main() solo si se llama directamente 
if __name__ == "__main__":
    main()
