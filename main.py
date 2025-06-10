import tempfile
import shutil
import os

def setup_temp_csv():
    temp_dir = tempfile.gettempdir()

    # Ruta absoluta al directorio actual del archivo
    base_dir = os.path.dirname(__file__)

    # Rutas absolutas de los archivos fuente en tu repositorio
    carros_origen = os.path.join(base_dir, "carros.csv")
    compradores_origen = os.path.join(base_dir, "compradores.csv")

    # Rutas temporales donde trabajará la app
    carros_temp = os.path.join(temp_dir, "carros.csv")
    compradores_temp = os.path.join(temp_dir, "compradores.csv")

    # Copiar solo si no existen en la carpeta temporal
    if not os.path.exists(carros_temp):
        shutil.copy(carros_origen, carros_temp)

    if not os.path.exists(compradores_temp):
        shutil.copy(compradores_origen, compradores_temp)

def get_ruta_carros():
    return os.path.join(tempfile.gettempdir(), "carros.csv")

def get_ruta_compradores():
    return os.path.join(tempfile.gettempdir(), "compradores.csv")

setup_temp_csv()

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
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
    buscar_y_modificar_carro_por_modelo,
    eliminar_carro,
    leer_todos_los_compradores,
    crear_comprador,
    actualizar_comprador
)
from models import CarroConId, CompradorConId, Comprador

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", include_in_schema=False)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# --- Carros ---

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

@app.put("/carro/modelo/{modelo}", response_model=CarroConId)
async def actualizar_carro_por_modelo(modelo: str, carro_actualizado: CarroConId):
    carro = buscar_y_modificar_carro_por_modelo(modelo, carro_actualizado)
    if carro is None:
        raise HTTPException(status_code=404, detail="Carro no encontrado por modelo")
    return carro

# --- Compradores ---

@app.get("/compradores", response_model=List[CompradorConId])
async def obtener_compradores():
    return leer_todos_los_compradores()

@app.post("/comprador", response_model=CompradorConId)
async def crear_nuevo_comprador(comprador: Comprador):
    return crear_comprador(comprador)

@app.put("/comprador/{id_comprador}", response_model=CompradorConId)
async def actualizar_comprador_por_id(id_comprador: int, comprador_actualizado: CompradorConId):
    comprador = actualizar_comprador(id_comprador, comprador_actualizado)
    if comprador is None:
        raise HTTPException(status_code=404, detail="Comprador no encontrado")
    return comprador

@app.get("/comprador/{id_comprador}/editar", include_in_schema=False)
async def formulario_editar_comprador(request: Request, id_comprador: int):
    compradores = leer_todos_los_compradores()
    comprador = next((c for c in compradores if c.id == id_comprador), None)
    if comprador is None:
        raise HTTPException(status_code=404, detail="Comprador no encontrado")
    return templates.TemplateResponse("editar_comprador.html", {"request": request, "comprador": comprador})

