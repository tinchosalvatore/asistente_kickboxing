from python_kickboxing_assistant.patrones.strategy.salud_strategy import SaludStrategy
from python_kickboxing_assistant.entidades.perfil_atleta import PerfilDeLuchador
from typing import Dict, Any

class EstrategiaSaludDescanso(SaludStrategy):
    """
    Estrategia que recomienda descanso obligatorio después de sesiones intensas (ej. Sparring).
    """
    def recomendar(self, perfil: 'PerfilDeLuchador') -> Dict[str, Any]:
        """Actualiza el estado del atleta a 'Descanso Obligatorio'."""
        perfil.set_estado_salud("Descanso Obligatorio")
        return {"nuevo_estado": "Descanso Obligatorio", "motivo": "Sesión intensa."}
