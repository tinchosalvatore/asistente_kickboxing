"""
Archivo integrador generado automaticamente
Directorio: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/patrones/factory
Fecha: 2025-11-04 16:21:12
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/patrones/factory/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: movimiento_factory.py
# Ruta: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/patrones/factory/movimiento_factory.py
# ================================================================================

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


