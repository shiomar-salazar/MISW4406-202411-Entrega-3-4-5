from dataclasses import dataclass, field
from propiedadesalpes.seedwork.aplicacion.dto import DTO

#@dataclass(frozen=True)
class InformacionGeoespacialDTO(DTO):
    latitud: str
    longitud: str

#@dataclass(frozen=True)
class DatosGreograficosDTO(DTO):
    ciudad: str
    pais: str

#@dataclass(frozen=True)
class DireccionDTO(DTO):
    direccion: str
    datos_geograficos: DatosGreograficosDTO

#@dataclass(frozen=True)
class LocalizacionDTO(DTO):
    direccion: DireccionDTO
    infromacion_geoespacial: InformacionGeoespacialDTO

#@dataclass(frozen=True)
class TipoIndustriaDTO(DTO):
    id_industria: str
    nombre: str
    descripcion: str

#@dataclass(frozen=True)
class DocumentoIdentidadDTO(DTO):
    tipo: str
    numero_identificacion: str
    
#@dataclass(frozen=True)
class CompaniaDTO(DTO):
    id: str
    nombre_compania: str
    representante_legal: str
    email_contacto: str
    telefono_contacto: str
    estado: str
    documento_identidad: DocumentoIdentidadDTO
    tipo_industria: TipoIndustriaDTO
    localizacion: LocalizacionDTO
