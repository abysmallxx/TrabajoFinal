#archivo.py
# Validar la información numérica 

def pedirDatosMedicamentos():
    # Validación del codigo de ublicacion (debe ser numérico de longitud 3)
    while True:
        try:
            codigo = int(input("Ingrese el código de la ubicación (debe tener 4 dígitos): "))
            if 1000 <= codigo <= 9999:
                break  # Salir del bucle si el código es válido
            else:
                print("Número de codigo de ubicacion incorrecto: Debe tener 4 dígitos.")
        except ValueError:
            print("Número de codigo de ubicacion incorrecto: Debe ser un número.")

    while True:
        try:
            lote = input("Ingrese número de lote del medicamento: ")
            break
        except:
            print("Numero de lote invalido")

    # Ingresar otros datos del medicamento
    nombre_med = input("Ingrese el nombre del medicamento: ")
    
    while True:
        try:
            distribuidor = int(input("Ingrese el codigo del proveedor (debe tener 3 digitos): "))
            if 100 <= distribuidor <= 999:
                break  # Salir del bucle si el código es válido
            else:
                print("Número de distribuidor incorrecto: Debe tener 3 dígitos.")
        except ValueError:
            print("Número de distribuidor incorrecto: Debe ser un número.")

    # Validación de la cantidad en bodega
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad en bodega: "))
            if cantidad >= 0:
                break  # Salir del bucle si la cantidad es válida
            else:
                print("La cantidad en bodega no puede ser negativa.")
        except ValueError:
            print("Cantidad incorrecta: Debe ser un número.")

    # Ingreso de la fecha de llegada
    fecha_llegada = input("Ingrese la fecha de llegada en el siguiente formato (YYYY-MM-DD): ")

    # Validación del precio de venta
    while True:
        try:
            precio_venta = float(input("Ingrese el precio de venta: "))
            if precio_venta > 0:
                break  # Salir del bucle si el precio es válido
            else:
                print("El precio de venta debe ser mayor a 0.")
        except ValueError:
            print("Precio incorrecto: Debe ser un número.")

    # Crear el diccionario con los datos del medicamento y devolverla
    medicamento = { 'lote': lote, 'nombre': nombre_med, 'distribuidor': distribuidor, 'cantidad': cantidad, 'fecha': fecha_llegada, 'precio': precio_venta, 'ubicacion': codigo}
    return medicamento

def pedirDatosProveedores():
    # Validación del código (debe ser numérico de longitud 3)
    while True:
        try:
            codigo = int(input("Ingrese código del proveedor (debe tener 3 dígitos): "))
            if 100 <= codigo <= 999:
                break  # Salir del bucle si el código es válido
            else:
                print("Código incorrecto: Debe tener 3 dígitos.")
        except ValueError:
            print("Código incorrecto: Debe ser un número.")

    # Ingreso del nombre
    nombre_pv = input("Ingrese el nombre del proveedor: ")

    # Ingreso del apellido
    apellido_pv = input("Ingrese el apellido del proveedor: ")
    # Ingreso de la entidad
    entidad = input("Ingrese la entidad del proveedor: ")
    while True:
        try:
            id = int(input("Ingrese el documento de identidad del proveedor (debe tener 7 dígitos): "))
            if 1000000 <= id <= 9999999:
                break  # Salir del bucle si el código es válido
            else:
                print("Documento incorrecto: Debe tener 7 dígitos.")
        except ValueError:
            print("Documento incorrecto: Debe ser un número.")
    proveedor = { 'codigo': codigo, 'nombre': nombre_pv, 'apellido': apellido_pv, 'id': id, 'entidad': entidad}
    return proveedor

def pedirDatosUbicaciones():
    # Ingreso del código (alfanumérico)
    while True:
        try:
            postal = input("Ingrese código de la ubicación (debe tener 4 dígitos alfanuméricos): ")
            if len(postal) != 4 or not postal.isalnum():
                raise ValueError("Código incorrecto: Debe tener exactamente 4 dígitos alfanuméricos.")
            else:
                break  # Salir del bucle si el código es válido
        except ValueError as e:
            print(e)

    # Ingreso del nombre de la ubicación
    nombre_ub = input("Ingrese el nombre de la ubicación: ")
    while True:
        try:
            telefono = int(input("Ingrese el telfono de la ubicación (debe tener 7 dígitos): "))
            if 1000000 <= telefono <= 9999999:
                break  # Salir del bucle si el código es válido
            else:
                print("Telefono incorrecto: Debe tener 7 dígitos.")
        except ValueError:
            print("Telefono incorrecto: Debe ser un número.")

    ubicacion = {'codigo': postal, 'nombre': nombre_ub, 'telefono': telefono}
    return ubicacion

