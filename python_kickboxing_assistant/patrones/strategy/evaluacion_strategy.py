# patrones/strategy/evaluacion_strategy.py
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Dict, Any

if TYPE_CHECKING:
    from python_kickboxing_assistant.entidades.sesion_entrenamiento import SesionDeEntrenamiento

class EvaluacionStrategy(ABC):
    """Interfaz para definir estrategias de evaluación de sesiones de entrenamiento."""

    @abstractmethod
    def evaluar(self, sesion: 'SesionDeEntrenamiento') -> Dict[str, Any]:
        """Evalúa una sesión y devuelve un diccionario con los resultados."""
        pass
