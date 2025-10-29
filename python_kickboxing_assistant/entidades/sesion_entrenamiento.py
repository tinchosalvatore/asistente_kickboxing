# entidades/sesion_entrenamiento.py
from __future__ import annotations
from typing import List, Dict, Any, Optional, TYPE_CHECKING
from .movimiento import Movimiento

from python_kickboxing_assistant.patrones.observer.observable import Observable

if TYPE_CHECKING:
    from .perfil_atleta import PerfilDeLuchador
    from ..patrones.strategy.evaluacion_strategy import EvaluacionStrategy

class SesionDeEntrenamiento(Observable['SesionDeEntrenamiento']):
    """
    Entidad que representa una sesión de entrenamiento.
    También es un Observable que notifica eventos de su ciclo de vida.
    """
    def __init__(self, tipo: str, atleta: 'PerfilDeLuchador', estrategia_evaluacion: 'EvaluacionStrategy'):
        super().__init__()
        self.tipo: str = tipo
        self.atleta: 'PerfilDeLuchador' = atleta
        self.estrategia_evaluacion: 'EvaluacionStrategy' = estrategia_evaluacion
        self.movimientos: List[Movimiento] = []
        self.resultado_evaluacion: Optional[Dict[str, Any]] = None

    def agregar_movimiento(self, movimiento: Movimiento):
        self.movimientos.append(movimiento)

    def get_movimientos(self) -> List[Movimiento]:
        return self.movimientos.copy() # Defensive copy

    def set_resultado_evaluacion(self, resultado: Dict[str, Any]):
        self.resultado_evaluacion = resultado

    def evaluar(self) -> None:
        """
        Evalúa la sesión utilizando la estrategia de evaluación asignada
        y almacena el resultado.
        """
        self.resultado_evaluacion = self.estrategia_evaluacion.evaluar(self)

    def get_resultado_evaluacion(self) -> Optional[Dict[str, Any]]:
        """
        Devuelve el resultado de la evaluación de la sesión.
        """
        return self.resultado_evaluacion

    def finalizar(self):
        """Notifica a los observadores que la sesión ha finalizado, pasando la sesión completa."""
        self.notificar_observadores(self)
