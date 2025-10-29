# servicios/servicio_salud.py
from __future__ import annotations
from typing import TYPE_CHECKING

from python_kickboxing_assistant.patrones.observer.observer import Observer
from python_kickboxing_assistant.patrones.strategy.salud_strategy import SaludStrategy
from python_kickboxing_assistant.patrones.strategy.impl.estrategia_salud_descanso import EstrategiaSaludDescanso

if TYPE_CHECKING:
    from python_kickboxing_assistant.entidades.sesion_entrenamiento import SesionDeEntrenamiento

class AnalizadorDeSalud(Observer['SesionDeEntrenamiento']):
    """
    Observer que analiza la salud del atleta después de una sesión.
    Utiliza una SaludStrategy para determinar la recomendación.
    """
    def __init__(self, estrategia: SaludStrategy = EstrategiaSaludDescanso()):
        self._estrategia = estrategia

    def actualizar(self, sesion: 'SesionDeEntrenamiento') -> None:
        """
        Recibe la notificación de que una sesión ha finalizado.
        """
        print(f"[AnalizadorDeSalud] Recibida notificación para la sesión tipo: {sesion.tipo}")
        if sesion.tipo == "Sparring":
            print("[AnalizadorDeSalud] La sesión fue de Sparring. Aplicando estrategia de salud.")
            atleta = sesion.atleta
            resultado = self._estrategia.recomendar(atleta)
            print(f"[AnalizadorDeSalud] Estrategia aplicada. Nuevo estado para {atleta.get_nombre()}: {resultado.get('nuevo_estado')}")
