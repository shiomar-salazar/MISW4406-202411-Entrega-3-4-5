""" Fábricas para la creación de objetos en la capa de infrastructura del dominio de propiedades

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos en la capa de infraestructura del dominio de propiedades

"""

from dataclasses import dataclass
from seedwork.dominio.fabricas import Fabrica
from seedwork.dominio.repositorios import Repositorio
from modulos.propiedades.dominio.repositorios import RepositorioPropiedades
from seedwork.infraestructura.vistas import Vista
from modulos.propiedades.dominio.entidades import Propiedad
from .repositorios import RepositorioPropiedadesPostgresSQL
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioPropiedades.__class__:
            return RepositorioPropiedadesPostgresSQL()
        else:
            raise ExcepcionFabrica(f"Error fábrica {obj}")
        
@dataclass
class FabricaVista(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Vista:
        if obj == Propiedad:
            return RepositorioPropiedadesPostgresSQL()
        else:
            raise ExcepcionFabrica(f'No existe fábrica para el objeto {obj}')