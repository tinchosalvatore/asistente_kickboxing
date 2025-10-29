# entrenamiento_live/timer_task.py
import threading
import time
from python_kickboxing_assistant.patrones.observer.observable import Observable
from python_kickboxing_assistant.constantes import (
    DURACION_ROUND_SEGUNDOS,
    DURACION_DESCANSO_SEGUNDOS,
    INICIO_ROUND,
    FIN_ROUND,
    INICIO_DESCANSO,
    FIN_DESCANSO,
)

class TimerTask(threading.Thread, Observable[str]):
    """
    Un hilo que gestiona el tiempo de los rounds y descansos, notificando
    a los observadores sobre cada cambio de estado.
    """
    def __init__(self, duracion_round: int = DURACION_ROUND_SEGUNDOS, duracion_descanso: int = DURACION_DESCANSO_SEGUNDOS):
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._duracion_round = duracion_round
        self._duracion_descanso = duracion_descanso
        self._detenido = threading.Event()

    def run(self) -> None:
        """Inicia el ciclo de round-descanso hasta que se detiene."""
        while not self._detenido.is_set():
            # Inicia el round
            self.notificar_observadores(INICIO_ROUND)
            if self._detenido.wait(self._duracion_round):
                break

            # Finaliza el round e inicia el descanso
            self.notificar_observadores(FIN_ROUND)
            self.notificar_observadores(INICIO_DESCANSO)
            if self._detenido.wait(self._duracion_descanso):
                break
            
            self.notificar_observadores(FIN_DESCANSO)

    def detener(self) -> None:
        """Señaliza al hilo que debe detenerse."""
        self._detenido.set()
