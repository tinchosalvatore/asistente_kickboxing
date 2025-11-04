"""
INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO
============================================================================
Directorio raiz: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant
Fecha de generacion: 2025-11-04 16:21:12
Total de archivos integrados: 42
Total de directorios procesados: 11
============================================================================
"""

# ==============================================================================
# TABLA DE CONTENIDOS
# ==============================================================================

# 
# DIRECTORIO: ..
#   0. main_kickboxing.py

# DIRECTORIO: .
#   1. __init__.py
#   2. constantes.py
#
# DIRECTORIO: entidades
#   3. __init__.py
#   4. movimiento.py
#   5. nutricion.py
#   6. perfil_atleta.py
#   7. sesion_entrenamiento.py
#
# DIRECTORIO: entidades/movimientos
#   8. __init__.py
#   9. cross.py
#   10. hook.py
#   11. jab.py
#   12. low_kick.py
#   13. uppercut.py
#
# DIRECTORIO: entrenamiento_live
#   14. __init__.py
#   15. coach_task.py
#   16. luchador_task.py
#   17. timer_task.py
#
# DIRECTORIO: excepciones
#   18. __init__.py
#   19. kickboxing_exception.py
#
# DIRECTORIO: patrones
#   20. __init__.py
#
# DIRECTORIO: patrones/factory
#   21. __init__.py
#   22. movimiento_factory.py
#
# DIRECTORIO: patrones/observer
#   23. __init__.py
#   24. observable.py
#   25. observer.py
#
# DIRECTORIO: patrones/strategy
#   26. __init__.py
#   27. comida_strategy.py
#   28. evaluacion_strategy.py
#   29. salud_strategy.py
#
# DIRECTORIO: patrones/strategy/impl
#   30. __init__.py
#   31. estrategia_comida_ligera.py
#   32. estrategia_comida_recuperacion.py
#   33. estrategia_de_calorias.py
#   34. estrategia_de_puntuacion.py
#   35. estrategia_salud_descanso.py
#
# DIRECTORIO: servicios
#   36. __init__.py
#   37. kickboxing_service_registry.py
#   38. servicio_entrenamiento.py
#   39. servicio_evaluacion.py
#   40. servicio_perfil.py
#   41. servicio_salud.py
#


################################################################################
# DIRECTORIO: ..
################################################################################

# ==============================================================================
# ARCHIVO 0/41: main_kickboxing.py
# Directorio: ..
# Ruta completa: /home/martinsalvatore/repos/python/asistente_kickboxing/main_kickboxing.py
# ==============================================================================


################################################################################
# DIRECTORIO: .
################################################################################

# ==============================================================================
# ARCHIVO 1/41: __init__.py
# Directorio: .
# Ruta completa: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 2/41: constantes.py
# Directorio: .
# Ruta completa: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/constantes.py
# ==============================================================================

# constantes.py
"""
Módulo para almacenar todas las constantes mágicas del sistema.
Esto centraliza la configuración y facilita los ajustes.
"""

# Potencia de Movimientos
POTENCIA_JAB = 10
POTENCIA_CROSS = 20
POTENCIA_LOW_KICK = 35
POTENCIA_HOOK = 25
POTENCIA_UPPERCUT = 30

# Calorías de Movimientos
CALORIAS_JAB = 1.0
CALORIAS_CROSS = 2.0
CALORIAS_LOW_KICK = 5.0
CALORIAS_HOOK = 3.0
CALORIAS_UPPERCUT = 3.5

# Tiempos de Entrenamiento
DURACION_ROUND_SEGUNDOS = 10
DURACION_DESCANSO_SEGUNDOS = 5
NUMERO_DE_ASALTOS = 2

# Nombres de Movimientos
JAB = "Jab"
CROSS = "Cross"
LOW_KICK = "LowKick"
HOOK = "Hook"
UPPERCUT = "Uppercut"

# Eventos de Observer
INICIO_ROUND = "INICIO_ROUND"
FIN_ROUND = "FIN_ROUND"
INICIO_DESCANSO = "INICIO_DESCANSO"
FIN_DESCANSO = "FIN_DESCANSO"
NUEVA_COMBINACION = "NUEVA_COMBINACION"
FIN_SESION = "FIN_SESION"

# Combinaciones de Movimientos
REPERTORIO_COMBINACIONES = [
    "Jab-Cross",
    "Jab-Jab-LowKick",
    "Cross-Jab-LowKick",
]



################################################################################
# DIRECTORIO: entidades
################################################################################

# ==============================================================================
# ARCHIVO 3/41: __init__.py
# Directorio: entidades
# Ruta completa: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/entidades/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 4/41: movimiento.py
# Directorio: entidades
# Ruta completa: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/entidades/movimiento.py
# ==============================================================================

# entidades/movimiento.py
from abc import ABC, abstractmethod

class Movimiento(ABC):
    """
    Interfaz que representa un movimiento de kickboxing.
    """
    def __init__(self, nombre: str, potencia: int, calorias: float):
        self._nombre = nombre
        self._potencia = potencia
        self._calorias = calorias

    def get_nombre(self) -> str:
        return self._nombre

    def get_potencia(self) -> int:
        return self._potencia

    def get_calorias(self) -> float:
        return self._calorias

    @abstractmethod
    def es_combinacion(self) -> bool:
        """Devuelve True si el movimiento es una combinación de otros."""
        pass


# ==============================================================================
# ARCHIVO 5/41: nutricion.py
# Directorio: entidades
# Ruta completa: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/entidades/nutricion.py
# ==============================================================================

# entidades/nutricion.py

class Comida:
    """
    Entidad que representa una sugerencia de comida.
    """
    def __init__(self, nombre: str, descripcion: str, calorias: int):
        self.nombre = nombre
        self.descripcion = descripcion
        self.calorias = calorias

    def get_nombre(self) -> str:
        return self.nombre


# ==============================================================================
# ARCHIVO 6/41: perfil_atleta.py
# Directorio: entidades
# Ruta completa: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/entidades/perfil_atleta.py
# ==============================================================================

# entidades/perfil_atleta.py
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .sesion_entrenamiento import SesionDeEntrenamiento

class PerfilDeLuchador:
    """
    Entidad que representa el perfil de un atleta.
    Contiene datos demográficos, de salud y el historial de entrenamiento.
    Esta clase solo contiene datos, la lógica de negocio está en los servicios.
    """
    def __init__(self, nombre: str, peso: float, altura: float):
        if peso <= 0:
            raise ValueError("El peso debe ser un número positivo.")
        if altura <= 0:
            raise ValueError("La altura debe ser un número positivo.")

        self.nombre: str = nombre
        self.peso: float = peso
        self.altura: float = altura
        self.estado_salud: str = "Óptimo"
        self.sesiones: List['SesionDeEntrenamiento'] = []

    def set_nombre(self, nombre: str):
        self.nombre = nombre

    def set_peso(self, peso: float):
        if peso <= 0:
            raise ValueError("El peso debe ser un número positivo.")
        self.peso = peso

    def set_altura(self, altura: float):
        if altura <= 0:
            raise ValueError("La altura debe ser un número positivo.")
        self.altura = altura

    def get_nombre(self) -> str:
        return self.nombre

    def get_estado_salud(self) -> str:
        return self.estado_salud

    def set_estado_salud(self, estado: str):
        self.estado_salud = estado

    def agregar_sesion(self, sesion: 'SesionDeEntrenamiento'):
        self.sesiones.append(sesion)


# ==============================================================================
# ARCHIVO 7/41: sesion_entrenamiento.py
# Directorio: entidades
# Ruta completa: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/entidades/sesion_entrenamiento.py
# ==============================================================================

# entidades/sesion_entrenamiento.py
from __future__ import annotations
from typing import List, Dict, Any, Optional, TYPE_CHECKING
from .movimiento import Movimiento

from python_kickboxing_assistant.patrones.observer.observable import Observable

if TYPE_CHECKING:
    from .perfil_atleta import PerfilDeLuchador
    from ..patrones.strategy.evaluacion_strategy import EvaluacionStrategy

class SesionDeEntrenamiento(Observable['SesionDeEntrenamiento']):
    """
    Entidad que representa una sesión de entrenamiento.
    También es un Observable que notifica eventos de su ciclo de vida.
    """
    def __init__(self, tipo: str, atleta: 'PerfilDeLuchador', estrategia_evaluacion: 'EvaluacionStrategy'):
        super().__init__()
        self.tipo: str = tipo
        self.atleta: 'PerfilDeLuchador' = atleta
        self.estrategia_evaluacion: 'EvaluacionStrategy' = estrategia_evaluacion
        self.movimientos: List[Movimiento] = []
        self.resultado_evaluacion: Optional[Dict[str, Any]] = None

    def agregar_movimiento(self, movimiento: Movimiento):
        self.movimientos.append(movimiento)

    def get_movimientos(self) -> List[Movimiento]:
        return self.movimientos.copy() # Defensive copy

    def set_resultado_evaluacion(self, resultado: Dict[str, Any]):
        self.resultado_evaluacion = resultado

    def evaluar(self) -> None:
        """
        Evalúa la sesión utilizando la estrategia de evaluación asignada
        y almacena el resultado.
        """
        self.resultado_evaluacion = self.estrategia_evaluacion.evaluar(self)

    def get_resultado_evaluacion(self) -> Optional[Dict[str, Any]]:
        """
        Devuelve el resultado de la evaluación de la sesión.
        """
        return self.resultado_evaluacion

    def finalizar(self):
        """Notifica a los observadores que la sesión ha finalizado, pasando la sesión completa."""
        self.notificar_observadores(self)



################################################################################
# DIRECTORIO: entidades/movimientos
################################################################################

# ==============================================================================
# ARCHIVO 8/41: __init__.py
# Directorio: entidades/movimientos
# Ruta completa: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/entidades/movimientos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 9/41: cross.py
# Directorio: entidades/movimientos
# Ruta completa: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/entidades/movimientos/cross.py
# ==============================================================================

# entidades/movimientos/cross.py
from python_kickboxing_assistant.entidades.movimiento import Movimiento
from python_kickboxing_assistant.constantes import (
    CROSS,
    POTENCIA_CROSS,
    CALORIAS_CROSS,
)

class Cross(Movimiento):
    """Representa el golpe de Cross."""
    def __init__(self):
        super().__init__(nombre=CROSS, potencia=POTENCIA_CROSS, calorias=CALORIAS_CROSS)

    def es_combinacion(self) -> bool:
        return False


# ==============================================================================
# ARCHIVO 10/41: hook.py
# Directorio: entidades/movimientos
# Ruta completa: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/entidades/movimientos/hook.py
# ==============================================================================

# entidades/movimientos/hook.py
from python_kickboxing_assistant.entidades.movimiento import Movimiento
from python_kickboxing_assistant.constantes import (
    HOOK,
    POTENCIA_HOOK,
    CALORIAS_HOOK,
)

class Hook(Movimiento):
    """Representa el golpe de Hook (gancho)."""
    def __init__(self):
        super().__init__(nombre=HOOK, potencia=POTENCIA_HOOK, calorias=CALORIAS_HOOK)

    def es_combinacion(self) -> bool:
        return False


# ==============================================================================
# ARCHIVO 11/41: jab.py
# Directorio: entidades/movimientos
# Ruta completa: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/entidades/movimientos/jab.py
# ==============================================================================

# entidades/movimientos/jab.py
from python_kickboxing_assistant.entidades.movimiento import Movimiento
from python_kickboxing_assistant.constantes import (
    JAB,
    POTENCIA_JAB,
    CALORIAS_JAB,
)

class Jab(Movimiento):
    """Representa el golpe de Jab."""
    def __init__(self):
        super().__init__(nombre=JAB, potencia=POTENCIA_JAB, calorias=CALORIAS_JAB)

    def es_combinacion(self) -> bool:
        return False


# ==============================================================================
# ARCHIVO 12/41: low_kick.py
# Directorio: entidades/movimientos
# Ruta completa: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/entidades/movimientos/low_kick.py
# ==============================================================================

# entidades/movimientos/low_kick.py
from python_kickboxing_assistant.entidades.movimiento import Movimiento
from python_kickboxing_assistant.constantes import (
    LOW_KICK,
    POTENCIA_LOW_KICK,
    CALORIAS_LOW_KICK,
)

class LowKick(Movimiento):
    """Representa la patada baja o Low Kick."""
    def __init__(self):
        super().__init__(nombre=LOW_KICK, potencia=POTENCIA_LOW_KICK, calorias=CALORIAS_LOW_KICK)

    def es_combinacion(self) -> bool:
        return False


# ==============================================================================
# ARCHIVO 13/41: uppercut.py
# Directorio: entidades/movimientos
# Ruta completa: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/entidades/movimientos/uppercut.py
# ==============================================================================

# entidades/movimientos/uppercut.py
from python_kickboxing_assistant.entidades.movimiento import Movimiento
from python_kickboxing_assistant.constantes import (
    UPPERCUT,
    POTENCIA_UPPERCUT,
    CALORIAS_UPPERCUT,
)

class Uppercut(Movimiento):
    """Representa el golpe de Uppercut."""
    def __init__(self):
        super().__init__(nombre=UPPERCUT, potencia=POTENCIA_UPPERCUT, calorias=CALORIAS_UPPERCUT)

    def es_combinacion(self) -> bool:
        return False



################################################################################
# DIRECTORIO: entrenamiento_live
################################################################################

# ==============================================================================
# ARCHIVO 14/41: __init__.py
# Directorio: entrenamiento_live
# Ruta completa: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/entrenamiento_live/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 15/41: coach_task.py
# Directorio: entrenamiento_live
# Ruta completa: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/entrenamiento_live/coach_task.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 16/41: luchador_task.py
# Directorio: entrenamiento_live
# Ruta completa: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/entrenamiento_live/luchador_task.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 17/41: timer_task.py
# Directorio: entrenamiento_live
# Ruta completa: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/entrenamiento_live/timer_task.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: excepciones
################################################################################

# ==============================================================================
# ARCHIVO 18/41: __init__.py
# Directorio: excepciones
# Ruta completa: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/excepciones/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 19/41: kickboxing_exception.py
# Directorio: excepciones
# Ruta completa: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/excepciones/kickboxing_exception.py
# ==============================================================================

# excepciones/kickboxing_exception.py

class KickboxingException(Exception):
    """Clase base para todas las excepciones personalizadas del sistema."""
    pass

class PersistenciaException(KickboxingException):
    """Lanzada cuando ocurre un error durante la serialización o deserialización del perfil."""
    pass

class AtletaNoAptoException(KickboxingException):
    """Lanzada cuando un atleta intenta entrenar pero su estado de salud no es 'Óptimo'."""
    pass



################################################################################
# DIRECTORIO: patrones
################################################################################

# ==============================================================================
# ARCHIVO 20/41: __init__.py
# Directorio: patrones
# Ruta completa: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/patrones/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: patrones/factory
################################################################################

# ==============================================================================
# ARCHIVO 21/41: __init__.py
# Directorio: patrones/factory
# Ruta completa: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/patrones/factory/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 22/41: movimiento_factory.py
# Directorio: patrones/factory
# Ruta completa: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/patrones/factory/movimiento_factory.py
# ==============================================================================

# patrones/factory/movimiento_factory.py
from typing import Type
from python_kickboxing_assistant.entidades.movimiento import Movimiento
from python_kickboxing_assistant.entidades.movimientos.jab import Jab
from python_kickboxing_assistant.entidades.movimientos.cross import Cross
from python_kickboxing_assistant.entidades.movimientos.low_kick import LowKick
from python_kickboxing_assistant.entidades.movimientos.hook import Hook
from python_kickboxing_assistant.entidades.movimientos.uppercut import Uppercut
from python_kickboxing_assistant.constantes import JAB, CROSS, LOW_KICK, HOOK, UPPERCUT

class MovimientoFactory:
    """
    Implementación del patrón Factory Method para crear movimientos.
    Centraliza la lógica de instanciación para desacoplar el cliente.
    """
    _constructores: dict[str, Type[Movimiento]] = {
        JAB: Jab,
        CROSS: Cross,
        LOW_KICK: LowKick,
        HOOK: Hook,
        UPPERCUT: Uppercut,
    }

    @staticmethod
    def crear_movimiento(tipo: str) -> Movimiento:
        """
        Crea una instancia de un movimiento basado en su tipo.

        Args:
            tipo: El nombre del movimiento a crear (e.g., "Jab").

        Returns:
            Una instancia de la clase de movimiento correspondiente.

        Raises:
            ValueError: Si el tipo de movimiento es desconocido.
        """
        constructor = MovimientoFactory._constructores.get(tipo)
        if not constructor:
            raise ValueError(f"Movimiento desconocido: {tipo}")
        return constructor()



################################################################################
# DIRECTORIO: patrones/observer
################################################################################

# ==============================================================================
# ARCHIVO 23/41: __init__.py
# Directorio: patrones/observer
# Ruta completa: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/patrones/observer/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 24/41: observable.py
# Directorio: patrones/observer
# Ruta completa: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/patrones/observer/observable.py
# ==============================================================================

# patrones/observer/observable.py
from typing import Generic, List, TypeVar
from .observer import Observer

T = TypeVar('T')

class Observable(Generic[T]):
    """
    Clase base para el patrón Observer. Gestiona una lista de observadores
    y notifica los cambios.
    """
    def __init__(self):
        self._observers: List[Observer[T]] = []

    def agregar_observador(self, observer: Observer[T]) -> None:
        """Añade un observador a la lista."""
        if observer not in self._observers:
            self._observers.append(observer)

    def quitar_observador(self, observer: Observer[T]) -> None:
        """Elimina un observador de la lista."""
        self._observers.remove(observer)

    def notificar_observadores(self, data: T) -> None:
        """Envía datos a todos los observadores suscritos."""
        for observer in self._observers:
            observer.actualizar(data)


# ==============================================================================
# ARCHIVO 25/41: observer.py
# Directorio: patrones/observer
# Ruta completa: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/patrones/observer/observer.py
# ==============================================================================

# patrones/observer/observer.py
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')

class Observer(Generic[T], ABC):
    """Interfaz para el patrón Observer. Define el método de actualización."""

    @abstractmethod
    def actualizar(self, data: T) -> None:
        """Recibe la actualización desde el observable."""
        pass



################################################################################
# DIRECTORIO: patrones/strategy
################################################################################

# ==============================================================================
# ARCHIVO 26/41: __init__.py
# Directorio: patrones/strategy
# Ruta completa: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/patrones/strategy/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 27/41: comida_strategy.py
# Directorio: patrones/strategy
# Ruta completa: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/patrones/strategy/comida_strategy.py
# ==============================================================================

# patrones/strategy/comida_strategy.py
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from python_kickboxing_assistant.entidades.nutricion import Comida

if TYPE_CHECKING:
    from python_kickboxing_assistant.entidades.sesion_entrenamiento import SesionDeEntrenamiento

class ComidaStrategy(ABC):
    """Interfaz para definir estrategias de sugerencia de comidas post-entrenamiento."""

    @abstractmethod
    def sugerir(self, sesion: 'SesionDeEntrenamiento') -> Comida:
        """Sugiere una comida basada en la sesión de entrenamiento."""
        pass


# ==============================================================================
# ARCHIVO 28/41: evaluacion_strategy.py
# Directorio: patrones/strategy
# Ruta completa: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/patrones/strategy/evaluacion_strategy.py
# ==============================================================================

# patrones/strategy/evaluacion_strategy.py
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Dict, Any

if TYPE_CHECKING:
    from python_kickboxing_assistant.entidades.sesion_entrenamiento import SesionDeEntrenamiento

class EvaluacionStrategy(ABC):
    """Interfaz para definir estrategias de evaluación de sesiones de entrenamiento."""

    @abstractmethod
    def evaluar(self, sesion: 'SesionDeEntrenamiento') -> Dict[str, Any]:
        """Evalúa una sesión y devuelve un diccionario con los resultados."""
        pass


# ==============================================================================
# ARCHIVO 29/41: salud_strategy.py
# Directorio: patrones/strategy
# Ruta completa: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/patrones/strategy/salud_strategy.py
# ==============================================================================

# patrones/strategy/salud_strategy.py
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Dict, Any

if TYPE_CHECKING:
    from python_kickboxing_assistant.entidades.perfil_atleta import PerfilDeLuchador

class SaludStrategy(ABC):
    """Interfaz para definir estrategias de recomendación de salud."""

    @abstractmethod
    def recomendar(self, perfil: 'PerfilDeLuchador') -> Dict[str, Any]:
        """Genera una recomendación de salud para el atleta."""
        pass



################################################################################
# DIRECTORIO: patrones/strategy/impl
################################################################################

# ==============================================================================
# ARCHIVO 30/41: __init__.py
# Directorio: patrones/strategy/impl
# Ruta completa: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/patrones/strategy/impl/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 31/41: estrategia_comida_ligera.py
# Directorio: patrones/strategy/impl
# Ruta completa: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/patrones/strategy/impl/estrategia_comida_ligera.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 32/41: estrategia_comida_recuperacion.py
# Directorio: patrones/strategy/impl
# Ruta completa: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/patrones/strategy/impl/estrategia_comida_recuperacion.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 33/41: estrategia_de_calorias.py
# Directorio: patrones/strategy/impl
# Ruta completa: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/patrones/strategy/impl/estrategia_de_calorias.py
# ==============================================================================

# patrones/strategy/impl/estrategia_de_calorias.py
from typing import Dict, Any
from python_kickboxing_assistant.patrones.strategy.evaluacion_strategy import EvaluacionStrategy
from python_kickboxing_assistant.entidades.sesion_entrenamiento import SesionDeEntrenamiento

class EstrategiaDeCalorias(EvaluacionStrategy):
    """Estrategia para evaluar una sesión contando las calorías totales quemadas."""

    def evaluar(self, sesion: SesionDeEntrenamiento) -> Dict[str, Any]:
        total_calorias = sum(mov.get_calorias() for mov in sesion.get_movimientos())
        return {"tipo": "Calorías", "valor": total_calorias}


# ==============================================================================
# ARCHIVO 34/41: estrategia_de_puntuacion.py
# Directorio: patrones/strategy/impl
# Ruta completa: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/patrones/strategy/impl/estrategia_de_puntuacion.py
# ==============================================================================

# patrones/strategy/impl/estrategia_de_puntuacion.py
from typing import Dict, Any
from python_kickboxing_assistant.patrones.strategy.evaluacion_strategy import EvaluacionStrategy
from python_kickboxing_assistant.entidades.sesion_entrenamiento import SesionDeEntrenamiento

class EstrategiaDePuntuacion(EvaluacionStrategy):
    """Estrategia para evaluar una sesión sumando la potencia de los movimientos."""

    def evaluar(self, sesion: SesionDeEntrenamiento) -> Dict[str, Any]:
        total_puntos = sum(mov.get_potencia() for mov in sesion.get_movimientos())
        return {"tipo": "Puntuación", "valor": total_puntos}


# ==============================================================================
# ARCHIVO 35/41: estrategia_salud_descanso.py
# Directorio: patrones/strategy/impl
# Ruta completa: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/patrones/strategy/impl/estrategia_salud_descanso.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: servicios
################################################################################

# ==============================================================================
# ARCHIVO 36/41: __init__.py
# Directorio: servicios
# Ruta completa: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/servicios/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 37/41: kickboxing_service_registry.py
# Directorio: servicios
# Ruta completa: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/servicios/kickboxing_service_registry.py
# ==============================================================================

# servicios/kickboxing_service_registry.py
from __future__ import annotations
from threading import Lock
from typing import Callable, Any

from python_kickboxing_assistant.entidades.movimiento import Movimiento
from python_kickboxing_assistant.entidades.movimientos.jab import Jab
from python_kickboxing_assistant.entidades.movimientos.cross import Cross
from python_kickboxing_assistant.entidades.movimientos.low_kick import LowKick
from python_kickboxing_assistant.entidades.perfil_atleta import PerfilDeLuchador

class KickboxingServiceRegistry:
    """
    Implementa los patrones Singleton y Registry.
    - Singleton: Garantiza una única instancia para toda la app.
    - Registry: Permite el despacho polimórfico para operaciones sobre movimientos.
    """
    _instance: KickboxingServiceRegistry | None = None
    _lock = Lock()

    def __new__(cls) -> KickboxingServiceRegistry:
        if cls._instance is None:
            with cls._lock: # Thread-safe
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._inicializar()
        return cls._instance

    def _inicializar(self) -> None:
        """Inicializa los servicios, el perfil y los registros."""
        # Perfil de atleta único gestionado por el Singleton
        self._perfil_atleta = PerfilDeLuchador(nombre="Rocky Balboa", peso=80.5, altura=180)

        # Implementación del patrón Registry para mostrar movimientos
        self._manejadores_display: dict[type[Movimiento], Callable[[Movimiento], None]] = {
            Jab: self._display_jab,
            Cross: self._display_cross,
            LowKick: self._display_low_kick,
        }

    @classmethod
    def get_instance(cls) -> KickboxingServiceRegistry:
        """Punto de acceso público para obtener la instancia del Singleton."""
        return cls()

    def get_perfil(self) -> PerfilDeLuchador:
        """Devuelve la instancia única del perfil del atleta."""
        return self._perfil_atleta

    # --- Métodos del Registry ---

    def mostrar_movimiento(self, movimiento: Movimiento) -> None:
        """Usa el registro para encontrar y ejecutar el handler de display correcto."""
        handler = self._manejadores_display.get(type(movimiento), self._display_generico)
        handler(movimiento)

    def _display_jab(self, mov: Movimiento) -> None:
        print(f"-> Jab rápido! Potencia: {mov.get_potencia()}")

    def _display_cross(self, mov: Movimiento) -> None:
        print(f"--> Cross potente! Potencia: {mov.get_potencia()}")

    def _display_low_kick(self, mov: Movimiento) -> None:
        print(f"==> Low Kick demoledor! Potencia: {mov.get_potencia()}")

    def _display_generico(self, mov: Movimiento) -> None:
        print(f"Movimiento genérico: {mov.get_nombre()}")


# ==============================================================================
# ARCHIVO 38/41: servicio_entrenamiento.py
# Directorio: servicios
# Ruta completa: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/servicios/servicio_entrenamiento.py
# ==============================================================================

from typing import Type
import time
from python_kickboxing_assistant.constantes import DURACION_ROUND_SEGUNDOS, DURACION_DESCANSO_SEGUNDOS, NUMERO_DE_ASALTOS
from python_kickboxing_assistant.entidades.sesion_entrenamiento import SesionDeEntrenamiento
from python_kickboxing_assistant.entidades.perfil_atleta import PerfilDeLuchador
from python_kickboxing_assistant.patrones.strategy.evaluacion_strategy import EvaluacionStrategy
from python_kickboxing_assistant.patrones.strategy.comida_strategy import ComidaStrategy
from python_kickboxing_assistant.entrenamiento_live.timer_task import TimerTask
from python_kickboxing_assistant.entrenamiento_live.coach_task import CoachTask
from python_kickboxing_assistant.entrenamiento_live.luchador_task import LuchadorTask
from python_kickboxing_assistant.patrones.strategy.impl.estrategia_comida_recuperacion import EstrategiaComidaRecuperacion
from python_kickboxing_assistant.patrones.strategy.impl.estrategia_comida_ligera import EstrategiaComidaLigera
from python_kickboxing_assistant.servicios.servicio_salud import AnalizadorDeSalud
from python_kickboxing_assistant.excepciones.kickboxing_exception import AtletaNoAptoException


class ServicioEntrenamiento:
    """
    Servicio para gestionar las sesiones de entrenamiento.
    """

    def iniciar_sesion(self, tipo: str, atleta: PerfilDeLuchador,
                         estrategia_evaluacion: EvaluacionStrategy) -> SesionDeEntrenamiento:
        """
        Inicia una nueva sesión de entrenamiento.
        Verifica la aptitud del atleta y suscribe observadores relevantes.
        """
        # Tarea 3.2: Usar la excepción AtletaNoAptoException
        if atleta.get_estado_salud() != "Óptimo":
            raise AtletaNoAptoException(f"El atleta {atleta.get_nombre()} no está 'Óptimo'. Estado actual: {atleta.get_estado_salud()}")

        sesion = SesionDeEntrenamiento(tipo, atleta, estrategia_evaluacion)

        # Tarea 1.2: Suscribir el observador de salud para sesiones de Sparring
        if sesion.tipo == "Sparring":
            analizador = AnalizadorDeSalud()
            sesion.agregar_observador(analizador)
            print("[ServicioEntrenamiento] AnalizadorDeSalud suscrito a la sesión de Sparring.")

        return sesion

    def ejecutar_sesion_en_vivo(self, sesion: SesionDeEntrenamiento):
        """
        Ejecuta una sesión de entrenamiento en vivo con un Timer y un Coach.
        La duración total, de los rounds y descansos se obtiene desde el fichero de constantes.
        """
        duracion_total_segundos = NUMERO_DE_ASALTOS * (DURACION_ROUND_SEGUNDOS + DURACION_DESCANSO_SEGUNDOS)
        print(f"Iniciando sesión de {sesion.tipo} para {sesion.atleta.nombre} durante {duracion_total_segundos} segundos...")

        timer = TimerTask(duracion_round=DURACION_ROUND_SEGUNDOS, duracion_descanso=DURACION_DESCANSO_SEGUNDOS)
        threads_to_manage = [timer]

        if sesion.tipo == "Sparring":
            coach = CoachTask(sesion, es_sparring=True)
            luchador1 = LuchadorTask("Luchador 1", sesion)
            luchador2 = LuchadorTask("Luchador 2", sesion)

            timer.agregar_observador(coach)
            timer.agregar_observador(luchador1)
            timer.agregar_observador(luchador2)

            threads_to_manage.extend([coach, luchador1, luchador2])
        else:
            coach = CoachTask(sesion)
            timer.agregar_observador(coach)
            threads_to_manage.append(coach)

        for t in threads_to_manage:
            t.start()

        # Esperar la duración total de la sesión
        time.sleep(duracion_total_segundos)

        # Detener los hilos de forma segura
        for t in threads_to_manage:
            t.detener()

        for t in threads_to_manage:
            t.join()

        print("La sesión en vivo ha terminado.")

    def finalizar_sesion(self, sesion: SesionDeEntrenamiento):
        """
        Finaliza una sesión de entrenamiento, realiza la evaluación
        y notifica a los observadores.
        """
        sesion.evaluar()
        print("Sesión evaluada.")
        
        # Tarea 1.2: Notificar a los observadores (como AnalizadorDeSalud)
        sesion.finalizar()
        print("Observadores notificados de la finalización de la sesión.")

    def obtener_sugerencia_comida(self, sesion: SesionDeEntrenamiento) -> ComidaStrategy:
        """
        Obtiene una sugerencia de comida basada en la intensidad de la sesión.
        """
        # Lógica simple para determinar la estrategia de comida
        if sesion.get_resultado_evaluacion().get('valor', 0) > 500:  # Umbral de ejemplo
            return EstrategiaComidaRecuperacion()
        else:
            return EstrategiaComidaLigera()


# ==============================================================================
# ARCHIVO 39/41: servicio_evaluacion.py
# Directorio: servicios
# Ruta completa: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/servicios/servicio_evaluacion.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 40/41: servicio_perfil.py
# Directorio: servicios
# Ruta completa: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/servicios/servicio_perfil.py
# ==============================================================================

# servicios/servicio_perfil.py
import pickle
import os
from typing import Optional

from python_kickboxing_assistant.entidades.perfil_atleta import PerfilDeLuchador
from python_kickboxing_assistant.excepciones.kickboxing_exception import PersistenciaException

DATA_DIR = "data"

class ServicioPerfil:
    """Servicio para gestionar la persistencia del perfil del atleta."""

    def persistir(self, perfil: PerfilDeLuchador) -> None:
        """
        Guarda el perfil del atleta en un archivo .dat usando pickle.

        Args:
            perfil: La instancia de PerfilDeLuchador a guardar.

        Raises:
            PersistenciaException: Si ocurre un error durante la escritura del archivo.
        """
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)
        
        file_path = os.path.join(DATA_DIR, f"{perfil.get_nombre()}.dat")
        try:
            with open(file_path, "wb") as f:
                pickle.dump(perfil, f)
        except (IOError, pickle.PicklingError) as e:
            raise PersistenciaException(f"Error al guardar el perfil: {e}") from e

    def recuperar(self, nombre_atleta: str) -> Optional[PerfilDeLuchador]:
        """
        Carga un perfil de atleta desde un archivo .dat.

        Args:
            nombre_atleta: El nombre del atleta para encontrar el archivo.

        Returns:
            La instancia de PerfilDeLuchador si se encuentra, de lo contrario None.

        Raises:
            PersistenciaException: Si ocurre un error durante la lectura del archivo.
        """
        file_path = os.path.join(DATA_DIR, f"{nombre_atleta}.dat")
        if not os.path.exists(file_path):
            return None
        
        try:
            with open(file_path, "rb") as f:
                return pickle.load(f)
        except (IOError, pickle.UnpicklingError) as e:
            raise PersistenciaException(f"Error al recuperar el perfil: {e}") from e


# ==============================================================================
# ARCHIVO 41/41: servicio_salud.py
# Directorio: servicios
# Ruta completa: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/servicios/servicio_salud.py
# ==============================================================================

# servicios/servicio_salud.py
from __future__ import annotations
from typing import TYPE_CHECKING

from python_kickboxing_assistant.patrones.observer.observer import Observer
from python_kickboxing_assistant.patrones.strategy.salud_strategy import SaludStrategy
from python_kickboxing_assistant.patrones.strategy.impl.estrategia_salud_descanso import EstrategiaSaludDescanso

if TYPE_CHECKING:
    from python_kickboxing_assistant.entidades.sesion_entrenamiento import SesionDeEntrenamiento

class AnalizadorDeSalud(Observer['SesionDeEntrenamiento']):
    """
    Observer que analiza la salud del atleta después de una sesión.
    Utiliza una SaludStrategy para determinar la recomendación.
    """
    def __init__(self, estrategia: SaludStrategy = EstrategiaSaludDescanso()):
        self._estrategia = estrategia

    def actualizar(self, sesion: 'SesionDeEntrenamiento') -> None:
        """
        Recibe la notificación de que una sesión ha finalizado.
        """
        print(f"[AnalizadorDeSalud] Recibida notificación para la sesión tipo: {sesion.tipo}")
        if sesion.tipo == "Sparring":
            print("[AnalizadorDeSalud] La sesión fue de Sparring. Aplicando estrategia de salud.")
            atleta = sesion.atleta
            resultado = self._estrategia.recomendar(atleta)
            print(f"[AnalizadorDeSalud] Estrategia aplicada. Nuevo estado para {atleta.get_nombre()}: {resultado.get('nuevo_estado')}")



################################################################################
# FIN DEL INTEGRADOR FINAL
# Total de archivos: 41
# Generado: 2025-11-04 16:21:12
################################################################################
