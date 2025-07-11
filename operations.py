import csv
from typing import List, Optional
from models import CarroConId, CompradorConId, Comprador

def leer_todos_los_carros() -> List[CarroConId]:
    carros = []
    try:
        with open('carros.csv', mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for row in lector:
                carros.append(CarroConId(
                    id=int(row['ID']),
                    marca=row['Marca'],
                    modelo=row['Modelo'],
                    precio=int(row['Precio']),
                    cilindrada=int(row['Cilindrada']),
                    potencia=int(row['Potencia']),
                    estado=row['Estado'],
                    eliminado=row['Eliminado']
                ))
    except FileNotFoundError:
        raise FileNotFoundError("Archivo de carros no encontrado")
    return carros

def crear_carro(carro: CarroConId) -> CarroConId:
    carros = leer_todos_los_carros()
    carro.id = max((c.id for c in carros), default=0) + 1
    with open('carros.csv', mode='a', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        if archivo.tell() == 0:
            escritor.writerow(['ID', 'Marca', 'Modelo', 'Precio', 'Cilindrada', 'Potencia', 'Estado', 'Eliminado'])
        escritor.writerow([carro.id, carro.marca, carro.modelo, carro.precio, carro.cilindrada, carro.potencia, carro.estado, carro.eliminado])
    return carro

def leer_carros_no_eliminados() -> List[CarroConId]:
    return [c for c in leer_todos_los_carros() if c.eliminado.lower() == "no"]

def leer_carros_eliminados() -> List[CarroConId]:
    return [c for c in leer_todos_los_carros() if c.eliminado.lower() == "si"]

def leer_carros_no_vendidos() -> List[CarroConId]:
    return [c for c in leer_todos_los_carros() if c.estado.lower() != "vendido"]

def leer_carros_vendidos() -> List[CarroConId]:
    return [c for c in leer_todos_los_carros() if c.estado.lower() == "vendido"]

def actualizar_carro(id_carro: int, carro_actualizado: CarroConId) -> Optional[CarroConId]:
    carros = leer_todos_los_carros()
    actualizado = None
    for i, carro in enumerate(carros):
        if carro.id == id_carro:

            carros[i] = carro_actualizado
            actualizado = carro_actualizado
            break
    if actualizado:

        with open('carros.csv', mode='w', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(['ID', 'Marca', 'Modelo', 'Precio', 'Cilindrada', 'Potencia', 'Estado', 'Eliminado'])
            for c in carros:
                escritor.writerow([c.id, c.marca, c.modelo, c.precio, c.cilindrada, c.potencia, c.estado, c.eliminado])
    return actualizado

def eliminar_carro(id_carro: int) -> Optional[CarroConId]:
    carro = buscar_carro_por_id(id_carro)
    if carro:
        carro.eliminado = "si"
        return actualizar_carro(id_carro, carro)
    return None

def buscar_carro_por_id(id_carro: int) -> Optional[CarroConId]:
    return next((c for c in leer_todos_los_carros() if c.id == id_carro), None)

def buscar_y_modificar_carro_por_modelo(modelo: str, carro_actualizado: CarroConId) -> Optional[CarroConId]:
    for carro in leer_todos_los_carros():
        if carro.modelo.lower() == modelo.lower():
            return actualizar_carro(carro.id, carro_actualizado)
    return None

def leer_todos_los_compradores() -> List[CompradorConId]:
    compradores = []
    try:
        with open('compradores.csv', mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for row in lector:
                compradores.append(CompradorConId(
                    id=int(row['ID']),
                    nombre=row['Nombre'],
                    apellido=row['Apellido'],
                    marca=row['Marca'],
                    modelo=row['Modelo'],
                    saldo_pendiente=row['SaldoPendiente'],
                    placa=row['Placa']
                ))
    except FileNotFoundError:
        raise FileNotFoundError("Archivo de compradores no encontrado")
    return compradores

def crear_comprador(comprador: Comprador) -> CompradorConId:
    nuevo_id = 1
    try:
        with open('compradores.csv', mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            ids = [int(row['ID']) for row in lector]
            if ids:
                nuevo_id = max(ids) + 1
    except FileNotFoundError:
        pass  # Si no existe, se inicia con ID 1

    with open('compradores.csv', mode='a', newline='', encoding='utf-8') as archivo:
        campos = ['ID', 'Nombre', 'Apellido', 'Marca', 'Modelo', 'SaldoPendiente', 'Placa']
        escritor = csv.DictWriter(archivo, fieldnames=campos)

        if archivo.tell() == 0:
            escritor.writeheader()

        escritor.writerow({
            'ID': nuevo_id,
            'Nombre': comprador.nombre,
            'Apellido': comprador.apellido,
            'Marca': comprador.marca,
            'Modelo': comprador.modelo,
            'SaldoPendiente': comprador.saldo_pendiente,
            'Placa': comprador.placa
        })

    return CompradorConId(id=nuevo_id, **comprador.dict())


def actualizar_comprador(id_comprador: int, comprador_actualizado: CompradorConId) -> Optional[CompradorConId]:
    compradores = leer_todos_los_compradores()
    actualizado = None
    for comprador in compradores:
        if comprador.id == id_comprador:
            comprador.nombre = comprador_actualizado.nombre
            comprador.apellido = comprador_actualizado.apellido
            comprador.marca = comprador_actualizado.marca
            comprador.modelo = comprador_actualizado.modelo
            comprador.saldo_pendiente = comprador_actualizado.saldo_pendiente
            comprador.placa = comprador_actualizado.placa
            actualizado = comprador
            break
    if actualizado:
        with open('compradores.csv', mode='w', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(['ID', 'Nombre', 'Apellido', 'Marca', 'Modelo', 'SaldoPendiente', 'Placa'])
            for c in compradores:
                escritor.writerow([
                    c.id, c.nombre, c.apellido, c.marca, c.modelo,
                    c.saldo_pendiente, c.placa,
                ])
    return actualizado