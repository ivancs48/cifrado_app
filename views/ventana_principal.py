import tkinter as tk
from tkinter import ttk, font
from views.ventana_cifrado import VentanaCifrado
from views.ventana_descifrado import VentanaDescifrado

class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Cifrado de Datos")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        
        # Configurar estilo
        self.configurar_estilo()
        
        # Crear componentes de la interfaz
        self.crear_widgets()
    
    def configurar_estilo(self):
        # Configurar fuentes
        self.titulo_font = font.Font(family="Helvetica", size=16, weight="bold")
        self.subtitulo_font = font.Font(family="Helvetica", size=12)
        self.boton_font = font.Font(family="Helvetica", size=10, weight="bold")
        
        # Configurar estilo de botones
        self.style = ttk.Style()
        self.style.configure('TButton', font=self.boton_font)
    
    def crear_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título de la aplicación
        titulo = ttk.Label(main_frame, text="Sistema de Cifrado de Datos", font=self.titulo_font)
        titulo.pack(pady=(20, 10))
        
        # Información del autor
        info_frame = ttk.LabelFrame(main_frame, text="Información del Autor", padding="10")
        info_frame.pack(fill=tk.X, padx=20, pady=20)
        
        # Modificar estos datos con tu información personal
        ttk.Label(info_frame, text="Nombre: Ivan Calderon", font=self.subtitulo_font).pack(anchor="w", pady=2)
        ttk.Label(info_frame, text="ID: 80169923", font=self.subtitulo_font).pack(anchor="w", pady=2)
        ttk.Label(info_frame, text="Curso: Aplicacion I", font=self.subtitulo_font).pack(anchor="w", pady=2)
        
        # Botones para navegar a otras ventanas
        botones_frame = ttk.Frame(main_frame)
        botones_frame.pack(pady=30)
        
        btn_cifrado = ttk.Button(botones_frame, text="Cifrar Número", 
                                 command=self.abrir_ventana_cifrado, width=20)
        btn_cifrado.grid(row=0, column=0, padx=10)
        
        btn_descifrado = ttk.Button(botones_frame, text="Descifrar Número", 
                                    command=self.abrir_ventana_descifrado, width=20)
        btn_descifrado.grid(row=0, column=1, padx=10)
    
    def abrir_ventana_cifrado(self):
        ventana_cifrado = tk.Toplevel(self.root)
        VentanaCifrado(ventana_cifrado)
    
    def abrir_ventana_descifrado(self):
        ventana_descifrado = tk.Toplevel(self.root)
        VentanaDescifrado(ventana_descifrado)