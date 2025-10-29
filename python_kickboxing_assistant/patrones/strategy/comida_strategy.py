# patrones/strategy/comida_strategy.py
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from python_kickboxing_assistant.entidades.nutricion import Comida

if TYPE_CHECKING:
    from python_kickboxing_assistant.entidades.sesion_entrenamiento import SesionDeEntrenamiento

class ComidaStrategy(ABC):
    """Interfaz para definir estrategias de sugerencia de comidas post-entrenamiento."""

    @abstractmethod
    def sugerir(self, sesion: 'SesionDeEntrenamiento') -> Comida:
        """Sugiere una comida basada en la sesión de entrenamiento."""
        pass
