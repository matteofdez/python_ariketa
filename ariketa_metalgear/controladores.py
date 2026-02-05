# Importa funciones del modelo para login y CRUD componentes
from modelo import check_login, get_all_components, create_component, update_component, delete_component
# Importa las vistas Tkinter (login y gestor componentes)
from vista import LoginView, ComponentsView



class Controller:
    # Constructor: crea la ventana de login
    def __init__(self):
        self.login_view = LoginView(self)
    
    # Inicia la aplicación con login
    def run(self):
        self.login_view.mainloop()
    
    # Verifica las credenciales snake/FOXHOUND con bcrypt
    def handle_login(self, username, password):
        return check_login(username, password)
    
    # Abre la ventana de componentes tras login exitoso
    def open_components_view(self):
        self.components_view = ComponentsView(self)
        self.components_view.mainloop()
    
    # Obtiene todos los componentes de la BD para mostrar en tabla
    def get_components(self):
        return get_all_components()
    
    # Crea o actualiza componente (nuevo y/o editar)
    def save_component(self, comp_id, name, desc, integrity):
        if comp_id is None:
            create_component(name, desc, integrity) 
        else:
            update_component(comp_id, name, desc, integrity)
    
    # Elimina el componente seleccionado
    def delete_component(self, comp_id):
        delete_component(comp_id)
