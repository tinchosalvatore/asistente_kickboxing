# patrones/strategy/impl/estrategia_de_calorias.py
from typing import Dict, Any
from python_kickboxing_assistant.patrones.strategy.evaluacion_strategy import EvaluacionStrategy
from python_kickboxing_assistant.entidades.sesion_entrenamiento import SesionDeEntrenamiento

class EstrategiaDeCalorias(EvaluacionStrategy):
    """Estrategia para evaluar una sesión contando las calorías totales quemadas."""

    def evaluar(self, sesion: SesionDeEntrenamiento) -> Dict[str, Any]:
        total_calorias = sum(mov.get_calorias() for mov in sesion.get_movimientos())
        return {"tipo": "Calorías", "valor": total_calorias}
