#principal.py
from BD.conexion import*
from archivo import*


def menuPrincipal():
    while True:
        print("==================== MENÚ PRINCIPAL ====================")
        print("1.- Medicamentos")
        print("2.- Proveedores")
        print("3.- Ubicaciones")
        print("4.- Salir")
        print("========================================================")
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion < 1 or opcion > 4:
                print("Opción incorrecta, ingrese nuevamente...")
            else:
                if opcion == 1:
                    menu_Medicamentos()
                elif opcion == 2:
                    menu_Proveedores()
                elif opcion == 3:
                    menu_Ubicaciones()
                elif opcion == 4:
                    print("¡Gracias por usar este sistema!")
                    print("Saliendo del programa...")
                    break
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número del 1 al 4.")

def menu_Medicamentos():
    while True:
        print(" ")
        print("Bienvenido al menú de medicamentos, acá podrá gestionar su información.")
        print(" ")
        print("==================== Menú Medicamentos ====================")
        print("1.- Ingresar un nuevo medicamento")
        print("2.- Actualizar la información de un medicamento")
        print("3.- Buscar un medicamento")
        print("4.- Ver la información de todos los medicamentos almacenados")
        print("5.- Eliminar un medicamento")
        print("6.- Volver al menú principal")
        print(" ")
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion < 1 or opcion > 6:
                print("Opción incorrecta, ingrese nuevamente...")
            elif opcion == 6:
                break
            else:
                ejecutarOpcion_Medicamentos(opcion)
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número del 1 al 6.")

def menu_Proveedores():
    while True:
        print(" ")
        print("Bienvenido al menú de proveedores, acá podrá gestionar su información.")
        print(" ")
        print("==================== Menú Proveedores ====================")
        print("1.- Ingresar un nuevo proveedor")
        print("2.- Actualizar la información de un proveedor")
        print("3.- Buscar un proveedor")
        print("4.- Ver la información de todos los proveedores")
        print("5.- Eliminar un proveedor")
        print("6.- Volver al menú principal")
        print(" ")
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion < 1 or opcion > 6:
                print("Opción incorrecta, ingrese nuevamente...")
            elif opcion == 6:
                break
            else:
                ejecutarOpcion_Proveedores(opcion)
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número del 1 al 6.")

def menu_Ubicaciones():
    while True:
        print(" ")
        print("Bienvenido al menú de ubicaciones, acá podrá gestionar su información.")
        print(" ")
        print("==================== Menú Ubicaciones ====================")
        print("1.- Ingresar una nueva ubicación")
        print("2.- Actualizar la información de una ubicación")
        print("3.- Buscar una ubicación")
        print("4.- Ver la información de todas las ubicaciones")
        print("5.- Eliminar una ubicación")
        print("6.- Volver al menú principal")
        print(" ")
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion < 1 or opcion > 6:
                print("Opción incorrecta, ingrese nuevamente...")
            elif opcion == 6:
                break
            else:
                ejecutarOpcion_Ubicaciones(opcion)
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número del 1 al 6.")

def ejecutarOpcion_Medicamentos(opcion):
    dao = DAO()  # Crear una instancia de la clase DAO

    tabla = "medicamentos"
    if opcion == 1:
        # Opción para ingresar nueva información
        datos = pedirDatosMedicamentos()  # Llama a la función para ingresar datos de medicamentos
        try:
            modificado= dao.ingresar(tabla, datos)  # Llama al método ingresar de la clase DAO
            print("¡Medicamento ingresado correctamente!")
            print(modificado)
        except Exception as e:
            print("Error al ingresar el medicamento:", e)

    elif opcion == 2:
        # Opción para actualizar información
        numero_lote = input("Ingrese el número de lote del medicamento a actualizar: ")
        # Crear la condición de búsqueda basada en el número de lote
        condicion = f"lote = '{numero_lote}'"
        medicamento = dao.buscar(tabla, condicion)  # Buscar el medicamento por número de lote
        try:
            if len(medicamento)!= 0:
                # Si se encontró el medicamento, pedir datos para actualizar
                datos = pedirDatosMedicamentos()
                # Actualizar la ubicación utilizando los datos ingresados
                dao.actualizar(tabla, condicion, datos)
                print("Medicamento actualizado correctamente")
            else:
                print("No se encontró ningún medicamento con ese número de lote.")
        except Exception as e:
            print("Error al intentar actualizar medicamentos:", e)


    elif opcion == 3:
         # Opción para buscar información
         try:
             # Solicitar al usuario el número de lote a buscar
            numero_lote = input("Ingrese el número de lote a buscar: ")
             # Definir la condición de búsqueda usando el número de lote
            condicion = f"lote = '{numero_lote}'"
            dao.buscar(tabla, condicion)  # Llama al método buscar de la clase DAO
         except Exception as e:
             print("Error al buscar medicamentos:", e)
     
    elif opcion == 4:
        # Opción para ver la información
        try:
            dao.listar(tabla)  # Obtener la lista de medicamentos
        except Exception as e:
            print("Error al intentar listar medicamentos:", e)

    elif opcion == 5:
        # Opción para eliminar información
        try:
            medicamentos = dao.listar(tabla)  # Obtener la lista de medicamentos
            if len(medicamentos) > 0:
                numero_lote = input("Ingrese el número de lote del medicamento a eliminar: ")
                # Crear la condición de eliminación basada en el número de lote
                condicion = f"lote = '{numero_lote}'"
                dao.eliminar(tabla, condicion)  # Llama al método eliminar de la clase DAO
                print("Medicamento eliminado correctamente.")
            else:
                print("No se encontraron medicamentos para eliminar.")
        except Exception as e:
            print("Error al intentar eliminar medicamentos:", e)
     

    elif opcion == 6:
        # Opción para volver al menú principal
        menuPrincipal()

    else:
        print("Opción no válida...")


def ejecutarOpcion_Proveedores(opcion):
    dao = DAO()  # Crear una instancia de la clase DAO

    tabla = "proveedores"
    if opcion == 1:
        # Opción para ingresar nueva información
        datos = pedirDatosProveedores()  # Llama a la función para ingresar datos de proveedores
        try:
            modificado= dao.ingresar(tabla, datos)  # Llama al método ingresar de la clase DAO
            print("¡Proveedor ingresado correctamente!")
            print(modificado)
        except Exception as e:
            print("Error al ingresar el proveedor:", e)

    elif opcion == 2:
        # Opción para actualizar información
        try:
            codigo = input("Ingrese el código del proveedor a actualizar: ")
            # Crear la condición de búsqueda basada en el código del proveedor
            condicion = f"codigo = '{codigo}'"
            proveedores = dao.buscar(tabla, condicion)  # Buscar el proveedor por código
            if len(proveedores) > 0:
                # Si se encontró el proveedor, pedir datos para actualizar
                datos = pedirDatosProveedores()
                # Actualizar el proveedor utilizando los datos ingresados
                dao.actualizar(tabla, condicion, datos)
                print("Proveedor actualizado correctamente")
            else:
                print("No se encontró ningún proveedor con ese código.")
        except Exception as e:
            print("Error al intentar actualizar proveedores:", e)
    

    elif opcion == 3:
        # Opción para buscar información
        try:
            codigo = input("Ingrese el código del proveedor a buscar: ")
            # Definir la condición de búsqueda usando el código del proveedor
            condicion = f"codigo = '{codigo}'"
            dao.buscar(tabla, condicion)  # Llama al método buscar de la clase DAO
        except Exception as e:
            print("Error al buscar proveedores:", e)

    elif opcion == 4:
        # Opción para ver la información
        try:
            dao.listar(tabla)  # Obtener la lista de proveedores
        except Exception as e:
            print("Error al intentar listar proveedores:", e)

    elif opcion == 5:
        # Opción para eliminar información
        try:
            proveedores = dao.listar(tabla)  # Obtener la lista de proveedores
            if len(proveedores) > 0:
                codigo = input("Ingrese el código del proveedor a eliminar: ")
                # Crear la condición de eliminación basada en el código del proveedor
                condicion = f"codigo = '{codigo}'"
                dao.eliminar(tabla, condicion)  # Llama al método eliminar de la clase DAO
                print("Proveedor eliminado correctamente.")
            else:
                print("No se encontraron proveedores para eliminar.")
        except Exception as e:
            print("Error al intentar eliminar proveedores:", e)

    elif opcion == 6:
        # Opción para volver al menú principal
        menuPrincipal()

    else:
        print("Opción no válida...")

def ejecutarOpcion_Ubicaciones(opcion):
    dao = DAO()  # Crear una instancia de la clase DAO

    tabla = "ubicaciones"
    if opcion == 1:
        # Opción para ingresar nueva información
        datos = pedirDatosUbicaciones()  # Llama a la función para ingresar datos de ubicaciones
        try:
            modificado= dao.ingresar(tabla, datos)  # Llama al método ingresar de la clase DAO
            print("¡Ubicación ingresada correctamente!")
            print(modificado)
        except Exception as e:
            print("Error al ingresar la ubicación:", e)

    elif opcion == 2:
        # Opción para actualizar información
        try:
            codigo = input("Ingrese el código de la ubicación a actualizar: ")
            # Crear la condición de búsqueda basada en el código de la ubicación
            condicion = f"codigo = '{codigo}'"
            ubicaciones = dao.buscar(tabla, condicion)  # Buscar la ubicación por código
            if len(ubicaciones) > 0:
                # Si se encontró la ubicación, pedir datos para actualizar
                datos = pedirDatosUbicaciones()
                # Actualizar la ubicación utilizando los datos ingresados
                dao.actualizar(tabla, condicion, datos)
                print("Ubicación actualizada correctamente")
            else:
                print("No se encontró ninguna ubicación con ese código.")
        except Exception as e:
            print("Error al intentar actualizar ubicaciones:", e)


    elif opcion == 3:
         # Opción para buscar información
         try:
             # Solicitar al usuario el código de la ubicación a buscar
             codigo = input("Ingrese el código de la ubicación a buscar: ")
             # Definir la condición de búsqueda usando el código de la ubicación
             condicion = f"codigo = '{codigo}'"
             dao.buscar(tabla, condicion)  # Llama al método buscar de la clase DAO
         except Exception as e:
             print("Error al buscar ubicaciones:", e)
     
    elif opcion == 4:
        # Opción para ver la información
        try:
            dao.listar(tabla)  # Obtener la lista de ubicaciones
        except Exception as e:
            print("Error al intentar listar ubicaciones:", e)

    elif opcion == 5:
        # Opción para eliminar información
        try:
            ubicaciones = dao.listar(tabla)  # Obtener la lista de ubicaciones
            if len(ubicaciones) > 0:
                codigo = input("Ingrese el código de la ubicación a eliminar: ")
                # Crear la condición de eliminación basada en el código de la ubicación
                condicion = f"codigo = '{codigo}'"
                dao.eliminar(tabla, condicion)  # Llama al método eliminar de la clase DAO
                print("Ubicación eliminada correctamente.")
            else:
                print("No se encontraron ubicaciones para eliminar.")
        except Exception as e:
            print("Error al intentar eliminar ubicaciones:", e)
     

    elif opcion == 6:
        # Opción para volver al menú principal
        menuPrincipal()

    else:
        print("Opción no válida...")

