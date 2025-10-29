# entidades/movimiento.py
from abc import ABC, abstractmethod

class Movimiento(ABC):
    """
    Interfaz que representa un movimiento de kickboxing.
    """
    def __init__(self, nombre: str, potencia: int, calorias: float):
        self._nombre = nombre
        self._potencia = potencia
        self._calorias = calorias

    def get_nombre(self) -> str:
        return self._nombre

    def get_potencia(self) -> int:
        return self._potencia

    def get_calorias(self) -> float:
        return self._calorias

    @abstractmethod
    def es_combinacion(self) -> bool:
        """Devuelve True si el movimiento es una combinación de otros."""
        pass
