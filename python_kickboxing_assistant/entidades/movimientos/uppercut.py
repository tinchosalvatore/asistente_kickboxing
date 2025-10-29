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
