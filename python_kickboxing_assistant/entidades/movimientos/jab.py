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
