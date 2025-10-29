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
