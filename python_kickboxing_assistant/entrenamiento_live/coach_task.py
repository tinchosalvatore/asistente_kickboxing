# entrenamiento_live/coach_task.py
import threading
import time
import random
from typing import List
from python_kickboxing_assistant.patrones.observer.observer import Observer
from python_kickboxing_assistant.patrones.observer.observable import Observable
from python_kickboxing_assistant.entidades.sesion_entrenamiento import SesionDeEntrenamiento
from python_kickboxing_assistant.patrones.factory.movimiento_factory import MovimientoFactory
from python_kickboxing_assistant.constantes import (
    REPERTORIO_COMBINACIONES,
    NUEVA_COMBINACION,
    INICIO_ROUND,
    FIN_ROUND,
    FIN_DESCANSO,
    DURACION_ROUND_SEGUNDOS # Importar para los comentarios del coach
)

class CoachTask(threading.Thread, Observer[str], Observable[str]):
    """
    Un hilo que simula a un coach "cantando" combinaciones de movimientos
    a intervalos regulares y añade los movimientos a la sesión.
    Actúa como Observer del TimerTask para saber cuándo empezar/parar.
    """
    def __init__(self, sesion: SesionDeEntrenamiento, intervalo_segundos: int = 2, es_sparring: bool = False):
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._sesion = sesion
        self._intervalo = intervalo_segundos
        self._detenido = threading.Event()
        self._entrenando = threading.Event()  # Controla si el coach debe "cantar" o comentar
        self._es_sparring = es_sparring
        self._tiempo_inicio_round = 0.0

    def run(self) -> None:
        """
        Inicia el ciclo de cantar combinaciones hasta que se detiene.
        Solo "canta" si la sesión está activa y *no* es un sparring.
        """
        if self._es_sparring:
            # Si es sparring, el coach no "canta" combinaciones con este método.
            # Sus comentarios serán manejados en el método 'actualizar'.
            return

        while not self._detenido.is_set():
            self._entrenando.wait()  # Espera hasta que se le indique que empiece a entrenar
            if self._detenido.is_set():
                break

            if self._entrenando.is_set():  # Doble chequeo por si se detuvo mientras esperaba
                # Elige una combinación al azar y la notifica (internamente)
                combinacion_str = random.choice(REPERTORIO_COMBINACIONES)
                print(f"Coach: ¡{combinacion_str}!")
                self.notificar_observadores(combinacion_str)  # Notifica la combinación cantada
                
                # Crear y añadir movimientos a la sesión
                movimientos_en_combinacion = combinacion_str.split('-')
                for mov_str in movimientos_en_combinacion:
                    try:
                        movimiento = MovimientoFactory.crear_movimiento(mov_str.strip())
                        self._sesion.agregar_movimiento(movimiento)
                    except ValueError as e:
                        print(f"Error al crear movimiento '{mov_str}': {e}")
                
            if self._detenido.wait(self._intervalo):
                break

    def actualizar(self, evento: str) -> None:
        """
        Recibe actualizaciones del TimerTask y controla el estado de entrenamiento.
        """
        if self._es_sparring:
            if evento == INICIO_ROUND:
                self._tiempo_inicio_round = time.time()
                print("Coach: ¡Round de sparring! ¡A controlar la distancia!")
                self._entrenando.set()  # Habilita los comentarios del coach si es necesario
            elif evento == FIN_ROUND:
                print("Coach: ¡Tiempo! ¡Buen trabajo!")
                self._entrenando.clear()
            elif evento == FIN_DESCANSO:
                print("Coach: ¡A por el siguiente! ¡Manos arriba siempre!")
            # Aquí se podrían añadir comentarios cada ciertos segundos del round
            # Pero requeriría un mecanismo de reloj interno en el coach o que el TimerTask notifique más seguido.

        else: # Comportamiento para sesiones que no son sparring (e.g., saco pesado)
            if evento == INICIO_ROUND:
                print("Coach: ¡Empieza el round! ¡A darle al saco!")
                self._entrenando.set()  # Habilita al coach para empezar a "cantar"
            elif evento == FIN_ROUND:
                print("Coach: ¡Fin del round! ¡Descanso!")
                self._entrenando.clear()  # Deshabilita al coach
            elif evento == FIN_DESCANSO:
                print("Coach: ¡Fin del descanso!")

    def detener(self) -> None:
        """
        Señaliza al hilo que debe detenerse y libera cualquier espera.
        """
        self._detenido.set()
        self._entrenando.set()  # Libera el wait() si estaba esperando
