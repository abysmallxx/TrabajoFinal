from tkinter import *
from tkinter import messagebox
#Importa el menu principal
from principal import menuPrincipal
# Importa las funciones de cargar_datos.py
from BD.cargar_datos import cargar_proveedores, cargar_ubicaciones, cargar_medicamentos
from BD.conexion import DAO

# Función para autenticar al usuario
def autenticar():
    # Pedir al usuario que ingrese su nombre de usuario y contraseña
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()

    # Verificar las credenciales
    if usuario == "informatica1" and contraseña == "bio123":
        # Mostrar un mensaje de éxito si las credenciales son correctas
        messagebox.showinfo("¡Éxito!", "Su inicio de sesión ha sido exitoso")
        # Cerrar la ventana después de la autenticación exitosa
        ventana.destroy()
        #Abre la base de datos llamada informatica1
        dao = DAO()
        dao.__init__()
        #Crea las tablas 
        dao.crear_tablas()
        #Luego de que la seccion se haya ingresado correctamente y se hayan creado las tablas, 
        #el codigo cargara los datos de las  tablas y abrirá el menu principal
        cargar_proveedores()
        cargar_ubicaciones()
        cargar_medicamentos()
        menuPrincipal()

    else:
        # Mostrar un mensaje de error si las credenciales son incorrectas
        messagebox.showerror("Error", "Usuario o contraseña incorrectos. Intente nuevamente.")

# Función para crear y mostrar la ventana de inicio de sesión
def crear_ventana_inicio_sesion():
    global entry_usuario, entry_contraseña,ventana

    # Crear la ventana principal
    ventana = Tk()
    ventana.title("Inicio de Sesión")

    # Permitir redimensionar la ventana
    #Admite parametros que son el ancho y el alto, son de tipo bool
    # si ponemos como parametros (0,0), no se puede redimensionar en ninguna direccion 
    #Si ponemos (1,0), se redimensiona el ancho pero no el alto.  Seria lo mismo si uso booleanos, eje: (True, False)
    ventana.resizable(True, True)

    # Configurar el fondo de la ventana
    # background para el color de fondo, foreground para el color de letra
    ventana.config(bg="black")

    # Cambiar el icono de la ventana, asegúrate de que udea.ico está en el mismo directorio.
    #Debe tener descargada una imagen con extension .ico
    # si no esta en .ico se debe convertir, en la red lo puedes hacer automaticamente 
    try:
        ventana.iconbitmap("udea.ico")
    except:
        print("Icono no encontrado. Asegúrate de que el archivo 'udea.ico' está en el directorio correcto.")
    #Tamaño por defecto se puede cambiar ej: raiz.geometry("1000x1000")

    # Etiqueta para el título
    lbl_titulo = Label(ventana, text="Inicio de Sesión", bg="black", fg="white", font=("Times New Roman", 18))
    lbl_titulo.pack(pady=10)

    # Etiqueta y campo de entrada para el usuario
    lbl_usuario = Label(ventana, text="Usuario:", bg="black", fg="white")
    lbl_usuario.pack()
    entry_usuario = Entry(ventana, bg="white", fg="black")
    entry_usuario.pack(pady=5)

    # Etiqueta y campo de entrada para la contraseña
    lbl_contraseña = Label(ventana, text="Contraseña:", bg="black", fg="white")
    lbl_contraseña.pack()
    entry_contraseña = Entry(ventana, bg="white", fg="black", show="*")
    entry_contraseña.pack(pady=5)

    # Botón para iniciar sesión
    btn_iniciar_sesion = Button(ventana, text="Iniciar Sesión", command=autenticar, bg="grey", fg="white")
    btn_iniciar_sesion.pack(pady=10)

    # Ejecutar el bucle principal de Tkinter
    ventana.mainloop()



