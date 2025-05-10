import csv
from typing import List, Optional
from models import CarroConId, CompradorConId

def leer_todos_los_carros() -> List[CarroConId]:
    carros = []
    try:
        with open('carros.csv', mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for row in lector:
                carro = CarroConId(
                    id=int(row['ID']),
                    marca=row['Marca'],
                    modelo=row['Modelo'],
                    precio=row['Precio'],
                    cilindrada=int(row['Cilindrada']),
                    potencia=int(row['Potencia']),
                    estado=row['Estado'],
                    eliminado=row['Eliminado']
                )
                carros.append(carro)
    except FileNotFoundError:
        raise FileNotFoundError("Archivo de carros no encontrado")
    except Exception as e:
        raise Exception(f"Error al leer carros: {e}")
    return carros

def crear_carro(carro: CarroConId) -> CarroConId:
    carros = leer_todos_los_carros()
    carro.id = max([c.id for c in carros], default=0) + 1
    carros.append(carro)
    with open('carros.csv', mode='a', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([carro.id, carro.marca, carro.modelo, carro.precio, carro.cilindrada, carro.potencia, carro.estado, carro.eliminado])
    return carro

def leer_carros_no_eliminados() -> List[CarroConId]:
    carros = leer_todos_los_carros()
    return [carro for carro in carros if carro.eliminado.lower() == "no"]

def leer_carros_eliminados() -> List[CarroConId]:
    carros = leer_todos_los_carros()
    return [carro for carro in carros if carro.eliminado.lower() == "si"]

def leer_carros_no_vendidos() -> List[CarroConId]:
    carros = leer_todos_los_carros()
    return [carro for carro in carros if carro.estado.lower() != "vendido"]

def leer_carros_vendidos() -> List[CarroConId]:
    carros = leer_todos_los_carros()
    return [carro for carro in carros if carro.estado.lower() == "vendido"]

def actualizar_carro(id_carro: int, carro_actualizado: CarroConId) -> Optional[CarroConId]:
    carros = leer_todos_los_carros()
    for carro in carros:
        if carro.id == id_carro:
            carro.marca = carro_actualizado.marca
            carro.modelo = carro_actualizado.modelo
            carro.precio = carro_actualizado.precio
            carro.cilindrada = carro_actualizado.cilindrada
            carro.potencia = carro_actualizado.potencia
            carro.estado = carro_actualizado.estado
            carro.eliminado = carro_actualizado.eliminado
            with open('carros.csv', mode='w', newline='', encoding='utf-8') as archivo:
                escritor = csv.writer(archivo)
                escritor.writerow(['ID', 'Marca', 'Modelo', 'Precio', 'Cilindrada', 'Potencia', 'Estado', 'Eliminado'])
                for c in carros:
                    escritor.writerow([c.id, c.marca, c.modelo, c.precio, c.cilindrada, c.potencia, c.estado, c.eliminado])
            return carro
    return None

def eliminar_carro(id_carro: int) -> Optional[CarroConId]:
    carros = leer_todos_los_carros()
    for carro in carros:
        if carro.id == id_carro:
            carro.eliminado = "si"
            with open('carros.csv', mode='w', newline='', encoding='utf-8') as archivo:
                escritor = csv.writer(archivo)
                escritor.writerow(['ID', 'Marca', 'Modelo', 'Precio', 'Cilindrada', 'Potencia', 'Estado', 'Eliminado'])
                for c in carros:
                    escritor.writerow([c.id, c.marca, c.modelo, c.precio, c.cilindrada, c.potencia, c.estado, c.eliminado])
            return carro
    return None

def buscar_carro_por_id(id_carro: int) -> Optional[CarroConId]:
    carros = leer_todos_los_carros()
    for carro in carros:
        if carro.id == id_carro:
            return carro
    return None

def buscar_carro_por_placa(placa: str) -> Optional[CarroConId]:
    compradores = leer_todos_los_compradores()
    for comprador in compradores:
        if comprador.placa.lower() == placa.lower():
            carros = leer_todos_los_carros()
            for carro in carros:
                if carro.modelo.lower() == comprador.modelo.lower() and carro.marca.lower() == comprador.marca.lower():
                    return carro
    return None

def buscar_y_modificar_carro_por_modelo(modelo: str, carro_actualizado: CarroConId) -> Optional[CarroConId]:
    carros = leer_todos_los_carros()
    for carro in carros:
        if carro.modelo.lower() == modelo.lower():
            carro.marca = carro_actualizado.marca
            carro.precio = carro_actualizado.precio
            carro.cilindrada = carro_actualizado.cilindrada
            carro.potencia = carro_actualizado.potencia
            carro.estado = carro_actualizado.estado
            carro.eliminado = carro_actualizado.eliminado
            with open('carros.csv', mode='w', newline='', encoding='utf-8') as archivo:
                escritor = csv.writer(archivo)
                escritor.writerow(['ID', 'Marca', 'Modelo', 'Precio', 'Cilindrada', 'Potencia', 'Estado', 'Eliminado'])
                for c in carros:
                    escritor.writerow([c.id, c.marca, c.modelo, c.precio, c.cilindrada, c.potencia, c.estado, c.eliminado])
            return carro
    return None

def leer_todos_los_compradores() -> List[CompradorConId]:
    compradores = []
    try:
        with open('compradores.csv', mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for row in lector:
                comprador = CompradorConId(
                    id=int(row['ID']),
                    nombre=row['Nombre'],
                    apellido=row['Apellido'],
                    marca=row['Marca'],
                    modelo=row['Modelo'],
                    saldo_pendiente=row['SaldoPendiente'],
                    placa=row['Placa']
                )
                compradores.append(comprador)
    except FileNotFoundError:
        raise FileNotFoundError("Archivo de compradores no encontrado")
    except Exception as e:
        raise Exception(f"Error al leer compradores: {e}")
    return compradores

def crear_comprador(comprador: CompradorConId) -> CompradorConId:
    compradores = leer_todos_los_compradores()
    comprador.id = max([c.id for c in compradores], default=0) + 1
    compradores.append(comprador)
    with open('compradores.csv', mode='a', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([comprador.id, comprador.nombre, comprador.apellido, comprador.marca, comprador.modelo, comprador.saldo_pendiente, comprador.placa])
    return comprador

def actualizar_comprador(id_comprador: int, comprador_actualizado: CompradorConId) -> Optional[CompradorConId]:
    compradores = leer_todos_los_compradores()
    for comprador in compradores:
        if comprador.id == id_comprador:
            comprador.nombre = comprador_actualizado.nombre
            comprador.apellido = comprador_actualizado.apellido
            comprador.marca = comprador_actualizado.marca
            comprador.modelo = comprador_actualizado.modelo
            comprador.saldo_pendiente = comprador_actualizado.saldo_pendiente
            comprador.placa = comprador_actualizado.placa
            with open('compradores.csv', mode='w', newline='', encoding='utf-8') as archivo:
                escritor = csv.writer(archivo)
                escritor.writerow(['ID', 'Nombre', 'Apellido', 'Marca', 'Modelo', 'SaldoPendiente', 'Placa'])
                for c in compradores:
                    escritor.writerow([c.id, c.nombre, c.apellido, c.marca, c.modelo, c.saldo_pendiente, c.placa])
            return comprador
    return None
