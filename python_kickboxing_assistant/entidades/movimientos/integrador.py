"""
Archivo integrador generado automaticamente
Directorio: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/entidades/movimientos
Fecha: 2025-11-04 16:21:12
Total de archivos integrados: 6
"""

# ================================================================================
# ARCHIVO 1/6: __init__.py
# Ruta: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/entidades/movimientos/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/6: cross.py
# Ruta: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/entidades/movimientos/cross.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/6: hook.py
# Ruta: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/entidades/movimientos/hook.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 4/6: jab.py
# Ruta: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/entidades/movimientos/jab.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 5/6: low_kick.py
# Ruta: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/entidades/movimientos/low_kick.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 6/6: uppercut.py
# Ruta: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/entidades/movimientos/uppercut.py
# ================================================================================

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


