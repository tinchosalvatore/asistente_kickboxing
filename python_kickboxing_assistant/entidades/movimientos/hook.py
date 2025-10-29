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
