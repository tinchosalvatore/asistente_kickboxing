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
