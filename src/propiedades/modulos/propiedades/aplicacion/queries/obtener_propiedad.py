from dataclasses import dataclass
from seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from seedwork.aplicacion.queries import ejecutar_query as query
from modulos.propiedades.dominio.entidades import Propiedad
from modulos.propiedades.aplicacion.dto import PropiedadDTO
from .base import PropiedadQueryBaseHandler


@dataclass
class ObtenerPropiedad(Query):    
    id_propiedad: str

class ObtenerPropiedadHandler(PropiedadQueryBaseHandler):

    FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def handle(self,  query) -> QueryResultado:
        vista = self.fabrica_vista.crear_objeto(Propiedad)
        propiedad = vista.obtener_por_id(query.id_propiedad)
        return QueryResultado(resultado=propiedad)

@query.register(ObtenerPropiedad)
def ejecutar_query_obtener_propiedad(query: ObtenerPropiedad):
    handler = ObtenerPropiedadHandler()
    return handler.handle(query)