# patrones/observer/observer.py
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')

class Observer(Generic[T], ABC):
    """Interfaz para el patrón Observer. Define el método de actualización."""

    @abstractmethod
    def actualizar(self, data: T) -> None:
        """Recibe la actualización desde el observable."""
        pass
