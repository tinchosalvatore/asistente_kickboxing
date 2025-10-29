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
