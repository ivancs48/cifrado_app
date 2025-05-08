import tkinter as tk
from tkinter import ttk, messagebox, font
from models.cifrado import Cifrado

class VentanaDescifrado:
    def __init__(self, root):
        self.root = root
        self.root.title("Descifrado de Números")
        self.root.geometry("500x350")
        self.root.resizable(False, False)
        
        # Configurar estilo
        self.configurar_estilo()
        
        # Crear componentes de la interfaz
        self.crear_widgets()
    
    def configurar_estilo(self):
        # Configurar fuentes
        self.titulo_font = font.Font(family="Helvetica", size=14, weight="bold")
        self.subtitulo_font = font.Font(family="Helvetica", size=12)
        self.resultado_font = font.Font(family="Courier", size=14, weight="bold")
        self.boton_font = font.Font(family="Helvetica", size=10, weight="bold")
        
        # Configurar estilo de botones
        self.style = ttk.Style()
        self.style.configure('TButton', font=self.boton_font)
    
    def crear_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título de la ventana
        titulo = ttk.Label(main_frame, text="Descifrado de Números", font=self.titulo_font)
        titulo.pack(pady=(10, 20))
        
        # Frame para ingreso de datos
        input_frame = ttk.LabelFrame(main_frame, text="Ingrese un número cifrado de 6 dígitos", padding="10")
        input_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Entrada de número cifrado
        self.numero_var = tk.StringVar()
        ttk.Label(input_frame, text="Número cifrado:").grid(row=0, column=0, padx=5, pady=10)
        self.entry_numero = ttk.Entry(input_frame, textvariable=self.numero_var, width=20, font=self.subtitulo_font)
        self.entry_numero.grid(row=0, column=1, padx=5, pady=10)
        
        # Botón para descifrar
        btn_descifrar = ttk.Button(input_frame, text="Descifrar", command=self.descifrar_numero)
        btn_descifrar.grid(row=0, column=2, padx=10, pady=10)
        
        # Frame para mostrar resultado
        result_frame = ttk.LabelFrame(main_frame, text="Resultado del descifrado", padding="10")
        result_frame.pack(fill=tk.X, padx=10, pady=20)
        
        # Etiqueta para mostrar el resultado
        self.resultado_var = tk.StringVar()
        self.resultado_var.set("------")
        resultado_label = ttk.Label(result_frame, textvariable=self.resultado_var, 
                                   font=self.resultado_font, foreground="green")
        resultado_label.pack(pady=10)
        
        # Explicación del proceso
        ttk.Separator(main_frame, orient="horizontal").pack(fill=tk.X, padx=10, pady=10)
        
        info_label = ttk.Label(main_frame, text="Proceso de descifrado:", font=self.subtitulo_font)
        info_label.pack(anchor="w", padx=10, pady=(10, 5))
            
    def descifrar_numero(self):
        try:
            # Obtener el número cifrado ingresado
            numero_str = self.numero_var.get().strip()
            
            # Validar que el valor ingresado sea un número
            if not numero_str.isdigit():
                messagebox.showerror("Error", "Debe ingresar un número entero")
                return
            
            # Validar que el número tenga 6 o menos dígitos (para permitir ceros a la izquierda)
            if len(numero_str) > 6:
                messagebox.showerror("Error", "El número debe tener máximo 6 dígitos")
                return
            
            # Convertir a entero
            numero_cifrado = int(numero_str)
            
            # Descifrar el número
            cifrador = Cifrado()
            resultado = cifrador.descifrar_numero(numero_cifrado)
            
            # Mostrar el resultado con formato de 6 dígitos
            self.resultado_var.set(f"{resultado:06d}")
            
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")