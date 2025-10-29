# patrones/observer/observable.py
from typing import Generic, List, TypeVar
from .observer import Observer

T = TypeVar('T')

class Observable(Generic[T]):
    """
    Clase base para el patrón Observer. Gestiona una lista de observadores
    y notifica los cambios.
    """
    def __init__(self):
        self._observers: List[Observer[T]] = []

    def agregar_observador(self, observer: Observer[T]) -> None:
        """Añade un observador a la lista."""
        if observer not in self._observers:
            self._observers.append(observer)

    def quitar_observador(self, observer: Observer[T]) -> None:
        """Elimina un observador de la lista."""
        self._observers.remove(observer)

    def notificar_observadores(self, data: T) -> None:
        """Envía datos a todos los observadores suscritos."""
        for observer in self._observers:
            observer.actualizar(data)
