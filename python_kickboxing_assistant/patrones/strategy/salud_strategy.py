# patrones/strategy/salud_strategy.py
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Dict, Any

if TYPE_CHECKING:
    from python_kickboxing_assistant.entidades.perfil_atleta import PerfilDeLuchador

class SaludStrategy(ABC):
    """Interfaz para definir estrategias de recomendación de salud."""

    @abstractmethod
    def recomendar(self, perfil: 'PerfilDeLuchador') -> Dict[str, Any]:
        """Genera una recomendación de salud para el atleta."""
        pass
