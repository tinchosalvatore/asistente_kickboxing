"""
Archivo integrador generado automaticamente
Directorio: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/servicios
Fecha: 2025-11-04 16:21:12
Total de archivos integrados: 6
"""

# ================================================================================
# ARCHIVO 1/6: __init__.py
# Ruta: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/servicios/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/6: kickboxing_service_registry.py
# Ruta: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/servicios/kickboxing_service_registry.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/6: servicio_entrenamiento.py
# Ruta: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/servicios/servicio_entrenamiento.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 4/6: servicio_evaluacion.py
# Ruta: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/servicios/servicio_evaluacion.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 5/6: servicio_perfil.py
# Ruta: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/servicios/servicio_perfil.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 6/6: servicio_salud.py
# Ruta: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/servicios/servicio_salud.py
# ================================================================================

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


