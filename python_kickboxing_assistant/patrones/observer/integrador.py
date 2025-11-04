"""
Archivo integrador generado automaticamente
Directorio: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/patrones/observer
Fecha: 2025-11-04 16:21:12
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/patrones/observer/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: observable.py
# Ruta: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/patrones/observer/observable.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/3: observer.py
# Ruta: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/patrones/observer/observer.py
# ================================================================================

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


