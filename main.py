import tkinter as tk
from views.ventana_principal import VentanaPrincipal

def main():
    # Crear la ventana principal
    root = tk.Tk()
    app = VentanaPrincipal(root)
    
    # Iniciar el bucle de eventos
    root.mainloop()

if __name__ == "__main__":
    main()