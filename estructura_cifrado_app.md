Sistema de Cifrado y Descifrado de Datos

Descripción
Esta aplicación de escritorio desarrollada en Python con Tkinter implementa un sistema para cifrar y descifrar números de 6 dígitos, diseñado para transmitir información sensible de manera segura a través de dispositivos móviles.

Características
Interfaz gráfica amigable con tres ventanas principales
Algoritmo de cifrado mediante transformación de dígitos
Validación de entradas para garantizar datos correctos
Arquitectura basada en el patrón Modelo-Vista
Instalación
Asegúrate de tener Python 3.6 o superior instalado
Clona o descarga este repositorio
No se requieren dependencias adicionales (Tkinter viene incluido con Python)

python main.py

Algoritmo de Cifrado
El proceso de cifrado sigue estos pasos:

Suma 7 a cada dígito y obtiene el residuo de dividir entre 10
Intercambia el primer dígito con el tercero
Intercambia el segundo dígito con el cuarto
Intercambia el quinto dígito con el sexto
El descifrado invierte este proceso para recuperar el número original.

Estructura del Proyecto
cifrado_app/
│
├── models/
│   ├── __init__.py
│   └── cifrado.py
│
├── views/
│   ├── __init__.py
│   ├── ventana_principal.py
│   ├── ventana_cifrado.py
│   └── ventana_descifrado.py
│
└── main.py

Ejemplos de Uso
Cifrado: El número 123456 se convierte en 018932
Descifrado: El número 018932 se convierte en 123456

Autor Ivan Calderon
ID: 80169923
Curso: Aplicaciones I