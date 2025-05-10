from pydantic import BaseModel
from typing import Optional

class CarroConId(BaseModel):
    id: int
    marca: str
    modelo: str
    precio: str
    cilindrada: int
    potencia: int
    estado: str
    eliminado: str

class CompradorConId(BaseModel):
    id: int
    nombre: str
    apellido: str
    marca: str
    modelo: str
    saldo_pendiente: str
    placa: str