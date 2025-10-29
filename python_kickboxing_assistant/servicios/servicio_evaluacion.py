from python_kickboxing_assistant.entidades.sesion_entrenamiento import SesionDeEntrenamiento
from python_kickboxing_assistant.patrones.strategy.evaluacion_strategy import EvaluacionStrategy


class ServicioDeEvaluacion:
    """
    Servicio para evaluar una sesión de entrenamiento utilizando una estrategia específica.
    """

    def __init__(self, estrategia: EvaluacionStrategy):
        self._estrategia = estrategia

    def evaluar_sesion(self, sesion: SesionDeEntrenamiento) -> dict:
        """
        Evalúa la sesión utilizando la estrategia configurada.
        """
        return self._estrategia.evaluar(sesion)

    @property
    def estrategia(self) -> EvaluacionStrategy:
        return self._estrategia

    @estrategia.setter
    def estrategia(self, estrategia: EvaluacionStrategy):
        self._estrategia = estrategia
