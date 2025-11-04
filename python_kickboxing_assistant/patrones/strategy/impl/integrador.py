"""
Archivo integrador generado automaticamente
Directorio: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/patrones/strategy/impl
Fecha: 2025-11-04 16:21:12
Total de archivos integrados: 6
"""

# ================================================================================
# ARCHIVO 1/6: __init__.py
# Ruta: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/patrones/strategy/impl/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/6: estrategia_comida_ligera.py
# Ruta: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/patrones/strategy/impl/estrategia_comida_ligera.py
# ================================================================================

# patrones/strategy/impl/estrategia_comida_ligera.py
from python_kickboxing_assistant.patrones.strategy.comida_strategy import ComidaStrategy
from python_kickboxing_assistant.entidades.sesion_entrenamiento import SesionDeEntrenamiento
from python_kickboxing_assistant.entidades.nutricion import Comida

class EstrategiaComidaLigera(ComidaStrategy):
    """Estrategia que sugiere una comida ligera para después de entrenamientos de baja intensidad."""

    def sugerir(self, sesion: SesionDeEntrenamiento) -> Comida:
        return Comida(
            nombre="Ensalada de Pollo y Quinoa",
            descripcion="Una opción ligera y rica en proteínas para una recuperación rápida.",
            calorias=400
        )


# ================================================================================
# ARCHIVO 3/6: estrategia_comida_recuperacion.py
# Ruta: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/patrones/strategy/impl/estrategia_comida_recuperacion.py
# ================================================================================

# patrones/strategy/impl/estrategia_comida_recuperacion.py
from python_kickboxing_assistant.patrones.strategy.comida_strategy import ComidaStrategy
from python_kickboxing_assistant.entidades.sesion_entrenamiento import SesionDeEntrenamiento
from python_kickboxing_assistant.entidades.nutricion import Comida

class EstrategiaComidaRecuperacion(ComidaStrategy):
    """Estrategia que sugiere una comida rica en nutrientes para recuperarse de un entrenamiento intenso."""

    def sugerir(self, sesion: SesionDeEntrenamiento) -> Comida:
        return Comida(
            nombre="Salmón a la plancha con batata y brócoli",
            descripcion="Alta en proteínas y carbohidratos complejos para reponer glucógeno y reparar músculo.",
            calorias=750
        )


# ================================================================================
# ARCHIVO 4/6: estrategia_de_calorias.py
# Ruta: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/patrones/strategy/impl/estrategia_de_calorias.py
# ================================================================================

# patrones/strategy/impl/estrategia_de_calorias.py
from typing import Dict, Any
from python_kickboxing_assistant.patrones.strategy.evaluacion_strategy import EvaluacionStrategy
from python_kickboxing_assistant.entidades.sesion_entrenamiento import SesionDeEntrenamiento

class EstrategiaDeCalorias(EvaluacionStrategy):
    """Estrategia para evaluar una sesión contando las calorías totales quemadas."""

    def evaluar(self, sesion: SesionDeEntrenamiento) -> Dict[str, Any]:
        total_calorias = sum(mov.get_calorias() for mov in sesion.get_movimientos())
        return {"tipo": "Calorías", "valor": total_calorias}


# ================================================================================
# ARCHIVO 5/6: estrategia_de_puntuacion.py
# Ruta: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/patrones/strategy/impl/estrategia_de_puntuacion.py
# ================================================================================

# patrones/strategy/impl/estrategia_de_puntuacion.py
from typing import Dict, Any
from python_kickboxing_assistant.patrones.strategy.evaluacion_strategy import EvaluacionStrategy
from python_kickboxing_assistant.entidades.sesion_entrenamiento import SesionDeEntrenamiento

class EstrategiaDePuntuacion(EvaluacionStrategy):
    """Estrategia para evaluar una sesión sumando la potencia de los movimientos."""

    def evaluar(self, sesion: SesionDeEntrenamiento) -> Dict[str, Any]:
        total_puntos = sum(mov.get_potencia() for mov in sesion.get_movimientos())
        return {"tipo": "Puntuación", "valor": total_puntos}


# ================================================================================
# ARCHIVO 6/6: estrategia_salud_descanso.py
# Ruta: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/patrones/strategy/impl/estrategia_salud_descanso.py
# ================================================================================

from python_kickboxing_assistant.patrones.strategy.salud_strategy import SaludStrategy
from python_kickboxing_assistant.entidades.perfil_atleta import PerfilDeLuchador
from typing import Dict, Any

class EstrategiaSaludDescanso(SaludStrategy):
    """
    Estrategia que recomienda descanso obligatorio después de sesiones intensas (ej. Sparring).
    """
    def recomendar(self, perfil: 'PerfilDeLuchador') -> Dict[str, Any]:
        """Actualiza el estado del atleta a 'Descanso Obligatorio'."""
        perfil.set_estado_salud("Descanso Obligatorio")
        return {"nuevo_estado": "Descanso Obligatorio", "motivo": "Sesión intensa."}


