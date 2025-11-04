"""
Archivo integrador generado automaticamente
Directorio: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/entrenamiento_live
Fecha: 2025-11-04 16:21:12
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/entrenamiento_live/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: coach_task.py
# Ruta: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/entrenamiento_live/coach_task.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/4: luchador_task.py
# Ruta: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/entrenamiento_live/luchador_task.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 4/4: timer_task.py
# Ruta: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/entrenamiento_live/timer_task.py
# ================================================================================

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


