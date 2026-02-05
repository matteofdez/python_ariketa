# Módulo principal de Tkinter
import tkinter as tk     
from tkinter import ttk, messagebox  

class LoginView(tk.Tk):
    # Ventana de login (pantalla 1)
    def __init__(self, controller):
        super().__init__()
        self.title("Outer Heaven - Login")
        self.geometry("400x300")
        self.controller = controller

        # Frame principal con padding
        main_frame = ttk.Frame(self, padding="50")
        main_frame.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(3, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)

        # Labels de campos
        ttk.Label(main_frame, text="Usuario").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        ttk.Label(main_frame, text="Contraseña").grid(row=1, column=0, padx=5, pady=5, sticky="w")

        # Variables para entrada de datos
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()

        # Campos de entrada
        ttk.Entry(main_frame, textvariable=self.username_var).grid(
            row=0, column=1, padx=5, pady=5, sticky="ew"
        )
        ttk.Entry(main_frame, textvariable=self.password_var, show="*").grid(
            row=1, column=1, padx=5, pady=5, sticky="ew"
        )
        ttk.Button(main_frame, text="Entrar", command=self.on_login).grid(
            row=2, column=0, columnspan=2, pady=20
        )

    # Valida login y abre gestor componentes
    def on_login(self):
        u = self.username_var.get().strip()
        p = self.password_var.get()

        if len(u) == 0:
            messagebox.showerror("Error", "Usuario requerido")
            return

        if self.controller.handle_login(u, p):
            self.destroy()
            self.controller.open_components_view()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")

class ComponentsView(tk.Tk):
    # Ventana gestor componentes (pantalla 2) con CRUD
    def __init__(self, controller):
        super().__init__()
        self.title("Gestor Metal Gear - Ventana2 - Componentes")
        self.geometry("800x500")
        self.controller = controller

        # Treeview con 4 columnas (incluye integridad)
        self.tree = ttk.Treeview(
            self,
            columns=("id", "name", "desc", "integrity"),
            show="headings"
        )
        self.tree.heading("id", text="ID")
        self.tree.heading("name", text="Nombre")
        self.tree.heading("desc", text="Descripción")
        self.tree.heading("integrity", text="Integridad")
        self.tree.column("id", width=50)
        self.tree.column("name", width=180)
        self.tree.column("desc", width=360)
        self.tree.column("integrity", width=80, anchor="e")
        self.tree.bind("<<TreeviewSelect>>", self.on_select)
        self.tree.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")

        # Labels de formulario
        ttk.Label(self, text="Nombre:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        ttk.Label(self, text="Descripción:").grid(row=2, column=0, sticky="ne", padx=5, pady=5)
        ttk.Label(self, text="Integridad (0-100):").grid(row=3, column=0, sticky="e", padx=5, pady=5)

        # Variables del formulario
        self.name_var = tk.StringVar()
        self.int_var = tk.StringVar()
        self.selected_id = None

        # Campos formulario
        ttk.Entry(self, textvariable=self.name_var, width=50).grid(
            row=1, column=1, columnspan=2, padx=5, pady=5, sticky="ew"
        )

        self.desc_text = tk.Text(self, height=4, width=50)
        self.desc_text.grid(row=2, column=1, columnspan=2, padx=5, pady=5, sticky="ew")

        ttk.Entry(self, textvariable=self.int_var, width=10).grid(
            row=3, column=1, padx=5, pady=5, sticky="w"
        )

        # Botones CRUD
        ttk.Button(self, text="Nuevo", command=self.on_new).grid(row=4, column=0, pady=10, padx=5)
        ttk.Button(self, text="Guardar", command=self.on_save).grid(row=4, column=1, pady=10, padx=5)
        ttk.Button(self, text="Eliminar", command=self.on_delete).grid(row=4, column=2, pady=10, padx=5)

        # Configuración grid responsive
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
 # Carga datos iniciales
        self.refresh() 

    # Limpia Treeview y recarga datos desde BD
    def refresh(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for row in self.controller.get_components():
            self.tree.insert("", "end", values=row)

    # Carga datos del componente seleccionado en formulario
    def on_select(self, event):
        item = self.tree.focus()
        if not item:
            return
        comp_id, name, desc, integrity = self.tree.item(item)["values"]
        self.selected_id = comp_id
        self.name_var.set(name or "")
        self.desc_text.delete(1.0, tk.END)
        self.desc_text.insert(1.0, desc or "")
        self.int_var.set(str(integrity))

    # Limpia formulario para nuevo componente
    def on_new(self):
        self.selected_id = None
        self.name_var.set("")
        self.desc_text.delete(1.0, tk.END)
        self.int_var.set("")

    # Valida y guarda el componente
    def on_save(self):
        name = self.name_var.get().strip()
        desc = self.desc_text.get(1.0, tk.END).strip()
        if not name:
            messagebox.showerror("Error", "El nombre es obligatorio")
            return

        # Validación integridad 0-100 en frontend
        try:
            integrity = int(self.int_var.get())
        except ValueError:
            messagebox.showerror("Error", "La integridad debe ser un número entero")
            return

        if integrity < 0 or integrity > 100:
            messagebox.showerror("Error", "La integridad debe estar entre 0 y 100")
            return

        try:
            self.controller.save_component(self.selected_id, name, desc, integrity)
            self.refresh()
            self.on_new()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Confirma y elimina componente seleccionado
    def on_delete(self):
        if self.selected_id is None:
            messagebox.showwarning("Advertencia", "Selecciona un componente")
            return
        if messagebox.askyesno("Confirmar", "¿Eliminar este componente?"):
            self.controller.delete_component(self.selected_id)
            self.refresh()
            self.on_new()
