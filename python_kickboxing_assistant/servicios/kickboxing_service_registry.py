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
