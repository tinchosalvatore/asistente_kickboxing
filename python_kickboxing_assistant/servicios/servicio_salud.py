# servicios/servicio_salud.py
from __future__ import annotations
from typing import TYPE_CHECKING

from python_kickboxing_assistant.patrones.observer.observer import Observer

if TYPE_CHECKING:
    from python_kickboxing_assistant.entidades.sesion_entrenamiento import SesionDeEntrenamiento

class AnalizadorDeSalud(Observer['SesionDeEntrenamiento']):
    """
    Observer que analiza la salud del atleta después de una sesión.
    Si la sesión es de Sparring, recomienda un descanso obligatorio.
    """
    def actualizar(self, sesion: 'SesionDeEntrenamiento') -> None:
        """
        Recibe la notificación de que una sesión ha finalizado.
        """
        print(f"[AnalizadorDeSalud] Recibida notificación para la sesión tipo: {sesion.tipo}")
        if sesion.tipo == "Sparring":
            print("[AnalizadorDeSalud] La sesión fue de Sparring. Actualizando estado de salud.")
            atleta = sesion.atleta
            atleta.set_estado_salud("Descanso Obligatorio")
            print(f"[AnalizadorDeSalud] Nuevo estado de salud para {atleta.get_nombre()}: {atleta.get_estado_salud()}")
