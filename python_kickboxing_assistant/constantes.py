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
DURACION_ROUND_SEGUNDOS = 180
DURACION_DESCANSO_SEGUNDOS = 5

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
