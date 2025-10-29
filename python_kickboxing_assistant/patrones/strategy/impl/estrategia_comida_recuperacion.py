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
