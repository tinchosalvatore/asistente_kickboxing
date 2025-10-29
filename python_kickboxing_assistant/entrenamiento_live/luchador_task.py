import threading
import time
import random
from typing import List

from python_kickboxing_assistant.patrones.observer.observer import Observer
from python_kickboxing_assistant.patrones.factory.movimiento_factory import MovimientoFactory
from python_kickboxing_assistant.constantes import (
    REPERTORIO_COMBINACIONES,
    INICIO_ROUND,
    FIN_ROUND,
)

class LuchadorTask(threading.Thread, Observer[str]):
    """
    Un hilo que simula a un luchador lanzando golpes o combinaciones
    durante un round de sparring.
    Actúa como Observer del TimerTask para saber cuándo empezar/parar.
    """
    def __init__(self, nombre_luchador: str, sesion, intervalo_min_seg: float = 0.5, intervalo_max_seg: float = 1.5):
        threading.Thread.__init__(self, daemon=True)
        self._nombre_luchador = nombre_luchador
        self._sesion = sesion
        self._intervalo_min_seg = intervalo_min_seg
        self._intervalo_max_seg = intervalo_max_seg
        self._detenido = threading.Event()
        self._entrenando = threading.Event() # Controla si el luchador debe "lanzar golpes"

    def run(self) -> None:
        """
        Inicia el ciclo de lanzar golpes hasta que se detiene.
        Solo lanza golpes si está entrenando (durante un round).
        """
        while not self._detenido.is_set():
            self._entrenando.wait() # Espera hasta que se le indique que empiece a entrenar
            if self._detenido.is_set():
                break

            if self._entrenando.is_set(): # Doble chequeo por si se detuvo mientras esperaba
                combinacion_str = random.choice(REPERTORIO_COMBINACIONES)
                print(f"{self._nombre_luchador}: ¡{combinacion_str}!")
                
                # Crear y añadir movimientos a la sesión (para evaluación posterior)
                movimientos_en_combinacion = combinacion_str.split('-')
                for mov_str in movimientos_en_combinacion:
                    try:
                        movimiento = MovimientoFactory.crear_movimiento(mov_str.strip())
                        self._sesion.agregar_movimiento(movimiento)
                    except ValueError as e:
                        print(f"Error al crear movimiento '{mov_str}': {e}")
                
            if self._detenido.wait(random.uniform(self._intervalo_min_seg, self._intervalo_max_seg)):
                break

    def actualizar(self, evento: str) -> None:
        """
        Recibe actualizaciones del TimerTask y controla el estado del luchador.
        """
        if evento == INICIO_ROUND:
            self._entrenando.set() # Habilita al luchador para empezar a lanzar golpes
        elif evento == FIN_ROUND:
            self._entrenando.clear() # Deshabilita al luchador

    def detener(self) -> None:
        """
        Señaliza al hilo que debe detenerse y libera cualquier espera.
        """
        self._detenido.set()
        self._entrenando.set() # Libera el wait() si estaba esperando
