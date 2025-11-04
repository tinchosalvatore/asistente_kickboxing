"""
Archivo integrador generado automaticamente
Directorio: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/patrones/strategy
Fecha: 2025-11-04 16:21:12
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/patrones/strategy/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: comida_strategy.py
# Ruta: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/patrones/strategy/comida_strategy.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/4: evaluacion_strategy.py
# Ruta: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/patrones/strategy/evaluacion_strategy.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 4/4: salud_strategy.py
# Ruta: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/patrones/strategy/salud_strategy.py
# ================================================================================

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


