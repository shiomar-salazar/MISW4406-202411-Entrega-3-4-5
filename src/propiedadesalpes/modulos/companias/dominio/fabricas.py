""" Fábricas para la creación de objetos del dominio de companias

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos del dominio de companias

"""

from .entidades import Compania
from .reglas import MinimoUnItinerario, RutaValida
from .excepciones import TipoObjetoNoExisteEnDominioVuelosExcepcion
from propiedadesalpes.seedwork.dominio.repositorios import Mapeador, Repositorio
from propiedadesalpes.seedwork.dominio.fabricas import Fabrica
from propiedadesalpes.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass



@dataclass
class FabricaCompania(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            compania: Compania = mapeador.dto_a_entidad(obj)

            #self.validar_regla(MinimoUnItinerario(reserva.itinerarios))
            #[self.validar_regla(RutaValida(ruta)) for itin in reserva.itinerarios for odo in itin.odos for segmento in odo.segmentos for ruta in segmento.legs]
            
            return compania