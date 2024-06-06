#BD/conexion.py
import mysql.connector
from mysql.connector import Error
from archivo import*

class DAO():
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port=3306,
                user="informatica1",
                password='bio123',
                database='informatica1'
            )
            print("Conexión establecida con éxito.\n")
            
            # Verificar si la base de datos ya existe
            cursor = self.conexion.cursor()
            cursor.execute("SHOW DATABASES")
            databases = cursor.fetchall()
            database_names = [db[0] for db in databases]
            if 'informatica1' not in database_names:
                cursor.execute("CREATE DATABASE informatica1")
                print("Base de datos 'informatica1' creada con éxito.\n")
            elif 'informatica1' in database_names:
                print('La base de datos ya existe')
                
        except Error as ex:
            print("Error al intentar la conexión: {0}".format(ex))
            self.conexion = None
            """       
            cursor.execute("SHOW DATABASES"):
            Esta línea ejecuta la consulta SQL "SHOW DATABASES", que devuelve una lista de todas las bases de datos disponibles en el servidor.
            
            databases = cursor.fetchall(): 
            Esta línea obtiene todos los resultados de la consulta ejecutada y los almacena en la variable databases. Cada fila de la tabla de resultados representa una base de datos en el servidor.
            
            database_names = [db[0] for db in databases]: Esta línea crea una lista de los nombres de las bases de datos recuperadas de la consulta. Utiliza una comprensión de lista para recorrer todas
            las filas de databases y extraer el primer elemento de cada fila, que es el nombre de la base de datos. Estos nombres se almacenan en la lista database_names.
            
            Luego se verifica si el nombre 'informatica1' no está presente en la lista database_names, es decir, si la base de datos 'informatica1' no existe en el servidor MySQL. 
            Si la base de datos 'informatica1' no está presente, se ejecuta una consulta SQL para crear una nueva base de datos con el nombre 'informatica1' en el servidor MySQL. 
            Finalmente, después de crear la base de datos 'informatica1', se imprime un mensaje indicando que la base de datos se creó correctamente.

            """


    def cerrar_conexion(self):
        """
        Esta función se encarga de cerrar la conexión activa a la base de datos si está abierta.
        Primero se verifica si la conexión está activa, es decir, si la conexión self.conexion está abierta. 
        Si la conexión está abierta, se cierra la conexión utilizando el método close(). 
        Esto es importante para liberar los recursos y mantener la integridad de la base de datos. 
        Después de cerrar la conexión, se imprime un mensaje indicando que la conexión se cerró con éxito, 
        lo que proporciona retroalimentación al usuario o al desarrollador sobre el estado de la conexión.

        """
        if self.conexion.is_connected():
            self.conexion.close()
            print("Conexión cerrada con éxito.\n")


    def crear_tablas(self):
        """
        La función crear_tablas se encarga de gestionar la creación de las tablas en la base de datos cuando la conexión está activa.
        Primero, verifica si la conexión está activa; de lo contrario, no tendría sentido intentar crear las tablas. 

        Luego, utiliza una estructura try-except para manejar cualquier error que pueda ocurrir durante la creación de las tablas, 
        imprimiendo un mensaje de error si es necesario.
        
        Dentro de la función crear_tablas, se definen tres funciones internas (create_table_medicamentos, create_table_proveedores y create_table_ubicaciones), 
        cada una diseñada para crear una tabla específica. Esto ayuda a modularizar el código y facilitar su mantenimiento.
        
        La función crea un cursor para ejecutar consultas SQL en la base de datos y ejecuta las consultas correspondientes para crear las tablas de medicamentos, proveedores y ubicaciones. 
        
        Después de ejecutar cada consulta, se realiza la confirmación de los cambios en la base de datos para que las tablas se creen de manera permanente.
        
        Se imprime un mensaje indicando que la tabla se creó con éxito para proporcionar retroalimentación al usuario o al desarrollador sobre el estado de la operación. 
        Se itera sobre los datos devueltos por el cursor,(en este caso no se están utilizando) . Finalmente, se cierra el cursor después de ejecutar la consulta para liberar los recursos.
        
        Las últimas líneas llaman a las funciones internas para crear las tablas respectivas de medicamentos, proveedores y ubicaciones, lo que inicia el proceso de creación de las tablas al llamar a la función crear_tablas.

        """
        if self.conexion is not None and self.conexion.is_connected():
            try:
                def create_table_proveedores():
                    cursor = self.conexion.cursor()
                    # Definir la consulta SQL para crear la tabla de proveedores
                    create_table_proveedores = """
                    CREATE TABLE Proveedores (
                    codigo INT PRIMARY KEY,
                    nombre VARCHAR(50),
                    apellido VARCHAR(50),
                    id VARCHAR(20),
                    entidad VARCHAR(100)
                    );
                    """
                    cursor.execute(create_table_proveedores)
                    self.conexion.commit()
                    print("Tabla de proveedores creada con éxito.\n")
                    for dato in cursor:
                        print(dato)  
                    cursor.close()

                create_table_proveedores()

                def create_table_ubicaciones():
                    cursor = self.conexion.cursor()
                    # Definir la consulta SQL para crear la tabla de ubicaciones
                    create_table_ubicaciones = """
                    CREATE TABLE Ubicaciones (
                    codigo INT PRIMARY KEY,
                    nombre VARCHAR(100),
                    telefono INT
                    );
                    """
                    cursor.execute(create_table_ubicaciones)
                    self.conexion.commit()
                    print("Tabla de ubicaciones creada con éxito.\n") 
                    for dato in cursor:
                        print(dato)  
                    cursor.close()
    
                create_table_ubicaciones()

                def create_table_medicamentos():
                    try:
                        cursor = self.conexion.cursor()
                        # Definir la consulta SQL para crear la tabla de medicamentos
                        create_table_medicamentos = """
                        CREATE TABLE Medicamentos (
                        lote VARCHAR(20) PRIMARY KEY,
                        nombre VARCHAR(100),
                        distribuidor INT,
                        cantidad INT,
                        fecha DATE,
                        precio DECIMAL(10, 2),
                        ubicacion INT
                        );
                        """

                        cursor.execute(create_table_medicamentos)
                        self.conexion.commit()
                        print("Tabla medicamentos creada con éxito.\n")
                        cursor.close()
                    except Error as ex:
                        print("Error al crear la tabla de medicamentos:", ex)

                create_table_medicamentos()

                
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

        else: print("No se puede crear las tablas porque no hay conexión establecida.")


    def ingresar(self, tabla, datos):
        """
        La función ingresar se encarga de agregar nuevos registros a una tabla específica en la base de datos.
        
        Toma tres argumentos: self, que se refiere a la instancia de la clase en la que se define la función; 
        tabla, que es el nombre de la tabla en la que se insertarán los datos; y datos, que es un diccionario
        que contiene los datos que se van a insertar, donde las claves son los nombres de las columnas y 
        los valores son los datos que se insertarán en esas columnas.
        
        Primero, verifica si hay una conexión activa a la base de datos. Si la conexión está activa, crea un cursor,
        que es una estructura de datos que permite ejecutar consultas SQL en la base de datos. 
        Luego, la consulta se crea de manera flexible y adaptada a los datos que se desean insertar. En lugar de tener 
        una consulta SQL estática que inserte datos fijos en la tabla.
        Utiliza los datos para generar una lista de valores y una lista de nombres de columnas.
        
        Después de construir la consulta SQL, la ejecuta utilizando el cursor. Los valores de los datos se pasan como argumentos 
        para completar los marcadores de posición en la consulta. 
        Una vez que se ha ejecutado la consulta, se confirman los cambios en la base de datos mediante el método commit.
        
        
        Si la inserción se realiza correctamente, se imprime un mensaje indicando que los datos se registraron con éxito.
        En caso de que ocurra un error durante el proceso, se imprime un mensaje de error.
       
         """
        # Opción 1
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                columnas = ', '.join(datos.keys())
                valores = ', '.join(['%s'] * len(datos))
                sql = f"INSERT INTO {tabla} ({columnas}) VALUES ({valores})"
                print(f"SQL: {sql}")
                print(f"Datos: {list(datos.values())}")
                cursor.execute(sql, list(datos.values()))
                self.conexion.commit()
                print(f"¡Registro añadido a la tabla {tabla}!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
            finally:
                cursor.close()
    
    def actualizar(self, tabla, datos, condicion):
        """
        La función actualizarRegistro se encarga de actualizar registros en una tabla específica. 
        Recibe varios argumentos: self, que hace referencia a la instancia actual de la clase; 
        tabla, una cadena que especifica la tabla en la que se actualizarán los registros; 
        datos, un diccionario con los nuevos valores para la actualización; 
        y condicion, una cadena que establece la condición que deben cumplir los registros a actualizar.
        
        Primero, se verifica si la conexión a la base de datos está activa. Luego, construye dinámicamente
        la consulta SQL de actualización utilizando los datos proporcionados, especialmente las claves y valores del diccionario datos. 
        Se crea un cursor para ejecutar la consulta SQL, se ejecuta la consulta con los valores proporcionados y se confirman los cambios en la DB.
        Si la actualización se realiza con éxito, se imprime un mensaje indicando que el registro en la tabla especificada ha sido actualizado. 
        Sin embargo, si ocurre algún error durante el proceso, se imprime un mensaje de error que describe la naturaleza del problema.

        """
        # Opción 2
        
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                updates = ', '.join([f"{key} = %s" for key in datos.keys()])
                sql = f"UPDATE {tabla} SET {updates} WHERE {condicion}"
                print(f"SQL: {sql}")  # Para depuración
                print(f"Datos: {list(datos.values())}")  # Para depuración
                cursor.execute(sql, list(datos.values()))
                self.conexion.commit()
                print(f"¡Registro en la tabla {tabla} actualizado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
            finally:
                cursor.close()
    
    
    def buscar(self, tabla, condicion):
        """
        Se utiliza para realizar consultas en una tabla específica de la base de datos. 
        
        Qué hace cada parte del código:

        Definición de la función y parámetros: La función buscar toma tres parámetros: self (una referencia a la instancia actual de la clase), 
        tabla (el nombre de la tabla en la que se realizará la búsqueda) y condicion (la condición que se aplicará a la búsqueda).
        
        Verificación de la conexión: La primera línea dentro de la función verifica si la conexión a la base de datos está activa 
        utilizando el método is_connected() de self.conexion. Esto asegura que la función solo intentará realizar la búsqueda si hay una conexión establecida.
        
        Bloque try-except: Dentro de un bloque try, se intenta realizar la búsqueda en la base de datos. 
        Si ocurre algún error durante este proceso, se manejará en el bloque except, donde se imprimirá un mensaje de error.
        
        Creación y ejecución de la consulta SQL: Se crea una consulta SQL utilizando f-strings para incluir dinámicamente el nombre de la tabla y la condición 
        proporcionados como argumentos. La consulta busca todas las columnas (*) en la tabla tabla donde se cumpla la condición especificada por condicion.
        
        Ejecución de la consulta: La consulta SQL se ejecuta utilizando el método execute() del cursor.
        
        Recuperación de resultados de forma ordenada: Los resultados de la consulta se recuperan y se muestran de manera ordenada.
        Primero, se muestra un encabezado indicando en qué tabla se realizó la búsqueda. Luego, se inicializa un contador para enumerar los resultados. 
        El bucle for itera sobre los resultados obtenidos, y dependiendo de la tabla (medicamentos, proveedores o ubicaciones), se imprime cada resultado
        en un formato específico que incluye un número de índice. Después de cada impresión, se incrementa el contador y finalmente se imprime una línea en blanco para mejorar la legibilidad.
        
        Retorno de resultados: Los resultados se devuelven fuera del bloque try para ser utilizados por el código que llama a la función. 
        Si no se produce ningún error, la función devuelve los resultados de la consulta.
        
        Manejo de errores: Si ocurre algún error durante el proceso de búsqueda, se captura en el bloque except y se imprime un mensaje de error. Esto ayuda a identificar y diagnosticar cualquier problema que pueda surgir durante la ejecución de la consulta.
        """

        # Opcion 3
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                consulta = f"SELECT * FROM {tabla} WHERE {condicion}"
                cursor.execute(consulta)
                resultados = cursor.fetchall()
    
                # Imprimir los resultados de manera formateada
                print(f"\nResultados de la búsqueda en la tabla '{tabla}':\n")
                contador = 1
                for resultado in resultados:
                    if tabla == 'medicamentos':
                        datos ="{0}. Lote: {1} | Nombre del medicamento: {2} | Código del distribuidor: {3} | Cantidad en bodega: {4} | Fecha de llegada: {5} | Precio de venta: {6} | Código de la ubicación {7}"
                        print(datos.format(contador, resultado[0], resultado[1], resultado[2], resultado[3], resultado[4], resultado[5], resultado[6]))
                    elif tabla == 'proveedores':
                        datos = "{0}. Código del proveedor: {1} | Nombre: {2} | Apellido: {3} | Numero de identificación: {4} | Entidad: {5}"
                        print(datos.format(contador, resultado[0], resultado[1], resultado[2], resultado[3], resultado[4]))
                    elif tabla == 'ubicaciones':
                        datos = "{0}. Código de la ubicación: {1} | Nombre: {2} | Telefono: {3}"
                        print(datos.format(contador, resultado[0], resultado[1], resultado[2]))
                    contador += 1
                
                return resultados
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
    
        
    def listar(self, tabla):
        """
        Verificación de Conexión:

        La función primero verifica si hay una conexión activa a la base de datos usando self.conexion.is_connected(). 
        Esto asegura que la función solo intentará realizar la operación si hay una conexión establecida.

        Creación del Cursor:        
        Si la conexión está activa, se crea un cursor con cursor = self.conexion.cursor(). 

        Selección de Columna de Ordenamiento:
        La función selecciona una columna para ordenar los resultados en función de la tabla especificada en el parámetro tabla:
        Para la tabla medicamentos, se usa la columna nombre_del_medicamento.
        Para la tabla proveedores, se usa la columna nombre.
        Para la tabla ubicaciones, se usa la columna nombre.
        Si la tabla no es reconocida, se imprime un mensaje de error y la función termina.

        Construcción y Ejecución de la Consulta SQL:        
        Se construye una consulta SQL para seleccionar todos los registros de la tabla y ordenarlos por la columna especificada: 
        consulta = f"SELECT * FROM {tabla} ORDER BY {orden} ASC".
        La consulta se ejecuta con cursor.execute(consulta) y los resultados se obtienen usando cursor.fetchall(), 
        que devuelve todos los registros obtenidos por la consulta.
        
        Impresión de Resultados:        
        Se imprime un encabezado indicando de qué tabla se están mostrando los resultados: print(f"\nResultados de la tabla '{tabla}':\n").
        Se inicializa un contador para numerar los registros.
        Se itera sobre los resultados usando un bucle for. Dependiendo de la tabla, se formatea e imprime cada registro de manera organizada:
        Para la tabla medicamentos, se imprime el lote, nombre del medicamento, distribuidor, cantidad en bodega, fecha de llegada, precio de venta, código del proveedor y código de ubicaciones.
        Para la tabla proveedores, se imprime el código, nombre, apellido, documento de identidad y entidad.
        Para la tabla ubicaciones, se imprime el código, nombre y teléfono.
        El contador se incrementa con cada registro.

        Manejo de Errores:        
        Si ocurre algún error durante la ejecución de la consulta, se captura con un bloque except y se imprime un mensaje de error con los detalles.
        """
        # Opcion 4
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                
                # Seleccionar la columna de ordenamiento según la tabla
                if tabla == 'medicamentos':
                    orden = 'nombre'
                elif tabla == 'proveedores':
                    orden = 'nombre'
                elif tabla == 'ubicaciones':
                    orden = 'nombre'
                else:
                    print(f"Tabla '{tabla}' no reconocida.")
                    return
    
                consulta = f"SELECT * FROM {tabla} ORDER BY {orden} ASC"
                cursor.execute(consulta)
                resultados = cursor.fetchall()
    
                # Imprimir resultados de manera organizada
                contador = 1
                for resultado in resultados:
                    if tabla == 'medicamentos':
                        datos ="{0}. Lote: {1} | Nombre del medicamento: {2} | Código del distribuidor: {3} | Cantidad en bodega: {4} | Fecha de llegada: {5} | Precio de venta: {6} | Código de la ubicación {7}"
                        print(datos.format(contador, resultado[0], resultado[1], resultado[2], resultado[3], resultado[4], resultado[5], resultado[6]))
                    elif tabla == 'proveedores':
                        datos = "{0}. Código del proveedor: {1} | Nombre: {2} | Apellido: {3} | Numero de identificación: {4} | Entidad: {5}"
                        print(datos.format(contador, resultado[0], resultado[1], resultado[2], resultado[3], resultado[4]))
                    elif tabla == 'ubicaciones':
                        datos = "{0}. Código de la ubicación: {1} | Nombre: {2} | Telefono: {3}"
                        print(datos.format(contador, resultado[0], resultado[1], resultado[2]))
                    contador += 1
                
                return resultados
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))


    def eliminar(self, tabla, condicion):
        """
        Verificación de conexión: La función verifica si hay una conexión establecida antes de intentar ejecutar la eliminación. 
        Esto asegura que no se realice ninguna operación si la conexión no está activa.

        Ejecución de la consulta SQL: Construye dinámicamente una consulta SQL de eliminación utilizando la tabla y la condición proporcionadas. 
        Luego, ejecuta la consulta utilizando el cursor.
        
        Confirmación de la transacción: Después de ejecutar la consulta, se confirma la transacción para aplicar los cambios permanentemente en la base de datos.
        
        Mensaje de confirmación: Si la eliminación se realiza correctamente, se imprime un mensaje indicando que el registro se eliminó de la tabla especificada.
        """
        #Opcion 5
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = f"DELETE FROM {tabla} WHERE {condicion}"
                print(f"SQL: {sql}")
                cursor.execute(sql)
                self.conexion.commit()
                print(f"¡Registro eliminado de la tabla {tabla}!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
            finally:
                cursor.close()