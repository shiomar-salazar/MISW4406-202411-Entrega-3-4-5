

from modulos.companias.dominio.eventos import companiaCreada
from seedwork.aplicacion.handlers import Handler
from modulos.companias.infraestructura.despachadores import Despachador

class HandlerCompaniaDominio(Handler):

    @staticmethod
    def handle_compania_creada(evento):
        try:
            despachador = Despachador()
            despachador.publicar_evento_rabbit(evento, 'eventos-compania')
        except Exception as e:
            print(f"ERROR AL PUBLICAR {e}")
        