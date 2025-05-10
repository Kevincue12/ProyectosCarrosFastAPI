from fastapi import FastAPI, HTTPException
from typing import List
from operations import (
    leer_todos_los_carros,
    leer_carros_no_eliminados,
    leer_carros_eliminados,
    leer_carros_no_vendidos,
    leer_carros_vendidos,
    crear_carro,
    actualizar_carro,
    buscar_carro_por_id,
    buscar_carro_por_placa,
    buscar_y_modificar_carro_por_modelo,
    eliminar_carro,
    leer_todos_los_compradores,
    crear_comprador,
    actualizar_comprador
)
from models import CarroConId, CompradorConId

app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de carros y compradores"}

# ----- Carros -----

@app.get("/carros", response_model=List[CarroConId])
async def obtener_todos_los_carros():
    return leer_todos_los_carros()

@app.get("/carros/activos", response_model=List[CarroConId])
async def obtener_carros_no_eliminados():
    return leer_carros_no_eliminados()

@app.get("/carros/eliminados", response_model=List[CarroConId])
async def obtener_carros_eliminados():
    return leer_carros_eliminados()

@app.get("/carros/no_vendidos", response_model=List[CarroConId])
async def obtener_carros_no_vendidos():
    return leer_carros_no_vendidos()

@app.get("/carros/vendidos", response_model=List[CarroConId])
async def obtener_carros_vendidos():
    return leer_carros_vendidos()

@app.post("/carro", response_model=CarroConId)
async def crear_nuevo_carro(carro: CarroConId):
    return crear_carro(carro)

@app.put("/carro/{id_carro}", response_model=CarroConId)
async def actualizar_carro_por_id(id_carro: int, carro_actualizado: CarroConId):
    carro = actualizar_carro(id_carro, carro_actualizado)
    if carro is None:
        raise HTTPException(status_code=404, detail="Carro no encontrado")
    return carro

@app.delete("/carro/{id_carro}", response_model=CarroConId)
async def eliminar_carro_por_id(id_carro: int):
    carro = eliminar_carro(id_carro)
    if carro is None:
        raise HTTPException(status_code=404, detail="Carro no encontrado para eliminar")
    return carro

@app.get("/carro/id/{id_carro}", response_model=CarroConId)
async def buscar_carro_id(id_carro: int):
    carro = buscar_carro_por_id(id_carro)
    if carro is None:
        raise HTTPException(status_code=404, detail="Carro no encontrado")
    return carro

@app.get("/carro/placa/{placa}", response_model=CarroConId)
async def buscar_carro_por_placa_endpoint(placa: str):
    carro = buscar_carro_por_placa(placa)
    if carro is None:
        raise HTTPException(status_code=404, detail="Carro no encontrado por placa")
    return carro

@app.put("/carro/modelo/{modelo}", response_model=CarroConId)
async def actualizar_carro_por_modelo(modelo: str, carro_actualizado: CarroConId):
    carro = buscar_y_modificar_carro_por_modelo(modelo, carro_actualizado)
    if carro is None:
        raise HTTPException(status_code=404, detail="Carro no encontrado por modelo")
    return carro

# ----- Compradores -----

@app.get("/compradores", response_model=List[CompradorConId])
async def obtener_compradores():
    return leer_todos_los_compradores()

@app.post("/comprador", response_model=CompradorConId)
async def crear_nuevo_comprador(comprador: CompradorConId):
    return crear_comprador(comprador)

@app.put("/comprador/{id_comprador}", response_model=CompradorConId)
async def actualizar_comprador_por_id(id_comprador: int, comprador_actualizado: CompradorConId):
    comprador = actualizar_comprador(id_comprador, comprador_actualizado)
    if comprador is None:
        raise HTTPException(status_code=404, detail="Comprador no encontrado")
    return comprador
