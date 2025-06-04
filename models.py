from pydantic import BaseModel

class CarroConId(BaseModel):
    id: int
    marca: str
    modelo: str
    precio: int
    cilindrada: int
    potencia: int
    estado: str
    eliminado: str


class Comprador(BaseModel):
    nombre: str
    apellido: str
    marca: str
    modelo: str
    saldo_pendiente: str
    placa: str

class CompradorConId(Comprador):
    id: int

