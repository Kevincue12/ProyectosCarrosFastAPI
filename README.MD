Kevin Cuevas – Ingeniería de Sistemas

Descripción General
Este proyecto es una aplicación FastAPI para gestionar datos de carros y compradores. La API permite realizar operaciones CRUD sobre ambas entidades, utilizando archivos CSV como sistema de almacenamiento.
Además, la API incluye:

Manejo de excepciones HTTP con respuestas personalizadas.

Filtro por estado (vendido/no vendido, eliminado/no eliminado).

Búsqueda por criterios como ID, placa y modelo.

Separación de responsabilidades en módulos.

Requisitos
Modelos

CarroConId

CompradorConId

CRUD

Operaciones completas para carros y compradores.

Persistencia

Datos almacenados en archivos carros.csv y compradores.csv.

Manejo de Excepciones

404 Not Found para registros inexistentes.

500 Internal Server Error con detalles.

Filtrado y Estados

Carros filtrables por estado: vendidos/no vendidos y eliminados/no eliminados.

Los compradores se asocian a carros mediante marca y modelo.

Buscadores

Carro por placa

Carro por modelo

Carro por ID

Trazabilidad

El estado de eliminación se gestiona con un campo eliminado ("sí" o "no").

Mapa de Endpoints
Carros

Método	Endpoint	Descripción
GET	/carros/noeliminados	Lista carros no eliminados
GET	/carros/eliminados	Lista carros eliminados
GET	/carros/novendidos	Lista carros no vendidos
GET	/carros/vendidos	Lista carros vendidos
GET	/carro/placa/{placa}	Busca carro por placa
GET /carro/{id_carro}	Busca carro por ID
POST /carro	Crea un nuevo carro
PUT	/carro/{id_carro}	Actualiza carro por ID
PUT	/carro/modelo/{modelo}	Actualiza carro por modelo
Compradores

Método	Endpoint	Descripción
GET	/compradores	Lista todos los compradores
POST	/comprador	Crea un nuevo comprador
PUT	/comprador/{id_comprador}	Actualiza comprador por ID