# patrones/strategy/impl/estrategia_de_puntuacion.py
from typing import Dict, Any
from python_kickboxing_assistant.patrones.strategy.evaluacion_strategy import EvaluacionStrategy
from python_kickboxing_assistant.entidades.sesion_entrenamiento import SesionDeEntrenamiento

class EstrategiaDePuntuacion(EvaluacionStrategy):
    """Estrategia para evaluar una sesión sumando la potencia de los movimientos."""

    def evaluar(self, sesion: SesionDeEntrenamiento) -> Dict[str, Any]:
        total_puntos = sum(mov.get_potencia() for mov in sesion.get_movimientos())
        return {"tipo": "Puntuación", "valor": total_puntos}
