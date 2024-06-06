#BD/cargar_datos.py
from .conexion import DAO  # Importa la clase DAO del archivo de conexión

def cargar_proveedores():
    dao = DAO()  # Crea una instancia de la clase DAO para manejar la conexión

    # Datos de proveedores
    datos_proveedores = [
        (203, 'Gabriel', 'García Arias',1002465, 'Novartis' ),
        (345, 'Laura Elizabeth', 'Duque Marín',1006581, 'Pfizer'),
        (421, 'Isabel', 'Romero Muñoz',4385674, 'Audifarma'),
        (500, 'Juan Camilo', 'Hoyos Diaz',2036745, 'Bayer'),
        (222, 'Adeline', 'Buendia Márquez',6578469,  'Grupo TQ')  
    ]

    # Cargar cada proveedor en la tabla
    for proveedor in datos_proveedores:
        codigo, nombre, apellido, id, entidad = proveedor
        datos = {
            'codigo': codigo,
            'nombre': nombre,
            'apellido': apellido,
            'id': id,
            'entidad': entidad
        }
        dao.ingresar('proveedores', datos)  # Llama al método ingresar de la clase DAO

    dao.cerrar_conexion()  # Cierra la conexión al finalizar
    print("Proveedores cargados exitosamente.")


def cargar_ubicaciones():
    dao = DAO()  # Crea una instancia de la clase DAO para manejar la conexión

    # Datos de ejemplo de ubicaciones
    datos_ubicaciones = [
        (5650, 'Hospital San Vicente', 9856123),
        (1220, 'Hospital Pablo Tobón Uribe', 5478875),
        (9680, 'Hospital Alma Mater de Antioquia', 1254444),
        (3330, 'Clínica del Norte', 6987969),
        (4230, 'Clínica CES', 1325567)
    ]

    # Cargar cada ubicación en la tabla
    for ubicacion in datos_ubicaciones:
        codigo, nombre, telefono = ubicacion
        datos = {
            'codigo': codigo,
            'nombre': nombre,
            'telefono': telefono
        }
        dao.ingresar('ubicaciones', datos)  # Llama al método ingresar de la clase DAO

    dao.cerrar_conexion()  # Cierra la conexión al finalizar
    print("Ubicaciones cargadas exitosamente.")


def cargar_medicamentos():
    dao = DAO()  # Crea una instancia de la clase DAO para manejar la conexión

    # Datos de ejemplo de medicamentos
    datos_medicamentos = [
        ('M001', 'Paracetamol', 203, 200, '2024-05-01', 5.99,5650 ),
        ('M002', 'Ibuprofeno', 345, 50, '2024-06-15', 7.50,1220),
        ('M003', 'Amoxicilina', 421, 80, '2024-04-20', 10.25,9680),
        ('M004', 'Omeprazol', 500, 120, '2024-05-30', 12.75,3330),
        ('M005', 'Paracetamol', 222, 100, '2024-05-30', 12.75,4230)
    ]

    # Cargar cada medicamento en la tabla
    for medicamento in datos_medicamentos:
        lote, nombre, distribuidor, cantidad, fecha, precio, ubicacion = medicamento
        datos = {
            'lote': lote,
            'nombre': nombre,
            'distribuidor': distribuidor,
            'cantidad': cantidad,
            'fecha': fecha,
            'precio': precio,
            'ubicacion': ubicacion
        }
        dao.ingresar('medicamentos', datos)  # Llama al método ingresar de la clase DAO

    dao.cerrar_conexion()  # Cierra la conexión al finalizar
    print("Medicamentos cargados exitosamente.")







